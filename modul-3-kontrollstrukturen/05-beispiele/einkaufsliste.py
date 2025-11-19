"""
Einkaufslisten-Manager
Ein vollständiges Beispiel für Menü-Systeme und Listen-Manipulation.

Konzepte:
- While-Schleife für Menü
- If-elif-else für Auswahl
- Listen manipulieren
- Input-Validierung
- Fehlerbehandlung
"""


def zeige_menu() -> None:
    """Zeigt das Hauptmenü an."""
    print("\n" + "=" * 40)
    print("      EINKAUFSLISTEN-MANAGER")
    print("=" * 40)
    print("1. Artikel hinzufügen")
    print("2. Liste anzeigen")
    print("3. Artikel löschen")
    print("4. Liste leeren")
    print("5. Beenden")
    print("=" * 40)


def artikel_hinzufuegen(liste: list[str]) -> None:
    """Fügt einen Artikel zur Liste hinzu."""
    artikel = input("\nArtikel: ").strip()
    
    if artikel == "":
        print("❌ Artikel darf nicht leer sein!")
        return
    
    liste.append(artikel)
    print(f"✓ '{artikel}' hinzugefügt")


def liste_anzeigen(liste: list[str]) -> None:
    """Zeigt die Einkaufsliste an."""
    if len(liste) == 0:
        print("\n📝 Liste ist leer")
        return
    
    print("\n" + "=" * 40)
    print("      IHRE EINKAUFSLISTE")
    print("=" * 40)
    
    for i, artikel in enumerate(liste, start=1):
        print(f"{i}. {artikel}")
    
    print("=" * 40)
    print(f"Gesamt: {len(liste)} Artikel")


def artikel_loeschen(liste: list[str]) -> None:
    """Löscht einen Artikel aus der Liste."""
    if len(liste) == 0:
        print("\n❌ Liste ist leer!")
        return
    
    # Erst Liste anzeigen
    liste_anzeigen(liste)
    
    try:
        nummer = int(input("\nWelchen Artikel löschen? (Nummer): "))
        
        if 1 <= nummer <= len(liste):
            artikel = liste.pop(nummer - 1)
            print(f"✓ '{artikel}' gelöscht")
        else:
            print(f"❌ Ungültige Nummer! Bitte zwischen 1 und {len(liste)}")
    
    except ValueError:
        print("❌ Bitte eine Zahl eingeben!")


def liste_leeren(liste: list[str]) -> None:
    """Leert die gesamte Liste nach Bestätigung."""
    if len(liste) == 0:
        print("\n❌ Liste ist bereits leer!")
        return
    
    bestaetigung = input(f"\n⚠️  Wirklich {len(liste)} Artikel löschen? (j/n): ")
    
    if bestaetigung.lower() in ["j", "ja", "y", "yes"]:
        liste.clear()
        print("✓ Liste geleert")
    else:
        print("Abgebrochen")


def main() -> None:
    """Hauptprogramm."""
    einkaufsliste: list[str] = []
    
    print("\n👋 Willkommen beim Einkaufslisten-Manager!")
    
    while True:
        zeige_menu()
        
        wahl = input("\nWahl: ").strip()
        
        if wahl == "1":
            artikel_hinzufuegen(einkaufsliste)
        
        elif wahl == "2":
            liste_anzeigen(einkaufsliste)
        
        elif wahl == "3":
            artikel_loeschen(einkaufsliste)
        
        elif wahl == "4":
            liste_leeren(einkaufsliste)
        
        elif wahl == "5":
            print("\n👋 Auf Wiedersehen!")
            break
        
        else:
            print("\n❌ Ungültige Wahl! Bitte 1-5 wählen.")


if __name__ == "__main__":
    main()

