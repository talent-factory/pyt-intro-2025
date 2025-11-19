# Lektion 3: JSON-Dateien

**Dauer:** 50 Minuten  
**Format:** 15 Min Theorie + 20 Min Live-Coding + 15 Min Übung

## 🎯 Lernziele

- JSON-Format verstehen
- JSON-Dateien lesen und schreiben
- Python-Datenstrukturen in JSON konvertieren
- Verschachtelte JSON-Daten verarbeiten

## 📖 Theorie (15 Min)

### Was ist JSON?

JSON = **J**ava**S**cript **O**bject **N**otation

Beispiel `person.json`:
```json
{
  "name": "Anna Muster",
  "alter": 25,
  "hobbies": ["Lesen", "Sport", "Musik"],
  "adresse": {
    "strasse": "Hauptstrasse 1",
    "stadt": "Zürich"
  }
}
```

### JSON-Modul

```python
import json
```

### Python → JSON (Serialisierung)

```python
import json

person = {
    "name": "Anna",
    "alter": 25,
    "hobbies": ["Lesen", "Sport"]
}

# In Datei schreiben
with open("person.json", "w") as f:
    json.dump(person, f, indent=2)

# Als String
json_string = json.dumps(person, indent=2)
```

### JSON → Python (Deserialisierung)

```python
import json

# Aus Datei lesen
with open("person.json", "r") as f:
    person = json.load(f)

# Aus String
json_string = '{"name": "Anna", "alter": 25}'
person = json.loads(json_string)
```

### Datentyp-Mapping

| Python | JSON |
|--------|------|
| dict | object |
| list | array |
| str | string |
| int, float | number |
| True/False | true/false |
| None | null |

## 💻 Live-Coding (20 Min)

### Beispiel 1: Einstellungen speichern

```python
import json

def einstellungen_laden(dateiname="config.json"):
    """Lädt Einstellungen aus JSON."""
    try:
        with open(dateiname, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        # Standard-Einstellungen
        return {
            "sprache": "de",
            "theme": "hell",
            "benachrichtigungen": True
        }

def einstellungen_speichern(einstellungen, dateiname="config.json"):
    """Speichert Einstellungen in JSON."""
    with open(dateiname, "w") as f:
        json.dump(einstellungen, f, indent=2)
    print("✓ Einstellungen gespeichert")

# Verwendung
config = einstellungen_laden()
print(f"Aktuelle Sprache: {config['sprache']}")

config["sprache"] = "en"
einstellungen_speichern(config)
```

### Beispiel 2: Kontakte mit JSON

```python
import json

def kontakte_laden(dateiname="kontakte.json"):
    """Lädt Kontakte aus JSON."""
    try:
        with open(dateiname, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def kontakte_speichern(kontakte, dateiname="kontakte.json"):
    """Speichert Kontakte in JSON."""
    with open(dateiname, "w") as f:
        json.dump(kontakte, f, indent=2, ensure_ascii=False)

def neuer_kontakt(kontakte):
    """Fügt neuen Kontakt hinzu."""
    kontakt = {
        "name": input("Name: "),
        "email": input("Email: "),
        "telefon": input("Telefon: "),
        "tags": input("Tags (komma-getrennt): ").split(",")
    }
    kontakte.append(kontakt)
    return kontakte

# Hauptprogramm
kontakte = kontakte_laden()
kontakte = neuer_kontakt(kontakte)
kontakte_speichern(kontakte)
```

### Beispiel 3: Verschachtelte Daten

```python
import json

# Komplexe Datenstruktur
kurs = {
    "name": "Python Basics",
    "dauer_wochen": 5,
    "teilnehmer": [
        {
            "name": "Anna",
            "noten": [5.5, 6.0, 5.0],
            "anwesend": True
        },
        {
            "name": "Max",
            "noten": [4.5, 5.0, 5.5],
            "anwesend": True
        }
    ]
}

# Speichern
with open("kurs.json", "w") as f:
    json.dump(kurs, f, indent=2, ensure_ascii=False)

# Laden und verarbeiten
with open("kurs.json", "r") as f:
    kurs_daten = json.load(f)

print(f"Kurs: {kurs_daten['name']}")
for teilnehmer in kurs_daten["teilnehmer"]:
    avg = sum(teilnehmer["noten"]) / len(teilnehmer["noten"])
    print(f"  {teilnehmer['name']}: {avg:.2f}")
```

## ✏️ Übungen (15 Min)

- [Übung 5: Aufgabenliste](../02-uebungen/uebung-5-aufgaben.md)
- [Übung 6: Konfiguration](../02-uebungen/uebung-6-config.md)

## 📚 Zusammenfassung

- JSON für strukturierte Daten
- `json.dump()` / `json.load()` für Dateien
- `json.dumps()` / `json.loads()` für Strings
- `indent=2` für lesbare Formatierung
- `ensure_ascii=False` für Umlaute

## 🔗 Weiter

- [Lektion 4: Module & Imports](./lektion-4-module.md)

