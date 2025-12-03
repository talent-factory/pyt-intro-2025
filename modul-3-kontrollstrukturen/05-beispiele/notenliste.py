"""
Notenliste - Notenstatistik berechnen
Musterlösung für Übung 6, Modul 3

Berechnet Statistiken für eine Liste von Noten:
- Durchschnitt
- Beste und schlechteste Note
- Anzahl bestanden / nicht bestanden
"""

print("=== Notenstatistik ===\n")

# Liste mit Noten
noten = [5.5, 4.2, 3.8, 6.0, 4.5, 5.0, 3.5]

# Variablen für Berechnungen initialisieren
summe = 0
beste_note = noten[0]
schlechteste_note = noten[0]
bestanden = 0
nicht_bestanden = 0

# Durch alle Noten iterieren
for note in noten:
    # Summe für Durchschnitt
    summe += note
    
    # Beste Note prüfen
    if note > beste_note:
        beste_note = note
    
    # Schlechteste Note prüfen
    if note < schlechteste_note:
        schlechteste_note = note
    
    # Bestanden/Nicht bestanden zählen
    if note >= 4.0:
        bestanden += 1
    else:
        nicht_bestanden += 1

# Durchschnitt berechnen
durchschnitt = summe / len(noten)

# Ausgabe
print(f"Noten: {noten}")
print()
print(f"Durchschnitt: {durchschnitt:.2f}")
print(f"Beste Note: {beste_note}")
print(f"Schlechteste Note: {schlechteste_note}")
print(f"Bestanden: {bestanden}")
print(f"Nicht bestanden: {nicht_bestanden}")

