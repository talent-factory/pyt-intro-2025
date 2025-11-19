# Leseauftrag Modul 5: Dateien & Module

**Zeitaufwand:** 60-90 Minuten

## 1. Dateien lesen und schreiben

### Dateien öffnen

```python
# Lesen
datei = open("text.txt", "r")
inhalt = datei.read()
datei.close()

# Besser: Context Manager
with open("text.txt", "r") as datei:
    inhalt = datei.read()
# Datei wird automatisch geschlossen
```

### Modi

- `"r"` - Lesen (read)
- `"w"` - Schreiben (write, überschreibt!)
- `"a"` - Anhängen (append)
- `"r+"` - Lesen und Schreiben

### Lesen

```python
# Alles lesen
with open("datei.txt", "r") as f:
    inhalt = f.read()

# Zeile für Zeile
with open("datei.txt", "r") as f:
    for zeile in f:
        print(zeile.strip())

# Alle Zeilen als Liste
with open("datei.txt", "r") as f:
    zeilen = f.readlines()
```

### Schreiben

```python
with open("ausgabe.txt", "w") as f:
    f.write("Hallo Welt!\n")
    f.write("Zweite Zeile\n")

# Mehrere Zeilen
zeilen = ["Zeile 1\n", "Zeile 2\n"]
with open("ausgabe.txt", "w") as f:
    f.writelines(zeilen)
```

## 2. CSV-Dateien

CSV = Comma-Separated Values (Tabellendaten)

```python
import csv

# Lesen
with open("daten.csv", "r") as f:
    reader = csv.reader(f)
    for zeile in reader:
        print(zeile)

# Schreiben
daten = [
    ["Name", "Alter", "Stadt"],
    ["Anna", "25", "Zürich"],
    ["Max", "30", "Bern"]
]

with open("ausgabe.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(daten)
```

## 3. JSON-Dateien

JSON = JavaScript Object Notation (strukturierte Daten)

```python
import json

# Python → JSON
person = {
    "name": "Anna",
    "alter": 25,
    "hobbies": ["Lesen", "Sport"]
}

with open("person.json", "w") as f:
    json.dump(person, f, indent=2)

# JSON → Python
with open("person.json", "r") as f:
    daten = json.load(f)
    print(daten["name"])
```

## 4. Module

### Importieren

```python
# Ganzes Modul
import math
print(math.pi)

# Spezifische Funktionen
from math import sqrt, pi
print(sqrt(16))

# Mit Alias
import datetime as dt
heute = dt.date.today()
```

### Eigene Module

Datei `mein_modul.py`:
```python
def gruesse(name):
    return f"Hallo {name}!"

PI = 3.14159
```

Verwendung:
```python
import mein_modul

print(mein_modul.gruesse("Anna"))
print(mein_modul.PI)
```

## 5. Wichtige Standard-Module

- `os` - Betriebssystem-Funktionen
- `sys` - System-Parameter
- `datetime` - Datum und Zeit
- `random` - Zufallszahlen
- `json` - JSON-Verarbeitung
- `csv` - CSV-Verarbeitung
- `math` - Mathematische Funktionen

## Zusammenfassung

- Dateien immer mit `with` öffnen
- CSV für Tabellen, JSON für strukturierte Daten
- Module mit `import` einbinden
- Eigene Module erstellen für Wiederverwendung
