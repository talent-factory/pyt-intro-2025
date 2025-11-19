"""
Typkonvertierung
Demonstriert Konvertierung zwischen verschiedenen Datentypen.

Konzepte:
- type() - Typ ermitteln
- int() - zu Integer
- float() - zu Float
- str() - zu String
- bool() - zu Boolean
"""

# Typ ermitteln
print("=== Typ ermitteln mit type() ===\n")

zahl_int = 42
zahl_float = 3.14
text = "Hallo"
wahrheit = True

print(f"{zahl_int} ist {type(zahl_int)}")
print(f"{zahl_float} ist {type(zahl_float)}")
print(f"'{text}' ist {type(text)}")
print(f"{wahrheit} ist {type(wahrheit)}\n")

# String zu Zahl
print("=== String zu Zahl ===\n")

alter_str = "25"
preis_str = "19.99"

print(f"Original: '{alter_str}' ({type(alter_str)})")

alter_int = int(alter_str)
print(f"Nach int(): {alter_int} ({type(alter_int)})")

preis_float = float(preis_str)
print(f"Nach float(): {preis_float} ({type(preis_float)})")
print()

# Berechnungen mit konvertierten Werten
print("=== Berechnungen ===\n")

zahl1_str = "10"
zahl2_str = "20"

# Ohne Konvertierung (String-Konkatenation!)
print(f"'{zahl1_str}' + '{zahl2_str}' = '{zahl1_str + zahl2_str}'")

# Mit Konvertierung (Addition!)
zahl1 = int(zahl1_str)
zahl2 = int(zahl2_str)
print(f"{zahl1} + {zahl2} = {zahl1 + zahl2}\n")

# Zahl zu String
print("=== Zahl zu String ===\n")

zahl = 42
print(f"Original: {zahl} ({type(zahl)})")

text = str(zahl)
print(f"Nach str(): '{text}' ({type(text)})")

# Verwendung in String-Konkatenation
nachricht = "Die Antwort ist " + str(zahl)
print(f"Nachricht: {nachricht}\n")

# Float zu Int (Nachkommastellen werden abgeschnitten!)
print("=== Float zu Int ===\n")

pi = 3.14159
print(f"Original: {pi}")
print(f"Nach int(): {int(pi)}")  # 3 (nicht gerundet!)

preis = 19.99
print(f"Original: {preis}")
print(f"Nach int(): {int(preis)}\n")  # 19

# Int zu Float
print("=== Int zu Float ===\n")

zahl = 42
print(f"Original: {zahl}")
print(f"Nach float(): {float(zahl)}\n")  # 42.0

# Zu Boolean
print("=== Zu Boolean ===\n")

print("Zahlen:")
print(f"bool(1):   {bool(1)}")    # True
print(f"bool(0):   {bool(0)}")    # False
print(f"bool(-1):  {bool(-1)}")   # True
print(f"bool(42):  {bool(42)}")   # True
print()

print("Strings:")
print(f"bool(''):     {bool('')}")      # False (leer)
print(f"bool('Hi'):   {bool('Hi')}")    # True
print(f"bool('0'):    {bool('0')}")     # True (nicht leer!)
print(f"bool('False'): {bool('False')}")  # True (nicht leer!)
print()

print("Andere Typen:")
print(f"bool([]):     {bool([])}")      # False (leere Liste)
print(f"bool([1]):    {bool([1])}")     # True
print(f"bool(None):   {bool(None)}")    # False
print()

# Fehlerhafte Konvertierungen
print("=== Fehlerhafte Konvertierungen ===\n")

print("Diese Konvertierungen funktionieren NICHT:")
print("int('Hallo')  → ValueError")
print("float('abc')  → ValueError")
print("int('3.14')   → ValueError (verwenden Sie float()!)")
print()

# Korrekte Konvertierung von Float-String zu Int
print("=== Float-String zu Int ===\n")

preis_str = "19.99"
print(f"String: '{preis_str}'")

# Falsch:
# preis_int = int(preis_str)  # ValueError!

# Richtig:
preis_float = float(preis_str)
preis_int = int(preis_float)

print(f"Über float(): {preis_int}\n")

# Praktisches Beispiel
print("=== Praktisches Beispiel ===\n")

# Simulation von input() (gibt immer String zurück)
eingabe = "25"  # Simuliert: input("Alter: ")

print(f"Eingabe: '{eingabe}' ({type(eingabe)})")

# Konvertierung für Berechnung
alter = int(eingabe)
naechstes_jahr = alter + 1

print(f"Alter: {alter}")
print(f"Nächstes Jahr: {naechstes_jahr}")

