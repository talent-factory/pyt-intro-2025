# Cheatsheet: JSON

```python
import json

# Schreiben
daten = {"name": "Anna", "alter": 25}
with open("daten.json", "w") as f:
    json.dump(daten, f, indent=2)

# Lesen
with open("daten.json", "r") as f:
    daten = json.load(f)
```
