# Handout: Dateien

## Textdateien

```python
# Lesen
with open("datei.txt", "r") as f:
    inhalt = f.read()

# Schreiben
with open("datei.txt", "w") as f:
    f.write("Text\n")
```

## CSV

```python
import csv

with open("daten.csv", "r") as f:
    reader = csv.reader(f)
    for zeile in reader:
        print(zeile)
```

## JSON

```python
import json

with open("daten.json", "w") as f:
    json.dump({"key": "value"}, f)
```
