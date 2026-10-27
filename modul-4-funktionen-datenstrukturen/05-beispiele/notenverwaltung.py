"""
Beispiel: Notenverwaltung

Zeigt den Umgang mit einem Dictionary, das Listen enthält:
- Schlüssel: Name der Person
- Wert: Liste der Noten (Schweizer Skala 1.0 - 6.0)

Funktionen: Note hinzufügen, Durchschnitt, beste/schlechteste Note,
Klassendurchschnitt, Notenverteilung und Statistik.

Das Programm läuft mit einem festen Demo-Ablauf (keine Eingaben nötig).
"""

BESTANDEN_AB = 4.0

# Globales Dictionary: Name -> Liste von Noten
noten = {
    "Anna": [5.5, 6.0, 5.0],
    "Max": [4.5, 5.0, 5.5],
    "Lisa": [3.5, 4.0, 3.0],
}


def note_hinzufuegen(student: str, note: float) -> None:
    """
    Fügt einem Studenten eine Note hinzu (legt ihn bei Bedarf neu an).

    Args:
        student: Name des Studenten
        note: Note zwischen 1.0 und 6.0
    """
    if note < 1.0 or note > 6.0:
        print(f"Ungültige Note {note} für {student} (erlaubt: 1.0 - 6.0).")
        return

    if student not in noten:
        noten[student] = []
    noten[student].append(note)


def durchschnitt(student: str) -> float:
    """
    Berechnet den Notendurchschnitt eines Studenten.

    Args:
        student: Name des Studenten

    Returns:
        Durchschnitt als float, 0.0 wenn keine Noten vorhanden sind
    """
    if student not in noten or len(noten[student]) == 0:
        return 0.0

    summe = 0
    for note in noten[student]:
        summe += note
    return summe / len(noten[student])


def beste_note(student: str) -> float:
    """
    Gibt die beste (höchste) Note eines Studenten zurück.

    Args:
        student: Name des Studenten

    Returns:
        Beste Note, 0.0 wenn keine Noten vorhanden sind
    """
    if student not in noten or len(noten[student]) == 0:
        return 0.0

    beste = noten[student][0]
    for note in noten[student]:
        if note > beste:
            beste = note
    return beste


def schlechteste_note(student: str) -> float:
    """
    Gibt die schlechteste (tiefste) Note eines Studenten zurück.

    Args:
        student: Name des Studenten

    Returns:
        Schlechteste Note, 0.0 wenn keine Noten vorhanden sind
    """
    if student not in noten or len(noten[student]) == 0:
        return 0.0

    schlechteste = noten[student][0]
    for note in noten[student]:
        if note < schlechteste:
            schlechteste = note
    return schlechteste


def klassendurchschnitt() -> float:
    """
    Berechnet den Durchschnitt aller Noten der ganzen Klasse.

    Returns:
        Klassendurchschnitt, 0.0 wenn keine Noten vorhanden sind
    """
    summe = 0
    anzahl = 0
    for student in noten:
        for note in noten[student]:
            summe += note
            anzahl += 1

    if anzahl == 0:
        return 0.0
    return summe / anzahl


def hat_bestanden(student: str) -> bool:
    """
    Prüft, ob der Durchschnitt eines Studenten mindestens 4.0 ist.

    Args:
        student: Name des Studenten

    Returns:
        True bei bestanden, sonst False
    """
    return durchschnitt(student) >= BESTANDEN_AB


def notenverteilung() -> dict:
    """
    Zählt, wie oft jede ganze Note (1 bis 6) in der Klasse vorkommt.

    Noten werden dabei abgerundet: 5.5 zählt zur Note 5.

    Returns:
        Dictionary Note (int) -> Anzahl
    """
    verteilung = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
    for student in noten:
        for note in noten[student]:
            ganze_note = int(note)
            verteilung[ganze_note] += 1
    return verteilung


def zeige_statistik(student: str) -> None:
    """
    Zeigt Min, Max, Durchschnitt und Status eines Studenten.

    Args:
        student: Name des Studenten
    """
    if hat_bestanden(student):
        status = "bestanden"
    else:
        status = "NICHT bestanden"

    print(f"{student}: Noten {noten[student]}")
    print(f"  Beste Note:          {beste_note(student)}")
    print(f"  Schlechteste Note:   {schlechteste_note(student)}")
    print(f"  Durchschnitt:        {durchschnitt(student):.2f}")
    print(f"  Status:              {status}")


if __name__ == "__main__":
    print("=" * 40)
    print("DEMO: NOTENVERWALTUNG")
    print("=" * 40)

    # 1. Neue Noten hinzufügen
    print("\n--- Noten hinzufügen ---")
    note_hinzufuegen("Anna", 5.5)
    note_hinzufuegen("Max", 6.0)
    note_hinzufuegen("Tom", 4.5)  # neuer Student
    note_hinzufuegen("Lisa", 7.0)  # ungültig

    # 2. Statistik pro Student
    print("\n--- Statistik pro Student ---")
    for name in noten:
        zeige_statistik(name)
        print("-" * 40)

    # 3. Klassendurchschnitt
    print("\n--- Klasse ---")
    print(f"Klassendurchschnitt: {klassendurchschnitt():.2f}")

    # 4. Notenverteilung
    print("\n--- Notenverteilung ---")
    verteilung = notenverteilung()
    for ganze_note in verteilung:
        balken = "#" * verteilung[ganze_note]
        print(f"Note {ganze_note}: {balken} ({verteilung[ganze_note]})")
