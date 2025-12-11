"""
Boolsche Werte und Vergleiche
Demonstriert Vergleichsoperatoren und logische Operatoren.

Konzepte:
- True und False
- Vergleichsoperatoren
- Logische Operatoren
- Wahrheitswerte
"""

# Boolsche Werte
print("=== Boolsche Werte ===\n")

ist_student = True
ist_rentner = False

print(f"Ist Student: {ist_student}")
print(f"Ist Rentner: {ist_rentner}")
print(f"Typ: {type(ist_student)}\n")

# Vergleichsoperatoren
print("=== Vergleichsoperatoren ===\n")

a = 10
b = 20

print(f"a = {a}, b = {b}")
print(f"a == b: {a == b}")  # Gleich
print(f"a != b: {a != b}")  # Ungleich
print(f"a < b:  {a < b}")  # Kleiner
print(f"a > b:  {a > b}")  # Grösser
print(f"a <= b: {a <= b}")  # Kleiner oder gleich
print(f"a >= b: {a >= b}")  # Grösser oder gleich
print()

# Vergleiche mit Variablen
print("=== Vergleiche mit Variablen ===\n")

alter = 20
temperatur = 25

ist_volljaehrig = alter >= 18
ist_warm = temperatur > 20

print(f"Alter: {alter}")
print(f"Volljährig (>= 18): {ist_volljaehrig}")
print(f"Temperatur: {temperatur}°C")
print(f"Warm (> 20): {ist_warm}\n")

# Logische Operatoren: and
print("=== Logischer Operator: and ===\n")

alter = 25
hat_fuehrerschein = True

darf_fahren = alter >= 18 and hat_fuehrerschein

print(f"Alter: {alter}")
print(f"Hat Führerschein: {hat_fuehrerschein}")
print(f"Darf fahren: {darf_fahren}")
print()

print("Wahrheitstabelle für 'and':")
print(f"True and True:   {True and True}")
print(f"True and False:  {True and False}")
print(f"False and True:  {False and True}")
print(f"False and False: {False and False}\n")

# Logische Operatoren: or
print("=== Logischer Operator: or ===\n")

ist_wochenende = True
ist_feiertag = False

ist_frei = ist_wochenende or ist_feiertag

print(f"Ist Wochenende: {ist_wochenende}")
print(f"Ist Feiertag: {ist_feiertag}")
print(f"Ist frei: {ist_frei}")
print()

print("Wahrheitstabelle für 'or':")
print(f"True or True:   {True or True}")
print(f"True or False:  {True or False}")
print(f"False or True:  {False or True}")
print(f"False or False: {False or False}\n")

# Logische Operatoren: not
print("=== Logischer Operator: not ===\n")

ist_regen = False
ist_trocken = not ist_regen

print(f"Ist Regen: {ist_regen}")
print(f"Ist trocken: {ist_trocken}")
print()

print("Wahrheitstabelle für 'not':")
print(f"not True:  {not True}")
print(f"not False: {not False}\n")

# Kombinierte Bedingungen
print("=== Kombinierte Bedingungen ===\n")

alter = 25
hat_ticket = True
ist_mitglied = False

# Zugang erlaubt wenn: (Alter >= 18 UND Ticket) ODER Mitglied
zugang = (alter >= 18 and hat_ticket) or ist_mitglied

print(f"Alter: {alter}")
print(f"Hat Ticket: {hat_ticket}")
print(f"Ist Mitglied: {ist_mitglied}")
print(f"Zugang erlaubt: {zugang}\n")

# String-Vergleiche
print("=== String-Vergleiche ===\n")

name1 = "Anna"
name2 = "anna"
name3 = "Anna"

print(f"'{name1}' == '{name2}': {name1 == name2}")  # False (Gross-/Klein!)
print(f"'{name1}' == '{name3}': {name1 == name3}")  # True

# Case-insensitive Vergleich
print(f"Gleich (ignoriert Gross/Klein): {name1.lower() == name2.lower()}")
print()

# Wahrheitswerte anderer Typen
print("=== Wahrheitswerte anderer Typen ===\n")

print(f"bool(1):      {bool(1)}")  # True
print(f"bool(0):      {bool(0)}")  # False
print(f"bool(-1):     {bool(-1)}")  # True
print(f"bool(''):     {bool('')}")  # False (leerer String)
print(f"bool('Hi'):   {bool('Hi')}")  # True
print(f"bool([]):     {bool([])}")  # False (leere Liste)
print(f"bool([1]):    {bool([1])}")  # True
print(f"bool(None):   {bool(None)}")  # False
