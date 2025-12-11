"""
Beispiel: CSV-Dateien

Zeigt:
- CSV lesen und schreiben
- DictReader und DictWriter
- Datenverarbeitung
"""

import csv


def kontakte_erstellen():
    """Erstellt Beispiel-Kontakte."""
    kontakte = [
        {
            "name": "Anna Muster",
            "email": "anna@example.com",
            "telefon": "079 123 45 67",
        },
        {"name": "Max Meier", "email": "max@example.com", "telefon": "078 987 65 43"},
        {
            "name": "Lisa Schmidt",
            "email": "lisa@example.com",
            "telefon": "077 555 12 34",
        },
    ]

    with open("kontakte.csv", "w", newline="") as f:
        fieldnames = ["name", "email", "telefon"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(kontakte)

    print("✓ Kontakte erstellt")


def kontakte_anzeigen():
    """Zeigt alle Kontakte."""
    print("\n" + "=" * 50)
    print("KONTAKTE")
    print("=" * 50)

    with open("kontakte.csv") as f:
        reader = csv.DictReader(f)
        for i, kontakt in enumerate(reader, 1):
            print(f"{i}. {kontakt['name']}")
            print(f"   Email: {kontakt['email']}")
            print(f"   Tel: {kontakt['telefon']}")
            print()


def kontakt_suchen(name):
    """Sucht Kontakt nach Name."""
    with open("kontakte.csv") as f:
        reader = csv.DictReader(f)
        for kontakt in reader:
            if name.lower() in kontakt["name"].lower():
                return kontakt
    return None


if __name__ == "__main__":
    print("=" * 50)
    print("CSV DEMO")
    print("=" * 50)

    kontakte_erstellen()
    kontakte_anzeigen()

    gefunden = kontakt_suchen("Max")
    if gefunden:
        print(f"\nGefunden: {gefunden['name']} ({gefunden['email']})")
