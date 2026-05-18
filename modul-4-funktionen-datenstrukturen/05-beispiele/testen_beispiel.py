"""
Beispiel: Funktionen zum Testen

Dieses Modul enthaelt einfache Funktionen, die als Grundlage
fuer die Testing-Lektion dienen. Jede Funktion hat einen
klaren Rueckgabewert und ist damit gut testbar.

Konzepte:
- Testbare Funktionen mit return
- Verschiedene Rueckgabetypen (bool, float, dict)
- Guard Clauses fuer Grenzfaelle
"""


def ist_gerade(zahl: int) -> bool:
    """
    Prueft ob eine Zahl gerade ist.

    Args:
        zahl: Ganze Zahl zum Pruefen

    Returns:
        True wenn gerade, False wenn ungerade
    """
    return zahl % 2 == 0


def berechne_durchschnitt(zahlen: list[float]) -> float:
    """
    Berechnet den Durchschnitt einer Liste von Zahlen.

    Args:
        zahlen: Liste von Zahlen

    Returns:
        Durchschnittswert, oder 0.0 bei leerer Liste
    """
    if len(zahlen) == 0:
        return 0.0
    summe = 0
    for zahl in zahlen:
        summe += zahl
    return summe / len(zahlen)


def erstelle_kontakt(name: str, email: str, telefon: str = "") -> dict[str, str]:
    """
    Erstellt einen Kontakt als Dictionary.

    Args:
        name: Name der Person
        email: E-Mail-Adresse
        telefon: Telefonnummer (optional, Standard: "")

    Returns:
        Dictionary mit name, email, telefon
    """
    return {"name": name, "email": email, "telefon": telefon}


if __name__ == "__main__":
    print("=" * 40)
    print("Funktionen zum Testen")
    print("=" * 40)

    # ist_gerade
    print(f"\n4 ist gerade: {ist_gerade(4)}")
    print(f"7 ist gerade: {ist_gerade(7)}")

    # berechne_durchschnitt
    noten = [5.5, 4.0, 6.0, 5.0]
    print(f"\nDurchschnitt von {noten}: {berechne_durchschnitt(noten):.2f}")
    print(f"Durchschnitt von []: {berechne_durchschnitt([])}")

    # erstelle_kontakt
    kontakt = erstelle_kontakt("Anna", "anna@example.com", "079 123 45 67")
    print(f"\nKontakt: {kontakt}")
