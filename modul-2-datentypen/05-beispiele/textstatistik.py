"""Erweiterte Textanalyse mit Statistiken"""


def analysiere_text(text: str) -> dict:
    """
    Analysiert einen Text und gibt Statistiken zurück.

    Args:
        text: Der zu analysierende Text

    Returns:
        Dictionary mit Statistiken
    """
    # Grundlegende Zählungen
    anzahl_zeichen = len(text)
    anzahl_zeichen_ohne_leer = len(text.replace(" ", ""))
    anzahl_woerter = len(text.split())
    anzahl_saetze = text.count(".") + text.count("!") + text.count("?")

    # Zeichen-Typen
    anzahl_buchstaben = sum(c.isalpha() for c in text)
    anzahl_zahlen = sum(c.isdigit() for c in text)
    anzahl_leerzeichen = text.count(" ")
    anzahl_gross = sum(c.isupper() for c in text)
    anzahl_klein = sum(c.islower() for c in text)

    # Berechnungen
    durchschnitt_woerter = anzahl_woerter / anzahl_saetze if anzahl_saetze > 0 else 0
    durchschnitt_zeichen = anzahl_zeichen / anzahl_woerter if anzahl_woerter > 0 else 0

    return {
        "zeichen": anzahl_zeichen,
        "zeichen_ohne_leer": anzahl_zeichen_ohne_leer,
        "buchstaben": anzahl_buchstaben,
        "zahlen": anzahl_zahlen,
        "leerzeichen": anzahl_leerzeichen,
        "gross": anzahl_gross,
        "klein": anzahl_klein,
        "woerter": anzahl_woerter,
        "saetze": anzahl_saetze,
        "woerter_pro_satz": durchschnitt_woerter,
        "zeichen_pro_wort": durchschnitt_zeichen,
    }


# Hauptprogramm
print("=" * 50)
print("           TEXTANALYSE")
print("=" * 50)

text = input("\nText eingeben:\n")

stats = analysiere_text(text)

# Ausgabe
print("\n" + "=" * 50)
print("STATISTIK")
print("=" * 50)
print(f"Zeichen gesamt:        {stats['zeichen']:8d}")
print(f"Zeichen ohne Leer:     {stats['zeichen_ohne_leer']:8d}")
print(f"Buchstaben:            {stats['buchstaben']:8d}")
print(f"  - Grossbuchstaben:   {stats['gross']:8d}")
print(f"  - Kleinbuchstaben:   {stats['klein']:8d}")
print(f"Zahlen:                {stats['zahlen']:8d}")
print(f"Leerzeichen:           {stats['leerzeichen']:8d}")
print(f"Wörter:                {stats['woerter']:8d}")
print(f"Sätze:                 {stats['saetze']:8d}")
print("-" * 50)
print(f"Wörter/Satz:           {stats['woerter_pro_satz']:8.1f}")
print(f"Zeichen/Wort:          {stats['zeichen_pro_wort']:8.1f}")
print("=" * 50)
