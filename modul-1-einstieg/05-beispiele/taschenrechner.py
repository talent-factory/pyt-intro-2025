"""
Beispiel: Einfacher Taschenrechner
Musterlösung für Übung 2
"""

# Zwei Zahlen definieren
a = 25
b = 5

print("=== Einfacher Taschenrechner ===\n")

# Grundrechenarten
print(f"Zahlen: a = {a}, b = {b}\n")

print("Grundrechenarten:")
print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b}")

# Erweiterte Operationen
print("\nErweiterte Operationen:")
print(f"{a} // {b} = {a // b} (Ganzzahldivision)")
print(f"{a} % {b} = {a % b} (Rest)")
print(f"{a} ** 2 = {a**2} (Quadrat)")

# Praktische Beispiele
print("\n=== Praktische Beispiele ===\n")

# Rechteck-Fläche
laenge = 10
breite = 5
flaeche = laenge * breite
print("Rechteck-Fläche:")
print(f"Länge: {laenge} m, Breite: {breite} m")
print(f"Fläche: {flaeche} m²\n")

# Durchschnitt berechnen
note1 = 5.5
note2 = 6.0
note3 = 5.0
durchschnitt = (note1 + note2 + note3) / 3
print("Notendurchschnitt:")
print(f"Noten: {note1}, {note2}, {note3}")
print(f"Durchschnitt: {durchschnitt:.2f}\n")

# Kreisfläche
radius = 5
PI = 3.14159
kreisflaeche = PI * radius**2
print("Kreisfläche:")
print(f"Radius: {radius} cm")
print(f"Fläche: {kreisflaeche:.2f} cm²")
