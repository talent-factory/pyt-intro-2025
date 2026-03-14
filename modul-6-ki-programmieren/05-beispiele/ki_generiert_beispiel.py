"""
KI-generiertes Beispiel: Einkaufslisten-Manager

Dieses Programm wurde mit Hilfe von Claude Code erstellt.
Jede Funktion ist mit einer Bewertung annotiert.

Konzepte:
- KI-generierten Code bewerten
- Qualitätsmerkmale erkennen
- Code anpassen und verbessern
"""


# KI-GENERIERT: Diese Funktion wurde von Claude Code erstellt
# BEWERTUNG: ✅ Gut - klare Struktur, gute Variablennamen


def erstelle_einkaufsliste(name):
    """
    Erstellt eine neue, leere Einkaufsliste.

    Args:
        name: Name der Einkaufsliste (z.B. "Wocheneinkauf")

    Returns:
        dict: Einkaufsliste mit Name und leerer Artikelliste
    """
    einkaufsliste = {
        "name": name,
        "artikel": [],
    }
    return einkaufsliste


# KI-GENERIERT: Diese Funktion wurde von Claude Code erstellt
# BEWERTUNG: ✅ Gut - Duplikat-Prüfung und Mengenangabe vorhanden


def artikel_hinzufuegen(einkaufsliste, artikel_name, menge=1, einheit="Stück"):
    """
    Fügt einen Artikel zur Einkaufsliste hinzu.

    Args:
        einkaufsliste: Die Einkaufsliste (dict)
        artikel_name: Name des Artikels
        menge: Anzahl/Menge (Standard: 1)
        einheit: Mengeneinheit (Standard: "Stück")

    Returns:
        bool: True wenn hinzugefügt, False wenn bereits vorhanden
    """
    # Prüfen ob Artikel bereits existiert
    for artikel in einkaufsliste["artikel"]:
        if artikel["name"].lower() == artikel_name.lower():
            print(f"'{artikel_name}' ist bereits auf der Liste!")
            return False

    # Neuen Artikel erstellen und hinzufügen
    neuer_artikel = {
        "name": artikel_name,
        "menge": menge,
        "einheit": einheit,
        "erledigt": False,
    }
    einkaufsliste["artikel"].append(neuer_artikel)
    return True


# KI-GENERIERT: Diese Funktion wurde von Claude Code erstellt
# BEWERTUNG: ⚠️ Angepasst - Original hatte keine Fehlerbehandlung
# ANPASSUNG: Try-Except und Eingabevalidierung hinzugefügt
#
# ORIGINAL (KI):
#   def artikel_entfernen(einkaufsliste, artikel_name):
#       for i, artikel in enumerate(einkaufsliste["artikel"]):
#           if artikel["name"] == artikel_name:
#               einkaufsliste["artikel"].pop(i)
#               return True
#       return False
#
# PROBLEM: Kein Hinweis wenn Artikel nicht gefunden wurde,
#          und Gross-/Kleinschreibung wurde nicht ignoriert.


def artikel_entfernen(einkaufsliste, artikel_name):
    """
    Entfernt einen Artikel von der Einkaufsliste.

    Args:
        einkaufsliste: Die Einkaufsliste (dict)
        artikel_name: Name des zu entfernenden Artikels

    Returns:
        bool: True wenn entfernt, False wenn nicht gefunden
    """
    for i, artikel in enumerate(einkaufsliste["artikel"]):
        # Anpassung: Gross-/Kleinschreibung ignorieren
        if artikel["name"].lower() == artikel_name.lower():
            entfernter = einkaufsliste["artikel"].pop(i)
            print(f"'{entfernter['name']}' wurde entfernt.")
            return True

    # Anpassung: Hilfreiche Fehlermeldung
    print(f"'{artikel_name}' wurde nicht auf der Liste gefunden.")
    return False


# KI-GENERIERT: Diese Funktion wurde von Claude Code erstellt
# BEWERTUNG: ⚠️ Angepasst - KI hatte nur print() verwendet
# ANPASSUNG: Formatierung verbessert, Zusammenfassung ergänzt
#
# ORIGINAL (KI):
#   def zeige_liste(einkaufsliste):
#       print(einkaufsliste["name"])
#       for a in einkaufsliste["artikel"]:
#           print(f"- {a['name']}: {a['menge']}")
#
# PROBLEM: Keine Trennlinien, keine Nummerierung,
#          kein Status (erledigt/offen), keine Zusammenfassung.


def zeige_einkaufsliste(einkaufsliste):
    """
    Zeigt die Einkaufsliste formatiert an.

    Args:
        einkaufsliste: Die Einkaufsliste (dict)
    """
    print("=" * 40)
    print(f"Einkaufsliste: {einkaufsliste['name']}")
    print("=" * 40)

    if not einkaufsliste["artikel"]:
        print("(Liste ist leer)")
        print("=" * 40)
        return

    # Artikel nummeriert anzeigen
    for nummer, artikel in enumerate(einkaufsliste["artikel"], 1):
        # Anpassung: Status-Symbol für erledigt/offen
        status = "✅" if artikel["erledigt"] else "⬜"
        print(
            f"  {nummer}. {status} {artikel['name']}: "
            f"{artikel['menge']} {artikel['einheit']}"
        )

    # Anpassung: Zusammenfassung am Ende
    gesamt = len(einkaufsliste["artikel"])
    erledigt = sum(1 for a in einkaufsliste["artikel"] if a["erledigt"])
    print("-" * 40)
    print(f"Gesamt: {gesamt} Artikel ({erledigt} erledigt, {gesamt - erledigt} offen)")
    print("=" * 40)


# KI-GENERIERT: Diese Funktion wurde von Claude Code erstellt
# BEWERTUNG: ✅ Gut - einfache, klare Logik


def artikel_abhaken(einkaufsliste, artikel_name):
    """
    Markiert einen Artikel als erledigt.

    Args:
        einkaufsliste: Die Einkaufsliste (dict)
        artikel_name: Name des Artikels

    Returns:
        bool: True wenn gefunden und abgehakt
    """
    for artikel in einkaufsliste["artikel"]:
        if artikel["name"].lower() == artikel_name.lower():
            artikel["erledigt"] = True
            print(f"'{artikel['name']}' wurde abgehakt. ✅")
            return True

    print(f"'{artikel_name}' nicht gefunden.")
    return False


# ============================================================
# Hauptprogramm
# ============================================================

if __name__ == "__main__":
    print("=" * 50)
    print("Einkaufslisten-Manager (KI-generiert)")
    print("=" * 50)

    # Liste erstellen
    print("\n--- Neue Liste erstellen ---")
    meine_liste = erstelle_einkaufsliste("Wocheneinkauf")

    # Artikel hinzufügen
    print("\n--- Artikel hinzufügen ---")
    artikel_hinzufuegen(meine_liste, "Milch", 2, "Liter")
    artikel_hinzufuegen(meine_liste, "Brot", 1, "Stück")
    artikel_hinzufuegen(meine_liste, "Äpfel", 6, "Stück")
    artikel_hinzufuegen(meine_liste, "Käse", 200, "Gramm")
    artikel_hinzufuegen(meine_liste, "Milch", 1, "Liter")  # Duplikat!

    # Liste anzeigen
    print("\n--- Aktuelle Liste ---")
    zeige_einkaufsliste(meine_liste)

    # Artikel abhaken
    print("\n--- Einkaufen ---")
    artikel_abhaken(meine_liste, "Milch")
    artikel_abhaken(meine_liste, "Brot")

    # Artikel entfernen
    print("\n--- Artikel entfernen ---")
    artikel_entfernen(meine_liste, "Käse")
    artikel_entfernen(meine_liste, "Schokolade")  # Nicht vorhanden

    # Finale Liste
    print("\n--- Finale Liste ---")
    zeige_einkaufsliste(meine_liste)

    print("\n" + "=" * 50)
    print("Fazit: KI-Code ist ein guter Startpunkt,")
    print("muss aber immer geprüft und angepasst werden!")
    print("=" * 50)
