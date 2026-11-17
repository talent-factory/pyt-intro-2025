"""
Pascal'sches Dreieck - ausgeglichen (zentriert)

Problem in pascal.py: Mehrstellige Zahlen (10, 15, 20, ...) sind breiter als
einstellige. Das Dreieck wird dadurch schief.

Lösung: Jeder Eintrag bekommt eine Zelle mit fester Breite. Die Breite richtet
sich nach der grössten Zahl im Dreieck. Jede Zahl wird in ihrer Zelle zentriert,
und jede Zeile wird um eine halbe Zelle weiter eingerückt als die nächste.
"""

groesse = int(input("Geben Sie die Grösse des Dreiecks ein: "))

# --- Schritt 1: Die grösste Zahl finden ---
# Die grösste Zahl steht in der letzten Zeile (Nummer groesse - 1).
# Wir berechnen sie mit der Binomialkoeffizient-Formel aus pascal.py.
letzte_zeile = groesse - 1
groesste_zahl = 1
for spalte in range(letzte_zeile + 1):
    # Wert der Spalte bestimmen (Binomialkoeffizient "letzte_zeile über spalte")
    wert = 1
    for schritt in range(spalte):
        wert = wert * (letzte_zeile - schritt) // (schritt + 1)
    if wert > groesste_zahl:
        groesste_zahl = wert

# --- Schritt 2: Zellenbreite festlegen ---
# Anzahl Stellen der grössten Zahl + 1 Leerzeichen Abstand
stellen = len(str(groesste_zahl))
breite = stellen + 1

# Die Breite muss gerade sein, damit eine halbe Zelle
# ein ganzes Zeichen ergibt (sonst wird die Einrückung ungenau)
if breite % 2 == 1:
    breite = breite + 1

# --- Schritt 3: Dreieck ausgeben ---
for zeile in range(groesse):
    # Pro Zeile weniger Einrückung: je eine halbe Zelle
    einrueckung = (groesse - zeile - 1) * breite // 2
    print(" " * einrueckung, end="")

    wert = 1
    for spalte in range(zeile + 1):
        # Zahl als Text in der Mitte einer Zelle mit fester Breite ausgeben
        print(str(wert).center(breite), end="")
        # Nächsten Wert der Zeile berechnen
        wert = wert * (zeile - spalte) // (spalte + 1)

    print()
