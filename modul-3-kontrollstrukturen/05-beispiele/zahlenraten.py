"""
Zahlenrate-Spiel
Ein interaktives Spiel zum Raten von Zahlen.

Konzepte:
- while-Schleifen (auch verschachtelt)
- if/elif/else
- Eingabevalidierung mit .isdigit()
- Zufallszahlen mit random.randint
- break und continue
"""

import random

print("=" * 50)
print("      Zahlenrate-Spiel")
print("=" * 50)
print()

# Spieleinstellungen
min_zahl = 1
max_zahl = 100
max_versuche = 7

# Äussere Schleife für mehrere Spiele
weiterspielen = True

while weiterspielen:
    # Zufallszahl generieren
    geheimzahl = random.randint(min_zahl, max_zahl)

    print(f"Ich habe mir eine Zahl zwischen {min_zahl} und {max_zahl} ausgedacht.")
    print(f"Sie haben {max_versuche} Versuche.\n")

    versuche = 0
    gewonnen = False

    # Spielschleife
    while versuche < max_versuche:
        versuche += 1

        # Eingabe einlesen und validieren
        eingabe = input(f"Versuch {versuche}/{max_versuche}: ").strip()

        if not eingabe.isdigit():
            print("Bitte geben Sie eine positive ganze Zahl ein!\n")
            versuche -= 1  # Versuch nicht zählen
            continue

        geraten = int(eingabe)

        # Prüfen, ob die Zahl im erlaubten Bereich liegt
        if geraten < min_zahl or geraten > max_zahl:
            print(f"Zahl muss zwischen {min_zahl} und {max_zahl} liegen!\n")
            versuche -= 1  # Versuch nicht zählen
            continue

        # Vergleichen
        if geraten == geheimzahl:
            gewonnen = True
            break
        elif geraten < geheimzahl:
            differenz = geheimzahl - geraten
            if differenz <= 5:
                print("Zu niedrig, aber ganz nah dran! 🔥")
            elif differenz <= 10:
                print("Zu niedrig, schon warm! 🌡️")
            else:
                print("Zu niedrig! ❄️")
        else:
            differenz = geraten - geheimzahl
            if differenz <= 5:
                print("Zu hoch, aber ganz nah dran! 🔥")
            elif differenz <= 10:
                print("Zu hoch, schon warm! 🌡️")
            else:
                print("Zu hoch! ❄️")

        print()

    # Auswertung
    print("=" * 50)
    if gewonnen:
        print("🎉 Glückwunsch! Sie haben gewonnen!")
        print(f"Die Zahl war {geheimzahl}")
        print(f"Versuche: {versuche}")

        # Bewertung
        if versuche == 1:
            print("Bewertung: Unglaublich! 🌟")
        elif versuche <= 3:
            print("Bewertung: Sehr gut! 👍")
        elif versuche <= 5:
            print("Bewertung: Gut! ✓")
        else:
            print("Bewertung: Geschafft! 😊")
    else:
        print("😢 Leider verloren!")
        print(f"Die Zahl war {geheimzahl}")
        print(f"Versuche: {versuche}")

    print("=" * 50)

    # Nochmal spielen?
    nochmal = input("\nNochmal spielen? (j/n): ").lower()
    if nochmal in ["j", "ja", "y", "yes"]:
        print("\n" * 2)
        # Spiel wird durch äussere Schleife wiederholt
    else:
        print("\nDanke fürs Spielen! 👋")
        weiterspielen = False
