"""
Passwort-Generator (Musterlösung)

Ein vollständiger Passwort-Generator, entwickelt mit KI-Unterstützung.
Dokumentiert den Entwicklungsprozess mit KI.

Konzepte:
- Zufallsgenerierung mit random
- String-Manipulation mit string-Modul
- Funktionsparameter mit Standardwerten
- Passwort-Sicherheitsbewertung

Entwicklungsprozess mit KI:
1. Prompt: "Erstelle einen Passwort-Generator in Python"
2. Erweiterung: "Füge Optionen für Zeichentypen hinzu"
3. Verfeinerung: "Ergänze eine Stärke-Bewertung"
4. Finalisierung: "Formatiere die Ausgabe schön"
"""

import random
import string

# ============================================================
# Passwort erstellen
# ============================================================
# KI-PROMPT: "Erstelle eine Funktion die ein zufälliges Passwort
#   generiert. Es soll konfigurierbar sein: Länge, mit/ohne
#   Grossbuchstaben, Ziffern, Sonderzeichen."


def erstelle_passwort(
    laenge=12,
    mit_grossbuchstaben=True,
    mit_ziffern=True,
    mit_sonderzeichen=False,
):
    """
    Erstellt ein zufälliges Passwort mit konfigurierbaren Optionen.

    Args:
        laenge: Gewünschte Passwortlänge (Standard: 12)
        mit_grossbuchstaben: Grossbuchstaben einbeziehen (Standard: True)
        mit_ziffern: Ziffern einbeziehen (Standard: True)
        mit_sonderzeichen: Sonderzeichen einbeziehen (Standard: False)

    Returns:
        str: Das generierte Passwort
    """
    # Zeichenpool aufbauen - immer mit Kleinbuchstaben starten
    zeichenpool = string.ascii_lowercase
    pflicht_zeichen = [random.choice(string.ascii_lowercase)]

    # Optional Grossbuchstaben hinzufügen
    if mit_grossbuchstaben:
        zeichenpool += string.ascii_uppercase
        pflicht_zeichen.append(random.choice(string.ascii_uppercase))

    # Optional Ziffern hinzufügen
    if mit_ziffern:
        zeichenpool += string.digits
        pflicht_zeichen.append(random.choice(string.digits))

    # Optional Sonderzeichen hinzufügen
    if mit_sonderzeichen:
        sonderzeichen = "!@#$%&*+-=?"
        zeichenpool += sonderzeichen
        pflicht_zeichen.append(random.choice(sonderzeichen))

    # Restliche Zeichen zufällig aus dem Pool wählen
    restlaenge = laenge - len(pflicht_zeichen)
    if restlaenge < 0:
        restlaenge = 0

    alle_zeichen = pflicht_zeichen + [
        random.choice(zeichenpool) for _ in range(restlaenge)
    ]

    # Zeichen mischen, damit Pflichtzeichen nicht immer vorne stehen
    random.shuffle(alle_zeichen)

    # Liste zu String zusammenfügen
    passwort = "".join(alle_zeichen)
    return passwort


# ============================================================
# Passwort-Stärke bewerten
# ============================================================
# KI-PROMPT: "Erstelle eine Funktion die ein Passwort bewertet.
#   Prüfe Länge, Zeichenvielfalt und gib eine Bewertung
#   von 1-5 Sternen zurück."


def bewerte_passwort_staerke(passwort):
    """
    Bewertet die Stärke eines Passworts.

    Kriterien:
    - Länge (min. 8, besser 12+)
    - Grossbuchstaben vorhanden
    - Kleinbuchstaben vorhanden
    - Ziffern vorhanden
    - Sonderzeichen vorhanden

    Args:
        passwort: Das zu bewertende Passwort

    Returns:
        dict: Bewertung mit Punkten, Sternen und Details
    """
    punkte = 0
    details = []

    # Kriterium 1: Länge
    if len(passwort) >= 12:
        punkte += 2
        details.append("✅ Sehr gute Länge (12+ Zeichen)")
    elif len(passwort) >= 8:
        punkte += 1
        details.append("⚠️ Akzeptable Länge (8-11 Zeichen)")
    else:
        details.append("❌ Zu kurz (unter 8 Zeichen)")

    # Kriterium 2: Kleinbuchstaben
    hat_klein = any(z.islower() for z in passwort)
    if hat_klein:
        punkte += 1
        details.append("✅ Kleinbuchstaben vorhanden")
    else:
        details.append("❌ Keine Kleinbuchstaben")

    # Kriterium 3: Grossbuchstaben
    hat_gross = any(z.isupper() for z in passwort)
    if hat_gross:
        punkte += 1
        details.append("✅ Grossbuchstaben vorhanden")
    else:
        details.append("❌ Keine Grossbuchstaben")

    # Kriterium 4: Ziffern
    hat_ziffer = any(z.isdigit() for z in passwort)
    if hat_ziffer:
        punkte += 1
        details.append("✅ Ziffern vorhanden")
    else:
        details.append("❌ Keine Ziffern")

    # Kriterium 5: Sonderzeichen
    hat_sonder = any(not z.isalnum() for z in passwort)
    if hat_sonder:
        punkte += 1
        details.append("✅ Sonderzeichen vorhanden")
    else:
        details.append("⚠️ Keine Sonderzeichen")

    # Sterne berechnen (max 6 Punkte → max 5 Sterne)
    if punkte >= 6:
        sterne = 5
    elif punkte >= 5:
        sterne = 4
    elif punkte >= 4:
        sterne = 3
    elif punkte >= 3:
        sterne = 2
    else:
        sterne = 1

    # Textbewertung
    bewertungen = {
        5: "Ausgezeichnet",
        4: "Stark",
        3: "Mittel",
        2: "Schwach",
        1: "Sehr schwach",
    }

    return {
        "punkte": punkte,
        "sterne": sterne,
        "bewertung": bewertungen[sterne],
        "sterne_anzeige": "★" * sterne + "☆" * (5 - sterne),
        "details": details,
    }


# ============================================================
# Mehrere Passwörter generieren
# ============================================================


def generiere_passwort_vorschlaege(anzahl=5):
    """
    Generiert mehrere Passwort-Vorschläge mit verschiedenen Stärken.

    Args:
        anzahl: Anzahl der Vorschläge (Standard: 5)

    Returns:
        list: Liste von Tuples (passwort, bewertung)
    """
    vorschlaege = []

    for _ in range(anzahl):
        # Zufällige Konfiguration
        laenge = random.choice([8, 10, 12, 14, 16])
        mit_gross = random.choice([True, True, True, False])
        mit_ziffern = random.choice([True, True, True, False])
        mit_sonder = random.choice([True, False, False, False])

        # Passwort generieren und bewerten
        passwort = erstelle_passwort(laenge, mit_gross, mit_ziffern, mit_sonder)
        bewertung = bewerte_passwort_staerke(passwort)

        vorschlaege.append((passwort, bewertung))

    return vorschlaege


# ============================================================
# Hauptprogramm
# ============================================================

if __name__ == "__main__":
    print("=" * 55)
    print("Passwort-Generator")
    print("=" * 55)

    # Einzelne Passwörter mit verschiedenen Optionen
    print("\n--- Verschiedene Konfigurationen ---")

    konfigurationen = [
        {"laenge": 8, "mit_grossbuchstaben": False, "mit_ziffern": False},
        {"laenge": 10, "mit_grossbuchstaben": True, "mit_ziffern": True},
        {"laenge": 12, "mit_grossbuchstaben": True, "mit_ziffern": True},
        {
            "laenge": 16,
            "mit_grossbuchstaben": True,
            "mit_ziffern": True,
            "mit_sonderzeichen": True,
        },
    ]

    for konfig in konfigurationen:
        passwort = erstelle_passwort(**konfig)
        bewertung = bewerte_passwort_staerke(passwort)
        print(f"\n  Passwort:  {passwort}")
        print(f"  Länge:     {len(passwort)}")
        print(f"  Stärke:    {bewertung['sterne_anzeige']} ({bewertung['bewertung']})")

    # Passwort bewerten
    print("\n" + "=" * 55)
    print("Passwort-Bewertung im Detail")
    print("=" * 55)

    test_passwort = erstelle_passwort(
        laenge=14,
        mit_grossbuchstaben=True,
        mit_ziffern=True,
        mit_sonderzeichen=True,
    )

    print(f"\nPasswort: {test_passwort}")
    bewertung = bewerte_passwort_staerke(test_passwort)
    print(f"Stärke:   {bewertung['sterne_anzeige']} ({bewertung['bewertung']})")
    print(f"Punkte:   {bewertung['punkte']}/6")
    print("\nDetails:")
    for detail in bewertung["details"]:
        print(f"  {detail}")

    # Mehrere Vorschläge
    print("\n" + "=" * 55)
    print("5 Passwort-Vorschläge")
    print("=" * 55)

    vorschlaege = generiere_passwort_vorschlaege(5)
    for i, (pw, bw) in enumerate(vorschlaege, 1):
        print(f"\n  {i}. {pw}")
        print(f"     {bw['sterne_anzeige']} {bw['bewertung']} ({len(pw)} Zeichen)")

    print("\n" + "=" * 55)
    print("Hinweis: Verwende in der Praxis einen echten")
    print("Passwort-Manager für sichere Passwörter!")
    print("=" * 55)
