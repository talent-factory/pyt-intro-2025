"""
Beispiel: Temperaturumrechner
Musterlösung für Übung 4
"""

print("=== Temperaturumrechner ===\n")

# Celsius zu Fahrenheit
# Formel: F = (C * 9/5) + 32
print("Celsius zu Fahrenheit:")
celsius = 25
fahrenheit = (celsius * 9 / 5) + 32
print(f"{celsius}°C = {fahrenheit}°F\n")

# Verschiedene Temperaturen testen
print("Wichtige Temperaturen:")
print(f"Gefrierpunkt: {0}°C = {(0 * 9 / 5) + 32}°F")
print(f"Siedepunkt: {100}°C = {(100 * 9 / 5) + 32}°F")
print(f"Körpertemperatur: {37}°C = {(37 * 9 / 5) + 32:.1f}°F\n")

# Fahrenheit zu Celsius
# Formel: C = (F - 32) * 5/9
print("Fahrenheit zu Celsius:")
fahrenheit = 77
celsius = (fahrenheit - 32) * 5 / 9
print(f"{fahrenheit}°F = {celsius:.1f}°C\n")

# Celsius zu Kelvin
# Formel: K = C + 273.15
print("Celsius zu Kelvin:")
celsius = 25
kelvin = celsius + 273.15
print(f"{celsius}°C = {kelvin}K\n")

# Kelvin zu Celsius
# Formel: C = K - 273.15
print("Kelvin zu Celsius:")
kelvin = 300
celsius = kelvin - 273.15
print(f"{kelvin}K = {celsius}°C\n")

# Umrechnungstabelle
print("=== Umrechnungstabelle ===")
print("Celsius | Fahrenheit | Kelvin")
print("--------|------------|-------")

temperaturen = [0, 10, 20, 30, 40, 100]
for c in temperaturen:
    f = (c * 9 / 5) + 32
    k = c + 273.15
    print(f"{c:7}°C | {f:10.1f}°F | {k:6.2f}K")
