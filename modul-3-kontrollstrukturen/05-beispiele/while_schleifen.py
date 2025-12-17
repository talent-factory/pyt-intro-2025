"""
While-Schleifen
Demonstriert while-Schleifen in Python.

Konzepte:
- Einfache while-Schleifen
- Zähler-Variablen
- Break und Continue
- Endlosschleifen vermeiden
"""

# Einfache while-Schleife
print("=== Einfache while-Schleife ===\n")

zaehler = 1

while zaehler <= 5:
    print(f"Durchlauf {zaehler}")
    zaehler += 1

print("Fertig!\n")

# Countdown
print("=== Countdown ===\n")

countdown = 5

while countdown > 0:
    print(countdown)
    countdown -= 1

print("Start!\n")

# Summe berechnen
print("=== Summe berechnen ===\n")

summe = 0
zahl = 1

while zahl <= 10:
    summe += zahl
    zahl += 1

print(f"Summe von 1 bis 10: {summe}\n")

# While mit break
print("=== While mit break ===\n")

zaehler = 1

while True:  # Endlosschleife
    print(zaehler)
    zaehler += 1

    if zaehler > 5:
        break  # Schleife beenden

print("Schleife beendet\n")

# While mit continue
print("=== While mit continue ===\n")

zaehler = 0

while zaehler < 10:
    zaehler += 1

    if zaehler % 2 == 0:  # Gerade Zahlen überspringen
        continue

    print(zaehler)  # Nur ungerade Zahlen

print()

# Benutzereingabe validieren
print("=== Eingabe validieren ===\n")

# Simulation (normalerweise mit input())
eingabe = "5"  # Simuliert: input("Zahl zwischen 1 und 10: ")

zahl = int(eingabe)

while zahl < 1 or zahl > 10:
    print("Ungültige Eingabe!")
    # zahl = int(input("Zahl zwischen 1 und 10: "))
    break  # Für Demo

print(f"Gültige Zahl: {zahl}\n")

# Fakultät berechnen
print("=== Fakultät berechnen ===\n")

n = 5
fakultaet = 1
zaehler = 1

while zaehler <= n:
    fakultaet *= zaehler
    zaehler += 1

print(f"{n}! = {fakultaet}\n")

# Zahlenraten (vereinfacht)
print("=== Zahlenraten (vereinfacht) ===\n")

geheimzahl = 7
versuche = 0
max_versuche = 3

# Simulation
geraten = 5

while versuche < max_versuche:
    versuche += 1

    if geraten == geheimzahl:
        print(f"Richtig! Nach {versuche} Versuchen")
        break
    elif geraten < geheimzahl:
        print("Zu niedrig!")
    else:
        print("Zu hoch!")

    # Für Demo nur ein Durchlauf
    geraten = 7  # Nächster Versuch

print()

# Fibonacci-Zahlen
print("=== Fibonacci-Zahlen ===\n")

a, b = 0, 1
zaehler = 0
max_zahlen = 10

print("Erste 10 Fibonacci-Zahlen:")

while zaehler < max_zahlen:
    print(a, end=" ")
    a, b = b, a + b
    zaehler += 1

print("\n")

# Wichtig: Endlosschleifen vermeiden!
print("=== Endlosschleifen vermeiden ===\n")

print("FALSCH - würde nie enden:")
print("zaehler = 1")
print("while zaehler <= 5:")
print("    print(zaehler)")
print("    # Fehler: zaehler wird nie erhöht!")
print()

print("RICHTIG:")
print("zaehler = 1")
print("while zaehler <= 5:")
print("    print(zaehler)")
print("    zaehler += 1  # Wichtig!")
