# Erste Experimente: Dateien & Module

**Zeitaufwand:** 60 Minuten

## Experiment 1: Textdatei (15 Min)

Erstellen Sie eine Datei `tagebuch.txt` und schreiben Sie 3 Einträge hinein.
Lesen Sie dann die Datei und geben Sie alle Einträge aus.

```python
# Schreiben
with open("tagebuch.txt", "w") as f:
    f.write("Tag 1: Heute war ein guter Tag\n")
    f.write("Tag 2: Python macht Spass\n")
    f.write("Tag 3: Bald fertig mit dem Kurs\n")

# Lesen
with open("tagebuch.txt", "r") as f:
    print(f.read())
```

## Experiment 2: CSV-Datei (15 Min)

Erstellen Sie eine CSV-Datei mit Ihren Lieblingsbüchern.

```python
import csv

buecher = [
    ["Titel", "Autor", "Jahr"],
    ["1984", "George Orwell", "1949"],
    ["Python Basics", "Max Muster", "2025"]
]

with open("buecher.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(buecher)
```

## Experiment 3: JSON-Datei (15 Min)

Speichern Sie Ihre Kontaktdaten als JSON.

```python
import json

kontakt = {
    "name": "Ihr Name",
    "email": "ihre@email.com",
    "hobbies": ["Hobby1", "Hobby2"]
}

with open("kontakt.json", "w") as f:
    json.dump(kontakt, f, indent=2)

# Wieder einlesen
with open("kontakt.json", "r") as f:
    daten = json.load(f)
    print(daten)
```

## Experiment 4: Eigenes Modul (15 Min)

Erstellen Sie `rechner.py`:

```python
def addiere(a, b):
    return a + b

def multipliziere(a, b):
    return a * b
```

Verwenden Sie es:

```python
import rechner

print(rechner.addiere(5, 3))
print(rechner.multipliziere(4, 7))
```
