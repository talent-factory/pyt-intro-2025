"""
Notensystem - Punkte in Noten umwandeln (alternative Version)
Musterlösung für Übung 1, Modul 3

Konvertiert Punkte (0-100) in Noten (2-6, vereinfachte Schweizer Skala).

Alternative Ansätze gegenüber der Basisversion (notensystem.py):
- Notenskala als Datenstruktur (wartbar und erweiterbar)
- Notenberechnung über Schleife statt if/elif-Kette
- Eingabevalidierung direkt im Hauptprogramm (ohne Funktionen)
"""

# Notenskala: Liste von Tupeln (Mindestpunktzahl, Note, Bewertung)
# WICHTIG: Muss absteigend nach Mindestpunktzahl sortiert sein!
# Der letzte Eintrag (0) dient als Auffangwert fuer alle Eingaben.
# Neue Notenstufen können einfach als Zeile hinzugefügt werden.
notenskala = [
    (90, 6, "Hervorragend!"),
    (80, 5, "Sehr gut!"),
    (70, 4, "Gut!"),
    (60, 3, "Genügend"),
    (0,  2, "Ungenügend"),
]

if __name__ == "__main__":
    print("=" * 40)
    print("Erweitertes Notensystem")
    print("=" * 40)

    # Eingabe mit Validierung
    # isdigit() akzeptiert nur Ziffern (0-9), negative Zahlen
    # werden dadurch bereits abgefangen
    while True:
        eingabe = input("\nPunkte (0-100): ")

        if not eingabe.isdigit():
            print("Fehler: Bitte eine gültige Zahl eingeben!")
            continue

        punkte = int(eingabe)

        if punkte > 100:
            print("Fehler: Wert muss zwischen 0 und 100 liegen!")
            continue

        break

    # Notenberechnung über die Notenskala
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
