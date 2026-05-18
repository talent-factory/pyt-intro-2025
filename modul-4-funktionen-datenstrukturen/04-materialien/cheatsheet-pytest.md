# Cheatsheet: Testing mit pytest

## Test schreiben

```python
# Datei: test_rechner.py (muss mit test_ beginnen!)

def addiere(a, b):
    return a + b

def test_addiere():           # Funktion muss mit test_ beginnen!
    assert addiere(2, 3) == 5
    assert addiere(-1, 1) == 0
```

## Tests ausfuehren

```bash
uv run pytest                    # Alle Tests ausfuehren
uv run pytest -v                 # Mit Details (verbose)
uv run pytest test_rechner.py    # Einzelne Datei
uv run pytest test_rechner.py::test_addiere  # Einzelner Test
```

## Assert-Beispiele

```python
assert ergebnis == 42            # Gleichheit
assert ergebnis != 0             # Ungleichheit
assert ist_gueltig is True       # Ist wahr
assert ist_leer is False         # Ist falsch
assert "apfel" in obstliste      # Enthalten
assert "birne" not in obstliste  # Nicht enthalten
assert len(liste) == 3           # Laenge pruefen
```

## Testbare Funktionen

```python
# Gut testbar: return statt print
def berechne_summe(zahlen):
    return sum(zahlen)

# Gut testbar: Parameter statt input
def begruessung(name):
    return f"Hallo {name}!"

# Test dazu
def test_begruessung():
    assert begruessung("Anna") == "Hallo Anna!"
```

## Haeufige Fehler

```python
# Datei nicht mit test_ benannt
rechner_test.py          # Wird NICHT gefunden
test_rechner.py          # Korrekt

# assert vergessen
def test_addiere():
    addiere(2, 3) == 5   # Prueft nichts!
    assert addiere(2, 3) == 5  # Korrekt

# Falsche Imports
from rechner import addiere  # Modul muss im gleichen Ordner sein
```
