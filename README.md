# Mini DICOM Series Viewer (Mini PACS Viewer)
### Medizinische Informatik – Python Projekt

Dieses Projekt ist ein eigenständig entwickelter DICOM Viewer, der grundlegende Funktionen eines PACS-Systems simuliert. Es dient dem praktischen Verständnis von radiologischen Workflows, Bildserien (CT/MR) und dem DICOM-Standard.

---

## 1. Hauptfunktionen

### • Laden einzelner DICOM-Dateien  
Der Viewer kann einzelne DICOM-Bilder (z. B. CR, XC, OT) laden und deren Metadaten anzeigen.

### • Automatisches Erkennen kompletter CT-/MR-Serien  
- Erkennung anhand von **StudyInstanceUID** und **SeriesInstanceUID**  
- Sortierung mittels **InstanceNumber** oder **ImagePositionPatient**  
- Nachbildung eines typischen PACS-Workflows  

### • Navigation zwischen Bildern  
- Buttons: *Vorheriges Bild / Nächstes Bild*  
- Tastatursteuerung: ← →  
- Anzeige der aktuellen Slice-Position (*Bild X / N*)  

### • Window Level & Window Width (WL/WW)  
Interaktive Anpassung von:  
- **Kontrast (WL)**  
- **Helligkeit (WW)**  
mittels zwei Slidern – wie in professionellen PACS-Viewern.

### • Anzeige medizinischer Metadaten  
Beispielsweise:  
- PatientID  
- StudyDate  
- Modality  
- SliceThickness  
- PixelSpacing  
- SeriesDescription  

---

## 2. Technische Umsetzung

### 2.1 Technologien
- Python 3  
- pydicom  
- Tkinter (GUI)  
- matplotlib  
- NumPy  

### 2.2 Architektur
- Laden des ersten DICOM-Bildes  
- Scannen des Verzeichnisses nach zugehörigen Serien  
- Sortierung der Slices  
- Aktualisierung der GUI bei Navigation oder WL/WW-Änderung  
- Rendering des Bildes im matplotlib-Canvas  

---

## 3. Projektstruktur

```
medical_dicom_viewer/
│
├── dicom_viewer_series.py      # Hauptprogramm (CT/MR Series Viewer)
├── README.md                   # Projektdokumentation
└── dicom_samples/              # Beispiel-DICOMs (nicht im Repo!)
```

⚠️ Aus Datenschutzgründen dürfen keine echten Patientendaten hochgeladen werden.

---

## 4. Screenshots

Nachfolgend ein Beispielbild der grafischen Benutzeroberfläche des Mini DICOM Series Viewers.  
Es zeigt zentrale Komponenten eines PACS-ähnlichen Workflows:

- Darstellung eines CT-/MR-Slices  
- Metadatenbereich (PatientID, Modality, StudyDate usw.)  
- Window-Level- und Window-Width-Slider  
- Navigation durch die Bildserie  

![DICOM Viewer Screenshot](./assets/viewer_screenshot.png)

---

## 5. Lernziele

Durch dieses Projekt wurden folgende Kompetenzen gestärkt:

- Verständnis des **DICOM-Standards** und radiologischer Workflows  
- Arbeiten mit **DICOM-Metadaten** und Bildserien  
- Implementierung von **Windowing-Algorithmen**  
- Entwicklung grafischer Benutzeroberflächen in Python  
- Algorithmische Sortierung von CT-/MR-Slices  
- Anwendung medizinisch relevanter Konzepte wie  
  *Slice Thickness*, *Pixel Spacing*, *Instance Number*  

---

## 6. Relevanz für die medizinische Informatik

Das Projekt simuliert wesentliche Funktionen eines PACS-Systems und demonstriert Kenntnisse in:

- Medical Imaging  
- Health IT / Radiologie-Systeme  
- Datenvisualisierung  
- Bildverarbeitung  
- Softwareentwicklung im Gesundheitswesen  

Es eignet sich hervorragend als Portfolio-Projekt für:

- Werkstudent/in im Bereich Gesundheits-IT  
- PACS/RIS-Support  
- Medical Software Development  
- Radiologie-Informatik  

---

## 7. Kontakt

Bei Interesse an meinem Projekt oder meiner Arbeit im Bereich der medizinischen Informatik freue ich mich über eine Nachricht.

