"""
Muster zeichnen
Demonstriert verschachtelte Schleifen für visuelle Muster.

Konzepte:
- Verschachtelte for-Schleifen
- print() mit end=""
- Mathematische Muster
- Bedingte Ausgabe
"""

print("=" * 50)
print("           MUSTER-GENERATOR")
print("=" * 50)


# ============================================================
# Rechteck
# ============================================================
breite = 8
hoehe = 5

print(f"\n=== Rechteck {breite}x{hoehe} ===\n")

for i in range(hoehe):
    for j in range(breite):
        print("*", end="")
    print()


# ============================================================
# Dreieck (rechtwinklig, links ausgerichtet)
# ============================================================
hoehe = 5

print(f"\n=== Dreieck (Höhe {hoehe}) ===\n")

for i in range(1, hoehe + 1):
    for j in range(i):
        print("*", end="")
    print()


# ============================================================
# Umgekehrtes Dreieck
# ============================================================
hoehe = 5

print(f"\n=== Umgekehrtes Dreieck (Höhe {hoehe}) ===\n")

for i in range(hoehe, 0, -1):
    for j in range(i):
        print("*", end="")
    print()


# ============================================================
# Pyramide (zentriert)
# ============================================================
hoehe = 5

print(f"\n=== Pyramide (Höhe {hoehe}) ===\n")

for i in range(1, hoehe + 1):
    # Leerzeichen vor den Sternen
    for j in range(hoehe - i):
        print(" ", end="")

    # Sterne in der Zeile (ungerade Anzahl: 1, 3, 5, ...)
    for k in range(2 * i - 1):
        print("*", end="")

    print()


# ============================================================
# Raute (Pyramide + umgekehrte Pyramide)
# ============================================================
groesse = 5

print(f"\n=== Raute (Grösse {groesse}) ===\n")

# Obere Hälfte (inkl. breiteste Zeile in der Mitte)
for i in range(1, groesse + 1):
    for j in range(groesse - i):
        print(" ", end="")
    for k in range(2 * i - 1):
        print("*", end="")
    print()

# Untere Hälfte
for i in range(groesse - 1, 0, -1):
    for j in range(groesse - i):
        print(" ", end="")
    for k in range(2 * i - 1):
        print("*", end="")
    print()


# ============================================================
# Schachbrett-Muster
# ============================================================
groesse = 8

print(f"\n=== Schachbrett {groesse}x{groesse} ===\n")

for zeile in range(groesse):
    for spalte in range(groesse):
        # Wenn die Summe der Indizes gerade ist: weisses Feld
        if (zeile + spalte) % 2 == 0:
            print("□", end=" ")
        else:
            print("■", end=" ")
    print()


# ============================================================
# Zahlen-Pyramide
# ============================================================
hoehe = 5

print(f"\n=== Zahlen-Pyramide (Höhe {hoehe}) ===\n")

for i in range(1, hoehe + 1):
    # Leerzeichen vor den Zahlen
    for j in range(hoehe - i):
        print(" ", end="")

    # Aufsteigende Zahlen: 1, 2, ..., i
    for k in range(1, i + 1):
        print(k, end="")

    # Absteigende Zahlen: i-1, i-2, ..., 1
    for k in range(i - 1, 0, -1):
        print(k, end="")

    print()


# ============================================================
# Multiplikationstabelle
# ============================================================
groesse = 10

print(f"\n=== Multiplikationstabelle {groesse}x{groesse} ===\n")

# Kopfzeile
print("   ", end="")
for i in range(1, groesse + 1):
    print(f"{i:3}", end=" ")
print()
print("   " + "-" * (groesse * 4))

# Tabelle: jede Zeile ein Faktor von 1 bis groesse
for i in range(1, groesse + 1):
    print(f"{i:2} |", end="")
    for j in range(1, groesse + 1):
        print(f"{i * j:3}", end=" ")
    print()


# ============================================================
# Abschluss
# ============================================================
print("\n" + "=" * 50)
print("Alle Muster angezeigt!")
print("=" * 50)
