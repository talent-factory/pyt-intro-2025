# Lektion 3: Listen vertiefen

**Dauer:** 50 Minuten  
**Format:** 15 Min Theorie + 20 Min Live-Coding + 15 Min Übung

## 🎯 Lernziele

- List Comprehensions verwenden
- Listen-Methoden beherrschen
- Listen als Funktionsparameter nutzen
- Verschachtelte Listen verstehen

## 📖 Theorie (15 Min)

### List Comprehensions

Kompakte Syntax zum Erstellen von Listen:

```python
# Klassisch
quadrate = []
for i in range(10):
    quadrate.append(i * i)

# List Comprehension
quadrate = [i * i for i in range(10)]
```

### Wichtige Listen-Methoden

```python
liste = [1, 2, 3]

# Hinzufügen
liste.append(4)        # [1, 2, 3, 4]
liste.extend([5, 6])   # [1, 2, 3, 4, 5, 6]
liste.insert(0, 0)     # [0, 1, 2, 3, 4, 5, 6]

# Entfernen
liste.remove(0)        # Entfernt ersten 0
element = liste.pop()  # Entfernt und gibt letztes Element zurück
liste.clear()          # Leert die Liste

# Suchen
index = liste.index(3) # Index von 3
anzahl = liste.count(2)# Wie oft kommt 2 vor?

# Sortieren
liste.sort()           # Sortiert aufsteigend
liste.reverse()        # Kehrt Reihenfolge um
```

### Slicing

```python
zahlen = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

zahlen[2:5]    # [2, 3, 4]
zahlen[:3]     # [0, 1, 2]
zahlen[7:]     # [7, 8, 9]
zahlen[::2]    # [0, 2, 4, 6, 8] (jedes 2.)
zahlen[::-1]   # [9, 8, 7, ...] (rückwärts)
```

## 💻 Live-Coding (20 Min)

### Beispiel 1: List Comprehensions

```python
# Gerade Zahlen filtern
zahlen = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
gerade = [x for x in zahlen if x % 2 == 0]
print(gerade)  # [2, 4, 6, 8, 10]

# Namen in Grossbuchstaben
namen = ["anna", "max", "lisa"]
gross = [name.upper() for name in namen]
print(gross)  # ['ANNA', 'MAX', 'LISA']
```

### Beispiel 2: Listen als Parameter

```python
def berechne_durchschnitt(zahlen):
    """Berechnet den Durchschnitt einer Zahlenliste."""
    if len(zahlen) == 0:
        return 0
    return sum(zahlen) / len(zahlen)

noten = [5.5, 4.0, 6.0, 5.0, 4.5]
durchschnitt = berechne_durchschnitt(noten)
print(f"Durchschnitt: {durchschnitt:.2f}")
```

### Beispiel 3: Listen transformieren

```python
def verdopple_werte(liste):
    """Verdoppelt alle Werte in einer Liste."""
    return [x * 2 for x in liste]

zahlen = [1, 2, 3, 4, 5]
verdoppelt = verdopple_werte(zahlen)
print(f"Original: {zahlen}")
print(f"Verdoppelt: {verdoppelt}")
```

## ✏️ Übungen (15 Min)

- [Übung 5: Listen-Methoden](../02-uebungen/uebung-5-methoden.md)

## 📚 Zusammenfassung

- List Comprehensions: `[x for x in liste if bedingung]`
- Wichtige Methoden: append, extend, remove, pop, sort
- Slicing: `liste[start:end:step]`
- Listen als Funktionsparameter

## 🔗 Weiter

- [Lektion 4: Dictionaries](./lektion-4-dictionaries.md)

