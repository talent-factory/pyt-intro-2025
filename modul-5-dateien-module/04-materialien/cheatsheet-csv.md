# Cheatsheet: CSV

```python
import csv

# Lesen
with open("daten.csv", "r") as f:
    reader = csv.reader(f)
    for zeile in reader:
        print(zeile)

# Schreiben
with open("daten.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Alter"])
    writer.writerow(["Anna", "25"])
```
