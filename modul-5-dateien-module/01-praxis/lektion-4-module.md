# Lektion 4: Module & Imports

**Dauer:** 50 Minuten  
**Format:** 15 Min Theorie + 20 Min Live-Coding + 15 Min Übung

## 🎯 Lernziele

- Module importieren
- Eigene Module erstellen
- Import-Varianten kennen
- Standard-Bibliothek nutzen

## 📖 Theorie (15 Min)

### Was sind Module?

Module sind **Python-Dateien** mit wiederverwendbarem Code.

### Importieren

```python
# Ganzes Modul
import math
print(math.pi)
print(math.sqrt(16))

# Spezifische Funktionen
from math import pi, sqrt
print(pi)
print(sqrt(16))

# Mit Alias
import datetime as dt
heute = dt.date.today()

# Alles importieren (nicht empfohlen!)
from math import *
```

### Eigenes Modul erstellen

Datei `rechner.py`:
```python
"""Einfacher Rechner."""

def addiere(a, b):
    """Addiert zwei Zahlen."""
    return a + b

def multipliziere(a, b):
    """Multipliziert zwei Zahlen."""
    return a * b

PI = 3.14159
```

Verwendung:
```python
import rechner

print(rechner.addiere(5, 3))
print(rechner.PI)
```

### `if __name__ == "__main__":`

```python
# mein_modul.py
def gruesse(name):
    return f"Hallo {name}!"

# Wird nur ausgeführt wenn direkt gestartet
if __name__ == "__main__":
    print(gruesse("Welt"))
```

## 💻 Live-Coding (20 Min)

### Beispiel 1: Eigenes Modul

Datei `texttools.py`:
```python
"""Werkzeuge für Textverarbeitung."""

def woerter_zaehlen(text):
    """Zählt Wörter in einem Text."""
    return len(text.split())

def gross_schreiben(text):
    """Wandelt Text in Großbuchstaben."""
    return text.upper()

def umkehren(text):
    """Kehrt Text um."""
    return text[::-1]

if __name__ == "__main__":
    # Tests
    test = "Hallo Welt"
    print(f"Wörter: {woerter_zaehlen(test)}")
    print(f"Groß: {gross_schreiben(test)}")
    print(f"Umgekehrt: {umkehren(test)}")
```

Verwendung in `main.py`:
```python
import texttools

text = "Python macht Spass"
print(f"Anzahl Wörter: {texttools.woerter_zaehlen(text)}")
print(f"Groß: {texttools.gross_schreiben(text)}")
```

### Beispiel 2: Datei-Utilities

Datei `datei_utils.py`:
```python
"""Utilities für Datei-Operationen."""

def datei_existiert(dateiname):
    """Prüft ob Datei existiert."""
    import os
    return os.path.exists(dateiname)

def datei_groesse(dateiname):
    """Gibt Dateigröße in Bytes zurück."""
    import os
    return os.path.getsize(dateiname)

def zeilen_zaehlen(dateiname):
    """Zählt Zeilen in Datei."""
    with open(dateiname, "r") as f:
        return len(f.readlines())
```

### Beispiel 3: Standard-Module nutzen

```python
# Datum und Zeit
import datetime

heute = datetime.date.today()
print(f"Heute: {heute}")

jetzt = datetime.datetime.now()
print(f"Jetzt: {jetzt.strftime('%H:%M:%S')}")

# Zufallszahlen
import random

zahl = random.randint(1, 100)
print(f"Zufallszahl: {zahl}")

auswahl = random.choice(["Rot", "Grün", "Blau"])
print(f"Zufällige Farbe: {auswahl}")

# Betriebssystem
import os

print(f"Aktuelles Verzeichnis: {os.getcwd()}")
print(f"Dateien: {os.listdir('.')}")

# Mathematik
import math

print(f"Pi: {math.pi}")
print(f"Wurzel aus 16: {math.sqrt(16)}")
print(f"5 hoch 3: {math.pow(5, 3)}")
```

## ✏️ Übungen (15 Min)

- [Übung 7: Eigenes Modul](../02-uebungen/uebung-7-modul.md)
- [Übung 8: Standard-Module](../02-uebungen/uebung-8-stdlib.md)

## 📚 Zusammenfassung

- Module mit `import` einbinden
- Eigene Module = .py Dateien
- `if __name__ == "__main__":` für Tests
- Wichtige Standard-Module:
  - `datetime` - Datum/Zeit
  - `random` - Zufallszahlen
  - `os` - Betriebssystem
  - `math` - Mathematik
  - `json` - JSON
  - `csv` - CSV

## 🔗 Weiter

- [Lektion 5: Abschluss-Projekt](./lektion-5-projekt.md)

