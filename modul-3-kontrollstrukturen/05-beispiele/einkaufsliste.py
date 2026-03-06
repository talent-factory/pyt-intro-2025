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

# Einkaufsliste initialisieren
einkaufsliste = []

print("\n👋 Willkommen beim Einkaufslisten-Manager!")

# Hauptschleife
while True:
    # Menü anzeigen
    print("\n" + "=" * 40)
    print("      EINKAUFSLISTEN-MANAGER")
    print("=" * 40)
    print("1. Artikel hinzufügen")
    print("2. Liste anzeigen")
    print("3. Artikel löschen")
    print("4. Liste leeren")
    print("5. Beenden")
    print("=" * 40)

    wahl = input("\nWahl: ").strip()

    if wahl == "1":
        # Artikel hinzufügen – beliebig viele, getrennt durch Komma oder Semikolon
        eingabe = input("\nArtikel (mehrere mit Komma trennen): ").strip()

        if eingabe == "":
            print("❌ Artikel darf nicht leer sein!")
        else:
            # Trennzeichen vereinheitlichen und aufteilen
            eingabe_bereinigt = eingabe.replace(";", ",")
            teile = [a.strip() for a in eingabe_bereinigt.split(",") if a.strip()]

            for artikel in teile:
                einkaufsliste.append(artikel)
                print(f"✓ '{artikel}' hinzugefügt")

    elif wahl == "2":
        # Liste anzeigen
        if len(einkaufsliste) == 0:
            print("\n📝 Liste ist leer")
        else:
            print("\n" + "=" * 40)
            print("      IHRE EINKAUFSLISTE")
            print("=" * 40)

            # Nummerierte Ausgabe
            nummer = 1
            for artikel in einkaufsliste:
                print(f"{nummer}. {artikel}")
                nummer += 1

            print("=" * 40)
            print(f"Gesamt: {len(einkaufsliste)} Artikel")

    elif wahl == "3":
        # Artikel löschen
        if len(einkaufsliste) == 0:
            print("\n❌ Liste ist leer!")
        else:
            # Erst Liste anzeigen
            print("\n" + "=" * 40)
            print("      IHRE EINKAUFSLISTE")
            print("=" * 40)

            nummer = 1
            for artikel in einkaufsliste:
                print(f"{nummer}. {artikel}")
                nummer += 1

            print("=" * 40)
            print(f"Gesamt: {len(einkaufsliste)} Artikel")

            # Artikel zum Löschen auswählen
            try:
                nummer = int(input("\nWelchen Artikel löschen? (Nummer): "))

                if 1 <= nummer <= len(einkaufsliste):
                    artikel = einkaufsliste.pop(nummer - 1)
                    print(f"✓ '{artikel}' gelöscht")
                else:
                    print(
                        f"❌ Ungültige Nummer! Bitte zwischen 1 und {len(einkaufsliste)}"
                    )

            except ValueError:
                print("❌ Bitte eine Zahl eingeben!")

    elif wahl == "4":
        # Liste leeren
        if len(einkaufsliste) == 0:
            print("\n❌ Liste ist bereits leer!")
        else:
            bestaetigung = input(
                f"\n⚠️  Wirklich {len(einkaufsliste)} Artikel löschen? (j/n): "
            )

            if bestaetigung.lower() in ["j", "ja", "y", "yes"]:
                einkaufsliste.clear()
                print("✓ Liste geleert")
            else:
                print("Abgebrochen")

    elif wahl == "5":
        print("\n👋 Auf Wiedersehen!")
        break

    else:
        print("\n❌ Ungültige Wahl! Bitte 1-5 wählen.")
