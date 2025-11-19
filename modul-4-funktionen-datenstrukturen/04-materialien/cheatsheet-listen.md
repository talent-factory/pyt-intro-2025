# Cheatsheet: Listen

## Erstellen

```python
zahlen = [1, 2, 3, 4, 5]
leer = []
gemischt = [1, "text", 3.14, True]
```

## Zugriff

```python
erste = zahlen[0]      # 1
letzte = zahlen[-1]    # 5
zweite = zahlen[1]     # 2
```

## Slicing

```python
zahlen[1:4]    # [2, 3, 4]
zahlen[:3]     # [1, 2, 3]
zahlen[3:]     # [4, 5]
zahlen[::2]    # [1, 3, 5] (jedes 2.)
zahlen[::-1]   # [5, 4, 3, 2, 1] (rückwärts)
```

## Methoden

```python
# Hinzufügen
liste.append(6)           # Am Ende
liste.insert(0, 0)        # An Position
liste.extend([7, 8])      # Mehrere

# Entfernen
liste.remove(3)           # Erstes Vorkommen
element = liste.pop()     # Letztes (mit Rückgabe)
element = liste.pop(0)    # An Position
liste.clear()             # Alle

# Suchen
index = liste.index(5)    # Index von 5
anzahl = liste.count(3)   # Wie oft kommt 3 vor?
if 5 in liste:            # Ist 5 enthalten?
    print("Gefunden!")

# Sortieren
liste.sort()              # Aufsteigend
liste.sort(reverse=True)  # Absteigend
liste.reverse()           # Umkehren
```

## List Comprehensions

```python
# Quadrate
quadrate = [x**2 for x in range(10)]

# Filtern
gerade = [x for x in zahlen if x % 2 == 0]

# Transformieren
gross = [name.upper() for name in namen]

# Kombiniert
quadrate_gerade = [x**2 for x in range(10) if x % 2 == 0]
```

## Nützliche Funktionen

```python
len(liste)        # Länge
sum(zahlen)       # Summe
min(zahlen)       # Minimum
max(zahlen)       # Maximum
sorted(liste)     # Sortierte Kopie
```
