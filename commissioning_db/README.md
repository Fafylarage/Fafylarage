# 🔧 Inbetriebnahme-Wissensdatenbank

## Automotive | E/E-Architektur | Gesamtfahrzeug | Steuergeräteintegration

Eine vollständige Python-Webanwendung zur Dokumentation, Analyse und Wiederverwendung von Inbetriebnahme-Erkenntnissen im Automotive-Umfeld.

---

## 📋 Funktionsübersicht

| Funktion | Beschreibung |
|----------|-------------|
| **Dashboard** | Übersicht mit KPIs, Top-10-Charts und letzten Einträgen |
| **Neuer Fehlerfall** | Strukturierte Erfassung aller relevanten Informationen |
| **Suche & Filter** | Globale Volltextsuche und erweiterte Filtermöglichkeiten |
| **Wissensdatenbank** | Automatische Ähnlichkeitssuche für bekannte Fehler |
| **Export** | Datenexport als CSV, Excel und PDF |
| **Detailansicht** | Vollständige Darstellung aller Fallinformationen |

---

## 🏗️ Projektstruktur

```
commissioning_db/
│
├── app.py              # Streamlit Hauptanwendung
├── database.py         # Datenbankoperationen (CRUD, Suche, Filter)
├── models.py           # SQLAlchemy Datenmodelle
├── commissioning.db    # SQLite Datenbank (wird automatisch erstellt)
├── requirements.txt    # Python-Abhängigkeiten
├── README.md           # Diese Datei
│
└── assets/             # Ordner für Anhänge und Assets
```

---

## 🗄️ Datenstruktur

Die Anwendung nutzt eine SQLite-Datenbank mit einer Haupttabelle `fehlerfaelle`:

| Feld | Typ | Beschreibung |
|------|-----|-------------|
| `id` | Integer (PK) | Eindeutige Fall-ID |
| `datum` | Date | Datum des Fehlerfalls |
| `projekt` | String | Projektname (z.B. eBus) |
| `baureihe` | String | Fahrzeug-Baureihe |
| `fahrzeugnummer` | String | Interne Fahrzeugnummer |
| `vin` | String (17) | Vehicle Identification Number |
| `softwarestand_fahrzeug` | String | SW-Version des Gesamtfahrzeugs |
| `verantwortlicher` | String | Zuständiger Ingenieur |
| `steuergeraet` | String | Betroffenes Steuergerät |
| `teilenummer` | String | Hardware-Teilenummer |
| `softwarestand_steuergeraet` | String | SW-Version des SG |
| `kommunikationsart` | String | Ethernet, CAN, CAN-FD, LIN, etc. |
| `fehlerbeschreibung` | Text | Detaillierte Fehlerbeschreibung |
| `fehlersymptome` | Text | Beobachtete Symptome |
| `logs` | Text | Relevante Log-Auszüge |
| `diagnosecodes` | Text | DTCs (Diagnostic Trouble Codes) |
| `dateien` | Text | Pfade zu angehängten Dateien |
| `verwendete_tools` | Text | Genutzte Diagnosetools |
| `durchgefuehrte_schritte` | Text | Analyseschritte |
| `messergebnisse` | Text | Ergebnisse von Messungen |
| `beobachtungen` | Text | Weitere Beobachtungen |
| `kommunikationsanalyse` | Text | Netzwerk-/Kommunikationsanalyse |
| `ursache` | Text | Identifizierte Fehlerursache |
| `root_cause_kategorie` | String | Kategorie (Software, Hardware, etc.) |
| `loesung` | Text | Durchgeführte Lösung |
| `lessons_learned` | Text | Erkenntnisse für die Zukunft |
| `status` | String | Offen / In Analyse / Gelöst / Nicht reproduzierbar |
| `tags` | Text | Schlagwörter für die Suche |
| `erstellt_am` | DateTime | Erstellungszeitpunkt |
| `aktualisiert_am` | DateTime | Letzte Aktualisierung |

---

## 🚀 Installation

### Voraussetzungen

- Python 3.12 oder höher
- pip (Python Paketmanager)

### Schritt 1: Repository klonen oder Dateien herunterladen

```bash
cd commissioning_db
```

### Schritt 2: Virtuelle Umgebung erstellen (empfohlen)

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

### Schritt 3: Abhängigkeiten installieren

```bash
pip install -r requirements.txt
```

---

## ▶️ Anwendung starten

```bash
streamlit run app.py
```

Die Anwendung öffnet sich automatisch im Standard-Webbrowser unter:

```
http://localhost:8501
```

### Optionale Startparameter

```bash
# Anderen Port verwenden
streamlit run app.py --server.port 8080

# Ohne automatisches Öffnen des Browsers
streamlit run app.py --server.headless true

# Dark Theme erzwingen
streamlit run app.py --theme.base dark
```

---

## 🎨 Design

- **Dunkles Theme** mit professioneller Automotive-Anmutung
- **Responsive Layout** für verschiedene Bildschirmgrößen
- **Farbcodierter Status:**
  - 🟢 Grün = Gelöst
  - 🔴 Rot = Offen
  - 🟠 Orange = In Analyse
  - ⚪ Grau = Nicht reproduzierbar

---

## 🔧 Technologie-Stack

| Komponente | Technologie |
|-----------|------------|
| Frontend | Streamlit |
| Backend | Python 3.12+ |
| Datenbank | SQLite |
| ORM | SQLAlchemy |
| Datenverarbeitung | Pandas |
| Excel-Export | openpyxl |
| PDF-Export | fpdf2 |

---

## 📝 Nutzungshinweise

1. **Erster Start**: Die Datenbank wird automatisch erstellt und ein Beispieldatensatz eingefügt.
2. **Wissensdatenbank**: Bei der Suche nach ähnlichen Fällen werden Steuergerät, Kommunikationsart, Tags und Fehlerbeschreibung berücksichtigt.
3. **Export**: Alle Daten können jederzeit als CSV, Excel oder PDF exportiert werden.
4. **Backup**: Die Datei `commissioning.db` enthält alle Daten und kann einfach gesichert werden.

---

## 📄 Lizenz

Interne Nutzung - Inbetriebnahme-Wissensdatenbank für das Automotive-Umfeld.
