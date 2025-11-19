"""
Beispiel: BMI-Rechner
Musterlösung für Aufgabe 2
"""

print("=== BMI-Rechner ===\n")

# Person 1
print("Person 1:")
groesse_1 = 1.75  # in Metern
gewicht_1 = 70  # in kg
bmi_1 = gewicht_1 / (groesse_1**2)

print(f"Größe: {groesse_1} m")
print(f"Gewicht: {gewicht_1} kg")
print(f"BMI: {bmi_1:.1f}")

# Kategorie bestimmen (vereinfacht für Modul 1)
if bmi_1 < 18.5:
    kategorie_1 = "Untergewicht"
elif bmi_1 < 25:
    kategorie_1 = "Normalgewicht"
elif bmi_1 < 30:
    kategorie_1 = "Übergewicht"
else:
    kategorie_1 = "Adipositas"

print(f"Kategorie: {kategorie_1}\n")

# Person 2
print("Person 2:")
groesse_2 = 1.80
gewicht_2 = 90
bmi_2 = gewicht_2 / (groesse_2**2)

print(f"Größe: {groesse_2} m")
print(f"Gewicht: {gewicht_2} kg")
print(f"BMI: {bmi_2:.1f}")

if bmi_2 < 18.5:
    kategorie_2 = "Untergewicht"
elif bmi_2 < 25:
    kategorie_2 = "Normalgewicht"
elif bmi_2 < 30:
    kategorie_2 = "Übergewicht"
else:
    kategorie_2 = "Adipositas"

print(f"Kategorie: {kategorie_2}\n")

# Person 3
print("Person 3:")
groesse_3 = 1.65
gewicht_3 = 55
bmi_3 = gewicht_3 / (groesse_3**2)

print(f"Größe: {groesse_3} m")
print(f"Gewicht: {gewicht_3} kg")
print(f"BMI: {bmi_3:.1f}")

if bmi_3 < 18.5:
    kategorie_3 = "Untergewicht"
elif bmi_3 < 25:
    kategorie_3 = "Normalgewicht"
elif bmi_3 < 30:
    kategorie_3 = "Übergewicht"
else:
    kategorie_3 = "Adipositas"

print(f"Kategorie: {kategorie_3}\n")

# Idealgewicht berechnen (BMI 22)
print("=== Idealgewicht (BMI 22) ===\n")
IDEAL_BMI = 22

for groesse in [1.65, 1.75, 1.80]:
    idealgewicht = IDEAL_BMI * (groesse**2)
    print(f"Größe {groesse} m: Idealgewicht {idealgewicht:.1f} kg")
