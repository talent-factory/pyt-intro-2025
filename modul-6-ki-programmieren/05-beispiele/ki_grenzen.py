"""
Grenzen von KI beim Programmieren

Dieses Skript zeigt Beispiele, wo KI-Assistenten
an ihre Grenzen stossen und falsche oder
unvollständige Ergebnisse liefern.

Konzepte:
- Mehrdeutige Prompts
- Halluzinierte Fakten
- Übervereinfachung
- Kritisches Denken bei KI-Code
"""


# ============================================================
# BEISPIEL 1: Mehrdeutiger Prompt
# ============================================================
# PROMPT: "Schreib eine Funktion die eine Liste filtert"
#
# PROBLEM: Was soll gefiltert werden? Welche Kriterien?
#          Die KI muss raten und liegt oft daneben.

# WAS DIE KI GENERIERT HAT:


def filtere_liste(liste):
    """
    KI hat geraten: Filtert None-Werte heraus.

    Aber der Benutzer wollte eigentlich:
    Alle geraden Zahlen filtern!
    """
    return [element for element in liste if element is not None]


# WAS SCHIEF GING:
# Die KI konnte nicht wissen, welche Art von Filterung gemeint war.
# Sie hat "None-Werte entfernen" geraten - das war nicht gemeint.
#
# WAS WIR LERNEN:
# Immer spezifisch sein! Statt "filtere eine Liste" besser:
# "Filtere alle geraden Zahlen aus einer Liste von Integers"


# Was wir eigentlich wollten:
def filtere_gerade_zahlen(zahlen):
    """
    Die Funktion, die wir eigentlich wollten.

    Args:
        zahlen: Liste von ganzen Zahlen

    Returns:
        list: Nur die geraden Zahlen
    """
    gerade = []
    for zahl in zahlen:
        if zahl % 2 == 0:
            gerade.append(zahl)
    return gerade


# ============================================================
# BEISPIEL 2: KI "halluziniert" Fachwissen
# ============================================================
# PROMPT: "Berechne den Body-Mass-Index und gib die
#          WHO-Kategorien zurück"
#
# PROBLEM: KI hat falsche Grenzwerte verwendet!

# WAS DIE KI GENERIERT HAT:


def berechne_bmi_ki_version(gewicht_kg, groesse_cm):
    """
    KI-generierte BMI-Berechnung.

    ACHTUNG: Die Kategoriegrenzen sind teilweise FALSCH!
    Die KI hat sie "halluziniert" statt nachzuschlagen.
    """
    groesse_m = groesse_cm / 100
    bmi = gewicht_kg / (groesse_m**2)

    # FEHLER: Diese Grenzen sind nicht korrekt!
    # Die KI hat falsche Werte erfunden:
    if bmi < 17.0:  # FALSCH: WHO sagt < 18.5
        kategorie = "Untergewicht"
    elif bmi < 24.0:  # FALSCH: WHO sagt < 25.0
        kategorie = "Normalgewicht"
    elif bmi < 29.0:  # FALSCH: WHO sagt < 30.0
        kategorie = "Übergewicht"
    else:
        kategorie = "Adipositas"

    return round(bmi, 1), kategorie


# WAS SCHIEF GING:
# Die KI kannte die WHO-Kategorien nicht genau und hat
# ähnliche, aber falsche Grenzwerte generiert.
# Jemand der 175cm gross und 74kg schwer ist:
#   BMI = 24.2 → KI sagt "Übergewicht" (Grenze 24.0), WHO sagt "Normalgewicht" (Grenze 25.0)
#
# WAS WIR LERNEN:
# Bei Fachwissen (Medizin, Recht, Finanzen) IMMER die
# KI-Angaben mit offiziellen Quellen überprüfen!


# Korrigierte Version mit richtigen WHO-Grenzwerten:
def berechne_bmi_korrekt(gewicht_kg, groesse_cm):
    """
    BMI-Berechnung mit korrekten WHO-Kategorien.

    WHO-Grenzwerte (korrekt):
    - Untergewicht: < 18.5
    - Normalgewicht: 18.5 - 24.9
    - Übergewicht: 25.0 - 29.9
    - Adipositas: >= 30.0

    Args:
        gewicht_kg: Gewicht in Kilogramm
        groesse_cm: Grösse in Zentimetern

    Returns:
        tuple: (bmi_wert, kategorie)
    """
    groesse_m = groesse_cm / 100
    bmi = gewicht_kg / (groesse_m**2)

    # Korrekte WHO-Grenzwerte (verifiziert!)
    if bmi < 18.5:
        kategorie = "Untergewicht"
    elif bmi < 25.0:
        kategorie = "Normalgewicht"
    elif bmi < 30.0:
        kategorie = "Übergewicht"
    else:
        kategorie = "Adipositas"

    return round(bmi, 1), kategorie


# ============================================================
# BEISPIEL 3: KI vereinfacht zu stark
# ============================================================
# PROMPT: "Schreibe ein Programm zur Validierung von
#          Schweizer Telefonnummern"
#
# PROBLEM: KI hat nur das einfachste Format berücksichtigt

# WAS DIE KI GENERIERT HAT:


def pruefe_telefon_ki_version(nummer):
    """
    KI-Version: Prüft nur ein einziges Format.

    Akzeptiert nur: 0791234567 (10 Ziffern mit 0 am Anfang)
    """
    return len(nummer) == 10 and nummer.startswith("0") and nummer.isdigit()


# WAS SCHIEF GING:
# Schweizer Telefonnummern können verschiedene Formate haben:
# - 079 123 45 67 (mit Leerzeichen)
# - +41 79 123 45 67 (internationale Vorwahl)
# - 0041 79 123 45 67 (mit 00-Vorwahl)
# - 079/123 45 67 (mit Schrägstrich)
# Die KI hat nur das einfachste Format erkannt.
#
# WAS WIR LERNEN:
# Bei Validierung immer an verschiedene Eingabeformate denken.
# Der Prompt muss die erwarteten Formate auflisten!


# Bessere Version:
def pruefe_telefon_verbessert(nummer):
    """
    Verbesserte Prüfung für Schweizer Telefonnummern.

    Akzeptierte Formate:
    - 0791234567
    - 079 123 45 67
    - +41 79 123 45 67
    - 0041 79 123 45 67

    Args:
        nummer: Telefonnummer als String

    Returns:
        tuple: (ist_gueltig: bool, bereinigt: str)
    """
    # Alle Formatierungszeichen entfernen
    bereinigt = nummer.replace(" ", "").replace("/", "").replace("-", "")

    # Internationale Vorwahl normalisieren
    if bereinigt.startswith("+41"):
        bereinigt = "0" + bereinigt[3:]
    elif bereinigt.startswith("0041"):
        bereinigt = "0" + bereinigt[4:]

    # Jetzt sollte es 10 Ziffern sein, beginnend mit 0
    if len(bereinigt) == 10 and bereinigt.startswith("0") and bereinigt.isdigit():
        return (True, bereinigt)

    return (False, nummer)


# ============================================================
# BEISPIEL 4: Kontext fehlt - KI rät falsch
# ============================================================
# PROMPT: "Sortiere die Noten"
#
# PROBLEM: "Sortieren" kann aufsteigend oder absteigend sein.
# In der Schweiz: Beste Note = 6 (höchste zuerst?)
# Die KI sortiert aufsteigend - wir wollten absteigend.

# WAS DIE KI GENERIERT HAT:


def sortiere_noten_ki_version(noten):
    """KI hat aufsteigend sortiert (1, 2, 3...)."""
    return sorted(noten)


# WAS SCHIEF GING:
# In der Schweiz zeigt man Noten oft von der besten zur
# schlechtesten an (6.0, 5.5, 5.0...). Die KI hat aber
# aufsteigend sortiert (1.0, 2.0, 3.0...).
#
# WAS WIR LERNEN:
# "Sortiere" ist mehrdeutig! Immer Sortierrichtung angeben
# und den Kontext erklären (Schweizer Notensystem, 6 = best).


# Spezifische Version:
def sortiere_noten_absteigend(noten):
    """
    Sortiert Noten von der besten zur schlechtesten.

    Im Schweizer System: 6 = beste Note, 1 = schlechteste.

    Args:
        noten: Liste von Noten (1.0-6.0)

    Returns:
        list: Noten absteigend sortiert
    """
    return sorted(noten, reverse=True)


# ============================================================
# Hauptprogramm
# ============================================================

if __name__ == "__main__":
    print("=" * 55)
    print("KI-Grenzen: Wo KI-Assistenten scheitern")
    print("=" * 55)

    # Beispiel 1: Mehrdeutiger Prompt
    print("\n--- Beispiel 1: Mehrdeutiger Prompt ---")
    test_liste = [1, None, 2, 3, None, 4, 5, 6]
    print(f"Eingabe: {test_liste}")
    print(f"KI-Ergebnis (None filtern): {filtere_liste(test_liste)}")
    zahlen = [1, 2, 3, 4, 5, 6]
    print(f"Gewünscht (gerade filtern): {filtere_gerade_zahlen(zahlen)}")

    # Beispiel 2: Halluzinierte Grenzwerte
    print("\n--- Beispiel 2: Falsche Grenzwerte ---")
    gewicht = 77
    groesse = 175
    bmi_ki, kat_ki = berechne_bmi_ki_version(gewicht, groesse)
    bmi_ok, kat_ok = berechne_bmi_korrekt(gewicht, groesse)
    print(f"Person: {gewicht}kg, {groesse}cm")
    print(f"KI-Version:    BMI {bmi_ki} → {kat_ki}")
    print(f"Korrekt (WHO): BMI {bmi_ok} → {kat_ok}")

    # Beispiel 3: Zu starke Vereinfachung
    print("\n--- Beispiel 3: Zu einfache Validierung ---")
    test_nummern = [
        "0791234567",
        "079 123 45 67",
        "+41 79 123 45 67",
        "0041 79 123 45 67",
    ]
    for nummer in test_nummern:
        ki_ok = pruefe_telefon_ki_version(nummer)
        ok, bereinigt = pruefe_telefon_verbessert(nummer)
        ki_symbol = "✅" if ki_ok else "❌"
        ok_symbol = "✅" if ok else "❌"
        print(f"  '{nummer}'")
        print(f"    KI-Version:    {ki_symbol}  Verbessert: {ok_symbol}")

    # Beispiel 4: Fehlender Kontext
    print("\n--- Beispiel 4: Fehlender Kontext ---")
    noten = [5.5, 4.0, 6.0, 3.5, 5.0]
    print(f"Noten: {noten}")
    print(f"KI (aufsteigend):  {sortiere_noten_ki_version(noten)}")
    print(f"Gewünscht (abst.): {sortiere_noten_absteigend(noten)}")

    print("\n" + "=" * 55)
    print("Fazit: KI-Code IMMER kritisch prüfen!")
    print("Besonders bei:")
    print("  - Fachwissen und Grenzwerten")
    print("  - Mehrdeutigen Aufgaben")
    print("  - Vollständigkeit der Lösung")
    print("=" * 55)
