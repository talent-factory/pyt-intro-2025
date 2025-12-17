# Nachbearbeitung Modul 5

**Zeitaufwand:** 6-8 Stunden
**Deadline:** Kursabschluss

## 🎯 Ziel

Vertiefen Sie die Konzepte aus Modul 5 und schliessen Sie den Kurs mit einem vollständigen Mini-Projekt ab.

## 📝 Aufgaben

| Aufgabe | Thema | Dauer | Schwierigkeit |
|---------|-------|-------|---------------|
| 1 | Kontaktverwaltung | 2-3 Std | ⭐⭐ Mittel |
| 2 | Todo-Listen-Manager | 2-3 Std | ⭐⭐⭐ Schwer |
| 3 | Mini-Projekt nach Wahl | 2-3 Std | ⭐⭐⭐ Schwer |
| 4 | Abschluss-Reflexion | 30 Min | ⭐ Einfach |

## 📚 Aufgabenübersicht

### [Aufgabe 1: Kontaktverwaltung](./aufgabe-1-kontakte.md) (2-3 Std)

Erstellen Sie eine vollständige Kontaktverwaltung mit Datei-Persistenz:
- Kontakte hinzufügen, bearbeiten, löschen
- Kontakte in CSV-Datei speichern
- Kontakte aus CSV-Datei laden
- Suchfunktion implementieren
- Menü-System mit Fehlerbehandlung

**Technologien:** CSV, Dictionaries, Funktionen, Fehlerbehandlung

### [Aufgabe 2: Todo-Listen-Manager](./aufgabe-2-todo.md) (2-3 Std)

Erstellen Sie einen Todo-Listen-Manager mit JSON-Persistenz:
- Aufgaben hinzufügen, bearbeiten, löschen
- Aufgaben als erledigt markieren
- Aufgaben in JSON-Datei speichern
- Aufgaben nach Status filtern
- Prioritäten und Fälligkeitsdaten

**Technologien:** JSON, Listen, Dictionaries, datetime-Modul

### [Aufgabe 3: Mini-Projekt nach Wahl](./aufgabe-3-projekt.md) (2-3 Std)

Wählen Sie eines der folgenden Projekte:

**Option A: Noten-Analyzer**
- Noten aus CSV einlesen
- Statistiken berechnen (Durchschnitt, Median, etc.)
- Ergebnisse in JSON exportieren
- Visualisierung als Text-Diagramm

**Option B: Konfigurationsverwaltung**
- Anwendungseinstellungen in JSON speichern
- Einstellungen laden und ändern
- Validierung der Einstellungen
- Export/Import-Funktionalität

**Option C: Log-Datei-Analyzer**
- Log-Dateien einlesen und parsen
- Fehler und Warnungen zählen
- Statistiken erstellen
- Bericht als CSV exportieren

**Option D: Eigene Idee**
- Muss Datei-I/O verwenden (CSV oder JSON)
- Muss Fehlerbehandlung implementieren
- Muss mindestens 3 Funktionen haben

### [Aufgabe 4: Abschluss-Reflexion](./reflexion.md) (30 Min)

Reflektieren Sie über den **gesamten Kurs** (Module 1-5):
- Was haben Sie gelernt?
- Was war am schwierigsten?
- Was hat Ihnen am meisten Spass gemacht?
- Wie werden Sie Python in Zukunft nutzen?
- Welche Themen möchten Sie vertiefen?

## ✅ Abgabe

**Mindestanforderung:** 2 von 3 Aufgaben + Abschluss-Reflexion

**Empfohlen:** Alle 3 Aufgaben für maximalen Lerneffekt und Kursabschluss-Zertifikat

### Format

- **Code:** Python-Dateien (`.py`)
- **Daten:** CSV/JSON-Beispieldateien
- **Reflexion:** Markdown (`.md`) oder PDF
- **Ordner:** `modul-5-nachbearbeitung/`

### Struktur

```
modul-5-nachbearbeitung/
├── aufgabe-1-kontakte.py
├── kontakte.csv
├── aufgabe-2-todo.py
├── todos.json
├── aufgabe-3-projekt.py
├── projekt-daten.csv/json
└── reflexion.md
```

### Einreichen

- Per E-Mail an Dozenten
- Oder: GitHub Repository (empfohlen)
- **Deadline:** 2 Wochen nach Modul 5

## 💡 Tipps

- **Beginnen Sie früh:** Nehmen Sie sich Zeit für die Projekte
- **Testen Sie ausführlich:** Probieren Sie verschiedene Szenarien
- **Fehlerbehandlung:** Denken Sie an try/except für Datei-Operationen
- **Context Manager:** Nutzen Sie immer `with open()` für Dateien
- **Kommentieren Sie:** Erklären Sie Ihren Code
- **Backup:** Speichern Sie Zwischenstände regelmässig

## 🆘 Hilfe

- Beispielcode in [05-beispiele](../05-beispiele/)
- Materialien in [04-materialien](../04-materialien/)
- Python-Dokumentation (csv, json, os, datetime)
- Fragen Sie Dozenten per E-Mail

## 📅 Deadline

**2 Wochen nach Modul 5** - Danach Kursabschluss und Zertifikat

## 🎓 Kursabschluss

Nach erfolgreicher Abgabe:

- ✅ Erhalten Sie ein Teilnahme-Zertifikat
- ✅ Haben Sie solide Python-Grundlagen
- ✅ Können Sie eigenständig Programme entwickeln
- ✅ Sind Sie bereit für fortgeschrittene Themen

**Herzlichen Glückwunsch zum Kursabschluss! 🎉🚀**
