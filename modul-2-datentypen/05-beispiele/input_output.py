"""
Input/Output
Demonstriert Benutzereingaben und formatierte Ausgaben.

Konzepte:
- input() - Benutzereingaben
- print() - Ausgaben
- Typkonvertierung bei Eingaben
- Formatierte Ausgaben
"""

print("=" * 40)
print("    Input/Output Demonstrator")
print("=" * 40)
print()

# Einfache Eingabe
print("=== Einfache Eingabe ===\n")

name = input("Wie heissen Sie? ")
print(f"Hallo {name}!\n")

# Wichtig: input() gibt immer String zurück!
print("=== Typ von input() ===\n")

eingabe = input("Geben Sie eine Zahl ein: ")
print(f"Eingabe: '{eingabe}'")
print(f"Typ: {type(eingabe)}")
print()

# Zahl eingeben (mit Konvertierung)
print("=== Zahl eingeben ===\n")

alter_str = input("Wie alt sind Sie? ")
alter = int(alter_str)

print(f"Sie sind {alter} Jahre alt")
print(f"Nächstes Jahr sind Sie {alter + 1}\n")

# Direkte Konvertierung
print("=== Direkte Konvertierung ===\n")

# Besser: Direkt konvertieren
groesse = float(input("Körpergrösse in Metern: "))
print(f"Sie sind {groesse} Meter gross\n")

# Mehrere Eingaben
print("=== Mehrere Eingaben ===\n")

vorname = input("Vorname: ")
nachname = input("Nachname: ")
alter = int(input("Alter: "))

vollname = f"{vorname} {nachname}"
geburtsjahr = 2025 - alter

print()
print("=" * 40)
print(f"Name:        {vollname}")
print(f"Alter:       {alter} Jahre")
print(f"Geburtsjahr: ca. {geburtsjahr}")
print("=" * 40)
print()

# print() mit mehreren Werten
print("=== print() mit mehreren Werten ===\n")

print("Hallo", "Welt")  # Automatisches Leerzeichen
print("Summe:", 5 + 3)
print("Name:", name, "Alter:", alter)
print()

# print() mit sep Parameter
print("=== sep Parameter ===\n")

print("A", "B", "C")  # Standard: Leerzeichen
print("A", "B", "C", sep="-")  # Mit Bindestrich
print("A", "B", "C", sep=" | ")  # Mit Pipe
print("2025", "01", "15", sep="-")  # Datum
print()

# print() mit end Parameter
print("=== end Parameter ===\n")

print("Zeile 1")  # Standard: Zeilenumbruch
print("Zeile 2")

print("Zeile 1", end=" ")  # Kein Zeilenumbruch
print("Zeile 2")

print("Laden", end="")
print(".", end="")
print(".", end="")
print(".")
print()

# Formatierte Ausgabe mit F-Strings
print("=== Formatierte Ausgabe ===\n")

name = "Anna"
alter = 25
groesse = 1.75
preis = 19.99

print(f"Name:   {name}")
print(f"Alter:  {alter} Jahre")
print(f"Grösse: {groesse} m")
print(f"Preis:  {preis:.2f} CHF")
print()

# Tabellen-Ausgabe
print("=== Tabellen-Ausgabe ===\n")

print(f"{'Name':<15} {'Alter':>5} {'Preis':>10}")
print("-" * 32)
print(f"{'Anna':<15} {25:>5} {19.99:>10.2f}")
print(f"{'Max Muster':<15} {30:>5} {29.50:>10.2f}")
print(f"{'Lisa':<15} {22:>5} {15.00:>10.2f}")
print()

# Interaktives Beispiel: Rechner
print("=== Interaktiver Rechner ===\n")

print("Einfacher Rechner")
print("-" * 20)

zahl1 = float(input("Erste Zahl: "))
zahl2 = float(input("Zweite Zahl: "))

summe = zahl1 + zahl2
differenz = zahl1 - zahl2
produkt = zahl1 * zahl2
quotient = zahl1 / zahl2

print()
print("Ergebnisse:")
print(f"{zahl1} + {zahl2} = {summe}")
print(f"{zahl1} - {zahl2} = {differenz}")
print(f"{zahl1} * {zahl2} = {produkt}")
print(f"{zahl1} / {zahl2} = {quotient:.2f}")
