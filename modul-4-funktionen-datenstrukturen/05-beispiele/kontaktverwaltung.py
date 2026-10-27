"""
Beispiel: Vollständige Kontaktverwaltung

Kombiniert Funktionen, Dictionaries und Listen:
- Jeder Kontakt ist ein Dictionary (name, email, telefon)
- Alle Kontakte stehen in einer Liste
- Funktionen: hinzufügen, anzeigen, suchen, löschen

Das Programm läuft mit einem festen Demo-Ablauf (keine Eingaben nötig).
"""

# Globale Liste für alle Kontakte
kontakte = []


def neuer_kontakt(name: str, email: str, telefon: str) -> None:
    """
    Fügt einen neuen Kontakt zur Liste hinzu.

    Args:
        name: Name der Person
        email: E-Mail-Adresse
        telefon: Telefonnummer
    """
    kontakt = {"name": name, "email": email, "telefon": telefon}
    kontakte.append(kontakt)
    print(f"Kontakt '{name}' wurde hinzugefügt.")


def zeige_kontakte() -> None:
    """
    Zeigt alle Kontakte nummeriert an.

    Returns:
        None
    """
    print("KONTAKTVERWALTUNG")
    print("=" * 40)

    if len(kontakte) == 0:
        print("Keine Kontakte vorhanden.")
        return

    nummer = 1
    for kontakt in kontakte:
        print(f"{nummer}. {kontakt['name']} ({kontakt['email']}, {kontakt['telefon']})")
        nummer += 1


def suche_kontakt(name: str) -> dict | None:
    """
    Sucht einen Kontakt nach Name (Gross-/Kleinschreibung egal).

    Args:
        name: Gesuchter Name (oder Teil davon)

    Returns:
        Der gefundene Kontakt als Dictionary, sonst None
    """
    for kontakt in kontakte:
        if name.lower() in kontakt["name"].lower():
            return kontakt
    return None


def loesche_kontakt(name: str) -> bool:
    """
    Löscht den Kontakt mit dem genau passenden Namen.

    Args:
        name: Name des Kontakts, der gelöscht werden soll

    Returns:
        True, wenn ein Kontakt gelöscht wurde, sonst False
    """
    for kontakt in kontakte:
        if kontakt["name"].lower() == name.lower():
            kontakte.remove(kontakt)
            print(f"Kontakt '{kontakt['name']}' wurde gelöscht.")
            return True
    print(f"Kein Kontakt mit dem Namen '{name}' gefunden.")
    return False


if __name__ == "__main__":
    print("=" * 40)
    print("DEMO: KONTAKTVERWALTUNG")
    print("=" * 40)

    # 1. Kontakte hinzufügen
    print("\n--- Kontakte hinzufügen ---")
    neuer_kontakt("Anna Muster", "anna@example.com", "079 123 45 67")
    neuer_kontakt("Max Meier", "max@example.com", "078 987 65 43")
    neuer_kontakt("Lisa Schmidt", "lisa@example.com", "077 555 12 34")

    # 2. Alle anzeigen
    print("\n--- Alle Kontakte ---")
    zeige_kontakte()

    # 3. Suchen
    print("\n--- Suche nach 'max' ---")
    gefunden = suche_kontakt("max")
    if gefunden is not None:
        print(f"Gefunden: {gefunden['name']}, Tel. {gefunden['telefon']}")
    else:
        print("Nicht gefunden.")

    print("\n--- Suche nach 'Peter' ---")
    gefunden = suche_kontakt("Peter")
    if gefunden is not None:
        print(f"Gefunden: {gefunden['name']}")
    else:
        print("Nicht gefunden.")

    # 4. Löschen
    print("\n--- Löschen ---")
    loesche_kontakt("Max Meier")
    loesche_kontakt("Peter Unbekannt")

    # 5. Liste nach dem Löschen
    print("\n--- Kontakte nach dem Löschen ---")
    zeige_kontakte()
