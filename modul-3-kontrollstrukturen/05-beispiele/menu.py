"""
Menü-System
Demonstriert ein vollständiges Menü-System mit verschiedenen Funktionen.

Konzepte:
- While-Schleife für Menü
- If-elif-else für Auswahl
- Funktionen für Modularität
- Input-Validierung
"""


def taschenrechner() -> None:
    """Einfacher Taschenrechner."""
    print("\n=== TASCHENRECHNER ===")

    try:
        zahl1 = float(input("Erste Zahl: "))
        operator = input("Operator (+, -, *, /): ")
        zahl2 = float(input("Zweite Zahl: "))

        if operator == "+":
            ergebnis = zahl1 + zahl2
        elif operator == "-":
            ergebnis = zahl1 - zahl2
        elif operator == "*":
            ergebnis = zahl1 * zahl2
        elif operator == "/":
            if zahl2 == 0:
                print("❌ Division durch 0 nicht möglich!")
                return
            ergebnis = zahl1 / zahl2
        else:
            print("❌ Ungültiger Operator!")
            return

        print(f"\n{zahl1} {operator} {zahl2} = {ergebnis}")

    except ValueError:
        print("❌ Ungültige Eingabe!")


def temperatur_umrechner() -> None:
    """Rechnet zwischen Celsius und Fahrenheit um."""
    print("\n=== TEMPERATUR-UMRECHNER ===")
    print("1. Celsius → Fahrenheit")
    print("2. Fahrenheit → Celsius")

    wahl = input("\nWahl: ")

    try:
        if wahl == "1":
            celsius = float(input("Celsius: "))
            fahrenheit = celsius * 9 / 5 + 32
            print(f"{celsius}°C = {fahrenheit:.1f}°F")

        elif wahl == "2":
            fahrenheit = float(input("Fahrenheit: "))
            celsius = (fahrenheit - 32) * 5 / 9
            print(f"{fahrenheit}°F = {celsius:.1f}°C")

        else:
            print("❌ Ungültige Wahl!")

    except ValueError:
        print("❌ Ungültige Eingabe!")


def bmi_rechner() -> None:
    """Berechnet den Body-Mass-Index."""
    print("\n=== BMI-RECHNER ===")

    try:
        gewicht = float(input("Gewicht (kg): "))
        groesse = float(input("Grösse (m): "))

        if gewicht <= 0 or groesse <= 0:
            print("❌ Werte müssen positiv sein!")
            return

        bmi = gewicht / (groesse**2)

        print(f"\nBMI: {bmi:.1f}")

        if bmi < 18.5:
            kategorie = "Untergewicht"
        elif bmi < 25:
            kategorie = "Normalgewicht"
        elif bmi < 30:
            kategorie = "Übergewicht"
        else:
            kategorie = "Adipositas"

        print(f"Kategorie: {kategorie}")

    except ValueError:
        print("❌ Ungültige Eingabe!")


def wuerfel_simulator() -> None:
    """Simuliert Würfelwürfe."""
    import random

    print("\n=== WÜRFEL-SIMULATOR ===")

    try:
        anzahl = int(input("Wie viele Würfel? "))

        if anzahl <= 0:
            print("❌ Anzahl muss positiv sein!")
            return

        print("\nErgebnisse:")
        summe = 0

        for i in range(anzahl):
            wurf = random.randint(1, 6)
            print(f"Würfel {i + 1}: {wurf}")
            summe += wurf

        print(f"\nSumme: {summe}")
        print(f"Durchschnitt: {summe / anzahl:.2f}")

    except ValueError:
        print("❌ Ungültige Eingabe!")


def passwort_generator() -> None:
    """Generiert ein zufälliges Passwort."""
    import random
    import string

    print("\n=== PASSWORT-GENERATOR ===")

    try:
        laenge = int(input("Passwort-Länge: "))

        if laenge < 4:
            print("❌ Passwort muss mindestens 4 Zeichen lang sein!")
            return

        # Zeichensätze
        buchstaben = string.ascii_letters
        zahlen = string.digits
        sonderzeichen = "!@#$%^&*"

        alle_zeichen = buchstaben + zahlen + sonderzeichen

        # Passwort generieren
        passwort = "".join(random.choice(alle_zeichen) for _ in range(laenge))

        print(f"\nGeneriertes Passwort: {passwort}")

    except ValueError:
        print("❌ Ungültige Eingabe!")


def main() -> None:
    """Hauptprogramm mit Menü."""
    print("\n" + "=" * 50)
    print("           WERKZEUG-SAMMLUNG")
    print("=" * 50)

    while True:
        print("\n1. Taschenrechner")
        print("2. Temperatur-Umrechner")
        print("3. BMI-Rechner")
        print("4. Würfel-Simulator")
        print("5. Passwort-Generator")
        print("6. Beenden")

        wahl = input("\nWahl: ").strip()

        if wahl == "1":
            taschenrechner()

        elif wahl == "2":
            temperatur_umrechner()

        elif wahl == "3":
            bmi_rechner()

        elif wahl == "4":
            wuerfel_simulator()

        elif wahl == "5":
            passwort_generator()

        elif wahl == "6":
            print("\n👋 Auf Wiedersehen!")
            break

        else:
            print("\n❌ Ungültige Wahl! Bitte 1-6 wählen.")


if __name__ == "__main__":
    main()
