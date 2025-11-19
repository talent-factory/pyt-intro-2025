# Lektion 5: Abschluss-Projekt

**Dauer:** 50 Minuten  
**Format:** 5 Min Einführung + 40 Min Projektarbeit + 5 Min Präsentation

## 🎯 Lernziele

- Alle gelernten Konzepte kombinieren
- Vollständiges Programm entwickeln
- Mit Dateien arbeiten
- Code strukturieren

## 📋 Projektauswahl

Wählen Sie **eines** der folgenden Projekte:

### Projekt 1: Aufgabenverwaltung (Todo-App)

**Anforderungen:**
- Aufgaben in JSON speichern
- Aufgaben hinzufügen, anzeigen, erledigen, löschen
- Kategorien/Tags
- Fälligkeitsdatum

**Datenstruktur:**
```json
{
  "aufgaben": [
    {
      "id": 1,
      "titel": "Python lernen",
      "beschreibung": "Modul 5 abschließen",
      "erledigt": false,
      "kategorie": "Lernen",
      "faellig": "2025-01-31"
    }
  ]
}
```

**Funktionen:**
- `aufgaben_laden()`
- `aufgaben_speichern()`
- `neue_aufgabe()`
- `aufgaben_anzeigen()`
- `aufgabe_erledigen(id)`
- `aufgabe_loeschen(id)`

### Projekt 2: Kontaktverwaltung

**Anforderungen:**
- Kontakte in CSV speichern
- Kontakte hinzufügen, suchen, bearbeiten, löschen
- Export nach JSON
- Statistiken (Anzahl Kontakte, etc.)

**CSV-Format:**
```
Name,Email,Telefon,Firma,Notizen
Anna Muster,anna@example.com,079 123 45 67,Firma AG,VIP Kunde
```

**Funktionen:**
- `kontakte_laden()`
- `kontakte_speichern()`
- `neuer_kontakt()`
- `kontakt_suchen(name)`
- `kontakt_bearbeiten(name)`
- `kontakt_loeschen(name)`
- `export_json()`

### Projekt 3: Notizen-System

**Anforderungen:**
- Notizen in Textdateien speichern
- Notizen erstellen, anzeigen, suchen
- Index in JSON (Titel, Datum, Tags)
- Volltextsuche

**Struktur:**
```
notizen/
  ├── index.json
  ├── notiz_001.txt
  ├── notiz_002.txt
  └── ...
```

**Funktionen:**
- `index_laden()`
- `index_speichern()`
- `neue_notiz(titel, inhalt, tags)`
- `notizen_anzeigen()`
- `notiz_suchen(suchbegriff)`
- `notiz_lesen(id)`

## 💻 Projektarbeit (40 Min)

### Schritt 1: Planung (5 Min)

1. Projekt wählen
2. Funktionen auflisten
3. Datenstruktur skizzieren

### Schritt 2: Grundgerüst (10 Min)

```python
"""
Mein Projekt-Name
Beschreibung
"""

import json  # oder csv
import os
from datetime import datetime

# Globale Variablen
DATEINAME = "daten.json"

# Funktionen hier...

def hauptmenu():
    """Zeigt Hauptmenü."""
    while True:
        print("\n" + "=" * 40)
        print("PROJEKT-NAME")
        print("=" * 40)
        print("1. Option 1")
        print("2. Option 2")
        print("3. Beenden")
        
        wahl = input("\nWahl: ")
        
        if wahl == "1":
            # Funktion aufrufen
            pass
        elif wahl == "2":
            # Funktion aufrufen
            pass
        elif wahl == "3":
            print("Auf Wiedersehen!")
            break

if __name__ == "__main__":
    hauptmenu()
```

### Schritt 3: Funktionen implementieren (20 Min)

Implementieren Sie die wichtigsten Funktionen:
- Laden/Speichern
- Hinzufügen
- Anzeigen
- Löschen

### Schritt 4: Testen (5 Min)

Testen Sie alle Funktionen!

## 🎤 Präsentation (5 Min)

Zeigen Sie Ihr Projekt:
- Was macht es?
- Welche Funktionen gibt es?
- Kurze Demo

## 💡 Tipps

- Klein anfangen, dann erweitern
- Funktionen einzeln testen
- Fehlerbehandlung (`try-except`)
- Kommentare schreiben
- Code strukturieren

## ✅ Erfolgskriterien

- [ ] Programm läuft ohne Fehler
- [ ] Daten werden gespeichert
- [ ] Mindestens 3 Funktionen implementiert
- [ ] Benutzerfreundliche Ausgabe
- [ ] Code ist kommentiert

## 🎉 Herzlichen Glückwunsch!

Sie haben den Python-Einführungskurs abgeschlossen!

**Sie können jetzt:**
- ✅ Python-Programme schreiben
- ✅ Mit Datentypen arbeiten
- ✅ Kontrollstrukturen nutzen
- ✅ Funktionen definieren
- ✅ Datenstrukturen verwenden
- ✅ Dateien verarbeiten
- ✅ Module erstellen

**Weiter geht's:** [Hausaufgaben](../03-nachbearbeitung/)

