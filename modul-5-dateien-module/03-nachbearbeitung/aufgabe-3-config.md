# Hausaufgabe: Konfigurationsverwaltung


Erstellen Sie ein System zur Verwaltung von Programmeinstellungen.

**Anforderungen:**

1. Einstellungen in JSON speichern
2. Funktionen:
   - `config_laden()` - Lädt Einstellungen
   - `config_speichern()` - Speichert Einstellungen
   - `einstellung_aendern(key, value)` - Ändert Wert
   - `einstellungen_anzeigen()` - Zeigt alle
   - `reset_defaults()` - Setzt auf Standard zurück

**Standard-Einstellungen:**
```json
{
  "sprache": "de",
  "theme": "hell",
  "benachrichtigungen": true,
  "auto_save": true,
  "max_eintraege": 100
}
```

**Zeitaufwand:** 2 Stunden

**Erweiterungen:**
- Validierung (z.B. sprache nur "de" oder "en")
- Backup vor Änderungen
- Import/Export

