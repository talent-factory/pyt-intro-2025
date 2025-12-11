"""
For-Schleifen
Demonstriert for-Schleifen in Python.

Konzepte:
- For-Schleifen mit range()
- Iteration über Listen
- Iteration über Strings
- Break und Continue
- Enumerate
"""

# Einfache for-Schleife
print("=== Einfache for-Schleife ===\n")

for i in range(5):
    print(f"Durchlauf {i}")

print()

# range() mit Start und Ende
print("=== range() mit Start und Ende ===\n")

for i in range(1, 6):
    print(i)

print()

# range() mit Schrittweite
print("=== range() mit Schrittweite ===\n")

print("Gerade Zahlen:")
for i in range(0, 11, 2):
    print(i, end=" ")

print("\n")

# Rückwärts zählen
print("=== Rückwärts zählen ===\n")

for i in range(5, 0, -1):
    print(i)

print("Start!\n")

# Über Liste iterieren
print("=== Über Liste iterieren ===\n")

fruechte = ["Apfel", "Banane", "Orange", "Kiwi"]

for frucht in fruechte:
    print(f"Ich mag {frucht}")

print()

# Mit Index
print("=== Mit Index ===\n")

for i in range(len(fruechte)):
    print(f"{i + 1}. {fruechte[i]}")

print()

# Enumerate (eleganter)
print("=== Enumerate ===\n")

for index, frucht in enumerate(fruechte, start=1):
    print(f"{index}. {frucht}")

print()

# Über String iterieren
print("=== Über String iterieren ===\n")

wort = "Python"

for buchstabe in wort:
    print(buchstabe)

print()

# Summe berechnen
print("=== Summe berechnen ===\n")

zahlen = [10, 20, 30, 40, 50]
summe = 0

for zahl in zahlen:
    summe += zahl

print(f"Zahlen: {zahlen}")
print(f"Summe: {summe}")
print(f"Durchschnitt: {summe / len(zahlen):.2f}\n")

# For mit break
print("=== For mit break ===\n")

for i in range(10):
    if i == 5:
        break
    print(i)

print("Schleife beendet\n")

# For mit continue
print("=== For mit continue ===\n")

for i in range(10):
    if i % 2 == 0:  # Gerade Zahlen überspringen
        continue
    print(i)

print()

# Multiplikationstabelle
print("=== Multiplikationstabelle ===\n")

zahl = 7

for i in range(1, 11):
    print(f"{zahl} x {i} = {zahl * i}")

print()

# Liste filtern
print("=== Liste filtern ===\n")

zahlen = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
gerade = []

for zahl in zahlen:
    if zahl % 2 == 0:
        gerade.append(zahl)

print(f"Alle Zahlen: {zahlen}")
print(f"Gerade Zahlen: {gerade}\n")

# Maximum finden
print("=== Maximum finden ===\n")

zahlen = [23, 45, 12, 67, 34, 89, 15]
maximum = zahlen[0]

for zahl in zahlen:
    if zahl > maximum:
        maximum = zahl

print(f"Zahlen: {zahlen}")
print(f"Maximum: {maximum}\n")

# Zeichen zählen
print("=== Zeichen zählen ===\n")

text = "Hallo Welt"
anzahl_l = 0

for zeichen in text:
    if zeichen.lower() == "l":
        anzahl_l += 1

print(f"Text: {text}")
print(f"Anzahl 'l': {anzahl_l}\n")

# Liste umkehren
print("=== Liste umkehren ===\n")

original = [1, 2, 3, 4, 5]
umgekehrt = []

for element in original:
    umgekehrt.insert(0, element)

print(f"Original: {original}")
print(f"Umgekehrt: {umgekehrt}")
