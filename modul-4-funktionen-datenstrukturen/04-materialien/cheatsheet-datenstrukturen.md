# Cheatsheet: Datenstrukturen

## Listen

```python
# Erstellen
liste = [1, 2, 3]
leer = []

# Zugriff
erste = liste[0]
letzte = liste[-1]

# Methoden
liste.append(4)        # Hinzufügen
liste.extend([5, 6])   # Mehrere hinzufügen
liste.insert(0, 0)     # An Position einfügen
liste.remove(3)        # Element entfernen
element = liste.pop()  # Letztes entfernen & zurückgeben
liste.sort()           # Sortieren
liste.reverse()        # Umkehren

# List Comprehension
quadrate = [x**2 for x in range(10)]
gerade = [x for x in liste if x % 2 == 0]
```

## Dictionaries

```python
# Erstellen
person = {"name": "Anna", "alter": 25}
leer = {}

# Zugriff
name = person["name"]
alter = person.get("alter", 0)  # Mit Default

# Ändern/Hinzufügen
person["alter"] = 26
person["stadt"] = "Zürich"

# Löschen
del person["stadt"]

# Iteration
for key in person.keys():
    print(key)

for value in person.values():
    print(value)

for key, value in person.items():
    print(f"{key}: {value}")
```

## Tupel

```python
# Erstellen
punkt = (10, 20)
person = ("Anna", 25, "Zürich")

# Zugriff
x = punkt[0]

# Unpacking
x, y = punkt
name, alter, stadt = person

# NICHT veränderbar!
# punkt[0] = 15  # Fehler!
```

## Sets

```python
# Erstellen
zahlen = {1, 2, 3, 3}  # {1, 2, 3}
leer = set()

# Hinzufügen/Entfernen
zahlen.add(4)
zahlen.remove(1)

# Mengenoperationen
a = {1, 2, 3}
b = {3, 4, 5}

a | b  # Vereinigung: {1, 2, 3, 4, 5}
a & b  # Schnittmenge: {3}
a - b  # Differenz: {1, 2}
```

## Wann was verwenden?

| Datenstruktur | Wann verwenden |
|---------------|----------------|
| **Liste** | Geordnete Sammlung, veränderbar |
| **Tupel** | Feste Daten, unveränderbar |
| **Dictionary** | Schlüssel-Wert-Paare |
| **Set** | Eindeutige Elemente, Mengenoperationen |
