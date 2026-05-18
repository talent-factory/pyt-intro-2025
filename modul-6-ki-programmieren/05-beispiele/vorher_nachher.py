"""
Vorher-Nachher-Vergleich: Anfänger vs. KI-Lösung

Dieses Skript zeigt den Unterschied zwischen
typischem Anfängercode und KI-optimiertem Code.

Konzepte:
- Code-Qualität erkennen
- Docstrings und Kommentare
- Fehlerbehandlung
- Bessere Variablennamen
"""


# ============================================================
# AUFGABE 1: Notenrechner
# ============================================================

# --- VORHER: Anfänger-Lösung ---


def noten_v1(l):
    """Version eines Anfängers."""
    s = 0
    for x in l:
        s = s + x
    d = s / len(l)
    if d >= 5.5:
        print("gut")
    elif d >= 4:
        print("ok")
    else:
        print("schlecht")
    print(d)


# --- NACHHER: KI-optimierte Lösung ---


def berechne_notenschnitt(noten_liste):
    """
    Berechnet den Notenschnitt und gibt eine Bewertung.

    Args:
        noten_liste: Liste von Noten (float, 1.0-6.0)

    Returns:
        dict: Ergebnis mit Schnitt, Bewertung und Details
    """
    # Fehlerbehandlung für leere Liste
    if not noten_liste:
        return {
            "schnitt": 0.0,
            "bewertung": "Keine Noten vorhanden",
            "anzahl": 0,
        }

    # Berechnung
    summe = sum(noten_liste)
    anzahl = len(noten_liste)
    schnitt = summe / anzahl

    # Bewertung bestimmen
    if schnitt >= 5.5:
        bewertung = "Sehr gut"
    elif schnitt >= 4.5:
        bewertung = "Gut"
    elif schnitt >= 4.0:
        bewertung = "Genügend"
    else:
        bewertung = "Ungenügend"

    return {
        "schnitt": round(schnitt, 2),
        "bewertung": bewertung,
        "anzahl": anzahl,
        "beste_note": max(noten_liste),
        "schlechteste_note": min(noten_liste),
    }


# VERGLEICH AUFGABE 1:
# ┌──────────────────────┬──────────────────────────────────┐
# │ Kriterium            │ Vorher → Nachher                 │
# ├──────────────────────┼──────────────────────────────────┤
# │ Funktionsname        │ noten_v1 → berechne_notenschnitt │
# │ Variablennamen       │ l, s, x, d → noten_liste, summe │
# │ Docstring            │ Minimal → Ausführlich mit Args   │
# │ Fehlerbehandlung     │ Keine → Leere Liste abgefangen   │
# │ Rückgabewert         │ Nur print → Dict mit Details     │
# │ Erweiterbarkeit      │ Schwer → Einfach erweiterbar     │
# └──────────────────────┴──────────────────────────────────┘


# ============================================================
# AUFGABE 2: Passwort-Prüfung
# ============================================================

# --- VORHER: Anfänger-Lösung ---


def pw_check(pw):
    """Anfänger-Version der Passwort-Prüfung."""
    if len(pw) > 8:
        ok = True
    else:
        ok = False
    return ok


# --- NACHHER: KI-optimierte Lösung ---


def pruefe_passwort(passwort):
    """
    Prüft die Stärke eines Passworts nach mehreren Kriterien.

    Args:
        passwort: Das zu prüfende Passwort als String

    Returns:
        dict: Ergebnis mit Bewertung und Details zu jedem Kriterium
    """
    ergebnis = {
        "laenge_ok": len(passwort) >= 8,
        "hat_grossbuchstabe": False,
        "hat_kleinbuchstabe": False,
        "hat_ziffer": False,
        "hat_sonderzeichen": False,
    }

    # Jedes Zeichen einzeln prüfen
    for zeichen in passwort:
        if zeichen.isupper():
            ergebnis["hat_grossbuchstabe"] = True
        elif zeichen.islower():
            ergebnis["hat_kleinbuchstabe"] = True
        elif zeichen.isdigit():
            ergebnis["hat_ziffer"] = True
        else:
            ergebnis["hat_sonderzeichen"] = True

    # Gesamtbewertung: Punkte zählen
    punkte = sum(1 for wert in ergebnis.values() if wert)

    if punkte == 5:
        ergebnis["staerke"] = "Sehr stark"
    elif punkte >= 3:
        ergebnis["staerke"] = "Mittel"
    else:
        ergebnis["staerke"] = "Schwach"

    return ergebnis


# VERGLEICH AUFGABE 2:
# ┌──────────────────────┬──────────────────────────────────┐
# │ Kriterium            │ Vorher → Nachher                 │
# ├──────────────────────┼──────────────────────────────────┤
# │ Funktionsname        │ pw_check → pruefe_passwort       │
# │ Parameter            │ pw → passwort                    │
# │ Prüfkriterien        │ Nur Länge → 5 Kriterien          │
# │ Rückgabewert         │ Nur bool → Dict mit Details      │
# │ Docstring            │ Minimal → Args und Returns       │
# │ Nützlichkeit         │ Kaum → Konkrete Verbesserungen   │
# └──────────────────────┴──────────────────────────────────┘


# ============================================================
# AUFGABE 3: Textanalyse
# ============================================================

# --- VORHER: Anfänger-Lösung ---


def text_info(t):
    """Anfänger-Version der Textanalyse."""
    print(len(t))
    w = t.split()
    print(len(w))


# --- NACHHER: KI-optimierte Lösung ---


def analysiere_text(text):
    """
    Führt eine umfassende Textanalyse durch.

    Args:
        text: Der zu analysierende Text als String

    Returns:
        dict: Analyseergebnisse mit verschiedenen Metriken
    """
    if not text.strip():
        return {"fehler": "Leerer Text übergeben"}

    # Wörter aufteilen
    woerter = text.split()
    anzahl_woerter = len(woerter)

    # Sätze zählen (einfache Methode)
    satzzeichen = ".!?"
    anzahl_saetze = sum(1 for zeichen in text if zeichen in satzzeichen)
    if anzahl_saetze == 0:
        anzahl_saetze = 1  # Mindestens ein Satz

    # Wortlängen berechnen
    wort_laengen = [len(wort.strip(".,!?;:")) for wort in woerter]
    durchschnittliche_wortlaenge = sum(wort_laengen) / len(wort_laengen)

    # Ergebnis zusammenstellen
    analyse = {
        "zeichen_gesamt": len(text),
        "zeichen_ohne_leerzeichen": len(text.replace(" ", "")),
        "anzahl_woerter": anzahl_woerter,
        "anzahl_saetze": anzahl_saetze,
        "durchschnittliche_wortlaenge": round(durchschnittliche_wortlaenge, 1),
        "laengstes_wort": max(woerter, key=len),
        "kuerzestes_wort": min(woerter, key=len),
    }

    return analyse


# VERGLEICH AUFGABE 3:
# ┌──────────────────────┬──────────────────────────────────┐
# │ Kriterium            │ Vorher → Nachher                 │
# ├──────────────────────┼──────────────────────────────────┤
# │ Funktionsname        │ text_info → analysiere_text      │
# │ Rückgabe             │ Nur print → Dict mit Metriken    │
# │ Umfang               │ 2 Metriken → 7 Metriken          │
# │ Fehlerbehandlung     │ Keine → Leerer Text abgefangen   │
# │ Wiederverwendbarkeit │ Keine → Als Baustein nutzbar     │
# └──────────────────────┴──────────────────────────────────┘


# ============================================================
# Hauptprogramm
# ============================================================

if __name__ == "__main__":
    print("=" * 50)
    print("Vorher-Nachher-Vergleich")
    print("=" * 50)

    # Aufgabe 1: Notenrechner
    print("\n--- Aufgabe 1: Notenrechner ---")
    noten = [5.5, 4.0, 6.0, 4.5, 5.0]

    print("\nVORHER (Anfänger-Lösung):")
    noten_v1(noten)

    print("\nNACHHER (KI-optimiert):")
    ergebnis = berechne_notenschnitt(noten)
    for schluessel, wert in ergebnis.items():
        print(f"  {schluessel}: {wert}")

    # Aufgabe 2: Passwort-Prüfung
    print("\n--- Aufgabe 2: Passwort-Prüfung ---")
    test_passwort = "Hallo123!"

    print(f"\nPasswort: '{test_passwort}'")
    print(f"\nVORHER (Anfänger): OK = {pw_check(test_passwort)}")

    print("\nNACHHER (KI-optimiert):")
    pw_ergebnis = pruefe_passwort(test_passwort)
    for schluessel, wert in pw_ergebnis.items():
        print(f"  {schluessel}: {wert}")

    # Aufgabe 3: Textanalyse
    print("\n--- Aufgabe 3: Textanalyse ---")
    beispiel_text = (
        "Python ist eine tolle Programmiersprache. Sie ist einfach zu lernen!"
    )

    print(f"\nText: '{beispiel_text}'")
    print("\nVORHER (Anfänger):")
    text_info(beispiel_text)

    print("\nNACHHER (KI-optimiert):")
    text_ergebnis = analysiere_text(beispiel_text)
    for schluessel, wert in text_ergebnis.items():
        print(f"  {schluessel}: {wert}")

    print("\n" + "=" * 50)
    print("Fazit: KI hilft bei Struktur, Fehlerbehandlung")
    print("und aussagekräftigen Namen!")
    print("=" * 50)
