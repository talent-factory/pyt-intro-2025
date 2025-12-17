# VS Code Konfiguration für pyt-intro-2025

## Python Interpreter auswählen

Falls VS Code die virtuelle Umgebung nicht automatisch erkennt:

1. **Command Palette öffnen**: `Cmd+Shift+P` (macOS) oder `Ctrl+Shift+P` (Windows/Linux)
2. **"Python: Select Interpreter"** eingeben
3. Die Option **`.venv/bin/python`** auswählen

## Probleme mit Import-Fehlern beheben

### Schritt 1: Python Extension neu laden

1. Command Palette öffnen: `Cmd+Shift+P`
2. **"Developer: Reload Window"** eingeben und ausführen

### Schritt 2: Pylance Language Server neu starten

1. Command Palette öffnen: `Cmd+Shift+P`
2. **"Python: Restart Language Server"** eingeben und ausführen

### Schritt 3: Virtuelle Umgebung manuell aktivieren

Im Terminal:

```bash
source .venv/bin/activate
```

Dann sollte im Terminal `(.venv)` vor dem Prompt erscheinen.

### Schritt 4: Tests ausführen

```bash
# Alle Tests
pytest

# Nur Modul 3 Tests
pytest tests/modul-3/ -v

# Einzelne Test-Datei
pytest tests/modul-3/test_alle_module.py -v
```

## Konfigurationsdateien

- **`.vscode/settings.json`**: VS Code Einstellungen für Python, Ruff, Testing
- **`pyrightconfig.json`**: Type-Checking Konfiguration für Pylance
- **`.env`**: Umgebungsvariablen (PYTHONPATH)
- **`pyproject.toml`**: Projekt-Dependencies und Ruff-Konfiguration

## Installierte Extensions (empfohlen)

Siehe `.vscode/extensions.json`:

- **Python** (ms-python.python)
- **Pylance** (ms-python.vscode-pylance)
- **Ruff** (charliermarsh.ruff)
- **Jupyter** (ms-toolsai.jupyter)

## Troubleshooting

### Import-Fehler trotz korrekter Konfiguration

1. Prüfen Sie, ob die `.venv` aktiviert ist:
   ```bash
   which python
   # Sollte zeigen: /Users/daniel/GitRepository/pyt-intro-2025/.venv/bin/python
   ```

2. Prüfen Sie, ob pytest installiert ist:
   ```bash
   .venv/bin/pytest --version
   # Sollte zeigen: pytest 9.0.2
   ```

3. Synchronisieren Sie die Dependencies:
   ```bash
   uv sync
   ```

### Rote Wellenlinien bei Imports in Test-Dateien

Dies ist normal, wenn die Test-Dateien Module aus den `05-beispiele` Ordnern importieren.
Die `pyrightconfig.json` ist so konfiguriert, dass diese Pfade erkannt werden.

Falls die Fehler bestehen bleiben:
1. VS Code neu laden (siehe oben)
2. Pylance neu starten (siehe oben)

## Weitere Hilfe

Bei weiteren Problemen:
- Prüfen Sie die Output-Konsole: `View > Output` > "Python" auswählen
- Prüfen Sie die Problems-Ansicht: `View > Problems`

