"""
Beispiel: Arbeiten mit Variablen
Für Lektion 2
"""

# Variablen erstellen
name = "Anna"
alter = 25
stadt = "Zürich"
ist_student = True

# Variablen ausgeben
print("=== Variablen ===")
print(f"Name: {name}")
print(f"Alter: {alter}")
print(f"Stadt: {stadt}")
print(f"Student: {ist_student}\n")

# Variablen ändern
alter = 26
print(f"Neues Alter: {alter}\n")

# Mit Variablen rechnen
x = 10
y = 5
summe = x + y
differenz = x - y
produkt = x * y

print("=== Berechnungen ===")
print(f"x = {x}, y = {y}")
print(f"Summe: {summe}")
print(f"Differenz: {differenz}")
print(f"Produkt: {produkt}\n")

# Variablen tauschen
a = 5
b = 10
print(f"Vorher: a = {a}, b = {b}")

# Tauschen
temp = a
a = b
b = temp
print(f"Nachher: a = {a}, b = {b}")
