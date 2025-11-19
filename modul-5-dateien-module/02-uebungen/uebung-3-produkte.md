# Übung: Produktliste CSV

**Dauer:** 15 Minuten

Erstellen Sie eine CSV-Datei mit Produkten:

```python
import csv

produkte = [
    ["Name", "Preis", "Menge"],
    ["Apfel", "2.50", "10"],
    ["Banane", "3.00", "5"]
]

with open("produkte.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(produkte)
```

Lesen Sie dann die Datei und berechnen Sie den Gesamtwert.

**Lösung:**
```python
import csv

gesamt = 0
with open("produkte.csv", "r") as f:
    reader = csv.reader(f)
    next(reader)  # Header überspringen
    for zeile in reader:
        preis = float(zeile[1])
        menge = int(zeile[2])
        gesamt += preis * menge

print(f"Gesamtwert: {gesamt:.2f} CHF")
```

