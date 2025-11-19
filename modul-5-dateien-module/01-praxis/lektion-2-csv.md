# Lektion 2: CSV-Dateien

**Dauer:** 50 Minuten  
**Format:** 15 Min Theorie + 20 Min Live-Coding + 15 Min Übung

## 🎯 Lernziele

- CSV-Format verstehen
- CSV-Dateien lesen
- CSV-Dateien schreiben
- Mit Headern arbeiten

## 📖 Theorie (15 Min)

### Was ist CSV?

CSV = **C**omma-**S**eparated **V**alues

Beispiel `kontakte.csv`:
```
Name,Email,Telefon
Anna Muster,anna@example.com,079 123 45 67
Max Meier,max@example.com,078 987 65 43
```

### CSV-Modul

```python
import csv
```

### CSV lesen

```python
import csv

with open("daten.csv", "r") as f:
    reader = csv.reader(f)
    for zeile in reader:
        print(zeile)  # Liste: ['Name', 'Email', 'Telefon']
```

### CSV schreiben

```python
import csv

daten = [
    ["Name", "Alter", "Stadt"],
    ["Anna", "25", "Zürich"],
    ["Max", "30", "Bern"]
]

with open("ausgabe.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(daten)
```

**Wichtig:** `newline=""` verhindert Leerzeilen!

### DictReader & DictWriter

```python
import csv

# Lesen als Dictionary
with open("daten.csv", "r") as f:
    reader = csv.DictReader(f)
    for zeile in reader:
        print(zeile["Name"], zeile["Email"])

# Schreiben als Dictionary
daten = [
    {"name": "Anna", "alter": 25},
    {"name": "Max", "alter": 30}
]

with open("ausgabe.csv", "w", newline="") as f:
    fieldnames = ["name", "alter"]
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(daten)
```

## 💻 Live-Coding (20 Min)

### Beispiel 1: Kontakte verwalten

```python
import csv

def kontakte_laden(dateiname):
    """Lädt Kontakte aus CSV."""
    kontakte = []
    try:
        with open(dateiname, "r") as f:
            reader = csv.DictReader(f)
            for zeile in reader:
                kontakte.append(zeile)
    except FileNotFoundError:
        pass
    return kontakte

def kontakte_speichern(dateiname, kontakte):
    """Speichert Kontakte in CSV."""
    with open(dateiname, "w", newline="") as f:
        fieldnames = ["name", "email", "telefon"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(kontakte)

def neuer_kontakt(kontakte):
    """Fügt neuen Kontakt hinzu."""
    name = input("Name: ")
    email = input("Email: ")
    telefon = input("Telefon: ")
    
    kontakte.append({
        "name": name,
        "email": email,
        "telefon": telefon
    })
    print("✓ Kontakt hinzugefügt")

# Hauptprogramm
kontakte = kontakte_laden("kontakte.csv")
neuer_kontakt(kontakte)
kontakte_speichern("kontakte.csv", kontakte)
```

### Beispiel 2: Noten verwalten

```python
import csv

def noten_laden(dateiname):
    """Lädt Noten aus CSV."""
    with open(dateiname, "r") as f:
        reader = csv.reader(f)
        next(reader)  # Header überspringen
        noten = {}
        for zeile in reader:
            name = zeile[0]
            noten[name] = [float(n) for n in zeile[1:]]
    return noten

def durchschnitt_berechnen(noten):
    """Berechnet Durchschnitt für alle."""
    for name, werte in noten.items():
        avg = sum(werte) / len(werte)
        print(f"{name}: {avg:.2f}")

# Verwendung
noten = noten_laden("noten.csv")
durchschnitt_berechnen(noten)
```

## ✏️ Übungen (15 Min)

- [Übung 3: Produktliste](../02-uebungen/uebung-3-produkte.md)
- [Übung 4: Notenauswertung](../02-uebungen/uebung-4-noten.md)

## 📚 Zusammenfassung

- CSV für Tabellendaten
- `csv.reader()` und `csv.writer()`
- `csv.DictReader()` für benannte Spalten
- `newline=""` beim Schreiben!

## 🔗 Weiter

- [Lektion 3: JSON-Dateien](./lektion-3-json.md)

