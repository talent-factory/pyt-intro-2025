"""
Beispiel: Datentypen
Für Lektion 2
"""

# int - Ganzzahlen
alter = 25
anzahl = 100
jahr = 2025

print("=== int (Ganzzahlen) ===")
print(f"alter = {alter}, type: {type(alter)}")
print(f"anzahl = {anzahl}, type: {type(anzahl)}")
print(f"jahr = {jahr}, type: {type(jahr)}\n")

# float - Dezimalzahlen
preis = 19.99
pi = 3.14159
temperatur = 36.5

print("=== float (Dezimalzahlen) ===")
print(f"preis = {preis}, type: {type(preis)}")
print(f"pi = {pi}, type: {type(pi)}")
print(f"temperatur = {temperatur}, type: {type(temperatur)}\n")

# str - Strings
name = "Anna"
stadt = "Zürich"
text = "Python macht Spaß!"

print("=== str (Strings) ===")
print(f"name = '{name}', type: {type(name)}")
print(f"stadt = '{stadt}', type: {type(stadt)}")
print(f"text = '{text}', type: {type(text)}\n")

# bool - Wahrheitswerte
ist_student = True
ist_fertig = False

print("=== bool (Wahrheitswerte) ===")
print(f"ist_student = {ist_student}, type: {type(ist_student)}")
print(f"ist_fertig = {ist_fertig}, type: {type(ist_fertig)}\n")

# Typkonvertierung
print("=== Typkonvertierung ===")
zahl_str = "42"
zahl_int = int(zahl_str)
print(f"'{zahl_str}' (str) → {zahl_int} (int)")

zahl_float = float(zahl_int)
print(f"{zahl_int} (int) → {zahl_float} (float)")

zahl_str_2 = str(zahl_int)
print(f"{zahl_int} (int) → '{zahl_str_2}' (str)")
