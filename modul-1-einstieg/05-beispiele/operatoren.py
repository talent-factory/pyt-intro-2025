"""
Beispiel: Operatoren
Für Lektion 4
"""

a = 17
b = 5

print("=== Arithmetische Operatoren ===\n")
print(f"a = {a}, b = {b}\n")

# Grundrechenarten
print("Grundrechenarten:")
print(f"{a} + {b} = {a + b} (Addition)")
print(f"{a} - {b} = {a - b} (Subtraktion)")
print(f"{a} * {b} = {a * b} (Multiplikation)")
print(f"{a} / {b} = {a / b:.2f} (Division)\n")

# Erweiterte Operationen
print("Erweiterte Operationen:")
print(f"{a} // {b} = {a // b} (Ganzzahldivision)")
print(f"{a} % {b} = {a % b} (Modulo/Rest)")
print(f"{a} ** 2 = {a**2} (Potenz)\n")

# Operator-Reihenfolge
print("=== Operator-Reihenfolge ===\n")
print(f"2 + 3 * 4 = {2 + 3 * 4} (erst *, dann +)")
print(f"(2 + 3) * 4 = {(2 + 3) * 4} (Klammern zuerst)\n")

# Praktische Beispiele
print("=== Praktische Beispiele ===\n")

# Gerade oder ungerade?
zahl = 17
rest = zahl % 2
print(f"Ist {zahl} gerade? Rest bei Division durch 2: {rest}")
if rest == 0:
    print("Ja, gerade")
else:
    print("Nein, ungerade")
print()

# Stunden und Minuten
minuten_gesamt = 125
stunden = minuten_gesamt // 60
minuten = minuten_gesamt % 60
print(f"{minuten_gesamt} Minuten = {stunden} Stunden und {minuten} Minuten")
