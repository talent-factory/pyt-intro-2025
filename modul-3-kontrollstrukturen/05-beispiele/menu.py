"""
Taschenrechner mit Menü
Demonstriert ein Menü-System für einen einfachen Taschenrechner.

Konzepte:
- while-Schleife für das Menü
- if/elif/else für die Auswahl
- String-Methoden für die Eingabevalidierung
- continue zum erneuten Anzeigen des Menüs
- break zum Beenden des Programms
"""

print("=" * 50)
print("           TASCHENRECHNER")
print("=" * 50)

# Hauptschleife - läuft, bis der Benutzer "5" zum Beenden wählt
while True:
    # Menü anzeigen
    print("\nWas möchten Sie tun?")
    print("1. Addieren")
    print("2. Subtrahieren")
    print("3. Multiplizieren")
    print("4. Dividieren")
    print("5. Beenden")

    wahl = input("\nIhre Wahl: ").strip()

    # Beenden
    if wahl == "5":
        print("\n👋 Auf Wiedersehen!")
        break

    # Gültige Wahl prüfen
    if wahl not in ["1", "2", "3", "4"]:
        print("\n❌ Ungültige Wahl! Bitte 1-5 eingeben.")
        continue

    # Zahlen einlesen und validieren
    eingabe_a = input("\nErste Zahl: ").strip()
    eingabe_b = input("Zweite Zahl: ").strip()

    # Validierung: Wir akzeptieren ganze Zahlen (auch negative)
    a_gueltig = eingabe_a.lstrip("-").isdigit()
    b_gueltig = eingabe_b.lstrip("-").isdigit()

    if not a_gueltig or not b_gueltig:
        print("❌ Bitte ganze Zahlen eingeben!")
        continue

    zahl1 = int(eingabe_a)
    zahl2 = int(eingabe_b)

    # Berechnung je nach Wahl
    if wahl == "1":
        ergebnis = zahl1 + zahl2
        operator = "+"
    elif wahl == "2":
        ergebnis = zahl1 - zahl2
        operator = "-"
    elif wahl == "3":
        ergebnis = zahl1 * zahl2
        operator = "*"
    else:  # wahl == "4"
        # Division durch 0 abfangen
        if zahl2 == 0:
            print("❌ Division durch 0 ist nicht möglich!")
            continue
        ergebnis = zahl1 / zahl2
        operator = "/"

    # Ergebnis ausgeben
    print(f"\n✓ Ergebnis: {zahl1} {operator} {zahl2} = {ergebnis}")
