# Modul 5: Dateien & Module

**Dauer:** 1 Tag (4 Lektionen à 50 Minuten)
**Voraussetzung:** Module 1-4 abgeschlossen
**Besonderheit:** Abschlussmodul mit Mini-Projekt

## 🎯 Lernziele

Nach diesem Modul können Sie:

1. ✅ Textdateien lesen und schreiben
2. ✅ CSV-Dateien verarbeiten und analysieren
3. ✅ JSON-Daten lesen, schreiben und manipulieren
4. ✅ Fehlerbehandlung mit try/except implementieren
5. ✅ Eigene Module erstellen und importieren
6. ✅ Python-Standard-Module nutzen (os, datetime, random, etc.)
7. ✅ Vollständige Anwendungen mit Datei-I/O entwickeln
8. ✅ Best Practices für Dateiverarbeitung anwenden

## 📖 Themen im Detail

### Datei-Grundlagen
- Dateien öffnen und schliessen (open, close)
- Context Manager (with-Statement)
- Modi: read, write, append
- Dateipfade und Navigation
- Encoding (UTF-8)

### CSV-Verarbeitung
- CSV-Modul nutzen
- Daten einlesen und parsen
- CSV-Dateien schreiben
- Datenanalyse mit CSV
- Excel-kompatible Formate

### JSON-Datenformat
- JSON-Struktur verstehen
- json.load() und json.dump()
- Verschachtelte Daten
- APIs und JSON
- Konfigurationsdateien

### Fehlerbehandlung
- Try/except/finally
- Spezifische Exceptions
- FileNotFoundError behandeln
- Robuste Programme schreiben
- Logging-Grundlagen

### Module & Packages
- Eigene Module erstellen
- Import-Varianten
- Standard-Library erkunden
- __name__ == "__main__"
- Projektstruktur

### Mini-Projekt
- Tagebuch-App mit Textdateien
- CSV-Datenanalyse
- Konfigurationsverwaltung mit JSON
- Notizen-App

## 📚 Modulstruktur

### [00-vorbereitung](./00-vorbereitung/) - Vorbereitung (2-3 Std)

**Vor dem Präsenztag:**
- Leseauftrag: Datei-I/O und Module verstehen
- Erste Experimente mit Textdateien
- Quiz zur Selbstkontrolle (10 Fragen)
- Beispieldateien herunterladen

### [01-praxis](./01-praxis/) - Präsenzunterricht (4 × 50 Min)

**Am Kurstag:**
- **Lektion 1:** Textdateien lesen und schreiben (50 Min)
- **Lektion 2:** CSV-Dateien verarbeiten (50 Min)
- **Lektion 3:** JSON-Daten manipulieren (50 Min)
- **Lektion 4:** Module & Abschluss-Projekt (50 Min)

### [02-uebungen](./02-uebungen/) - Übungen während der Präsenz

**Praktische Übungen:**
1. Übung 1: Notizen-App
2. Übung 2: Textstatistik
3. Übung 3: Produktliste CSV
4. Übung 4: Notenauswertung CSV
5. Übung 5: Aufgabenliste JSON
6. Übung 6: Konfiguration JSON
7. Übung 7: Eigenes Modul
8. Übung 8: Standard-Module

### [03-nachbearbeitung](./03-nachbearbeitung/) - Hausaufgaben (6-8 Std)

**Nach dem Präsenztag:**
- Aufgabe 1: Tagebuch-App (Textdatei und JSON-Export)
- Aufgabe 2: CSV-Datenanalyse (Verkaufsdaten)
- Aufgabe 3: Konfigurationsverwaltung (JSON)
- Abschluss-Reflexion über den gesamten Kurs

### [04-materialien](./04-materialien/) - Referenzmaterialien

**Nachschlagewerke:**
- Cheatsheet CSV
- Cheatsheet JSON
- Handout Dateien
- Häufige Fehler

### [05-beispiele](./05-beispiele/) - Beispielprogramme

**13 vollständige Python-Programme** (Übersicht in der [05-beispiele/README](./05-beispiele/README.md)):
- textdateien.py, csv_beispiel.py, json_beispiel.py - Grundlagen
- aufgabenliste.py, notenverwaltung.py, config.py - Anwendungen mit CSV/JSON
- datei_utils.py, text_tools.py, backup_tool.py - eigene Module
- log_analyzer.py, daten_konverter.py - Werkzeuge
- notizen_app.py, notizen_app_streamlit.py - Notizen-App (Konsole und Streamlit)

## ⏱️ Zeitplan

| Phase | Aktivität | Dauer |
|-------|-----------|-------|
| **Vor Tag 5** | Leseauftrag + Experimente | 2-3 Std |
| **Tag 5** | 4 Lektionen Präsenzunterricht | 4 × 50 Min |
| **Tag 5** | Pausen | 40 Min |
| **Nach Tag 5** | 3 Aufgaben + Reflexion | 6-8 Std |
| **Gesamt** | | **12-15 Std** |

## ✅ Erfolgskriterien

Nach erfolgreichem Abschluss des Moduls:

- [ ] Alle Vorbereitungsaufgaben erledigt
- [ ] Alle 4 Lektionen besucht
- [ ] Mindestens 6 von 8 Übungen gelöst
- [ ] Alle 3 Nachbearbeitungsaufgaben eingereicht
- [ ] Mini-Projekt abgeschlossen
- [ ] Abschluss-Reflexion geschrieben
- [ ] Kurs erfolgreich abgeschlossen! 🎓

## 💡 Tipps für den Erfolg

- **Datensicherheit:** Arbeiten Sie mit Kopien wichtiger Dateien
- **Context Manager:** Nutzen Sie immer `with open()` für Dateien
- **Fehlerbehandlung:** Antizipieren Sie mögliche Fehler
- **Klein starten:** Testen Sie Code mit kleinen Beispieldateien
- **Backup:** Speichern Sie Zwischenstände regelmässig

## 🎓 Kursabschluss

Dieses Modul bildet den Abschluss des Python-Basiskurses. Nach erfolgreichem Abschluss:

- ✅ Haben Sie solide Python-Grundlagen
- ✅ Können Sie eigenständig Programme entwickeln
- ✅ Verstehen Sie die wichtigsten Konzepte
- ✅ Sind Sie bereit für fortgeschrittene Themen

### Mögliche nächste Schritte:
- **Fortgeschrittener Python-Kurs:** OOP, Decorators, Generators
- **Datenanalyse:** Pandas, NumPy, Matplotlib
- **Web-Entwicklung:** Flask, Django
- **Automatisierung:** Scripting, Task-Automation
- **Data Science:** Machine Learning, AI

## 🔗 Weiterführende Links

- [Python Dokumentation: File I/O](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)
- [Real Python: Reading and Writing Files](https://realpython.com/read-write-files-python/)
- [Python CSV Modul](https://docs.python.org/3/library/csv.html)
- [Python JSON Modul](https://docs.python.org/3/library/json.html)

---

**Herzlichen Glückwunsch zum Kursabschluss! 🚀🎓**
