"""
Notensystem - Punkte in Noten umwandeln (verbesserte Version)
Musterlösung für Übung 1, Modul 3

Konvertiert Punkte (0-100) in Schweizer Noten (2-6).

Verbesserungen gegenüber der Basisversion:
- Notenskala als Datenstruktur (wartbar und erweiterbar)
- Eingabevalidierung ohne Funktionen
- Notenberechnung über Schleife statt if/elif-Kette
"""

# Notenskala: Liste von Tupeln (Mindestpunktzahl, Note, Bewertung)
# Neue Notenstufen können einfach als Zeile hinzugefügt werden
notenskala = [
    (90, 6, "Hervorragend!"),
    (80, 5, "Sehr gut!"),
    (70, 4, "Gut!"),
    (60, 3, "Genügend"),
    (0,  2, "Ungenügend"),
]

# Titel
print("=" * 40)
print("Erweitertes Notensystem")
print("=" * 40)

# Eingabe mit Validierung
while True:
    eingabe = input("\nPunkte (0-100): ")

    if not eingabe.isdigit():
        print("Fehler: Bitte eine gültige Zahl eingeben!")
        continue

    punkte = int(eingabe)

    if punkte < 0 or punkte > 100:
        print("Fehler: Wert muss zwischen 0 und 100 liegen!")
        continue

    break

# Notenberechnung über die Notenskala
for mindestpunktzahl, note, bewertung in notenskala:
    if punkte >= mindestpunktzahl:
        break

# Ausgabe
print()
print("=" * 40)
print(f"Punkte:    {punkte}")
print(f"Note:      {note}")
print(f"Bewertung: {bewertung}")
print("=" * 40)
