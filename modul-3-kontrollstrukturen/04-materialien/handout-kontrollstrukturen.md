# Handout: Kontrollstrukturen

**Modul 3 | Python Einführung**

## If-Anweisungen

### Einfaches If
```python
if bedingung:
    # Code
```

### If-Else
```python
if bedingung:
    # Code wenn True
else:
    # Code wenn False
```

### If-Elif-Else
```python
if bedingung1:
    # Code 1
elif bedingung2:
    # Code 2
else:
    # Code 3
```

## While-Schleifen

```python
zaehler = 1
while zaehler <= 5:
    print(zaehler)
    zaehler += 1
```

### Break & Continue
```python
while True:
    if bedingung:
        break  # Schleife beenden
    if andere_bedingung:
        continue  # Nächste Iteration
```

## For-Schleifen

### Mit range()
```python
for i in range(5):  # 0-4
    print(i)

for i in range(1, 6):  # 1-5
    print(i)

for i in range(0, 10, 2):  # 0,2,4,6,8
    print(i)
```

### Über Listen
```python
fruechte = ["Apfel", "Banane"]
for frucht in fruechte:
    print(frucht)
```

## Listen

### Erstellen
```python
liste = [1, 2, 3]
leer = []
```

### Zugriff
```python
liste[0]   # Erstes Element
liste[-1]  # Letztes Element
```

### Methoden
```python
liste.append(4)      # Hinzufügen
liste.remove(2)      # Entfernen
liste.pop()          # Letztes entfernen
len(liste)           # Länge
liste.sort()         # Sortieren
```

## Vergleichsoperatoren

| Operator | Bedeutung |
|----------|-----------|
| `==` | Gleich |
| `!=` | Ungleich |
| `<` | Kleiner |
| `>` | Grösser |
| `<=` | Kleiner oder gleich |
| `>=` | Grösser oder gleich |

## Logische Operatoren

| Operator | Bedeutung |
|----------|-----------|
| `and` | Und |
| `or` | Oder |
| `not` | Nicht |

## Tipps

✅ **DO:**
- Einrückung beachten (4 Leerzeichen)
- Aussagekräftige Variablennamen
- Kommentare bei komplexer Logik

❌ **DON'T:**
- Endlosschleifen ohne break
- Zu viele Verschachtelungen
- Zähler vergessen zu aktualisieren
