# Übung: Konfiguration JSON

**Dauer:** 15 Minuten

Erstellen Sie Funktionen zum Laden und Speichern von Einstellungen:

**Lösung:**
```python
import json

def config_laden():
    try:
        with open("config.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {"sprache": "de", "theme": "hell"}

def config_speichern(config):
    with open("config.json", "w") as f:
        json.dump(config, f, indent=2)

# Test
config = config_laden()
config["sprache"] = "en"
config_speichern(config)
```

