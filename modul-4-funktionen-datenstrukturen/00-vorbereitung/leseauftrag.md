# Leseauftrag: Funktionen & Datenstrukturen

**Dauer:** ca. 60 Minuten

## 🎯 Lernziele

Nach diesem Leseauftrag verstehen Sie:
- Was Funktionen sind und warum sie wichtig sind
- Wie man Funktionen definiert und aufruft
- Welche Datenstrukturen Python bietet
- Wann man welche Datenstruktur verwendet

## 📖 Teil 1: Funktionen (30 Min)

### Was sind Funktionen?

Funktionen sind **wiederverwendbare Code-Blöcke**, die eine bestimmte Aufgabe erfüllen.

**Vorteile:**
- Code nicht wiederholen (DRY: Don't Repeat Yourself)
- Code übersichtlicher
- Einfacher zu testen
- Einfacher zu warten

### Funktionen definieren

```python
def gruesse(name):
    """Begrüsst eine Person."""
    print(f"Hallo {name}!")

# Funktion aufrufen
gruesse("Anna")  # Hallo Anna!
```

**Syntax:**
```python
def funktionsname(parameter1, parameter2):
    """Docstring: Was macht die Funktion?"""
    # Code
    return ergebnis
```

### Rückgabewerte

```python
def addiere(a, b):
    """Addiert zwei Zahlen."""
    return a + b

ergebnis = addiere(5, 3)  # 8
```

### Parameter-Arten

```python
# Positionelle Parameter
def gruesse(vorname, nachname):
    print(f"Hallo {vorname} {nachname}!")

# Benannte Parameter
gruesse(vorname="Anna", nachname="Muster")

# Default-Werte
def gruesse(name, formal=False):
    if formal:
        print(f"Guten Tag, {name}!")
    else:
        print(f"Hallo {name}!")
```

## 📖 Teil 2: Datenstrukturen (30 Min)

### Listen (veränderbar)

```python
# Erstellen
zahlen = [1, 2, 3, 4, 5]
namen = ["Anna", "Bob", "Clara"]

# Zugriff
print(zahlen[0])  # 1

# Ändern
zahlen[0] = 10

# Methoden
zahlen.append(6)
zahlen.remove(3)
```

**Wann verwenden?**
- Geordnete Sammlung
- Duplikate erlaubt
- Veränderbar

### Dictionaries (Schlüssel-Wert-Paare)

```python
# Erstellen
person = {
    "name": "Anna",
    "alter": 25,
    "stadt": "Zürich"
}

# Zugriff
print(person["name"])  # Anna

# Ändern
person["alter"] = 26

# Hinzufügen
person["beruf"] = "Entwicklerin"
```

**Wann verwenden?**
- Strukturierte Daten
- Zugriff über Schlüssel
- Keine Duplikate bei Schlüsseln

### Tupel (unveränderbar)

```python
# Erstellen
koordinaten = (47.3769, 8.5417)  # Zürich

# Zugriff
lat = koordinaten[0]
lon = koordinaten[1]

# Unpacking
lat, lon = koordinaten
```

**Wann verwenden?**
- Daten sollen nicht geändert werden
- Mehrere Rückgabewerte

### Sets (eindeutige Elemente)

```python
# Erstellen
zahlen = {1, 2, 3, 3, 4}  # {1, 2, 3, 4}

# Operationen
zahlen.add(5)
zahlen.remove(1)

# Mengenoperationen
a = {1, 2, 3}
b = {3, 4, 5}
print(a & b)  # {3} (Schnittmenge)
print(a | b)  # {1, 2, 3, 4, 5} (Vereinigung)
```

**Wann verwenden?**
- Duplikate entfernen
- Mengenoperationen

## 📝 Zusammenfassung

| Datenstruktur | Veränderbar | Geordnet | Duplikate | Syntax |
|---------------|-------------|----------|-----------|--------|
| Liste | ✅ | ✅ | ✅ | `[1, 2, 3]` |
| Dictionary | ✅ | ❌* | ❌ (Keys) | `{"a": 1}` |
| Tupel | ❌ | ✅ | ✅ | `(1, 2, 3)` |
| Set | ✅ | ❌ | ❌ | `{1, 2, 3}` |

*Ab Python 3.7 behalten Dictionaries die Einfügereihenfolge

## ✅ Checkliste

- [ ] Funktionen verstanden
- [ ] Parameter-Arten kennen
- [ ] Alle 4 Datenstrukturen kennen
- [ ] Wann welche Struktur verwenden

**Weiter zu:** [Erste Experimente](./erste-experimente.md)
