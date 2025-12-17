# Ruff - Code-Formatierung und Linting

## Übersicht

Ruff ist ein extrem schneller Python Linter und Code-Formatter, der in diesem Projekt verwendet wird.

## Verfügbare Skripte

### 1. Code prüfen (ohne Änderungen)

```bash
./check_code.sh
```

**Was macht es:**
- Prüft alle Python-Dateien auf Linting-Fehler
- Prüft, ob der Code korrekt formatiert ist
- **Ändert keine Dateien**
- Exit Code 0 = alles OK, Exit Code 1 = Probleme gefunden

**Wann verwenden:**
- Vor einem Commit
- In CI/CD Pipeline
- Um zu sehen, was geändert werden würde

### 2. Code automatisch korrigieren

```bash
./format_code.sh
```

**Was macht es:**
1. **Linting mit Auto-Fix**: Behebt automatisch behebbare Fehler
   - Entfernt Whitespace in leeren Zeilen
   - Sortiert Imports
   - Ersetzt veraltete Syntax (z.B. `format()` → f-strings)
   - Fügt fehlende Newlines am Dateiende hinzu

2. **Code-Formatierung**: Formatiert den Code nach PEP 8
   - Einheitliche Einrückung
   - Konsistente Zeilenlänge (88 Zeichen)
   - Einheitliche Anführungszeichen

3. **Finale Prüfung**: Zeigt verbleibende Probleme an

**Wann verwenden:**
- Nach größeren Code-Änderungen
- Vor einem Pull Request
- Um alle Dateien auf einmal zu formatieren

## Manuelle Ruff-Befehle

### Nur Linting (mit Auto-Fix)

```bash
# Alle Dateien
.venv/bin/ruff check . --fix

# Nur eine Datei
.venv/bin/ruff check modul-1-einstieg/05-beispiele/hello_world.py --fix

# Nur ein Verzeichnis
.venv/bin/ruff check modul-3-kontrollstrukturen/ --fix
```

### Nur Formatierung

```bash
# Alle Dateien
.venv/bin/ruff format .

# Nur eine Datei
.venv/bin/ruff format modul-1-einstieg/05-beispiele/hello_world.py

# Nur prüfen (ohne zu ändern)
.venv/bin/ruff format . --check
```

### Nur prüfen (ohne Änderungen)

```bash
# Linting
.venv/bin/ruff check .

# Formatierung
.venv/bin/ruff format . --check
```

## Häufige Fehler und Fixes

### W293: Blank line contains whitespace
**Problem:** Leere Zeilen enthalten Leerzeichen oder Tabs
**Fix:** Automatisch mit `--fix`

### F541: f-string without any placeholders
**Problem:** f-String ohne Platzhalter (z.B. `f"Hallo"` statt `"Hallo"`)
**Fix:** Automatisch mit `--fix`

### I001: Import block is un-sorted or un-formatted
**Problem:** Imports sind nicht sortiert
**Fix:** Automatisch mit `--fix`

### UP032: Use f-string instead of `format` call
**Problem:** Veraltete `.format()` Methode
**Fix:** Automatisch mit `--fix`

### E721: Use `is` and `is not` for type comparisons
**Problem:** `type(x) == int` statt `isinstance(x, int)`
**Fix:** Manuell ändern (nicht automatisch)

### F401: Module imported but unused
**Problem:** Import wird nicht verwendet
**Fix:** Manuell entfernen oder mit `# noqa: F401` markieren

## Konfiguration

Die Ruff-Konfiguration befindet sich in `pyproject.toml`:

```toml
[tool.ruff]
target-version = "py310"
line-length = 88

[tool.ruff.lint]
select = ["E", "W", "F", "I", "N", "UP"]
ignore = ["E501", "E741"]
```

### Aktivierte Regeln:
- **E**: pycodestyle Fehler (PEP 8)
- **W**: pycodestyle Warnungen
- **F**: Pyflakes (logische Fehler)
- **I**: isort (Import-Sortierung)
- **N**: pep8-naming (Namenskonventionen)
- **UP**: pyupgrade (moderne Python-Syntax)

### Ignorierte Regeln:
- **E501**: Zeile zu lang (wird automatisch formatiert)
- **E741**: Mehrdeutige Variablennamen (für Anfänger OK)

## VS Code Integration

Ruff ist in VS Code integriert (siehe `.vscode/settings.json`):

- **Format on Save**: Automatische Formatierung beim Speichern
- **Auto-Fix on Save**: Automatische Fehlerkorrektur beim Speichern
- **Import Organization**: Automatische Import-Sortierung

## Tipps

1. **Vor jedem Commit**: `./check_code.sh` ausführen
2. **Nach größeren Änderungen**: `./format_code.sh` ausführen
3. **In VS Code**: Code wird automatisch beim Speichern formatiert
4. **CI/CD**: `./check_code.sh` in Pipeline einbauen

## Weitere Informationen

- [Ruff Dokumentation](https://docs.astral.sh/ruff/)
- [Ruff Rules](https://docs.astral.sh/ruff/rules/)
- [PEP 8 Style Guide](https://peps.python.org/pep-0008/)

