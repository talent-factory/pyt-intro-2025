"""
Beispiel: Notizen-App (Lösung zu Übung 1)

Eine einfache, voll lauffähige Notizen-App. Der Benutzer wird über ein
Menü interaktiv nach Notizen gefragt. Die Notizen werden mit Zeitstempel
in der Datei 'notizen.txt' gespeichert.

Zeigt:
- Dateien öffnen mit 'with'
- An eine Datei anhängen (Modus 'a')
- Aus einer Datei lesen (Modus 'r')
- Fehlerbehandlung mit try / except (FileNotFoundError)
- Datum und Uhrzeit mit datetime
"""

from datetime import datetime

# Name der Datei, in der die Notizen gespeichert werden
NOTIZEN_DATEI = "notizen.txt"


def formatiere_notiz(notiz: str, zeitpunkt: datetime | None = None) -> str:
    """
    Erzeugt eine Notiz-Zeile mit Zeitstempel.

    Diese reine Funktion enthält keine Ein-/Ausgabe und kann darum sowohl
    von der Konsolen-App als auch von der Streamlit-App genutzt werden.

    Args:
        notiz: Der Notiztext.
        zeitpunkt: Zeitstempel der Notiz. Standard ist die aktuelle Zeit.

    Returns:
        Formatierte Zeile, z. B. '[2026-06-02 14:30] Einkaufen gehen'.
    """
    if zeitpunkt is None:
        zeitpunkt = datetime.now()
    zeit = zeitpunkt.strftime("%Y-%m-%d %H:%M")
    return f"[{zeit}] {notiz}"


def neue_notiz() -> None:
    """
    Fragt den Benutzer nach einer Notiz und speichert sie.

    Die Notiz wird mit aktuellem Datum und Uhrzeit an die Datei
    'notizen.txt' angehängt. Bereits vorhandene Notizen bleiben
    erhalten, weil die Datei im Modus 'a' (append) geöffnet wird.
    """
    notiz = input("Notiz: ")

    # Leere Eingaben nicht speichern
    if notiz.strip() == "":
        print("✗ Leere Notiz wurde nicht gespeichert.")
        return

    # Datei im Anhänge-Modus 'a' öffnen
    with open(NOTIZEN_DATEI, "a", encoding="utf-8") as datei:
        datei.write(formatiere_notiz(notiz) + "\n")

    print("✓ Notiz gespeichert")


def zeige_notizen() -> None:
    """
    Zeigt alle gespeicherten Notizen an.

    Falls noch keine Notizen-Datei existiert, wird ein freundlicher
    Hinweis ausgegeben statt eines Programmfehlers.
    """
    try:
        with open(NOTIZEN_DATEI, encoding="utf-8") as datei:
            inhalt = datei.read()

        print("=" * 50)
        print("MEINE NOTIZEN")
        print("=" * 50)

        # Wenn die Datei zwar existiert, aber leer ist
        if inhalt.strip() == "":
            print("Keine Notizen vorhanden.")
        else:
            print(inhalt, end="")

        print("=" * 50)

    except FileNotFoundError:
        print("Keine Notizen vorhanden.")


def menue_anzeigen() -> None:
    """Zeigt das Auswahlmenü an."""
    print()
    print("=" * 50)
    print("NOTIZEN-APP")
    print("=" * 50)
    print("1 - Neue Notiz erfassen")
    print("2 - Alle Notizen anzeigen")
    print("3 - Programm beenden")
    print("=" * 50)


def main() -> None:
    """Hauptprogramm: zeigt das Menü und fragt nach Notizen."""
    print("Willkommen in deiner Notizen-App!")

    while True:
        menue_anzeigen()
        auswahl = input("Deine Auswahl (1-3): ")

        if auswahl == "1":
            neue_notiz()
        elif auswahl == "2":
            zeige_notizen()
        elif auswahl == "3":
            print("Auf Wiedersehen! 👋")
            break
        else:
            print("✗ Ungültige Eingabe. Bitte 1, 2 oder 3 wählen.")


if __name__ == "__main__":
    main()
