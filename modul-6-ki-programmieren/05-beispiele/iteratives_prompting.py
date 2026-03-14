"""
Iteratives Prompting: Schritt für Schritt zur Lösung

Dieses Skript dokumentiert einen iterativen Dialog mit
einer KI über 3 Runden, um ein Programm zu entwickeln.

Konzepte:
- Schrittweise Verfeinerung
- Aufbauende Prompts
- Funktionserweiterung
- Dialog mit der KI
"""


# ============================================================
# RUNDE 1: Einfacher Start
# ============================================================
# PROMPT: "Erstelle eine einfache Einkaufsliste in Python.
#   Ich möchte Artikel hinzufügen und anzeigen können."
#
# KI-ANTWORT: "Hier ist eine einfache Version mit einer
#   Liste und zwei Funktionen."


def artikel_hinzufuegen_v1(einkaufsliste, artikel):
    """
    Version 1: Einfach einen Artikel zur Liste hinzufügen.

    Args:
        einkaufsliste: Liste von Artikeln
        artikel: Name des neuen Artikels
    """
    einkaufsliste.append(artikel)
    print(f"'{artikel}' hinzugefügt.")


def liste_anzeigen_v1(einkaufsliste):
    """
    Version 1: Liste einfach anzeigen.

    Args:
        einkaufsliste: Liste von Artikeln
    """
    if not einkaufsliste:
        print("Die Liste ist leer.")
        return

    print("Einkaufsliste:")
    for i, artikel in enumerate(einkaufsliste, 1):
        print(f"  {i}. {artikel}")


def demo_version_1():
    """Demonstriert Version 1 der Einkaufsliste."""
    print("=" * 45)
    print("RUNDE 1: Einfache Einkaufsliste")
    print("=" * 45)

    liste = []
    artikel_hinzufuegen_v1(liste, "Milch")
    artikel_hinzufuegen_v1(liste, "Brot")
    artikel_hinzufuegen_v1(liste, "Eier")
    print()
    liste_anzeigen_v1(liste)


# ============================================================
# RUNDE 2: Preise hinzufügen
# ============================================================
# PROMPT: "Gut! Jetzt möchte ich zu jedem Artikel auch
#   einen Preis speichern können. Und am Ende soll die
#   Gesamtsumme angezeigt werden."
#
# KI-ANTWORT: "Ich verwende jetzt Dictionaries statt
#   einfache Strings, damit wir Preise speichern können."


def artikel_hinzufuegen_v2(einkaufsliste, artikel, preis):
    """
    Version 2: Artikel mit Preis hinzufügen.

    Args:
        einkaufsliste: Liste von Artikel-Dicts
        artikel: Name des Artikels
        preis: Preis in CHF
    """
    einkaufsliste.append({"name": artikel, "preis": preis})
    print(f"'{artikel}' ({preis:.2f} CHF) hinzugefügt.")


def liste_anzeigen_v2(einkaufsliste):
    """
    Version 2: Liste mit Preisen und Gesamtsumme anzeigen.

    Args:
        einkaufsliste: Liste von Artikel-Dicts
    """
    if not einkaufsliste:
        print("Die Liste ist leer.")
        return

    print("Einkaufsliste:")
    print("-" * 35)
    gesamtsumme = 0.0

    for i, artikel in enumerate(einkaufsliste, 1):
        name = artikel["name"]
        preis = artikel["preis"]
        gesamtsumme += preis
        print(f"  {i}. {name:<20s} {preis:>6.2f} CHF")

    print("-" * 35)
    print(f"  {'Gesamt:':<23s} {gesamtsumme:>6.2f} CHF")


def demo_version_2():
    """Demonstriert Version 2 mit Preisen."""
    print("\n" + "=" * 45)
    print("RUNDE 2: Mit Preisen und Gesamtsumme")
    print("=" * 45)

    liste = []
    artikel_hinzufuegen_v2(liste, "Milch", 1.80)
    artikel_hinzufuegen_v2(liste, "Brot", 3.50)
    artikel_hinzufuegen_v2(liste, "Eier (6er)", 4.20)
    artikel_hinzufuegen_v2(liste, "Käse", 5.90)
    print()
    liste_anzeigen_v2(liste)


# ============================================================
# RUNDE 3: Sortierung und Zusammenfassung
# ============================================================
# PROMPT: "Super! Letzte Erweiterung: Ich möchte die Liste
#   nach Preis sortieren können (teuerste zuerst) und eine
#   Zusammenfassung sehen mit Durchschnittspreis, teuerstem
#   und günstigstem Artikel."
#
# KI-ANTWORT: "Ich füge eine Sortierfunktion und eine
#   Zusammenfassungs-Funktion hinzu."


def artikel_hinzufuegen_v3(einkaufsliste, artikel, preis, kategorie="Sonstiges"):
    """
    Version 3: Artikel mit Preis und Kategorie hinzufügen.

    Args:
        einkaufsliste: Liste von Artikel-Dicts
        artikel: Name des Artikels
        preis: Preis in CHF
        kategorie: Kategorie des Artikels
    """
    einkaufsliste.append(
        {
            "name": artikel,
            "preis": preis,
            "kategorie": kategorie,
        }
    )


def sortiere_nach_preis(einkaufsliste, absteigend=True):
    """
    Sortiert die Einkaufsliste nach Preis.

    Args:
        einkaufsliste: Liste von Artikel-Dicts
        absteigend: True = teuerste zuerst (Standard)

    Returns:
        list: Sortierte Kopie der Liste
    """
    sortierte_liste = sorted(
        einkaufsliste,
        key=lambda artikel: artikel["preis"],
        reverse=absteigend,
    )
    return sortierte_liste


def zeige_zusammenfassung(einkaufsliste):
    """
    Zeigt eine detaillierte Zusammenfassung der Einkaufsliste.

    Args:
        einkaufsliste: Liste von Artikel-Dicts
    """
    if not einkaufsliste:
        print("Keine Artikel vorhanden.")
        return

    # Preise sammeln
    preise = [artikel["preis"] for artikel in einkaufsliste]
    gesamtsumme = sum(preise)
    durchschnitt = gesamtsumme / len(preise)

    # Teuersten und günstigsten Artikel finden
    teuerster = max(einkaufsliste, key=lambda a: a["preis"])
    guenstigster = min(einkaufsliste, key=lambda a: a["preis"])

    # Ausgabe
    print("=" * 45)
    print("Zusammenfassung")
    print("=" * 45)
    print(f"Anzahl Artikel:    {len(einkaufsliste)}")
    print(f"Gesamtsumme:       {gesamtsumme:.2f} CHF")
    print(f"Durchschnitt:      {durchschnitt:.2f} CHF")
    print(f"Teuerster Artikel: {teuerster['name']} ({teuerster['preis']:.2f} CHF)")
    print(
        f"Günstigster:       {guenstigster['name']} ({guenstigster['preis']:.2f} CHF)"
    )
    print("=" * 45)


def liste_anzeigen_v3(einkaufsliste, sortiert=False):
    """
    Version 3: Sortierte Liste mit Kategorien anzeigen.

    Args:
        einkaufsliste: Liste von Artikel-Dicts
        sortiert: Nach Preis sortieren (Standard: False)
    """
    if not einkaufsliste:
        print("Die Liste ist leer.")
        return

    # Optional sortieren
    anzeige_liste = einkaufsliste
    if sortiert:
        anzeige_liste = sortiere_nach_preis(einkaufsliste)

    titel = "Einkaufsliste (sortiert nach Preis)" if sortiert else "Einkaufsliste"
    print(titel)
    print("-" * 45)

    gesamtsumme = 0.0
    for i, artikel in enumerate(anzeige_liste, 1):
        name = artikel["name"]
        preis = artikel["preis"]
        kategorie = artikel["kategorie"]
        gesamtsumme += preis
        print(f"  {i}. {name:<18s} {preis:>6.2f} CHF  [{kategorie}]")

    print("-" * 45)
    print(f"  {'Gesamt:':<21s} {gesamtsumme:>6.2f} CHF")


def demo_version_3():
    """Demonstriert die finale Version 3."""
    print("\n" + "=" * 45)
    print("RUNDE 3: Sortierung und Zusammenfassung")
    print("=" * 45)

    liste = []
    artikel_hinzufuegen_v3(liste, "Milch", 1.80, "Milchprodukte")
    artikel_hinzufuegen_v3(liste, "Brot", 3.50, "Backwaren")
    artikel_hinzufuegen_v3(liste, "Eier (6er)", 4.20, "Frischware")
    artikel_hinzufuegen_v3(liste, "Käse", 5.90, "Milchprodukte")
    artikel_hinzufuegen_v3(liste, "Äpfel (1kg)", 3.90, "Früchte")
    artikel_hinzufuegen_v3(liste, "Joghurt", 1.20, "Milchprodukte")

    # Unsortiert anzeigen
    print()
    liste_anzeigen_v3(liste)

    # Sortiert anzeigen
    print()
    liste_anzeigen_v3(liste, sortiert=True)

    # Zusammenfassung
    print()
    zeige_zusammenfassung(liste)


# ============================================================
# Hauptprogramm
# ============================================================

if __name__ == "__main__":
    print("=" * 50)
    print("Iteratives Prompting: 3 Runden zur Lösung")
    print("=" * 50)
    print()
    print("Dieses Beispiel zeigt, wie man durch schrittweises")
    print("Verfeinern der Prompts ein Programm entwickelt.")

    # Alle drei Versionen demonstrieren
    demo_version_1()
    demo_version_2()
    demo_version_3()

    print("\n" + "=" * 50)
    print("Fazit: Iteratives Prompting")
    print("=" * 50)
    print("Runde 1: Einfacher Start → Grundfunktionen")
    print("Runde 2: Erweiterung → Mehr Daten (Preise)")
    print("Runde 3: Verfeinerung → Sortierung & Analyse")
    print()
    print("Tipp: Starte einfach und baue schrittweise auf!")
    print("=" * 50)
