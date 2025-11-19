# Cheatsheet: Schleifen

## While-Schleife

```python
# Basis
zaehler = 0
while zaehler < 5:
    print(zaehler)
    zaehler += 1

# Mit Break
while True:
    eingabe = input("Zahl (0=Ende): ")
    if eingabe == "0":
        break

# Mit Continue
zaehler = 0
while zaehler < 10:
    zaehler += 1
    if zaehler % 2 == 0:
        continue
    print(zaehler)  # Nur ungerade
```

## For-Schleife

```python
# Range
for i in range(5):           # 0,1,2,3,4
for i in range(1, 6):        # 1,2,3,4,5
for i in range(0, 10, 2):    # 0,2,4,6,8
for i in range(5, 0, -1):    # 5,4,3,2,1

# Liste
for element in liste:
    print(element)

# Mit Index
for i in range(len(liste)):
    print(f"{i}: {liste[i]}")

# Enumerate
for i, element in enumerate(liste):
    print(f"{i}: {element}")
```

## Verschachtelt

```python
# Schleife in Schleife
for i in range(3):
    for j in range(3):
        print(f"({i},{j})")

# If in Schleife
for zahl in zahlen:
    if zahl % 2 == 0:
        print(f"{zahl} ist gerade")
```

## Häufige Muster

```python
# Summe
summe = 0
for zahl in zahlen:
    summe += zahl

# Maximum
maximum = zahlen[0]
for zahl in zahlen:
    if zahl > maximum:
        maximum = zahl

# Filtern
gerade = []
for zahl in zahlen:
    if zahl % 2 == 0:
        gerade.append(zahl)

# Zählen
anzahl = 0
for zahl in zahlen:
    if zahl > 10:
        anzahl += 1
```
