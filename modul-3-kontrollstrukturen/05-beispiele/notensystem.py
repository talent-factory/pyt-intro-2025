"""
Notensystem - Punkte in Noten umwandeln
Musterlösung für Übung 1, Modul 3

Konvertiert Punkte (0-100) in Schweizer Noten (2-6):
- 90-100: Note 6
- 80-89:  Note 5
- 70-79:  Note 4
- 60-69:  Note 3
- 0-59:   Note 2

Konzepte:
- if/elif/else für die Notenberechnung
- while-Schleife mit continue für die Eingabevalidierung
- String-Methoden (.isdigit()) für die Validierung

Siehe modul-4-funktionen-datenstrukturen/05-beispiele/notensystem_improved.py
für eine wartbarere Variante mit Datenstruktur (kommt in Modul 4).
"""

print("=" * 50)
print("           ERWEITERTES NOTENSYSTEM")
print("=" * 50)

# ============================================================
# Eingabe mit Validierung
# ============================================================
# Schleife wiederholt die Eingabeaufforderung so lange, bis eine
# gültige Zahl zwischen 0 und 100 eingegeben wurde.
while True:
    eingabe = input("\nPunkte (0-100): ").strip()

    # Prüfen, ob die Eingabe nur aus Ziffern besteht
    if not eingabe.isdigit():
        print("Fehler: Bitte geben Sie eine positive ganze Zahl ein!")
        continue

    punkte = int(eingabe)

    # Prüfen, ob die Zahl im gültigen Bereich liegt
    if punkte > 100:
        print("Fehler: Wert muss zwischen 0 und 100 liegen!")
        continue

    # Eingabe ist gültig - Schleife verlassen
    break

# ============================================================
# Notenberechnung
# ============================================================
if punkte >= 90:
    note = 6
    feedback = "Hervorragend! 🌟"
elif punkte >= 80:
    note = 5
    feedback = "Sehr gut! 👍"
elif punkte >= 70:
    note = 4
    feedback = "Gut!"
elif punkte >= 60:
    note = 3
    feedback = "Genügend"
else:
    note = 2
    feedback = "Ungenügend"

# ============================================================
# Ausgabe
# ============================================================
print()
print("=" * 50)
print(f"Punkte:    {punkte}")
print(f"Note:      {note}")
print(f"Bewertung: {feedback}")
print("=" * 50)
