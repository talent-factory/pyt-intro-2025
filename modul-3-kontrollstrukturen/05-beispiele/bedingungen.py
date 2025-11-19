"""
Bedingte Anweisungen
Demonstriert if, elif, else in Python.

Konzepte:
- Einfache if-Anweisungen
- if-else
- if-elif-else
- Verschachtelte Bedingungen
- Logische Operatoren
"""

# Einfache if-Anweisung
print("=== Einfache if-Anweisung ===\n")

alter = 20

if alter >= 18:
    print("Sie sind volljährig")

print()

# if-else
print("=== if-else ===\n")

temperatur = 15

if temperatur > 20:
    print("Es ist warm")
else:
    print("Es ist kalt")

print()

# if-elif-else
print("=== if-elif-else ===\n")

punkte = 85

if punkte >= 90:
    note = 6
elif punkte >= 80:
    note = 5
elif punkte >= 70:
    note = 4
elif punkte >= 60:
    note = 3
else:
    note = 2

print(f"Punkte: {punkte}")
print(f"Note: {note}")
print()

# Mehrere Bedingungen mit and
print("=== Logische Operatoren: and ===\n")

alter = 25
hat_fuehrerschein = True

if alter >= 18 and hat_fuehrerschein:
    print("Darf Auto fahren")
else:
    print("Darf nicht Auto fahren")

print()

# Mehrere Bedingungen mit or
print("=== Logische Operatoren: or ===\n")

ist_wochenende = True
ist_feiertag = False

if ist_wochenende or ist_feiertag:
    print("Frei!")
else:
    print("Arbeitstag")

print()

# Verschachtelte if-Anweisungen
print("=== Verschachtelte if-Anweisungen ===\n")

alter = 20
hat_ticket = True

if alter >= 18:
    if hat_ticket:
        print("Zugang erlaubt")
    else:
        print("Ticket erforderlich")
else:
    print("Zu jung")

print()

# Praktisches Beispiel: Rabatt-Rechner
print("=== Rabatt-Rechner ===\n")

preis = 100
ist_mitglied = True
bestellwert = 150

rabatt = 0

if ist_mitglied:
    rabatt = 10  # 10% Mitglieder-Rabatt
    
if bestellwert >= 100:
    rabatt += 5  # Zusätzlich 5% ab 100 CHF

endpreis = preis * (1 - rabatt / 100)

print(f"Originalpreis: {preis:.2f} CHF")
print(f"Rabatt: {rabatt}%")
print(f"Endpreis: {endpreis:.2f} CHF")
print()

# Vergleichsoperatoren
print("=== Vergleichsoperatoren ===\n")

a = 10
b = 20

print(f"a = {a}, b = {b}")
print(f"a == b: {a == b}")  # Gleich
print(f"a != b: {a != b}")  # Ungleich
print(f"a < b:  {a < b}")   # Kleiner
print(f"a > b:  {a > b}")   # Grösser
print(f"a <= b: {a <= b}")  # Kleiner oder gleich
print(f"a >= b: {a >= b}")  # Grösser oder gleich
print()

# Bereichsprüfung
print("=== Bereichsprüfung ===\n")

zahl = 15

if 10 <= zahl <= 20:
    print(f"{zahl} liegt zwischen 10 und 20")
else:
    print(f"{zahl} liegt nicht zwischen 10 und 20")

print()

# String-Vergleiche
print("=== String-Vergleiche ===\n")

passwort = "geheim123"

if len(passwort) >= 8:
    print("Passwort ist lang genug")
else:
    print("Passwort zu kurz (min. 8 Zeichen)")

if passwort.isalnum():
    print("Passwort enthält nur Buchstaben und Zahlen")
else:
    print("Passwort enthält Sonderzeichen")

