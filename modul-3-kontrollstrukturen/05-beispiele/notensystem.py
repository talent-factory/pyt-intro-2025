"""
Notensystem - Punkte in Noten umwandeln
Musterlösung für Übung 1, Modul 3

Konvertiert Punkte (0-100) in Schweizer Noten (2-6):
- 90-100: Note 6
- 80-89:  Note 5
- 70-79:  Note 4
- 60-69:  Note 3
- 0-59:   Note 2
"""


def eingabe_zahl(prompt, minimum=0, maximum=100):
    """
    Fragt nach einer Zahl und validiert die Eingabe.

    Args:
        prompt: Text der Eingabeaufforderung
        minimum: Kleinster erlaubter Wert (Standard: 0)
        maximum: Grösster erlaubter Wert (Standard: 100)

    Returns:
        int: Validierte Zahl im erlaubten Bereich
    """
    while True:
        eingabe = input(prompt)

        # Prüfen ob gültige Zahl eingegeben wurde
        if not eingabe.isdigit():
            print("Fehler: Bitte geben Sie eine gültige Zahl ein!\n")
            continue

        zahl = int(eingabe)

        # Prüfen ob Zahl im gültigen Bereich liegt
        if zahl < minimum or zahl > maximum:
            print(f"Fehler: Wert muss zwischen {minimum} und {maximum} liegen!\n")
            continue

        return zahl


print("=== Erweitertes Notensystem ===\n")

# Eingabe mit Validierung
punkte = eingabe_zahl("Punkte (0-100): ")

# Notenberechnung
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

# Ausgabe
print(f"\nNote: {note}")
print(f"Bewertung: {feedback}")
