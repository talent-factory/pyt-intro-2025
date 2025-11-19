# Handout: Funktionen

## Definition

```python
def funktionsname(parameter1, parameter2="default"):
    """Docstring: Beschreibung der Funktion."""
    # Code
    return ergebnis
```

## Wichtige Konzepte

### 1. Einfache Funktion
```python
def gruesse():
    print("Hallo!")

gruesse()  # Aufruf
```

### 2. Mit Parametern
```python
def addiere(a, b):
    return a + b

summe = addiere(5, 3)  # 8
```

### 3. Default-Werte
```python
def gruesse(name="Gast"):
    print(f"Hallo {name}!")

gruesse()         # Hallo Gast!
gruesse("Anna")   # Hallo Anna!
```

### 4. Mehrere Rückgabewerte
```python
def statistik(zahlen):
    return min(zahlen), max(zahlen), sum(zahlen)/len(zahlen)

minimum, maximum, durchschnitt = statistik([1,2,3,4,5])
```

## Best Practices

✅ **DO:**
- Aussagekräftige Namen verwenden
- Docstrings schreiben
- Eine Aufgabe pro Funktion
- Return verwenden statt print

❌ **DON'T:**
- Zu lange Funktionen (>20 Zeilen)
- Globale Variablen ändern
- Zu viele Parameter (>5)
