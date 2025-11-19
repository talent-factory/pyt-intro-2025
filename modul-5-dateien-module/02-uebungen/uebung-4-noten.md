# Übung: Notenauswertung CSV

**Dauer:** 15 Minuten

Gegeben: `noten.csv` mit Spalten: Name, Note1, Note2, Note3

Berechnen Sie für jeden Studenten den Durchschnitt.

**Lösung:**
```python
import csv

with open("noten.csv", "r") as f:
    reader = csv.DictReader(f)
    for zeile in reader:
        noten = [float(zeile["Note1"]), 
                 float(zeile["Note2"]), 
                 float(zeile["Note3"])]
        avg = sum(noten) / len(noten)
        print(f"{zeile['Name']}: {avg:.2f}")
```

