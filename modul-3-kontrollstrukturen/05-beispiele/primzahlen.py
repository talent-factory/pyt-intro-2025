"""
Primzahlen-Finder
Demonstriert verschachtelte Schleifen und mathematische Algorithmen.

Konzepte:
- Verschachtelte for-Schleifen
- Break für Optimierung
- Listen
- Mathematik
"""

print("=" * 50)
print("           PRIMZAHLEN-FINDER")
print("=" * 50)

# Hauptschleife
while True:
    print("\n1. Primzahl-Test")
    print("2. Primzahlen bis N")
    print("3. Primfaktorzerlegung")
    print("4. Beenden")

    wahl = input("\nWahl: ").strip()

    if wahl == "1":
        # Primzahl-Test
        eingabe = input("\nZahl: ").strip()

        if not eingabe.isdigit():
            print("❌ Bitte eine positive ganze Zahl eingeben!")
            continue

        n = int(eingabe)

        # Prüfen ob n eine Primzahl ist
        ist_prim = False

        if n < 2:
            ist_prim = False
        elif n == 2:
            ist_prim = True
        elif n % 2 == 0:
            ist_prim = False
        else:
            # Nur bis Wurzel prüfen, nur ungerade Teiler
            ist_prim = True
            for teiler in range(3, int(n**0.5) + 1, 2):
                if n % teiler == 0:
                    ist_prim = False
                    break

        if ist_prim:
            print(f"✓ {n} ist eine Primzahl")
        else:
            print(f"✗ {n} ist keine Primzahl")

    elif wahl == "2":
        # Primzahlen bis N
        eingabe = input("\nBis zu welcher Zahl? ").strip()

        if not eingabe.isdigit():
            print("❌ Bitte eine positive ganze Zahl eingeben!")
            continue

        n = int(eingabe)
        primzahlen = []

        # Alle Zahlen von 2 bis n durchgehen
        for zahl in range(2, n + 1):
            # Prüfen ob zahl eine Primzahl ist
            ist_prim = False

            if zahl == 2:
                ist_prim = True
            elif zahl % 2 == 0:
                ist_prim = False
            else:
                ist_prim = True
                for teiler in range(3, int(zahl**0.5) + 1, 2):
                    if zahl % teiler == 0:
                        ist_prim = False
                        break

            if ist_prim:
                primzahlen.append(zahl)

        print(f"\nPrimzahlen bis {n}:")

        # Ausgabe in Zeilen zu je 10 Zahlen
        for i in range(0, len(primzahlen), 10):
            zeile = ""
            for j in range(i, min(i + 10, len(primzahlen))):
                if j > i:
                    zeile += ", "
                zeile += str(primzahlen[j])
            print(zeile)

        print("\nStatistik:")
        print(f"- Anzahl: {len(primzahlen)}")
        if len(primzahlen) > 0:
            print(f"- Kleinste: {primzahlen[0]}")
            print(f"- Grösste: {primzahlen[-1]}")

    elif wahl == "3":
        # Primfaktorzerlegung
        eingabe = input("\nZahl: ").strip()

        if not eingabe.isdigit():
            print("❌ Bitte eine positive ganze Zahl eingeben!")
            continue

        n = int(eingabe)

        if n < 2:
            print("❌ Zahl muss mindestens 2 sein!")
            continue

        # Primfaktoren finden
        faktoren = []
        teiler = 2
        original_n = n

        while n > 1:
            while n % teiler == 0:
                faktoren.append(teiler)
                n //= teiler
            teiler += 1

            # Optimierung: Wenn teiler > √n, dann ist n prim
            if teiler * teiler > n and n > 1:
                faktoren.append(n)
                break

        print(f"\nPrimfaktorzerlegung von {original_n}:")

        # Faktoren als String zusammenbauen
        faktoren_str = ""
        for i in range(len(faktoren)):
            if i > 0:
                faktoren_str += " × "
            faktoren_str += str(faktoren[i])

        print(f"{original_n} = {faktoren_str}")

    elif wahl == "4":
        print("\n👋 Auf Wiedersehen!")
        break

    else:
        print("\n❌ Ungültige Wahl! Bitte 1-4 wählen.")
