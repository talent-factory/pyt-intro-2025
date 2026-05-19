"""
Musterlösung zu Aufgabe 1: Textanalyse-Tool

Analysiert einen vom Benutzer eingegebenen Text und gibt
grundlegende Statistiken, Wort-Analyse und Formatierungen aus.

Enthält zusätzlich folgende Bonus-Aufgaben:
- Vokal-Analyse
- Erweiterte Satz-Erkennung mit `!` und `?`
"""

# Titel
print("=" * 40)
print("        Textanalyse-Tool")
print("=" * 40)

# Text einlesen
text = input("\nBitte geben Sie einen Text ein:\n> ")

# Falls kein Text eingegeben wurde, Programm beenden
if len(text.strip()) == 0:
    print("\nKein Text eingegeben. Programm wird beendet.")
else:
    # -------- Grundlegende Statistiken --------
    anzahl_zeichen_mit = len(text)
    anzahl_zeichen_ohne = len(text.replace(" ", ""))

    # Sätze: Punkte, Ausrufezeichen und Fragezeichen zählen
    anzahl_saetze = text.count(".") + text.count("!") + text.count("?")

    # Wörter aufteilen
    rohe_woerter = text.split()

    # Wörter von Satzzeichen am Rand bereinigen
    woerter = []
    for wort in rohe_woerter:
        wort_sauber = wort.strip(".,!?;:")
        if len(wort_sauber) > 0:
            woerter.append(wort_sauber)

    anzahl_woerter = len(woerter)

    # -------- Vokal-Analyse (Bonus) --------
    anzahl_vokale = 0
    for zeichen in text.lower():
        if zeichen in "aeiouäöü":
            anzahl_vokale += 1

    # -------- Wort-Analyse --------
    laengstes = ""
    kuerzestes = ""
    gesamt_laenge = 0

    if anzahl_woerter > 0:
        # Start-Werte: erstes Wort
        laengstes = woerter[0]
        kuerzestes = woerter[0]

        # Alle Wörter durchgehen
        for wort in woerter:
            gesamt_laenge += len(wort)
            if len(wort) > len(laengstes):
                laengstes = wort
            if len(wort) < len(kuerzestes):
                kuerzestes = wort

        durchschnitt = gesamt_laenge / anzahl_woerter
    else:
        durchschnitt = 0

    # -------- Ausgabe --------
    print()
    print("=" * 40)
    print("Analyse-Ergebnisse:")
    print("=" * 40)

    print("\nGrundlegende Statistiken:")
    print(f"- Zeichen (mit Leerzeichen): {anzahl_zeichen_mit}")
    print(f"- Zeichen (ohne Leerzeichen): {anzahl_zeichen_ohne}")
    print(f"- Wörter: {anzahl_woerter}")
    print(f"- Sätze: {anzahl_saetze}")
    print(f"- Vokale: {anzahl_vokale}")

    print("\nWort-Analyse:")
    if anzahl_woerter > 0:
        print(f"- Längstes Wort: {laengstes} ({len(laengstes)} Zeichen)")
        print(f"- Kürzestes Wort: {kuerzestes} ({len(kuerzestes)} Zeichen)")
        print(f"- Durchschnittliche Wortlänge: {durchschnitt:.1f} Zeichen")
    else:
        print("- Keine Wörter im Text gefunden.")

    print("\nFormatierungen:")
    print(f"- Grossbuchstaben: {text.upper()}")
    print(f"- Kleinbuchstaben: {text.lower()}")
    print(f"- Titel-Format: {text.title()}")
    print("=" * 40)
