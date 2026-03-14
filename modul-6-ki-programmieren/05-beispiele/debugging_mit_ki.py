"""
Debugging mit KI-Unterstützung

Dieses Skript zeigt den Prozess, wie man KI
zum Finden und Beheben von Bugs einsetzt.

Konzepte:
- Fehlerbeschreibung formulieren
- KI-Prompts für Debugging
- Bugfix-Dokumentation
- Vorher-Nachher-Vergleich
"""


# ============================================================
# BUG 1: Falsches Ergebnis bei der Durchschnittsberechnung
# ============================================================

# BUG 1: Die Funktion gibt bei [10, 20, 30] den Wert 30 zurück
#         statt 20. Der Durchschnitt ist falsch.
#
# KI-PROMPT: "Meine Funktion berechne_schnitt() gibt bei
#   [10, 20, 30] den Wert 30 statt 20 zurück. Hier ist
#   der Code: [Code eingefügt]. Findest du den Fehler?"
#
# KI-ANTWORT: "Der Bug ist in der Schleife: Du verwendest
#   summe = zahl statt summe += zahl. Dadurch wird die Summe
#   immer mit der letzten Zahl überschrieben, nicht addiert."
#
# FIX: summe = zahl → summe += zahl


def berechne_schnitt_buggy(zahlen):
    """BUGGY VERSION: Falsches Ergebnis."""
    summe = 0
    for zahl in zahlen:
        summe = zahl  # BUG: Überschreibt statt addiert!
    return summe / len(zahlen)


def berechne_schnitt_fix(zahlen):
    """
    FIXED VERSION: Korrekte Durchschnittsberechnung.

    Args:
        zahlen: Liste von Zahlen

    Returns:
        float: Durchschnittswert
    """
    if not zahlen:
        return 0.0

    summe = 0
    for zahl in zahlen:
        summe += zahl  # FIX: += statt =
    return summe / len(zahlen)


# ============================================================
# BUG 2: Funktion gibt immer "Ungenügend" zurück
# ============================================================

# BUG 2: egal welche Note man eingibt, die Funktion gibt
#         immer "Ungenügend" zurück.
#
# KI-PROMPT: "Meine bewerte_note()-Funktion gibt immer
#   'Ungenügend' zurück, egal ob ich 6.0 oder 1.0 eingebe.
#   Was stimmt nicht?"
#
# KI-ANTWORT: "Du hast die Reihenfolge der if-elif-Bedingungen
#   falsch herum. Du prüfst zuerst 'note < 4.0' - das trifft
#   auf die meisten Noten nicht zu, aber durch die elif-Kette
#   wird die Variable 'bewertung' nie gesetzt, wenn die erste
#   Bedingung nicht zutrifft. Eigentlich ist das Problem: du
#   prüfst aufsteigend statt absteigend, dadurch matcht >= 1.0
#   immer zuerst."
#
# FIX: Reihenfolge der Bedingungen umkehren (höchste zuerst prüfen)


def bewerte_note_buggy(note):
    """BUGGY VERSION: Gibt immer 'Ungenügend' zurück."""
    # BUG: Reihenfolge falsch! >= 1.0 trifft IMMER zu!
    if note >= 1.0:
        bewertung = "Ungenügend"
    elif note >= 4.0:
        bewertung = "Genügend"
    elif note >= 5.0:
        bewertung = "Gut"
    elif note >= 5.5:
        bewertung = "Sehr gut"
    else:
        bewertung = "Ungültig"
    return bewertung


def bewerte_note_fix(note):
    """
    FIXED VERSION: Korrekte Notenbewertung.

    Die Bedingungen werden von der höchsten zur niedrigsten
    Note geprüft, damit die spezifischste Bedingung zuerst greift.

    Args:
        note: Schulnote (1.0-6.0)

    Returns:
        str: Bewertungstext
    """
    # FIX: Höchste Note zuerst prüfen!
    if note >= 5.5:
        bewertung = "Sehr gut"
    elif note >= 5.0:
        bewertung = "Gut"
    elif note >= 4.0:
        bewertung = "Genügend"
    elif note >= 1.0:
        bewertung = "Ungenügend"
    else:
        bewertung = "Ungültig"
    return bewertung


# ============================================================
# BUG 3: IndexError bei leerer Liste
# ============================================================

# BUG 3: Das Programm stürzt mit "IndexError: list index
#         out of range" ab, wenn eine leere Liste übergeben wird.
#
# KI-PROMPT: "Meine Funktion finde_zweitgroesste() stürzt ab
#   mit IndexError wenn die Liste leer ist oder nur ein
#   Element hat. Wie kann ich das beheben?"
#
# KI-ANTWORT: "Du greifst auf sortierte[−2] zu, ohne vorher
#   zu prüfen, ob die Liste mindestens 2 Elemente hat.
#   Füge eine Eingabevalidierung am Anfang hinzu."
#
# FIX: Prüfung auf Mindestlänge der Liste hinzugefügt


def finde_zweitgroesste_buggy(zahlen):
    """BUGGY VERSION: Stürzt bei zu kurzer Liste ab."""
    # BUG: Keine Prüfung ob genug Elemente vorhanden!
    sortierte = sorted(zahlen)
    return sortierte[-2]  # IndexError wenn weniger als 2 Elemente!


def finde_zweitgroesste_fix(zahlen):
    """
    FIXED VERSION: Findet die zweitgrösste Zahl sicher.

    Args:
        zahlen: Liste von Zahlen

    Returns:
        Die zweitgrösste Zahl oder None bei zu wenig Elementen
    """
    # FIX: Eingabevalidierung hinzugefügt
    if len(zahlen) < 2:
        print("Fehler: Mindestens 2 Zahlen nötig!")
        return None

    # Duplikate entfernen für echte "zweitgrösste"
    eindeutige = list(set(zahlen))

    if len(eindeutige) < 2:
        print("Fehler: Mindestens 2 verschiedene Zahlen nötig!")
        return None

    sortierte = sorted(eindeutige)
    return sortierte[-2]


# ============================================================
# Debugging-Tipps
# ============================================================


def zeige_debugging_tipps():
    """Zeigt hilfreiche Tipps für das Debugging mit KI."""
    tipps = [
        "Beschreibe das ERWARTETE und das TATSÄCHLICHE Verhalten",
        "Füge den relevanten Code-Ausschnitt ein",
        "Nenne die genaue Fehlermeldung (falls vorhanden)",
        "Gib ein konkretes Beispiel mit Eingabe und Ausgabe",
        "Frage: 'Findest du den Bug?' statt 'Ist das richtig?'",
    ]

    print("=" * 50)
    print("Tipps für Debugging-Prompts")
    print("=" * 50)
    for i, tipp in enumerate(tipps, 1):
        print(f"  {i}. {tipp}")
    print("=" * 50)


# ============================================================
# Hauptprogramm
# ============================================================

if __name__ == "__main__":
    print("=" * 55)
    print("Debugging mit KI-Unterstützung")
    print("=" * 55)

    # Bug 1: Durchschnittsberechnung
    print("\n--- Bug 1: Falscher Durchschnitt ---")
    test_zahlen = [10, 20, 30]
    print(f"Eingabe: {test_zahlen}")
    print(f"Buggy:   {berechne_schnitt_buggy(test_zahlen)} (erwartet: 20.0)")
    print(f"Fixed:   {berechne_schnitt_fix(test_zahlen)} (erwartet: 20.0)")
    print("Fix: 'summe = zahl' → 'summe += zahl'")

    # Bug 2: Notenbewertung
    print("\n--- Bug 2: Falsche Bewertung ---")
    test_noten = [6.0, 5.5, 5.0, 4.0, 3.0]
    print(f"{'Note':<6} {'Buggy':<15} {'Fixed':<15}")
    print("-" * 36)
    for note in test_noten:
        buggy = bewerte_note_buggy(note)
        fixed = bewerte_note_fix(note)
        print(f"{note:<6} {buggy:<15} {fixed:<15}")
    print("Fix: Reihenfolge der if-Bedingungen umkehren")

    # Bug 3: IndexError
    print("\n--- Bug 3: IndexError ---")
    print("Test mit [5, 3, 8, 1, 9]:")
    ergebnis = finde_zweitgroesste_fix([5, 3, 8, 1, 9])
    print(f"  Zweitgrösste: {ergebnis} (erwartet: 8)")

    print("\nTest mit leerer Liste []:")
    ergebnis = finde_zweitgroesste_fix([])
    print(f"  Ergebnis: {ergebnis} (erwartet: None)")

    print("\nTest mit [5, 5, 5]:")
    ergebnis = finde_zweitgroesste_fix([5, 5, 5])
    print(f"  Ergebnis: {ergebnis} (erwartet: None)")

    # Debugging-Tipps
    print()
    zeige_debugging_tipps()

    print("\n" + "=" * 55)
    print("Fazit: Gute Fehlerbeschreibungen helfen der KI,")
    print("den Bug schneller zu finden!")
    print("=" * 55)
