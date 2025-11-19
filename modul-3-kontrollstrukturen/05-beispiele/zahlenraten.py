"""
Zahlenrate-Spiel
Ein interaktives Spiel zum Raten von Zahlen.

Konzepte:
- While-Schleifen
- If-elif-else
- Input/Output
- Zufallszahlen
- Break
"""

import random


def main() -> None:
    """Hauptprogramm für das Zahlenrate-Spiel."""
    print("=" * 40)
    print("      Zahlenrate-Spiel")
    print("=" * 40)
    print()
    
    # Spieleinstellungen
    min_zahl = 1
    max_zahl = 100
    max_versuche = 7
    
    # Zufallszahl generieren
    geheimzahl = random.randint(min_zahl, max_zahl)
    
    print(f"Ich habe mir eine Zahl zwischen {min_zahl} und {max_zahl} ausgedacht.")
    print(f"Sie haben {max_versuche} Versuche.\n")
    
    versuche = 0
    gewonnen = False
    
    # Spielschleife
    while versuche < max_versuche:
        versuche += 1
        
        # Eingabe
        try:
            eingabe = input(f"Versuch {versuche}/{max_versuche}: ")
            geraten = int(eingabe)
        except ValueError:
            print("Bitte geben Sie eine gültige Zahl ein!\n")
            versuche -= 1  # Versuch nicht zählen
            continue
        
        # Prüfen
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
    print("=" * 40)
    if gewonnen:
        print(f"🎉 Glückwunsch! Sie haben gewonnen!")
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
        print(f"😢 Leider verloren!")
        print(f"Die Zahl war {geheimzahl}")
        print(f"Versuche: {versuche}")
    
    print("=" * 40)
    
    # Nochmal spielen?
    nochmal = input("\nNochmal spielen? (j/n): ").lower()
    if nochmal in ["j", "ja", "y", "yes"]:
        print("\n" * 2)
        main()  # Rekursiv nochmal starten
    else:
        print("\nDanke fürs Spielen! 👋")


if __name__ == "__main__":
    main()

