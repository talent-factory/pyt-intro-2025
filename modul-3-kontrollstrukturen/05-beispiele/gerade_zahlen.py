"""
Gerade Zahlen filtern
Musterlösung für Übung 5, Modul 3

Filtert alle geraden Zahlen aus einer Liste von 1-20.
"""

print("=== Gerade Zahlen filtern ===\n")

# Liste mit Zahlen 1-20 erstellen
alle_zahlen = list(range(1, 21))

# Gerade Zahlen filtern
gerade_zahlen = []

for zahl in alle_zahlen:
    if zahl % 2 == 0:
        gerade_zahlen.append(zahl)

# Ausgabe
print(f"Alle Zahlen: {alle_zahlen}")
print(f"Gerade Zahlen: {gerade_zahlen}")
print(f"Anzahl: {len(gerade_zahlen)}")
