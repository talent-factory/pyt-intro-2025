"""
Beispiel: Dictionary-Operationen

Zeigt:
- Dictionaries erstellen
- Zugriff und Manipulation
- Iteration
"""


def zeige_person(person: dict[str, str]) -> None:
    """Zeigt Person formatiert."""
    print("\nPerson:")
    for key, value in person.items():
        print(f"  {key}: {value}")


def erstelle_kontakt(name: str, email: str, telefon: str) -> dict[str, str]:
    """Erstellt einen Kontakt."""
    return {"name": name, "email": email, "telefon": telefon}


def suche_kontakt(kontakte: list[dict[str, str]], name: str) -> dict[str, str] | None:
    """Sucht Kontakt nach Name."""
    for kontakt in kontakte:
        if kontakt["name"].lower() == name.lower():
            return kontakt
    return None


if __name__ == "__main__":
    print("=" * 50)
    print("DICTIONARY DEMO")
    print("=" * 50)

    # Kontakte erstellen
    kontakte = [
        erstelle_kontakt("Anna Muster", "anna@example.com", "079 123 45 67"),
        erstelle_kontakt("Max Meier", "max@example.com", "078 987 65 43"),
        erstelle_kontakt("Lisa Schmidt", "lisa@example.com", "077 555 12 34"),
    ]

    # Alle anzeigen
    print("\nAlle Kontakte:")
    for i, kontakt in enumerate(kontakte, 1):
        print(f"{i}. {kontakt['name']} ({kontakt['email']})")

    # Suchen
    gesuchter = suche_kontakt(kontakte, "Max")
    if gesuchter:
        zeige_person(gesuchter)
