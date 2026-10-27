"""
Beispiel: Deutsch-Englisch Wörterbuch

Zeigt:
- Dictionary für Übersetzungen (Deutsch -> Englisch)
- Nachschlagen, Hinzufügen, Löschen, Alle anzeigen
- Rückwärts-Übersetzung (Englisch -> Deutsch)
- Set für die Menge der Anfangsbuchstaben (jeder nur einmal)

Das Programm läuft mit einem festen Demo-Ablauf (keine Eingaben nötig).
"""

# Globales Dictionary: Deutsch -> Englisch
woerterbuch = {
    "hund": "dog",
    "katze": "cat",
    "haus": "house",
    "buch": "book",
}


def uebersetze(wort: str) -> str | None:
    """
    Übersetzt ein deutsches Wort ins Englische.

    Args:
        wort: Deutsches Wort

    Returns:
        Englische Übersetzung, None wenn das Wort unbekannt ist
    """
    wort = wort.lower()
    if wort in woerterbuch:
        return woerterbuch[wort]
    return None


def uebersetze_rueckwaerts(englisch: str) -> str | None:
    """
    Sucht zu einem englischen Wort das deutsche Wort.

    Args:
        englisch: Englisches Wort

    Returns:
        Deutsches Wort, None wenn nicht gefunden
    """
    for deutsch, uebersetzung in woerterbuch.items():
        if uebersetzung == englisch.lower():
            return deutsch
    return None


def neues_wort(deutsch: str, englisch: str) -> None:
    """
    Fügt ein Wort hinzu (überschreibt eine vorhandene Übersetzung).

    Args:
        deutsch: Deutsches Wort
        englisch: Englische Übersetzung
    """
    woerterbuch[deutsch.lower()] = englisch.lower()
    print(f"Gespeichert: {deutsch.lower()} -> {englisch.lower()}")


def loesche_wort(deutsch: str) -> bool:
    """
    Löscht ein deutsches Wort aus dem Wörterbuch.

    Args:
        deutsch: Deutsches Wort

    Returns:
        True, wenn gelöscht wurde, sonst False
    """
    wort = deutsch.lower()
    if wort in woerterbuch:
        del woerterbuch[wort]
        print(f"Gelöscht: {wort}")
        return True
    print(f"'{wort}' ist nicht im Wörterbuch.")
    return False


def zeige_alle() -> None:
    """Zeigt alle Wörter alphabetisch sortiert an."""
    print("Wörterbuch Deutsch-Englisch")
    print("=" * 40)

    nummer = 1
    for deutsch in sorted(woerterbuch):
        print(f"{nummer}. {deutsch} -> {woerterbuch[deutsch]}")
        nummer += 1


def anfangsbuchstaben() -> set:
    """
    Sammelt die Anfangsbuchstaben aller deutschen Wörter.

    Ein Set speichert jeden Buchstaben nur einmal, auch wenn
    mehrere Wörter damit beginnen.

    Returns:
        Set mit den Anfangsbuchstaben
    """
    buchstaben = set()
    for deutsch in woerterbuch:
        buchstaben.add(deutsch[0])
    return buchstaben


def quiz_frage(deutsch: str, antwort: str) -> bool:
    """
    Prüft eine Quiz-Antwort (ohne Eingabe: Antwort wird übergeben).

    Args:
        deutsch: Abgefragtes deutsches Wort
        antwort: Gegebene englische Antwort

    Returns:
        True bei richtiger Antwort, sonst False
    """
    richtig = uebersetze(deutsch)
    if richtig is not None and antwort.lower() == richtig:
        print(f"'{deutsch}' -> '{antwort}': richtig!")
        return True
    print(f"'{deutsch}' -> '{antwort}': falsch (richtig wäre '{richtig}').")
    return False


if __name__ == "__main__":
    print("=" * 40)
    print("DEMO: WÖRTERBUCH")
    print("=" * 40)

    # 1. Alle Wörter zeigen
    print()
    zeige_alle()

    # 2. Übersetzen
    print("\n--- Übersetzen ---")
    for suchwort in ["Hund", "Auto"]:
        ergebnis = uebersetze(suchwort)
        if ergebnis is not None:
            print(f"{suchwort} = {ergebnis}")
        else:
            print(f"{suchwort} = (unbekannt)")

    # 3. Neue Wörter hinzufügen
    print("\n--- Wörter hinzufügen ---")
    neues_wort("Auto", "car")
    neues_wort("Apfel", "apple")

    # 4. Rückwärts-Übersetzung
    print("\n--- Englisch -> Deutsch ---")
    print(f"house = {uebersetze_rueckwaerts('house')}")
    print(f"tree = {uebersetze_rueckwaerts('tree')}")

    # 5. Löschen
    print("\n--- Löschen ---")
    loesche_wort("katze")
    loesche_wort("katze")

    # 6. Set: Anfangsbuchstaben
    print("\n--- Anfangsbuchstaben (Set) ---")
    print(sorted(anfangsbuchstaben()))
    print(f"Wörter: {len(woerterbuch)}, verschiedene Anfangsbuchstaben: "
          f"{len(anfangsbuchstaben())}")

    # 7. Quiz mit festen Antworten
    print("\n--- Quiz ---")
    punkte = 0
    if quiz_frage("hund", "dog"):
        punkte += 1
    if quiz_frage("buch", "bok"):
        punkte += 1
    if quiz_frage("auto", "car"):
        punkte += 1
    print(f"Punkte: {punkte} von 3")

    # 8. Endstand
    print()
    zeige_alle()
