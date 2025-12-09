import os
import tkinter as tk
from tkinter import filedialog, messagebox

import pydicom
from pydicom.errors import InvalidDicomError

import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

import numpy as np

# =========================
# متغيّرات عالمية
# =========================
series_slices = []   # قائمة من (dataset, pixel_array)
current_index = 0

root = None
metadata_text = None
canvas = None
ax = None
slice_label = None

window_level_slider = None
window_width_slider = None


# =========================
# دالة Window Level / Width
# =========================
def apply_window(pixel_array, window_level, window_width):
    """
    تطبيق Window Level / Window Width على الصورة.
    الفكرة:
    - قص القيم خارج المجال [WL - WW/2, WL + WW/2]
    - تحويلها إلى تدرج رمادي 0–255
    """
    if window_width <= 0:
        window_width = 1  # تجنب القسمة على صفر

    # تحويل إلى float لسهولة العمليات
    img = pixel_array.astype(np.float32)

    lower = window_level - (window_width / 2.0)
    upper = window_level + (window_width / 2.0)

    # قص القيم خارج المجال
    img = np.clip(img, lower, upper)

    # تحويل إلى 0–1
    img = (img - lower) / (upper - lower)
    img = img * 255.0
    img = np.clip(img, 0, 255)

    return img.astype(np.uint8)


# =========================
# تحميل ملف DICOM وبناء السلسلة
# =========================
def load_dicom_file():
    """
    اختيار ملف DICOM واحد، ثم بناء سلسلة (Series) كاملة من نفس المجلد.
    """
    global series_slices, current_index

    file_path = filedialog.askopenfilename(
        title="DICOM-Datei auswählen",
        filetypes=[("DICOM files", "*.dcm"), ("Alle Dateien", "*.*")]
    )

    if not file_path:
        return

    try:
        ds = pydicom.dcmread(file_path)
    except InvalidDicomError:
        messagebox.showerror("Fehler", "Die ausgewählte Datei ist keine gültige DICOM-Datei.")
        return
    except Exception as e:
        messagebox.showerror("Fehler", f"Beim Laden der Datei ist ein Fehler aufgetreten:\n{e}")
        return

    folder = os.path.dirname(file_path)
    series_slices = build_series_from_folder(folder, ds)

    if not series_slices:
        messagebox.showerror("Fehler", "Es konnten keine passenden DICOM-Bilder in der Serie gefunden werden.")
        return

    current_index = find_index_of_ds_in_series(series_slices, ds)

    show_current_slice()


def build_series_from_folder(folder, reference_ds):
    """
    قراءة كل ملفات .dcm في المجلد نفسه، واختيار تلك التي تنتمي لنفس Study/Series.
    """
    series = []

    ref_study_uid = getattr(reference_ds, "StudyInstanceUID", None)
    ref_series_uid = getattr(reference_ds, "SeriesInstanceUID", None)

    for fname in os.listdir(folder):
        if not fname.lower().endswith(".dcm"):
            continue
        fpath = os.path.join(folder, fname)
        try:
            ds = pydicom.dcmread(fpath)
        except Exception:
            continue

        study_uid = getattr(ds, "StudyInstanceUID", None)
        series_uid = getattr(ds, "SeriesInstanceUID", None)

        if ref_study_uid is not None and study_uid != ref_study_uid:
            continue
        if ref_series_uid is not None and series_uid != ref_series_uid:
            continue

        try:
            pixel_array = ds.pixel_array
        except Exception:
            continue

        series.append((ds, pixel_array))

    # ترتيب السلسلة حسب InstanceNumber أو Z-Position
    def sort_key(item):
        ds, _ = item
        inst = getattr(ds, "InstanceNumber", None)
        if inst is not None:
            return inst
        ipp = getattr(ds, "ImagePositionPatient", None)
        if ipp is not None and len(ipp) >= 3:
            return ipp[2]
        return 0

    series.sort(key=sort_key)
    return series


def find_index_of_ds_in_series(series, reference_ds):
    """
    إيجاد index للصورة التي اختارها المستخدم ضمن السلسلة الكاملة (إن أمكن).
    """
    ref_sop = getattr(reference_ds, "SOPInstanceUID", None)
    if ref_sop is None:
        return 0

    for i, (ds, _) in enumerate(series):
        if getattr(ds, "SOPInstanceUID", None) == ref_sop:
            return i
    return 0


# =========================
# عرض الصورة الحالية
# =========================
def show_current_slice():
    """
    عرض الصورة الحالية + تحديث الميتاداتا + تسمية الـ Slice
    """
    global series_slices, current_index, ax, canvas

    if not series_slices:
        return

    # ضبط حدود الـ index
    current_index = max(0, min(current_index, len(series_slices) - 1))

    ds, pixel_array = series_slices[current_index]

    # تحديث الميتاداتا
    update_metadata_view(ds)

    # الحصول على قيم WL/WW من الـ Sliders
    if window_level_slider is not None and window_width_slider is not None:
        wl = window_level_slider.get()
        ww = window_width_slider.get()
    else:
        # قيم افتراضية إذا لم تكن الـ sliders جاهزة
        wl, ww = 40, 400

    # تطبيق Windowing
    try:
        windowed_img = apply_window(pixel_array, wl, ww)
    except Exception:
        # في حالة حدوث مشكلة نعرض الصورة الأصلية
        windowed_img = pixel_array

    # رسم الصورة
    ax.clear()
    ax.imshow(windowed_img, cmap="gray")
    ax.axis("off")

    title_parts = []
    if hasattr(ds, "PatientID"):
        title_parts.append(f"PatientID: {ds.PatientID}")
    if hasattr(ds, "Modality"):
        title_parts.append(f"Modality: {ds.Modality}")
    if hasattr(ds, "StudyDate"):
        title_parts.append(f"StudyDate: {ds.StudyDate}")

    if title_parts:
        ax.set_title(" | ".join(title_parts), fontsize=10)

    canvas.draw()

    # تحديث Label الخاص بالـ Slice
    if slice_label is not None:
        slice_label.config(text=f"Bild {current_index + 1} / {len(series_slices)}")


# =========================
# الميتاداتا
# =========================
def update_metadata_view(ds):
    """
    عرض بعض الحقول المهمة من الـ DICOM Header في Text-Widget
    """
    metadata_text.delete("1.0", tk.END)

    def safe_get(tag, default="—"):
        return getattr(ds, tag, default)

    patient_name = safe_get("PatientName")
    patient_id = safe_get("PatientID")
    modality = safe_get("Modality")
    study_date = safe_get("StudyDate")
    study_description = safe_get("StudyDescription")
    series_description = safe_get("SeriesDescription")
    body_part = safe_get("BodyPartExamined")
    slice_thickness = safe_get("SliceThickness")
    pixel_spacing = safe_get("PixelSpacing")

    lines = [
        f"Patient Name     : {patient_name}",
        f"Patient ID       : {patient_id}",
        f"Modality         : {modality}",
        f"Study Date       : {study_date}",
        f"Study Desc.      : {study_description}",
        f"Series Desc.     : {series_description}",
        f"Body Part        : {body_part}",
        f"Slice Thickness  : {slice_thickness}",
        f"Pixel Spacing    : {pixel_spacing}",
    ]

    metadata_text.insert(tk.END, "\n".join(lines))


# =========================
# التنقل بين الصور
# =========================
def show_next_slice(event=None):
    global current_index
    if not series_slices:
        return
    current_index += 1
    if current_index >= len(series_slices):
        current_index = len(series_slices) - 1
    show_current_slice()


def show_prev_slice(event=None):
    global current_index
    if not series_slices:
        return
    current_index -= 1
    if current_index < 0:
        current_index = 0
    show_current_slice()


# =========================
# إعداد الـ GUI
# =========================
def setup_gui():
    global root, metadata_text, canvas, ax, slice_label
    global window_level_slider, window_width_slider

    root = tk.Tk()
    root.title("Mini DICOM Series Viewer – WL/WW – Medical Informatics Projekt")
    root.geometry("1100x650")

    # القائمة العلوية
    menubar = tk.Menu(root)
    file_menu = tk.Menu(menubar, tearoff=0)
    file_menu.add_command(label="DICOM öffnen...", command=load_dicom_file)
    file_menu.add_separator()
    file_menu.add_command(label="Beenden", command=root.quit)
    menubar.add_cascade(label="Datei", menu=file_menu)
    root.config(menu=menubar)

    # إطار رئيسي
    main_frame = tk.Frame(root)
    main_frame.pack(fill=tk.BOTH, expand=True)

    # يسار: الميتاداتا
    left_frame = tk.Frame(main_frame)
    left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=False, padx=10, pady=10)

    label_meta = tk.Label(left_frame, text="DICOM Metadaten", font=("Arial", 12, "bold"))
    label_meta.pack(anchor="w")

    metadata_text = tk.Text(left_frame, wrap="word", width=40)
    metadata_text.pack(fill=tk.BOTH, expand=True)
    metadata_text.insert(tk.END, "Bitte eine DICOM-Serie über 'Datei -> DICOM öffnen...' auswählen.\n")

    # يمين: الصورة + التحكم
    right_frame = tk.Frame(main_frame)
    right_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)

    # شكل matplotlib
    fig = Figure(figsize=(5, 5))
    ax = fig.add_subplot(111)
    ax.axis("off")

    canvas = FigureCanvasTkAgg(fig, master=right_frame)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack(fill=tk.BOTH, expand=True)

    # التحكم بـ Window Level / Width
    wlww_frame = tk.Frame(right_frame)
    wlww_frame.pack(fill=tk.X, pady=5)

    tk.Label(wlww_frame, text="Window Level (WL)").pack(anchor="w")
    window_level_slider = tk.Scale(
        wlww_frame,
        from_=-1000,
        to=1000,
        orient=tk.HORIZONTAL,
        command=lambda x: show_current_slice()
    )
    window_level_slider.set(40)  # قيمة أولية نموذجية لـ CT Thorax
    window_level_slider.pack(fill=tk.X)

    tk.Label(wlww_frame, text="Window Width (WW)").pack(anchor="w")
    window_width_slider = tk.Scale(
        wlww_frame,
        from_=1,
        to=2000,
        orient=tk.HORIZONTAL,
        command=lambda x: show_current_slice()
    )
    window_width_slider.set(400)  # قيمة أولية نموذجية
    window_width_slider.pack(fill=tk.X)

    # أزرار التنقّل
    nav_frame = tk.Frame(right_frame)
    nav_frame.pack(fill=tk.X, pady=5)

    btn_prev = tk.Button(nav_frame, text="◀ Vorheriges Bild", command=show_prev_slice)
    btn_prev.pack(side=tk.LEFT, padx=5)

    slice_label = tk.Label(nav_frame, text="Bild 0 / 0")
    slice_label.pack(side=tk.LEFT, padx=10)

    btn_next = tk.Button(nav_frame, text="Nächstes Bild ▶", command=show_next_slice)
    btn_next.pack(side=tk.LEFT, padx=5)

    # ربط الأسهم من لوحة المفاتيح
    root.bind("<Left>", show_prev_slice)
    root.bind("<Right>", show_next_slice)

    return root


# =========================
# نقطة البدء
# =========================
if __name__ == "__main__":
    root = setup_gui()
    root.mainloop()
