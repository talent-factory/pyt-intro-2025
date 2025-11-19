# Häufige Fehler bei Funktionen & Datenstrukturen

## 1. Funktion vergessen aufzurufen

❌ **Falsch:**
```python
def gruesse():
    print("Hallo!")

gruesse  # Vergessen: ()
```

✅ **Richtig:**
```python
gruesse()  # Mit Klammern!
```

## 2. Return vergessen

❌ **Falsch:**
```python
def addiere(a, b):
    summe = a + b  # Kein return!

ergebnis = addiere(5, 3)  # None
```

✅ **Richtig:**
```python
def addiere(a, b):
    return a + b
```

## 3. Liste vs. Tupel verwechseln

❌ **Falsch:**
```python
punkt = (10, 20)
punkt[0] = 15  # Fehler! Tupel unveränderbar
```

✅ **Richtig:**
```python
punkt = [10, 20]  # Liste verwenden
punkt[0] = 15
```

## 4. Dictionary-Key nicht gefunden

❌ **Falsch:**
```python
person = {"name": "Anna"}
alter = person["alter"]  # KeyError!
```

✅ **Richtig:**
```python
alter = person.get("alter", 0)  # Mit Default
```

## 5. Liste in Schleife ändern

❌ **Falsch:**
```python
zahlen = [1, 2, 3, 4, 5]
for zahl in zahlen:
    if zahl % 2 == 0:
        zahlen.remove(zahl)  # Problematisch!
```

✅ **Richtig:**
```python
zahlen = [x for x in zahlen if x % 2 != 0]
```

## 6. Globale Variable in Funktion ändern

❌ **Falsch:**
```python
counter = 0

def increment():
    counter = counter + 1  # Fehler!
```

✅ **Richtig:**
```python
def increment(counter):
    return counter + 1

counter = increment(counter)
```

## 7. Leere Liste als Default-Parameter

❌ **Falsch:**
```python
def add_item(item, liste=[]):
    liste.append(item)
    return liste
```

✅ **Richtig:**
```python
def add_item(item, liste=None):
    if liste is None:
        liste = []
    liste.append(item)
    return liste
```

## 8. Set statt Liste für geordnete Daten

❌ **Falsch:**
```python
reihenfolge = {1, 2, 3}  # Set ist ungeordnet!
```

✅ **Richtig:**
```python
reihenfolge = [1, 2, 3]  # Liste verwenden
```
