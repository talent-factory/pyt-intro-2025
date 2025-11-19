"""
Verschachtelte Strukturen
Demonstriert verschachtelte Kontrollstrukturen.

Konzepte:
- If in If
- Schleife in Schleife
- If in Schleife
- Schleife in If
"""

# If in If
print("=== If in If ===\n")

alter = 20
hat_fuehrerschein = True
hat_auto = False

if alter >= 18:
    print("Volljährig")
    if hat_fuehrerschein:
        print("Hat Führerschein")
        if hat_auto:
            print("Kann fahren")
        else:
            print("Braucht Auto")
    else:
        print("Braucht Führerschein")
else:
    print("Zu jung")

print()

# Schleife in Schleife
print("=== Schleife in Schleife ===\n")

for i in range(3):
    for j in range(3):
        print(f"i={i}, j={j}")

print()

# Multiplikationstabelle
print("=== Multiplikationstabelle ===\n")

for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i*j:3}", end=" ")
    print()

print()

# Muster: Dreieck
print("=== Muster: Dreieck ===\n")

for i in range(5):
    for j in range(i + 1):
        print("*", end="")
    print()

print()

# Muster: Umgekehrtes Dreieck
print("=== Muster: Umgekehrtes Dreieck ===\n")

for i in range(5, 0, -1):
    for j in range(i):
        print("*", end="")
    print()

print()

# If in Schleife
print("=== If in Schleife ===\n")

zahlen = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("Gerade Zahlen:")
for zahl in zahlen:
    if zahl % 2 == 0:
        print(zahl, end=" ")

print("\n")

# Schleife in If
print("=== Schleife in If ===\n")

ist_wochenende = True

if ist_wochenende:
    print("Wochenend-Aktivitäten:")
    aktivitaeten = ["Ausschlafen", "Sport", "Freunde treffen"]
    for aktivitaet in aktivitaeten:
        print(f"- {aktivitaet}")
else:
    print("Arbeitstag")

print()

# Verschachtelte Listen
print("=== Verschachtelte Listen ===\n")

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Matrix:")
for zeile in matrix:
    for element in zeile:
        print(f"{element:3}", end=" ")
    print()

print()

# Summe einer Matrix
print("=== Summe einer Matrix ===\n")

summe = 0
for zeile in matrix:
    for element in zeile:
        summe += element

print(f"Summe aller Elemente: {summe}\n")

# Schachbrett-Muster
print("=== Schachbrett-Muster ===\n")

for i in range(8):
    for j in range(8):
        if (i + j) % 2 == 0:
            print("□", end=" ")
        else:
            print("■", end=" ")
    print()

print()

# Primzahlen finden
print("=== Primzahlen bis 30 ===\n")

for zahl in range(2, 31):
    ist_primzahl = True
    
    for teiler in range(2, int(zahl ** 0.5) + 1):
        if zahl % teiler == 0:
            ist_primzahl = False
            break
    
    if ist_primzahl:
        print(zahl, end=" ")

print("\n")

# Verschachtelte Bedingungen in Schleife
print("=== Notenklassifizierung ===\n")

noten = [5.5, 4.2, 3.8, 6.0, 4.5]

for i, note in enumerate(noten, start=1):
    print(f"Student {i}: Note {note}", end=" - ")
    
    if note >= 5.5:
        print("Sehr gut")
    elif note >= 4.0:
        print("Bestanden")
    else:
        print("Nicht bestanden")

print()

# Pyramide
print("=== Pyramide ===\n")

hoehe = 5

for i in range(1, hoehe + 1):
    # Leerzeichen
    for j in range(hoehe - i):
        print(" ", end="")
    # Sterne
    for k in range(2 * i - 1):
        print("*", end="")
    print()

