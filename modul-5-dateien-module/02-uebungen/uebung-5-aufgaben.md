# Übung: Aufgabenliste JSON

**Dauer:** 15 Minuten

Erstellen Sie eine Aufgabenliste in JSON:

```python
import json

aufgaben = [
    {"titel": "Python lernen", "erledigt": False},
    {"titel": "Einkaufen", "erledigt": True}
]

with open("aufgaben.json", "w") as f:
    json.dump(aufgaben, f, indent=2)
```

Lesen Sie die Datei und zeigen Sie nur unerledigte Aufgaben.

<details>
<summary><b>Lösung anzeigen</b></summary>

```python
import json

with open("aufgaben.json", "r") as f:
    aufgaben = json.load(f)

print("Unerledigte Aufgaben:")
for aufgabe in aufgaben:
    if not aufgabe["erledigt"]:
        print(f"- {aufgabe['titel']}")
```

</details>

