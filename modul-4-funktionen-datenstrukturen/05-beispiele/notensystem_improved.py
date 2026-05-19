"""
Notensystem mit Datenstruktur - Alternative zum if/elif-Ansatz

Konvertiert Punkte (0-100) in Noten (2-6, Schweizer Skala).

Demonstriert Konzepte aus Modul 4:
- Listen von Tupeln als Datenstruktur (wartbar und erweiterbar)
- Tupel-Unpacking in einer for-Schleife
- sorted() mit einer key-Funktion (lambda)
- if __name__ == "__main__":-Guard für ausführbare Module

Die einfache if/elif-Variante des Notensystems finden Sie in
modul-3-kontrollstrukturen/05-beispiele/notensystem.py.
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
