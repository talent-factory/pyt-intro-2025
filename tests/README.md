# Test-Suite für Python-Intro-2025

Diese Test-Suite testet vollständige Python-Programme aus den Modulen 1-5 des Python-Programmierung Basis Kurses. Modul 6 hat aktuell keine Tests.

## Übersicht

### Abgedeckte Module

- **Modul 1 (Einstieg)**: 10 Programme, 10 Test-Dateien
- **Modul 2 (Datentypen)**: 5 Programme, 5 Test-Dateien
- **Modul 3 (Kontrollstrukturen)**: 10 Programme, 1 konsolidierte Test-Datei
- **Modul 4 (Funktionen und Datenstrukturen)**: 10 Programme, 10 Test-Dateien
- **Modul 5 (Dateien und Module)**: 4 Programme, 4 Test-Dateien
- **Modul 6 (KI-Programmieren)**: keine Tests

**Gesamt:** 39 Programme getestet (Modul 1–5)

### Test-Struktur

```
tests/
├── README.md                    # Diese Datei
├── conftest.py                  # Gemeinsame Fixtures
├── __init__.py
├── modul-1/                     # Tests für Modul 1
│   ├── __init__.py
│   ├── test_hello_world.py
│   ├── test_variablen.py
│   ├── test_datentypen.py
│   ├── test_operatoren.py
│   ├── test_berechnungen.py
│   ├── test_taschenrechner.py
│   ├── test_temperatur.py
│   ├── test_altersrechner.py
│   ├── test_waehrungsrechner.py
│   └── test_bmi_rechner.py
├── modul-2/                     # Tests für Modul 2
│   ├── __init__.py
│   ├── test_strings.py
│   ├── test_formatierung.py
│   ├── test_vergleiche.py
│   ├── test_typkonvertierung.py
│   └── test_input_output.py
├── modul-3/                     # Tests für Modul 3
│   ├── __init__.py
│   └── test_alle_module.py
├── modul-4/                     # Tests für Modul 4
│   ├── test_dictionaries.py
│   ├── test_email_validator.py
│   ├── test_funktionen_basis.py
│   ├── test_listen_operationen.py
│   ├── test_parameter.py
│   ├── test_passwort_validator.py
│   ├── test_tabelle.py
│   ├── test_testen_beispiel.py
│   ├── test_textstatistik.py
│   └── test_tupel_sets.py
└── modul-5/                     # Tests für Modul 5
    ├── test_csv_beispiel.py
    ├── test_json_beispiel.py
    ├── test_notizen_app.py
    └── test_textdateien.py
```

## Installation

### Voraussetzungen

- Python 3.10 oder höher
- pip (Python Package Manager)

### pytest installieren

```bash
pip install pytest pytest-cov
```

Oder mit requirements.txt (falls vorhanden):

```bash
pip install -r requirements.txt
```

## Tests ausführen

### Alle Tests ausführen

```bash
# Im Projekt-Root-Verzeichnis
pytest
```

### Tests mit ausführlicher Ausgabe

```bash
pytest -v
```

### Tests für ein bestimmtes Modul

```bash
# Nur Modul 1
pytest tests/modul-1/

# Nur Modul 2
pytest tests/modul-2/

# Nur Modul 3
pytest tests/modul-3/

# Nur Modul 4
pytest tests/modul-4/

# Nur Modul 5
pytest tests/modul-5/
```

### Tests mit Marker ausführen

```bash
# Nur Modul 1 Tests
pytest -m modul1

# Nur Modul 2 Tests
pytest -m modul2

# Nur Modul 3 Tests
pytest -m modul3

# Nur Modul 4 Tests
pytest -m modul4

# Nur Modul 5 Tests
pytest -m modul5
```

### Einzelne Test-Datei ausführen

```bash
pytest tests/modul-1/test_temperatur.py
```

### Einzelnen Test ausführen

```bash
pytest tests/modul-1/test_temperatur.py::test_celsius_zu_fahrenheit
```

### Tests mit Coverage-Report

```bash
# Coverage-Report in Terminal
pytest --cov=modul-1-einstieg --cov=modul-2-datentypen --cov=modul-3-kontrollstrukturen --cov=modul-4-funktionen-datenstrukturen --cov=modul-5-dateien-module

# HTML-Coverage-Report erstellen
pytest --cov=modul-1-einstieg --cov=modul-2-datentypen --cov=modul-3-kontrollstrukturen --cov=modul-4-funktionen-datenstrukturen --cov=modul-5-dateien-module --cov-report=html

# HTML-Report öffnen
open htmlcov/index.html
```

## Test-Kategorien

### Import-Tests

Prüfen, ob Module ohne Fehler importiert werden können.

```python
def test_modul_import():
    """Test: Modul kann importiert werden."""
    import hello_world
    assert True
```

### Funktions-Tests

Testen spezifische Funktionen mit verschiedenen Inputs.

```python
@pytest.mark.parametrize("celsius,expected_fahrenheit", [
    (0, 32),
    (25, 77),
    (100, 212),
])
def test_celsius_zu_fahrenheit(celsius, expected_fahrenheit):
    fahrenheit = (celsius * 9 / 5) + 32
    assert abs(fahrenheit - expected_fahrenheit) < 0.1
```

### Edge-Case-Tests

Testen Grenzfälle und spezielle Situationen.

```python
def test_division_durch_null():
    """Test: Division durch Null wird korrekt behandelt."""
    with pytest.raises(ZeroDivisionError):
        result = 10 / 0
```

### Datentyp-Tests

Prüfen, ob Rückgabewerte den erwarteten Typ haben.

```python
def test_typ_ermitteln():
    """Test: type() ermittelt den Typ korrekt."""
    assert type(42) == int
    assert type(3.14) == float
```

## Besonderheiten

### Interaktive Programme

Programme mit `input()` verwenden Mocking:

```python
from unittest.mock import patch

def test_mit_input():
    with patch('builtins.input', return_value='42'):
        # Code der input() aufruft
        alter = input("Alter: ")
        assert alter == "42"
```

### Programme mit Endlosschleifen

Programme mit `while True` werden beim Import gemockt:

```python
with patch('builtins.input', return_value='q'):
    import menu  # Beendet die Schleife mit 'q'
```

### Output-Capturing

Ausgaben werden erfasst und geprüft:

```python
import sys
from io import StringIO

old_stdout = sys.stdout
sys.stdout = captured = StringIO()

# Code ausführen
print("Test")

output = captured.getvalue()
sys.stdout = old_stdout

assert "Test" in output
```

## Pytest-Konfiguration

Die Konfiguration befindet sich in `pytest.ini`:

```ini
[pytest]
testpaths = tests
python_files = test_*.py
python_classes = Test*
python_functions = test_*

addopts =
    -v
    --tb=short
    --strict-markers
    --disable-warnings
    --color=yes

markers =
    modul1: Tests für Modul 1 (Einstieg)
    modul2: Tests für Modul 2 (Datentypen)
    modul3: Tests für Modul 3 (Kontrollstrukturen)
    modul4: Tests für Modul 4 (Funktionen und Datenstrukturen)
    modul5: Tests für Modul 5 (Dateien und Module)
    modul6: Tests für Modul 6 (KI-Programmieren)
    slow: Langsam laufende Tests
    integration: Integrationstests
```

## Nützliche pytest-Optionen

| Option | Beschreibung |
|--------|--------------|
| `-v` | Verbose Output (detailliert) |
| `-s` | Zeige print()-Ausgaben |
| `-x` | Stoppe bei erstem Fehler |
| `--lf` | Führe nur fehlgeschlagene Tests aus |
| `--ff` | Führe fehlgeschlagene zuerst aus |
| `-k EXPRESSION` | Führe nur Tests aus, die EXPRESSION matchen |
| `--collect-only` | Zeige alle Tests ohne sie auszuführen |
| `-m MARKER` | Führe nur Tests mit MARKER aus |

### Beispiele

```bash
# Stoppe beim ersten Fehler
pytest -x

# Zeige print()-Ausgaben
pytest -s

# Führe nur Tests aus, die "temperatur" im Namen haben
pytest -k temperatur

# Zeige alle verfügbaren Tests
pytest --collect-only

# Führe nur fehlgeschlagene Tests erneut aus
pytest --lf
```

## Erwartete Ergebnisse

Bei erfolgreicher Ausführung sollten Sie sehen:

```
============================= test session starts ==============================
platform darwin -- Python 3.12.x, pytest-8.x.x
collected XXX items

tests/modul-1/test_hello_world.py ....                                   [  4%]
tests/modul-1/test_variablen.py ...                                      [  8%]
...
tests/modul-3/test_alle_module.py ............................           [100%]

============================== XXX passed in X.XXs ==============================
```

## Troubleshooting

### Import-Fehler

**Problem**: `ImportError: No module named '...'`

**Lösung**: Stellen Sie sicher, dass Sie sich im Projekt-Root befinden:

```bash
cd /path/to/pyt-intro-2025
pytest
```

### Input-Tests schlagen fehl

**Problem**: Tests mit `input()` hängen oder schlagen fehl

**Lösung**: Diese Tests verwenden Mocking. Wenn sie fehlschlagen, wird der Test mit `pytest.skip()` übersprungen.

### Encoding-Fehler

**Problem**: `UnicodeDecodeError`

**Lösung**: Stellen Sie sicher, dass Python UTF-8 verwendet:

```bash
export PYTHONIOENCODING=utf-8
pytest
```

## Weitere Informationen

- [pytest Dokumentation](https://docs.pytest.org/)
- [pytest parametrize](https://docs.pytest.org/en/stable/parametrize.html)
- [pytest fixtures](https://docs.pytest.org/en/stable/fixture.html)
- [unittest.mock](https://docs.python.org/3/library/unittest.mock.html)

## Erweiterungen

### Eigene Tests hinzufügen

1. Erstellen Sie eine neue Datei `test_*.py` im entsprechenden Modul-Ordner
2. Importieren Sie pytest und das zu testende Modul
3. Schreiben Sie Testfunktionen mit `test_*` Präfix
4. Verwenden Sie `@pytest.mark.modul*` Marker

Beispiel:

```python
import pytest

@pytest.mark.modul1
def test_mein_neuer_test():
    """Test: Beschreibung."""
    assert 1 + 1 == 2
```

### Continuous Integration

Diese Tests können in CI/CD-Pipelines integriert werden:

**GitHub Actions** (`.github/workflows/tests.yml`):

```yaml
name: Tests
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - uses: actions/setup-python@v2
        with:
          python-version: '3.12'
      - run: pip install pytest pytest-cov
      - run: pytest --cov
```

## Kontakt

Bei Fragen zu den Tests wenden Sie sich an den Kursleiter.

---

**Viel Erfolg beim Testen!** 🎉
