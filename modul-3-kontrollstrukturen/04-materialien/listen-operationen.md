# Listen-Operationen

## Erstellen

```python
zahlen = [1, 2, 3, 4, 5]
namen = ["Anna", "Max", "Lisa"]
gemischt = [1, "Hallo", 3.14, True]
leer = []
```

## Zugriff

```python
liste[0]    # Erstes Element
liste[1]    # Zweites Element
liste[-1]   # Letztes Element
liste[-2]   # Vorletztes Element
```

## Slicing

```python
liste[1:4]   # Index 1-3
liste[:3]    # Erste 3
liste[3:]    # Ab Index 3
liste[::2]   # Jedes 2.
liste[::-1]  # Rückwärts
```

## Methoden

```python
# Hinzufügen
liste.append(x)      # Am Ende
liste.insert(i, x)   # An Position i
liste.extend([a,b])  # Liste anhängen

# Entfernen
liste.remove(x)      # Erstes x
liste.pop()          # Letztes Element
liste.pop(i)         # Element an i
liste.clear()        # Alles löschen

# Suchen
liste.index(x)       # Position von x
liste.count(x)       # Anzahl x
x in liste           # Ist x in Liste?

# Sortieren
liste.sort()         # Aufsteigend
liste.sort(reverse=True)  # Absteigend
liste.reverse()      # Umkehren

# Sonstiges
len(liste)           # Länge
liste.copy()         # Kopie
```

## Operationen

```python
# Kombinieren
liste1 + liste2

# Vervielfachen
liste * 3

# Vergleichen
liste1 == liste2
```

## List Comprehension

```python
# Quadratzahlen
quadrate = [x**2 for x in range(10)]

# Filtern
gerade = [x for x in zahlen if x % 2 == 0]

# Transformieren
gross = [name.upper() for name in namen]
```
