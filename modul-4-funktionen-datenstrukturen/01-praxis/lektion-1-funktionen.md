# Lektion 1: Funktionen definieren

**Dauer:** 50 Minuten  
**Format:** 15 Min Theorie + 20 Min Live-Coding + 15 Min Übung

## 🎯 Lernziele

Nach dieser Lektion können Sie:
- Funktionen mit `def` definieren
- Funktionen aufrufen
- Docstrings schreiben
- Den Unterschied zwischen Definition und Aufruf verstehen

## 📖 Theorie (15 Min)

### Was sind Funktionen?

Funktionen sind **wiederverwendbare Code-Blöcke**, die eine bestimmte Aufgabe erfüllen.

**Vorteile:**
- Code nicht wiederholen (DRY: Don't Repeat Yourself)
- Bessere Lesbarkeit
- Einfachere Wartung
- Modularer Aufbau

### Syntax

```python
def funktionsname():
    """Docstring: Beschreibt was die Funktion macht."""
    # Code hier
    print("Hallo aus der Funktion!")
```

**Wichtig:**
- `def` leitet die Definition ein
- Funktionsname in snake_case
- Doppelpunkt `:` am Ende
- Einrückung (4 Leerzeichen)
- Docstring in dreifachen Anführungszeichen

### Funktionen aufrufen

```python
# Definition
def gruesse():
    """Gibt eine Begrüssung aus."""
    print("Hallo Welt!")

# Aufruf
gruesse()  # Ausgabe: Hallo Welt!
```

### Mehrfache Aufrufe

```python
def zeige_trennlinie():
    """Zeigt eine Trennlinie."""
    print("=" * 40)

zeige_trennlinie()
print("Titel")
zeige_trennlinie()
```

## 💻 Live-Coding (20 Min)

### Beispiel 1: Einfache Begrüssung

```python
def begruessung():
    """Gibt eine freundliche Begrüssung aus."""
    print("Willkommen zum Python-Kurs!")
    print("Schön, dass Sie da sind!")

# Aufruf
begruessung()
```

### Beispiel 2: Mehrere Funktionen

```python
def zeige_header():
    """Zeigt einen Header."""
    print("=" * 40)
    print("MEIN PROGRAMM")
    print("=" * 40)

def zeige_menu():
    """Zeigt ein Menü."""
    print("1. Option A")
    print("2. Option B")
    print("3. Beenden")

def zeige_footer():
    """Zeigt einen Footer."""
    print("-" * 40)
    print("© 2025 Mein Programm")

# Programm
zeige_header()
zeige_menu()
zeige_footer()
```

### Beispiel 3: Funktionen in Schleifen

```python
def zeige_stern():
    """Zeigt einen Stern."""
    print("⭐", end=" ")

# 10 Sterne ausgeben
for i in range(10):
    zeige_stern()
print()  # Neue Zeile
```

## ✏️ Übungen (15 Min)

### Übung 1: Eigene Funktionen (10 Min)

Siehe [Übung 1: Einfache Funktionen](../02-uebungen/uebung-1-funktionen.md)

### Übung 2: Funktionen kombinieren (5 Min)

Siehe [Übung 2: Funktionen mit Return](../02-uebungen/uebung-2-return.md)

## 📚 Zusammenfassung

- Funktionen mit `def funktionsname():` definieren
- Docstrings dokumentieren die Funktion
- Funktionen mit `funktionsname()` aufrufen
- Funktionen machen Code wiederverwendbar

## 🔗 Weiter

- [Lektion 2: Parameter & Rückgabewerte](./lektion-2-parameter.md)
- [Beispiele](../05-beispiele/funktionen_basis.py)

