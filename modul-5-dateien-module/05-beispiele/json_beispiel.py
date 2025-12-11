"""
Beispiel: JSON-Dateien

Zeigt:
- JSON lesen und schreiben
- Verschachtelte Datenstrukturen
- Konfigurationsverwaltung
"""

import json

def config_erstellen() -> None:
    """Erstellt Standard-Konfiguration."""
    config = {
        "app": {
            "name": "Meine App",
            "version": "1.0.0"
        },
        "einstellungen": {
            "sprache": "de",
            "theme": "hell",
            "benachrichtigungen": True
        },
        "benutzer": {
            "name": "Max Muster",
            "email": "max@example.com"
        }
    }

    with open("config.json", "w") as f:
        json.dump(config, f, indent=2, ensure_ascii=False)

    print("✓ Konfiguration erstellt")

def config_laden() -> dict | None:
    """Lädt Konfiguration."""
    try:
        with open("config.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return None

def config_anzeigen() -> None:
    """Zeigt Konfiguration."""
    config = config_laden()
    if config:
        print("\n" + "=" * 50)
        print("KONFIGURATION")
        print("=" * 50)
        print(json.dumps(config, indent=2, ensure_ascii=False))

def einstellung_aendern(kategorie: str, key: str, wert: str | bool | int) -> None:
    """Ändert eine Einstellung."""
    config = config_laden()
    if config and kategorie in config:
        config[kategorie][key] = wert
        with open("config.json", "w") as f:
            json.dump(config, f, indent=2, ensure_ascii=False)
        print(f"✓ {kategorie}.{key} = {wert}")

if __name__ == "__main__":
    print("=" * 50)
    print("JSON DEMO")
    print("=" * 50)
    
    config_erstellen()
    config_anzeigen()
    
    einstellung_aendern("einstellungen", "sprache", "en")
    config_anzeigen()
