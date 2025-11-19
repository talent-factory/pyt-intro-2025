"""
String-Formatierung
Demonstriert verschiedene Arten der String-Formatierung.

Konzepte:
- F-Strings (modern, empfohlen)
- Format-Methode
- Alte %-Formatierung
- Formatierungs-Optionen
"""

# Variablen
name = "Anna"
alter = 25
groesse = 1.75
preis = 19.99

# F-Strings (empfohlen!)
print("=== F-Strings (Modern) ===\n")

print(f"Ich heisse {name}")
print(f"Ich bin {alter} Jahre alt")
print(f"Ich bin {groesse} Meter gross")
print()

# F-Strings mit Berechnungen
print("=== F-Strings mit Berechnungen ===\n")

a = 10
b = 20

print(f"Die Summe von {a} und {b} ist {a + b}")
print(f"Das Produkt von {a} und {b} ist {a * b}")
print(f"Nächstes Jahr bin ich {alter + 1} Jahre alt")
print()

# Formatierungs-Optionen
print("=== Formatierungs-Optionen ===\n")

# Dezimalstellen
print(f"Preis: {preis:.2f} CHF")  # 2 Dezimalstellen
print(f"Preis: {preis:.1f} CHF")  # 1 Dezimalstelle
print()

# Breite und Ausrichtung
print(f"Rechtsbündig: {preis:>10.2f} CHF")
print(f"Linksbündig:  {preis:<10.2f} CHF")
print(f"Zentriert:    {preis:^10.2f} CHF")
print()

# Zahlen mit Tausender-Trennzeichen
grosse_zahl = 1234567.89
print(f"Mit Trennzeichen: {grosse_zahl:,.2f}")
print()

# Prozent-Formatierung
anteil = 0.75
print(f"Anteil: {anteil:.0%}")  # 75%
print(f"Anteil: {anteil:.2%}")  # 75.00%
print()

# Mehrere Variablen
print("=== Mehrere Variablen ===\n")

print(f"{name} ist {alter} Jahre alt und {groesse}m gross")
print(f"Der Preis beträgt {preis:.2f} CHF")
print()

# Ausdrücke in F-Strings
print("=== Ausdrücke in F-Strings ===\n")

print(f"Grossbuchstaben: {name.upper()}")
print(f"Länge des Namens: {len(name)}")
print(f"Erste 2 Buchstaben: {name[:2]}")
print()

# Mehrzeilige F-Strings
print("=== Mehrzeilige F-Strings ===\n")

nachricht = f"""
Name:   {name}
Alter:  {alter} Jahre
Grösse: {groesse} m
Preis:  {preis:.2f} CHF
"""

print(nachricht)

# Alte Methoden (nicht empfohlen, aber gut zu kennen)
print("=== Alte Formatierungs-Methoden ===\n")

# format()-Methode
text1 = "Ich heisse {} und bin {} Jahre alt".format(name, alter)
print(f"format(): {text1}")

# %-Formatierung (sehr alt)
text2 = "Ich heisse %s und bin %d Jahre alt" % (name, alter)
print(f"%-Format: {text2}")
print()

# Praktisches Beispiel: Tabelle
print("=== Tabelle mit Formatierung ===\n")

print(f"{'Name':<15} {'Alter':>5} {'Preis':>10}")
print("-" * 32)
print(f"{'Anna':<15} {25:>5} {19.99:>10.2f}")
print(f"{'Max Muster':<15} {30:>5} {29.50:>10.2f}")
print(f"{'Lisa':<15} {22:>5} {15.00:>10.2f}")

