"""
Code mit Bugs - Übung zum Fehlerfinden

Dieses Skript enthält Funktionen mit typischen Anfängerfehlern.
Kannst du alle Bugs finden?

Konzepte:
- Off-by-one Fehler
- Falsche Vergleichsoperatoren
- Fehlende return-Anweisungen
- Endlosschleifen
"""


# ============================================================
# BUG 1: Off-by-one Fehler in einer Schleife
# ============================================================


def summiere_bis(n):
    """
    Soll die Summe von 1 bis n (inklusive) berechnen.

    Beispiel: summiere_bis(5) soll 15 ergeben (1+2+3+4+5)

    Args:
        n: Obere Grenze (inklusive)

    Returns:
        int: Summe von 1 bis n
    """
    summe = 0
    # HIER IST EIN BUG - kannst du ihn finden?
    # range(1, n) geht nur bis n-1, nicht bis n!
    for i in range(1, n):  # BUG: sollte range(1, n + 1) sein
        summe += i
    return summe


# ============================================================
# BUG 2: Falscher Vergleichsoperator
# ============================================================


def ist_bestanden(punkte):
    """
    Prüft, ob eine Prüfung bestanden ist.
    Bestanden ab 60 Punkten (60 zählt als bestanden).

    Args:
        punkte: Erreichte Punktzahl

    Returns:
        bool: True wenn bestanden
    """
    # HIER IST EIN BUG - kannst du ihn finden?
    # < statt <= bedeutet: 60 Punkte gelten als nicht bestanden!
    if punkte < 60:  # BUG: sollte <= 59 oder < 60... nein, Logik ist falsch
        return False
    # Eigentlich ist die Logik hier korrekt, aber schauen wir nochmal:
    # Wir wollen: bestanden AB 60 Punkte
    # punkte < 60 → nicht bestanden → das ist korrekt
    # ABER: Wir verwenden > statt >= beim Check:
    if punkte > 60:  # BUG: sollte >= 60 sein (60 ist auch bestanden!)
        return True
    return False


# ============================================================
# BUG 3: Fehlende return-Anweisung
# ============================================================


def finde_maximum(zahlen):
    """
    Findet die grösste Zahl in einer Liste.

    Args:
        zahlen: Liste von Zahlen

    Returns:
        Die grösste Zahl oder None bei leerer Liste
    """
    if not zahlen:
        return None

    maximum = zahlen[0]
    for zahl in zahlen:
        if zahl > maximum:
            maximum = zahl

    # HIER IST EIN BUG - kannst du ihn finden?
    # Die Funktion berechnet das Maximum, gibt es aber nicht zurück!
    print(f"Das Maximum ist: {maximum}")
    # BUG: return maximum fehlt hier!


# ============================================================
# BUG 4: Endlosschleife (falsches Inkrement)
# ============================================================


def zaehle_runter(start):
    """
    Zählt von start bis 1 herunter und sammelt die Zahlen.

    Args:
        start: Startwert (positive Zahl)

    Returns:
        list: Liste der Zahlen von start bis 1
    """
    zahlen = []
    aktuell = start

    # HIER IST EIN BUG - kannst du ihn finden?
    # aktuell wird hochgezählt statt runtergezählt → Endlosschleife!
    while aktuell > 0:
        zahlen.append(aktuell)
        aktuell += 1  # BUG: sollte aktuell -= 1 sein

        # Sicherheitsabbruch für die Demo (sonst echte Endlosschleife!)
        if len(zahlen) > 100:
            print("ABBRUCH: Endlosschleife erkannt!")
            break

    return zahlen


# ============================================================
# Hauptprogramm - Bugs demonstrieren
# ============================================================


def main():
    """Führt alle fehlerhaften Funktionen aus und zeigt die Probleme."""

    print("=" * 50)
    print("Code mit Bugs - Findest du die Fehler?")
    print("=" * 50)

    # Bug 1: Off-by-one
    print("\n--- Bug 1: Off-by-one Fehler ---")
    ergebnis = summiere_bis(5)
    print(f"summiere_bis(5) = {ergebnis}")
    print("Erwartet: 15 (1+2+3+4+5)")
    print(f"Stimmt das? {'✅ Ja' if ergebnis == 15 else '❌ Nein!'}")

    # Bug 2: Falscher Operator
    print("\n--- Bug 2: Falscher Vergleichsoperator ---")
    ergebnis_60 = ist_bestanden(60)
    print(f"ist_bestanden(60) = {ergebnis_60}")
    print("Erwartet: True (60 ist bestanden)")
    print(f"Stimmt das? {'✅ Ja' if ergebnis_60 else '❌ Nein!'}")

    # Bug 3: Fehlendes return
    print("\n--- Bug 3: Fehlende return-Anweisung ---")
    zahlen = [3, 7, 2, 9, 4]
    ergebnis = finde_maximum(zahlen)
    print(f"finde_maximum({zahlen}) = {ergebnis}")
    print("Erwartet: 9")
    print(f"Stimmt das? {'✅ Ja' if ergebnis == 9 else '❌ Nein!'}")

    # Bug 4: Endlosschleife
    print("\n--- Bug 4: Endlosschleife ---")
    print("zaehle_runter(5) wird aufgerufen...")
    ergebnis = zaehle_runter(5)
    print(f"Ergebnis: {ergebnis[:10]}...")  # Nur erste 10 zeigen
    print("Erwartet: [5, 4, 3, 2, 1]")
    print(f"Länge: {len(ergebnis)} (erwartet: 5)")

    print("\n" + "=" * 50)
    print("Tipp: Nutze eine KI, um die Bugs zu finden!")
    print("Kopiere den Code und frage: 'Findest du die Bugs?'")
    print("=" * 50)


if __name__ == "__main__":
    main()
