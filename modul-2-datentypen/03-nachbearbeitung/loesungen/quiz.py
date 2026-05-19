"""
Musterlösung zu Aufgabe 3: Interaktives Quiz

Ein interaktives Python-Quiz mit 5 Fragen verschiedener Typen:
- Zahlen-Frage
- Ja/Nein-Frage
- Multiple Choice
- Zählen von Buchstaben
- Multiple Choice (Berechnung)

Punkte werden gezählt und am Ende mit einer Bewertung ausgegeben.
"""

# Titel
print("=" * 40)
print("         Python-Quiz")
print("=" * 40)
print("\nWillkommen zum Python-Quiz!")
print("Beantworten Sie 5 Fragen und testen Sie Ihr Wissen.\n")
print("=" * 40)

# Punktestand
punkte = 0
gesamt_fragen = 5


# ============================================================
# Frage 1: Zahlen-Frage
# ============================================================
print("\nFrage 1 von 5:")
print("Was ist 5 + 3?")
antwort = input("Ihre Antwort: ").strip()

if antwort == "8":
    print("✓ Richtig! (+1 Punkt)")
    punkte = punkte + 1
else:
    print("✗ Falsch! Richtig wäre: 8")
print("-" * 40)


# ============================================================
# Frage 2: Ja/Nein-Frage
# ============================================================
print("\nFrage 2 von 5:")
print("Ist Python eine Programmiersprache? (ja/nein)")
antwort = input("Ihre Antwort: ").lower().strip()

if antwort == "ja" or antwort == "j" or antwort == "yes" or antwort == "y":
    print("✓ Richtig! (+1 Punkt)")
    punkte = punkte + 1
else:
    print("✗ Falsch! Richtig wäre: ja")
print("-" * 40)


# ============================================================
# Frage 3: Multiple Choice
# ============================================================
print("\nFrage 3 von 5:")
print("Welcher Datentyp ist \"Hallo\"?")
print("a) int")
print("b) float")
print("c) str")
print("d) bool")
antwort = input("Ihre Antwort: ").lower().strip()

if antwort == "c" or antwort == "str":
    print("✓ Richtig! (+1 Punkt)")
    punkte = punkte + 1
else:
    print("✗ Falsch! Richtig wäre: c (str)")
print("-" * 40)


# ============================================================
# Frage 4: Zahlen-Frage (Wortlänge zählen)
# ============================================================
print("\nFrage 4 von 5:")
print("Wie viele Buchstaben hat \"Python\"?")
antwort = input("Ihre Antwort: ").strip()

if antwort == "6":
    print("✓ Richtig! (+1 Punkt)")
    punkte = punkte + 1
else:
    print("✗ Falsch! Richtig wäre: 6")
print("-" * 40)


# ============================================================
# Frage 5: Zahlen-Frage (Berechnung)
# ============================================================
print("\nFrage 5 von 5:")
print("Was gibt 10 / 2 zurück?")
antwort = input("Ihre Antwort: ").strip()

# Sowohl 5 als auch 5.0 akzeptieren
if antwort == "5" or antwort == "5.0":
    print("✓ Richtig! (+1 Punkt)")
    punkte = punkte + 1
else:
    print("✗ Falsch! Richtig wäre: 5.0")
print("-" * 40)


# ============================================================
# Auswertung
# ============================================================
print("\n" + "=" * 40)
print("         Quiz beendet!")
print("=" * 40)

prozent = (punkte / gesamt_fragen) * 100
print(f"\nErgebnis: {punkte} von {gesamt_fragen} Punkten ({prozent:.0f}%)\n")

if prozent == 100:
    print("Bewertung: Perfekt! 🏆")
elif prozent >= 80:
    print("Bewertung: Sehr gut! 👍")
elif prozent >= 60:
    print("Bewertung: Gut! ✓")
elif prozent >= 40:
    print("Bewertung: Geht so. 🤔")
else:
    print("Bewertung: Weiter üben! 📚")

print("\nDanke fürs Mitspielen!")
print("=" * 40)
