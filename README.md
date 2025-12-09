{\rtf1\ansi\ansicpg1252\cocoartf2636
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;\f1\fnil\fcharset178 GeezaPro;\f2\fnil\fcharset0 LucidaGrande;
\f3\froman\fcharset0 Times-Roman;\f4\fnil\fcharset134 STSongti-SC-Regular;\f5\fmodern\fcharset0 Courier;
\f6\fnil\fcharset0 AppleColorEmoji;}
{\colortbl;\red255\green255\blue255;\red0\green0\blue0;}
{\*\expandedcolortbl;;\cssrgb\c0\c0\c0;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh10200\viewkind0
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f0\fs24 \cf0 Mini
\f1  
\f0 DICOM
\f1  
\f0 Series
\f1  
\f0 Viewer
\f1  
\f0 (Mini
\f1  
\f0 PACS
\f1  
\f0 Viewer)
\f1 \

\f0 Medizinische
\f1  
\f0 Informatik
\f1  
\f0 \'96
\f1  
\f0 Python
\f1  
\f0 Projekt
\f1 \
\

\f0 Dieses
\f1  
\f0 Projekt
\f1  
\f0 ist
\f1  
\f0 ein
\f1  
\f0 eigenst\'e4ndig
\f1  
\f0 entwickelter
\f1  
\f0 DICOM
\f1  
\f0 Viewer,
\f1  
\f0 der
\f1  
\f0 grundlegende
\f1  
\f0 Funktionen
\f1  
\f0 eines
\f1  
\f0 PACS-Systems
\f1  
\f0 simuliert
\f1 . 
\f0 Er
\f1  
\f0 wurde
\f1  
\f0 im
\f1  
\f0 Rahmen
\f1  
\f0 meiner
\f1  
\f0 Vertiefung
\f1  
\f0 in
\f1  
\f0 der
\f1  
\f0 Medizinischen
\f1  
\f0 Informatik
\f1  
\f0 erstellt
\f1  
\f0 und
\f1  
\f0 dient
\f1  
\f0 dem
\f1  
\f0 praktischen
\f1  
\f0 Verst\'e4ndnis
\f1  
\f0 von
\f1  
\f0 radiologischen
\f1  
\f0 Workflows,
\f1  
\f0 Bildserien
\f1  
\f0 (CT/MR)
\f1  
\f0 und
\f1  
\f0 dem
\f1  
\f0 DICOM-Standard
\f1 .\
\

\f0 Hauptfunktionen
\f1 \
\

\f0 \'97\uc0\u8235 L\uc0\u8236 aden
\f1  
\f0 einzelner
\f1  
\f0 DICOM-Dateien
\f1 \

\f0 Der
\f1  
\f0 Viewer
\f1  
\f0 kann
\f1  
\f0 einzelne
\f1  
\f0 DICOM-Bilder
\f1  
\f0 (z
\f1 . 
\f0 B
\f1 . 
\f0 CR,
\f1  
\f0 XC,
\f1  
\f0 OT)
\f1  
\f0 laden
\f1  
\f0 und
\f1  
\f0 deren
\f1  
\f0 Metadaten
\f1  
\f0 anzeigen
\f1 .\
\

\f0 \'97Automatisches
\f1  
\f0 Erkennen
\f1  
\f0 kompletter
\f1  
\f0 CT-/MR-Serien
\f1 \

\f0 -
\f1  
\f0 Erkennung
\f1  
\f0 anhand
\f1  
\f0 von
\f1  
\f0 **StudyInstanceUID**
\f1  
\f0 und
\f1  
\f0 **SeriesInstanceUID**
\f1 \

\f0 -
\f1  
\f0 Sortierung
\f1  
\f0 mit
\f1  
\f0 **InstanceNumber**
\f1  
\f0 oder
\f1  
\f0 **ImagePositionPatient**
\f1 \

\f0 -
\f1  
\f0 Typischer
\f1  
\f0 Workflow
\f1  
\f0 wie
\f1  
\f0 in
\f1  
\f0 PACS-Systemen
\f1 \
\

\f0 \'97Navigation
\f1  
\f0 zwischen
\f1  
\f0 Bildern
\f1 \

\f0 -
\f1  
\f0 Buttons:
\f1  
\f0 **Vorheriges
\f1  
\f0 Bild
\f1  
\f0 /
\f1  
\f0 N\'e4chstes
\f1  
\f0 Bild**
\f1 \

\f0 -
\f1  
\f0 Tastatur:
\f1  
\f0 **
\f2 \uc0\u8592 
\f1  
\f2 \uc0\u8594 
\f1  
\f0 Pfeiltasten**
\f1 \

\f0 -
\f1  
\f0 Anzeige
\f1  
\f0 der
\f1  
\f0 aktuellen
\f1  
\f0 Slice-Position
\f1  
\f0 im
\f1  
\f0 Format
\f1  
\f0 *Bild
\f1  
\f0 X
\f1  
\f0 /
\f1  
\f0 N*
\f1 \
\

\f0 \'97Window
\f1  
\f0 Level
\f1  
\f0 &
\f1  
\f0 Window
\f1  
\f0 Width
\f1  
\f0 (WL/WW)
\f1 \

\f0 Interaktive
\f1  
\f0 Anpassung
\f1  
\f0 von:
\f1 \

\f0 -
\f1  
\f0 **Kontrast**
\f1 \

\f0 -
\f1  
\f0 **Helligkeit**
\f1 \
\

\f0 Mittels
\f1  
\f0 zwei
\f1  
\f0 Slidern
\f1  
\f0 \'97
\f1  
\f0 wie
\f1  
\f0 in
\f1  
\f0 professionellen
\f1  
\f0 PACS-Viewern
\f1 .\
\

\f0 \'97Anzeige
\f1  
\f0 medizinischer
\f1  
\f0 Metadaten
\f1 \

\f0 Anzeige
\f1  
\f0 relevanter
\f1  
\f0 DICOM-Felder,
\f1  
\f0 z
\f1 . 
\f0 B
\f1 .
\f0 :
\f1 \

\f0 -
\f1  
\f0 PatientID
\f1   \

\f0 -
\f1  
\f0 StudyDate
\f1   \

\f0 -
\f1  
\f0 Modality
\f1   \

\f0 -
\f1  
\f0 SliceThickness
\f1   \

\f0 -
\f1  
\f0 PixelSpacing
\f1   \

\f0 -
\f1  
\f0 SeriesDescription
\f1   \
\
 
\f0 Technische
\f1  
\f0 Umsetzung
\f1 \
\
 
\f0 Technologien:
\f1 \

\f0 -
\f1  
\f0 **Python
\f1  
\f0 3**
\f1 \

\f0 -
\f1  
\f0 **pydicom**
\f1 \

\f0 -
\f1  
\f0 **Tkinter
\f1  
\f0 (GUI)**
\f1 \

\f0 -
\f1  
\f0 **matplotlib**
\f1 \

\f0 -
\f1  
\f0 **NumPy**
\f1 \
\

\f0 Architektur:
\f1 \

\f0 -
\f1  
\f0 Laden
\f1  
\f0 des
\f1  
\f0 ersten
\f1  
\f0 DICOM-Bildes
\f1   \

\f0 -
\f1  
\f0 Scannen
\f1  
\f0 des
\f1  
\f0 Verzeichnisses
\f1  
\f0 nach
\f1  
\f0 zugeh\'f6rigen
\f1  
\f0 Serien
\f1   \

\f0 -
\f1  
\f0 Sortierung
\f1  
\f0 der
\f1  
\f0 Series
\f1   \

\f0 -
\f1  
\f0 Aktualisierung
\f1  
\f0 der
\f1  
\f0 GUI
\f1  
\f0 bei
\f1  
\f0 Navigation
\f1  
\f0 oder
\f1  
\f0 WL/WW-\'c4nderung
\f1   \

\f0 -
\f1  
\f0 Rendering
\f1  
\f0 des
\f1  
\f0 Bildes
\f1  
\f0 im
\f1  
\f0 matplotlib-Canvas
\f1   \
\
\
 
\f0 Projektstruktur
\f1 \
\pard\pardeftab720\sa240\partightenfactor0

\f3 \cf0 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 medical_dicom_viewer/\uc0\u8232 
\f4 \'a9\'a6
\f3 \uc0\u8232 
\f4 \'a9\'c0\'a9\'a4\'a9\'a4
\f3  dicom_viewer_series.py # Hauptprogramm (CT/MR Series Viewer)\uc0\u8232 
\f4 \'a9\'c0\'a9\'a4\'a9\'a4
\f3  dicom_viewer.py # Einfache Version (Optional)\uc0\u8232 
\f4 \'a9\'c0\'a9\'a4\'a9\'a4
\f3  README.md # Projektdokumentation\uc0\u8232 
\f4 \'a9\'b8\'a9\'a4\'a9\'a4
\f3  dicom_samples/ # Beispiel-DICOMs (nicht im Repo!)\
\pard\pardeftab720\partightenfactor0

\f5\fs26 \cf0 \
\
\pard\tx566\tx1133\tx1700\tx2267\tx2834\tx3401\tx3968\tx4535\tx5102\tx5669\tx6236\tx6803\pardirnatural\partightenfactor0

\f1\fs24 \cf0 \

\f6 \uc0\u9888 \u65039 
\f1  
\f0 *Aus
\f1  
\f0 Datenschutzgr\'fcnden
\f1  
\f0 sollten
\f1  
\f0 keine
\f1  
\f0 echten
\f1  
\f0 Patientendaten
\f1  
\f0 hochgeladen
\f1  
\f0 werden
\f1 .
\f0 *
\f1 \
\
\
\

\f0 Beispielbilder
\f1  
\f0 (Screenshots)
\f1 \
\

\f0 (Hier
\f1  
\f0 k\'f6nnen
\f1  
\f0 sp\'e4ter
\f1  
\f0 Screenshots
\f1  
\f0 des
\f1  
\f0 Viewers
\f1  
\f0 eingef\'fcgt
\f1  
\f0 werden
\f1 .
\f0 )
\f1 \
\

\f0 Lernziele
\f1 \
\

\f0 Durch
\f1  
\f0 dieses
\f1  
\f0 Projekt
\f1  
\f0 wurden
\f1  
\f0 folgende
\f1  
\f0 Kompetenzen
\f1  
\f0 ausgebaut:
\f1 \
\

\f0 -
\f1  
\f0 Verst\'e4ndnis
\f1  
\f0 des
\f1  
\f0 **DICOM-Standards**
\f1  
\f0 und
\f1  
\f0 radiologischer
\f1  
\f0 Workflows
\f1   \

\f0 -
\f1  
\f0 Arbeiten
\f1  
\f0 mit
\f1  
\f0 **DICOM-Metadaten**
\f1  
\f0 und
\f1  
\f0 Bildserien
\f1   \

\f0 -
\f1  
\f0 Implementierung
\f1  
\f0 von
\f1  
\f0 **Windowing-Algorithmen**
\f1   \

\f0 -
\f1  
\f0 praktische
\f1  
\f0 GUI-Entwicklung
\f1  
\f0 in
\f1  
\f0 Python
\f1   \

\f0 -
\f1  
\f0 Algorithmische
\f1  
\f0 Sortierung
\f1  
\f0 von
\f1  
\f0 CT-/MR-Slices
\f1   \

\f0 -
\f1  
\f0 Anwendung
\f1  
\f0 medizinisch
\f1  
\f0 relevanter
\f1  
\f0 Konzepte
\f1  
\f0 wie
\f1   \
  
\f0 **Slice
\f1  
\f0 Thickness**,
\f1  
\f0 **Pixel
\f1  
\f0 Spacing**,
\f1  
\f0 **Instance
\f1  
\f0 Number**
\f1   \
\

\f0 Relevanz
\f1  
\f0 f\'fcr
\f1  
\f0 die
\f1  
\f0 medizinische
\f1  
\f0 Informatik
\f1 \
\

\f0 Das
\f1  
\f0 Projekt
\f1  
\f0 simuliert
\f1  
\f0 wesentliche
\f1  
\f0 Funktionen
\f1  
\f0 eines
\f1  
\f0 PACS-Systems
\f1  
\f0 und
\f1  
\f0 demonstriert
\f1  
\f0 Wissen
\f1  
\f0 in:
\f1 \
\

\f0 -
\f1  
\f0 Medical
\f1  
\f0 Imaging
\f1   \

\f0 -
\f1  
\f0 Health
\f1  
\f0 IT
\f1  
\f0 /
\f1  
\f0 Radiologie-Systeme
\f1   \

\f0 -
\f1  
\f0 Datenvisualisierung
\f1   \

\f0 -
\f1  
\f0 Bildverarbeitung
\f1   \

\f0 -
\f1  
\f0 Softwareentwicklung
\f1  
\f0 im
\f1  
\f0 Gesundheitswesen
\f1   \
\

\f0 Es
\f1  
\f0 eignet
\f1  
\f0 sich
\f1  
\f0 ideal
\f1  
\f0 als
\f1  
\f0 Portfolio-Projekt
\f1  
\f0 f\'fcr:
\f1 \
\

\f0 -
\f1  
\f0 Werkstudent/in
\f1  
\f0 Gesundheit
\f1  
\f0 IT
\f1   \

\f0 -
\f1  
\f0 PACS/RIS
\f1  
\f0 Support
\f1   \

\f0 -
\f1  
\f0 Medical
\f1  
\f0 Software
\f1  
\f0 Development
\f1   \

\f0 -
\f1  
\f0 Radiologie-Informatik
\f1   \
\

\f0 \
Kontakt
\f1 \

\f0 Bei
\f1  
\f0 Interesse
\f1  
\f0 an
\f1  
\f0 meinem
\f1  
\f0 Projekt
\f1  
\f0 oder
\f1  
\f0 meiner
\f1  
\f0 Arbeit
\f1  
\f0 im
\f1  
\f0 Bereich
\f1  
\f0 der
\f1  
\f0 medizinischen
\f1  
\f0 Informatik
\f1  
\f0 freue
\f1  
\f0 ich
\f1  
\f0 mich
\f1  
\f0 \'fcber
\f1  
\f0 eine
\f1  
\f0 Nachricht
\f1 .\
\
\kerning1\expnd0\expndtw0 \outl0\strokewidth0 \
}
