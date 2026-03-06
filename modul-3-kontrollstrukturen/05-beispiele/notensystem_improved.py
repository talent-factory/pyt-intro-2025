"""
Notensystem - Punkte in Noten umwandeln (alternative Version)
Alternative Musterlösung für Übung 1, Modul 3

Konvertiert Punkte (0-100) in Noten (2-6, Schweizer Skala).

Alternative Ansätze gegenüber der Basisversion (notensystem.py):
- Notenskala als Datenstruktur (wartbar und erweiterbar)
- Notenberechnung über Schleife statt if/elif-Kette
- Eingabevalidierung inline statt in separater Funktion
- Schutz durch if __name__ == '__main__': Guard
"""

# Notenskala: Liste von Tupeln (Mindestpunktzahl, Note, Bewertung)
# WICHTIG: Muss absteigend nach Mindestpunktzahl sortiert sein!
# Der letzte Eintrag (0) dient als Auffangwert fuer alle gueltigen
# Punktzahlen unter 60.
# Neue Notenstufen können einfach als Zeile hinzugefügt werden.
notenskala = sorted(
    [
        (90, 6, "Hervorragend!"),
        (80, 5, "Sehr gut!"),
        (70, 4, "Gut!"),
        (60, 3, "Genügend"),
        (0, 2, "Ungenügend"),
    ],
    key=lambda x: x[0],
    reverse=True,
)

if __name__ == "__main__":
    print("=" * 40)
    print("Erweitertes Notensystem")
    print("=" * 40)

    # Eingabe mit Validierung
    # isdigit() akzeptiert nur Ziffern (0-9), negative Zahlen
    # werden dadurch bereits abgefangen
    while True:
        eingabe = input("\nPunkte (0-100): ").strip()

        if not eingabe.isdigit():
            print("Fehler: Bitte eine gültige Zahl eingeben!")
            continue

        punkte = int(eingabe)

        if punkte > 100:
            print("Fehler: Wert muss zwischen 0 und 100 liegen!")
            continue

        break

    # Durchlaufe die Notenskala von oben (höchste Punktzahl) nach unten.
    # Die erste Schwelle, die erreicht wird, bestimmt die Note.
    # Der Eintrag mit 0 Punkten stellt sicher, dass immer eine Note
    # gefunden wird.
    for mindestpunktzahl, note, bewertung in notenskala:
        if punkte >= mindestpunktzahl:
            break

    # Ergebnis formatiert ausgeben
    print()
    print("=" * 40)
    print(f"Punkte:    {punkte}")
    print(f"Note:      {note}")
    print(f"Bewertung: {bewertung}")
    print("=" * 40)
