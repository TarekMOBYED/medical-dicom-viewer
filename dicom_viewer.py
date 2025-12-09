import tkinter as tk
from tkinter import filedialog, messagebox
import pydicom
from pydicom.errors import InvalidDicomError
import matplotlib.pyplot as plt


def load_dicom_file():
    # فتح نافذة اختيار ملف
    file_path = filedialog.askopenfilename(
        title="DICOM-Datei auswählen",
        filetypes=[("DICOM files", "*.dcm"), ("Alle Dateien", "*.*")]
    )

    if not file_path:
        return  # المستخدم أغلق النافذة بدون اختيار ملف

    try:
        # قراءة ملف DICOM
        ds = pydicom.dcmread(file_path)
    except InvalidDicomError:
        messagebox.showerror("Fehler", "Die ausgewählte Datei ist keine gültige DICOM-Datei.")
        return
    except Exception as e:
        messagebox.showerror("Fehler", f"Beim Laden der Datei ist ein Fehler aufgetreten:\n{e}")
        return

    # تحديث منطقة النص بالمعلومات (Meta-Data)
    update_metadata_view(ds)

    # محاولة عرض الصورة
    try:
        pixel_array = ds.pixel_array  # يتطلب numpy (موجود ضمن Abhängigkeiten von pydicom/matplotlib)
    except AttributeError:
        messagebox.showwarning("Hinweis", "Diese DICOM-Datei enthält keine Bilddaten (Pixel Data).")
        return
    except Exception as e:
        messagebox.showerror("Fehler", f"Bilddaten konnten nicht gelesen werden:\n{e}")
        return

    show_image(pixel_array, ds)


def update_metadata_view(ds):
    """
    عرض بعض الحقول المهمة من الـ DICOM Header في Text-Widget
    """
    # تنظيف النص القديم
    metadata_text.delete("1.0", tk.END)

    def safe_get(tag, default="—"):
        return getattr(ds, tag, default)

    # استخراج بعض الحقول المفيدة
    patient_name = safe_get("PatientName")
    patient_id = safe_get("PatientID")
    modality = safe_get("Modality")
    study_date = safe_get("StudyDate")
    study_description = safe_get("StudyDescription")
    series_description = safe_get("SeriesDescription")

    lines = [
        f"Patient Name   : {patient_name}",
        f"Patient ID     : {patient_id}",
        f"Modality       : {modality}",
        f"Study Date     : {study_date}",
        f"Study Desc.    : {study_description}",
        f"Series Desc.   : {series_description}",
    ]

    metadata_text.insert(tk.END, "\n".join(lines))


def show_image(pixel_array, ds):
    """
    عرض الصورة باستخدام matplotlib في نافذة منفصلة.
    """
    plt.figure()
    plt.imshow(pixel_array, cmap="gray")
    plt.axis("off")

    # محاولة عرض عنوان بسيط للصورة من الميتاداتا
    title_parts = []
    if hasattr(ds, "PatientID"):
        title_parts.append(f"PatientID: {ds.PatientID}")
    if hasattr(ds, "Modality"):
        title_parts.append(f"Modality: {ds.Modality}")
    if hasattr(ds, "StudyDate"):
        title_parts.append(f"StudyDate: {ds.StudyDate}")

    if title_parts:
        plt.title(" | ".join(title_parts))

    plt.show()


# === إنشاء واجهة Tkinter الأساسية ===
root = tk.Tk()
root.title("Mini DICOM Viewer – Medical Informatics Student Projekt")
root.geometry("600x400")

# قائمة (Menü)
menubar = tk.Menu(root)
file_menu = tk.Menu(menubar, tearoff=0)
file_menu.add_command(label="DICOM öffnen...", command=load_dicom_file)
file_menu.add_separator()
file_menu.add_command(label="Beenden", command=root.quit)
menubar.add_cascade(label="Datei", menu=file_menu)
root.config(menu=menubar)

# إطار لعرض الميتاداتا
frame = tk.Frame(root)
frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

label = tk.Label(frame, text="DICOM Metadaten", font=("Arial", 12, "bold"))
label.pack(anchor="w")

metadata_text = tk.Text(frame, wrap="word", height=15)
metadata_text.pack(fill=tk.BOTH, expand=True)

# نص أولي
metadata_text.insert(tk.END, "Bitte eine DICOM-Datei über 'Datei -> DICOM öffnen...' auswählen.\n")

# تشغيل الحلقة الرئيسية
root.mainloop()
