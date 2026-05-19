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
- if-elif-else für Notenberechnung
- while-Schleife mit continue für Eingabevalidierung
- String-Methoden (isdigit) für Validierung
"""

print("=== Erweitertes Notensystem ===\n")

# Eingabe mit Validierung: solange wiederholen, bis eine gültige Zahl
# zwischen 0 und 100 eingegeben wurde.
while True:
    eingabe = input("Punkte (0-100): ")

    # Prüfen, ob die Eingabe nur aus Ziffern besteht
    if not eingabe.isdigit():
        print("Fehler: Bitte geben Sie eine gültige Zahl ein!\n")
        continue

    punkte = int(eingabe)

    # Prüfen, ob die Zahl im gültigen Bereich liegt
    if punkte < 0 or punkte > 100:
        print("Fehler: Wert muss zwischen 0 und 100 liegen!\n")
        continue

    # Eingabe ist gültig - Schleife verlassen
    break

# Notenberechnung mit if-elif-else
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
