"""
Beispiel: Textdateien lesen und schreiben

Zeigt:
- Dateien öffnen mit 'with'
- Lesen und Schreiben
- Zeile für Zeile verarbeiten
"""

def tagebuch_eintrag(text: str) -> None:
    """Fügt Tagebuch-Eintrag hinzu."""
    from datetime import datetime
    with open("tagebuch.txt", "a") as f:
        zeit = datetime.now().strftime("%Y-%m-%d %H:%M")
        f.write(f"[{zeit}] {text}\n")
    print("✓ Eintrag gespeichert")

def tagebuch_anzeigen() -> None:
    """Zeigt alle Einträge."""
    try:
        with open("tagebuch.txt", "r") as f:
            print("=" * 50)
            print("TAGEBUCH")
            print("=" * 50)
            for zeile in f:
                print(zeile.strip())
    except FileNotFoundError:
        print("Noch keine Einträge.")

def datei_analysieren(dateiname: str) -> None:
    """Analysiert Textdatei."""
    with open(dateiname, "r") as f:
        zeilen = f.readlines()

    print(f"\nAnalyse von {dateiname}:")
    print(f"  Zeilen: {len(zeilen)}")
    print(f"  Wörter: {sum(len(z.split()) for z in zeilen)}")
    print(f"  Zeichen: {sum(len(z) for z in zeilen)}")

if __name__ == "__main__":
    print("=" * 50)
    print("TEXTDATEIEN DEMO")
    print("=" * 50)
    
    tagebuch_eintrag("Heute war ein guter Tag!")
    tagebuch_eintrag("Python macht Spass!")
    tagebuch_anzeigen()
    
    datei_analysieren("tagebuch.txt")
