"""
Refactoring-Beispiel: Von einer grossen Funktion zu kleinen

Dieses Skript zeigt, wie KI beim Refactoring hilft:
Eine grosse, unübersichtliche Funktion wird in kleine,
verständliche Funktionen aufgeteilt.

Konzepte:
- Single Responsibility Principle
- Funktionen extrahieren
- Code-Lesbarkeit verbessern
- KI als Refactoring-Assistent
"""


# ============================================================
# VORHER: Eine grosse Funktion die alles macht
# ============================================================
# KI-PROMPT: "Ich habe diese grosse Funktion. Kannst du sie in
#   kleinere, übersichtlichere Funktionen aufteilen?"

# HINWEIS: Diese Funktion funktioniert, ist aber schwer zu
# verstehen, zu testen und zu erweitern.


def verarbeite_noten_vorher(noten_liste):
    """
    VORHER: Eine Funktion die ALLES macht.
    - Validierung
    - Berechnung
    - Statistik
    - Ausgabe
    """
    # Validierung
    if not noten_liste:
        print("Fehler: Keine Noten vorhanden!")
        return
    for note in noten_liste:
        if note < 1.0 or note > 6.0:
            print(f"Fehler: Note {note} ist ungültig (1.0-6.0)!")
            return

    # Durchschnitt berechnen
    summe = 0
    for note in noten_liste:
        summe = summe + note
    durchschnitt = summe / len(noten_liste)

    # Beste und schlechteste Note finden
    beste = noten_liste[0]
    schlechteste = noten_liste[0]
    for note in noten_liste:
        if note > beste:
            beste = note
        if note < schlechteste:
            schlechteste = note

    # Bestanden/Nicht bestanden zählen
    bestanden = 0
    nicht_bestanden = 0
    for note in noten_liste:
        if note >= 4.0:
            bestanden = bestanden + 1
        else:
            nicht_bestanden = nicht_bestanden + 1

    # Notenverteilung
    verteilung = {"Sehr gut": 0, "Gut": 0, "Genügend": 0, "Ungenügend": 0}
    for note in noten_liste:
        if note >= 5.5:
            verteilung["Sehr gut"] = verteilung["Sehr gut"] + 1
        elif note >= 4.5:
            verteilung["Gut"] = verteilung["Gut"] + 1
        elif note >= 4.0:
            verteilung["Genügend"] = verteilung["Genügend"] + 1
        else:
            verteilung["Ungenügend"] = verteilung["Ungenügend"] + 1

    # Alles ausgeben
    print("=" * 40)
    print("Notenauswertung")
    print("=" * 40)
    print(f"Anzahl Noten: {len(noten_liste)}")
    print(f"Durchschnitt: {durchschnitt:.2f}")
    print(f"Beste Note: {beste}")
    print(f"Schlechteste Note: {schlechteste}")
    print(f"Bestanden: {bestanden}")
    print(f"Nicht bestanden: {nicht_bestanden}")
    print(f"Bestehensquote: {bestanden / len(noten_liste) * 100:.1f}%")
    print("-" * 40)
    print("Verteilung:")
    for kategorie, anzahl in verteilung.items():
        balken = "█" * anzahl
        print(f"  {kategorie:12s}: {balken} ({anzahl})")
    print("=" * 40)


# ============================================================
# NACHHER: Aufgeteilt in kleine, klare Funktionen
# ============================================================
# KI hat die grosse Funktion in diese Teile zerlegt:
#
# REFACTORING-ENTSCHEIDUNGEN:
# 1. Validierung → eigene Funktion (wiederverwendbar)
# 2. Berechnung → eigene Funktion (testbar)
# 3. Statistik → eigene Funktion (erweiterbar)
# 4. Ausgabe → eigene Funktion (austauschbar)


def validiere_noten(noten_liste):
    """
    Prüft, ob alle Noten gültig sind.

    REFACTORING-GRUND: Validierung ist eine eigenständige Aufgabe.
    Kann auch von anderen Funktionen genutzt werden.

    Args:
        noten_liste: Liste von Noten

    Returns:
        tuple: (ist_gueltig: bool, fehlermeldung: str)
    """
    if not noten_liste:
        return (False, "Keine Noten vorhanden")

    for note in noten_liste:
        if note < 1.0 or note > 6.0:
            return (False, f"Note {note} ist ungültig (1.0-6.0)")

    return (True, "Alle Noten gültig")


def berechne_statistik(noten_liste):
    """
    Berechnet statistische Kennzahlen für die Noten.

    REFACTORING-GRUND: Berechnung von Ausgabe getrennt.
    Ergebnis kann weiterverwendet werden.

    Args:
        noten_liste: Liste von gültigen Noten

    Returns:
        dict: Statistische Kennzahlen
    """
    summe = 0.0
    for note in noten_liste:
        summe += note

    return {
        "anzahl": len(noten_liste),
        "durchschnitt": round(summe / len(noten_liste), 2),
        "beste_note": max(noten_liste),
        "schlechteste_note": min(noten_liste),
    }


def zaehle_bestanden(noten_liste, grenze=4.0):
    """
    Zählt bestandene und nicht bestandene Noten.

    REFACTORING-GRUND: Die Bestehensgrenze ist jetzt
    ein Parameter und kann angepasst werden.

    Args:
        noten_liste: Liste von Noten
        grenze: Bestehensgrenze (Standard: 4.0)

    Returns:
        dict: Anzahl bestanden und nicht bestanden
    """
    bestanden = 0
    nicht_bestanden = 0

    for note in noten_liste:
        if note >= grenze:
            bestanden += 1
        else:
            nicht_bestanden += 1

    quote = bestanden / len(noten_liste) * 100 if noten_liste else 0

    return {
        "bestanden": bestanden,
        "nicht_bestanden": nicht_bestanden,
        "quote": round(quote, 1),
    }


def erstelle_notenverteilung(noten_liste):
    """
    Erstellt die Notenverteilung nach Kategorien.

    REFACTORING-GRUND: Verteilung ist unabhängig von
    anderen Berechnungen und kann einzeln getestet werden.

    Args:
        noten_liste: Liste von Noten

    Returns:
        dict: Kategorie → Anzahl
    """
    verteilung = {
        "Sehr gut (5.5-6.0)": 0,
        "Gut (4.5-5.4)": 0,
        "Genügend (4.0-4.4)": 0,
        "Ungenügend (<4.0)": 0,
    }

    for note in noten_liste:
        if note >= 5.5:
            verteilung["Sehr gut (5.5-6.0)"] += 1
        elif note >= 4.5:
            verteilung["Gut (4.5-5.4)"] += 1
        elif note >= 4.0:
            verteilung["Genügend (4.0-4.4)"] += 1
        else:
            verteilung["Ungenügend (<4.0)"] += 1

    return verteilung


def zeige_auswertung(statistik, bestanden_info, verteilung):
    """
    Gibt die Notenauswertung formatiert aus.

    REFACTORING-GRUND: Ausgabe von Logik getrennt.
    Könnte leicht durch eine andere Ausgabe ersetzt werden
    (z.B. HTML, CSV, etc.).

    Args:
        statistik: Dict mit statistischen Kennzahlen
        bestanden_info: Dict mit Bestanden-Infos
        verteilung: Dict mit Notenverteilung
    """
    print("=" * 40)
    print("Notenauswertung (refactored)")
    print("=" * 40)

    # Statistik anzeigen
    print(f"Anzahl Noten:     {statistik['anzahl']}")
    print(f"Durchschnitt:     {statistik['durchschnitt']:.2f}")
    print(f"Beste Note:       {statistik['beste_note']}")
    print(f"Schlechteste:     {statistik['schlechteste_note']}")

    # Bestanden-Info
    print("-" * 40)
    print(f"Bestanden:        {bestanden_info['bestanden']}")
    print(f"Nicht bestanden:  {bestanden_info['nicht_bestanden']}")
    print(f"Bestehensquote:   {bestanden_info['quote']}%")

    # Verteilung als Balkendiagramm
    print("-" * 40)
    print("Verteilung:")
    for kategorie, anzahl in verteilung.items():
        balken = "█" * anzahl
        print(f"  {kategorie:22s}: {balken} ({anzahl})")

    print("=" * 40)


def verarbeite_noten_nachher(noten_liste):
    """
    NACHHER: Hauptfunktion ruft kleine Funktionen auf.

    Viel kürzer und übersichtlicher! Jeder Schritt ist
    klar benannt und verständlich.

    Args:
        noten_liste: Liste von Noten (1.0-6.0)
    """
    # Schritt 1: Validierung
    ist_gueltig, meldung = validiere_noten(noten_liste)
    if not ist_gueltig:
        print(f"Fehler: {meldung}")
        return

    # Schritt 2: Berechnungen
    statistik = berechne_statistik(noten_liste)
    bestanden_info = zaehle_bestanden(noten_liste)
    verteilung = erstelle_notenverteilung(noten_liste)

    # Schritt 3: Ausgabe
    zeige_auswertung(statistik, bestanden_info, verteilung)


# ============================================================
# Hauptprogramm
# ============================================================

if __name__ == "__main__":
    print("=" * 50)
    print("Refactoring-Beispiel: Vorher vs. Nachher")
    print("=" * 50)

    # Test-Noten
    noten = [5.5, 4.0, 3.5, 6.0, 4.5, 5.0, 3.0, 4.5, 5.5, 4.0]

    # VORHER: Eine grosse Funktion
    print("\n--- VORHER: Eine grosse Funktion ---")
    verarbeite_noten_vorher(noten)

    # NACHHER: Kleine, klare Funktionen
    print("\n--- NACHHER: Kleine, klare Funktionen ---")
    verarbeite_noten_nachher(noten)

    # Bonus: Einzelne Funktionen sind jetzt auch einzeln nutzbar!
    print("\n--- Bonus: Funktionen einzeln nutzen ---")
    statistik = berechne_statistik(noten)
    print(f"Nur der Durchschnitt: {statistik['durchschnitt']}")

    bestanden = zaehle_bestanden(noten)
    print(f"Nur die Quote: {bestanden['quote']}%")

    print("\n" + "=" * 50)
    print("Fazit: Kleine Funktionen sind")
    print("- leichter zu verstehen")
    print("- einfacher zu testen")
    print("- besser wiederverwendbar")
    print("=" * 50)
