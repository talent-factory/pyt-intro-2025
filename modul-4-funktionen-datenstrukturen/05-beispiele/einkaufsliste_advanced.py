"""
Beispiel: Einkaufsliste (erweitert)

Zeigt ein Dictionary mit verschachtelten Dictionaries:
- Schlüssel: Artikelname
- Wert: Dictionary mit "menge" und "preis" (pro Stück)

Funktionen: hinzufügen, Menge ändern, entfernen, anzeigen, Total.

Das Programm läuft mit einem festen Demo-Ablauf (keine Eingaben nötig).
"""

# Globales Dictionary: Artikel -> {"menge": ..., "preis": ...}
einkaufsliste = {}


def artikel_hinzufuegen(name: str, menge: int, preis: float) -> None:
    """
    Fügt einen Artikel hinzu. Existiert er schon, wird die Menge erhöht.

    Args:
        name: Name des Artikels
        menge: Anzahl Stück
        preis: Preis pro Stück in CHF
    """
    if name in einkaufsliste:
        einkaufsliste[name]["menge"] += menge
        print(f"{name}: Menge erhöht auf {einkaufsliste[name]['menge']}")
    else:
        einkaufsliste[name] = {"menge": menge, "preis": preis}
        print(f"{name}: {menge} x {preis:.2f} CHF hinzugefügt")


def menge_aendern(name: str, neue_menge: int) -> None:
    """
    Setzt die Menge eines Artikels neu (0 entfernt den Artikel).

    Args:
        name: Name des Artikels
        neue_menge: Neue Anzahl
    """
    if name not in einkaufsliste:
        print(f"{name}: nicht auf der Liste.")
        return

    if neue_menge <= 0:
        artikel_entfernen(name)
    else:
        einkaufsliste[name]["menge"] = neue_menge
        print(f"{name}: Menge jetzt {neue_menge}")


def artikel_entfernen(name: str) -> None:
    """
    Entfernt einen Artikel von der Liste.

    Args:
        name: Name des Artikels
    """
    if name in einkaufsliste:
        del einkaufsliste[name]
        print(f"{name}: entfernt")
    else:
        print(f"{name}: nicht auf der Liste.")


def zeilen_total(name: str) -> float:
    """
    Berechnet Menge mal Preis für einen Artikel.

    Args:
        name: Name des Artikels

    Returns:
        Zeilen-Total in CHF
    """
    artikel = einkaufsliste[name]
    return artikel["menge"] * artikel["preis"]


def gesamt_total() -> float:
    """
    Berechnet die Summe aller Zeilen-Totale.

    Returns:
        Gesamtbetrag in CHF
    """
    summe = 0.0
    for name in einkaufsliste:
        summe += zeilen_total(name)
    return summe


def teuerster_artikel() -> str | None:
    """
    Findet den Artikel mit dem höchsten Zeilen-Total.

    Returns:
        Name des Artikels, None wenn die Liste leer ist
    """
    teuerster = None
    hoechster_betrag = 0.0
    for name in einkaufsliste:
        betrag = zeilen_total(name)
        if betrag > hoechster_betrag:
            hoechster_betrag = betrag
            teuerster = name
    return teuerster


def zeige_liste() -> None:
    """Zeigt die Einkaufsliste als Tabelle mit Total an."""
    print("EINKAUFSLISTE")
    print("=" * 40)

    if len(einkaufsliste) == 0:
        print("Die Liste ist leer.")
        return

    print(f"{'Artikel':<12}{'Menge':>6}{'Preis':>10}{'Total':>10}")
    print("-" * 40)
    for name in sorted(einkaufsliste):
        menge = einkaufsliste[name]["menge"]
        preis = einkaufsliste[name]["preis"]
        print(f"{name:<12}{menge:>6}{preis:>10.2f}{zeilen_total(name):>10.2f}")
    print("-" * 40)
    print(f"{'Gesamt (CHF)':<28}{gesamt_total():>12.2f}")


if __name__ == "__main__":
    print("=" * 40)
    print("DEMO: EINKAUFSLISTE")
    print("=" * 40)

    # 1. Artikel hinzufügen
    print("\n--- Artikel hinzufügen ---")
    artikel_hinzufuegen("Milch", 2, 1.50)
    artikel_hinzufuegen("Brot", 1, 3.20)
    artikel_hinzufuegen("Äpfel", 6, 0.60)
    artikel_hinzufuegen("Käse", 1, 7.80)
    artikel_hinzufuegen("Milch", 1, 1.50)  # Menge wird erhöht

    # 2. Anzeigen
    print()
    zeige_liste()

    # 3. Ändern und entfernen
    print("\n--- Änderungen ---")
    menge_aendern("Äpfel", 4)
    artikel_entfernen("Brot")
    artikel_entfernen("Schokolade")

    # 4. Ergebnis
    print()
    zeige_liste()

    print(f"\nTeuerster Posten: {teuerster_artikel()}")
