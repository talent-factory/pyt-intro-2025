"""
Prompt-Beispiele für KI-gestütztes Programmieren

Dieses Skript zeigt, wie die Qualität eines Prompts
das Ergebnis beeinflusst.

Konzepte:
- Gute vs. schlechte Prompts
- Spezifität und Kontext
- Iteratives Verfeinern
"""


# ============================================================
# PAAR 1: Einfache Berechnung
# ============================================================

# SCHLECHTER PROMPT: "Schreib eine Funktion für Durchschnitt"
# WARUM SCHLECHT: Unklar - welche Eingabe? Was bei leerer Liste?
#                 Keine Angabe zu Rückgabewert oder Fehlerbehandlung.


def durchschnitt_schlecht(zahlen):
    return sum(zahlen) / len(zahlen)


# GUTER PROMPT: "Schreibe eine Python-Funktion berechne_durchschnitt(),
#   die eine Liste von Zahlen entgegennimmt und den Durchschnitt
#   als float zurückgibt. Bei leerer Liste soll 0.0 zurückgegeben
#   werden. Verwende deutsche Variablennamen und einen Docstring."


def berechne_durchschnitt(zahlen):
    """
    Berechnet den Durchschnitt einer Liste von Zahlen.

    Args:
        zahlen: Liste von Zahlen (int oder float)

    Returns:
        float: Durchschnittswert, 0.0 bei leerer Liste
    """
    if not zahlen:
        return 0.0

    summe = 0.0
    for zahl in zahlen:
        summe += zahl

    return summe / len(zahlen)


# ============================================================
# PAAR 2: Textverarbeitung
# ============================================================

# SCHLECHTER PROMPT: "Mach was mit Text"
# WARUM SCHLECHT: Völlig unspezifisch - was soll mit dem Text passieren?


def text_funktion(text):
    return text.upper()


# GUTER PROMPT: "Erstelle eine Funktion zaehle_woerter(), die einen
#   deutschen Text als String erhält und ein Dictionary zurückgibt,
#   in dem jedes Wort als Schlüssel und seine Häufigkeit als Wert
#   steht. Gross-/Kleinschreibung soll ignoriert werden."


def zaehle_woerter(text):
    """
    Zählt die Häufigkeit jedes Wortes in einem Text.

    Args:
        text: Ein String mit Wörtern

    Returns:
        dict: Wort -> Anzahl (Kleinschreibung)
    """
    if not text.strip():
        return {}

    woerter = text.lower().split()
    haeufigkeit = {}

    for wort in woerter:
        # Satzzeichen am Ende entfernen
        wort = wort.strip(".,!?;:")
        if wort:
            if wort in haeufigkeit:
                haeufigkeit[wort] += 1
            else:
                haeufigkeit[wort] = 1

    return haeufigkeit


# ============================================================
# PAAR 3: Listenverarbeitung
# ============================================================

# SCHLECHTER PROMPT: "Filter eine Liste"
# WARUM SCHLECHT: Welche Liste? Welcher Filter? Welches Kriterium?


def filter_liste(liste):
    return [x for x in liste if x > 0]


# GUTER PROMPT: "Schreibe eine Funktion filtere_gerade_zahlen(),
#   die eine Liste von ganzen Zahlen erhält und eine neue Liste
#   nur mit den geraden Zahlen zurückgibt. Verwende eine
#   for-Schleife (keine List Comprehension) und erkläre den
#   Code mit Kommentaren."


def filtere_gerade_zahlen(zahlen):
    """
    Filtert alle geraden Zahlen aus einer Liste.

    Args:
        zahlen: Liste von ganzen Zahlen

    Returns:
        list: Neue Liste nur mit geraden Zahlen
    """
    # Neue Liste für die Ergebnisse erstellen
    gerade_zahlen = []

    # Jede Zahl in der Liste prüfen
    for zahl in zahlen:
        # Modulo-Operator: Rest bei Division durch 2
        # Wenn Rest 0 ist, ist die Zahl gerade
        if zahl % 2 == 0:
            gerade_zahlen.append(zahl)

    return gerade_zahlen


# ============================================================
# PAAR 4: Datenvalidierung
# ============================================================

# SCHLECHTER PROMPT: "Prüf eine E-Mail"
# WARUM SCHLECHT: Wie genau prüfen? Welche Regeln? Was zurückgeben?


def check_email(email):
    return "@" in email


# GUTER PROMPT: "Erstelle eine Funktion pruefe_email(), die eine
#   E-Mail-Adresse als String erhält und prüft, ob sie gültig ist.
#   Prüfe: enthält genau ein @, hat Text vor und nach dem @,
#   hat einen Punkt nach dem @. Gib True/False zurück und
#   bei False eine Fehlermeldung als Tuple (bool, str)."


def pruefe_email(email):
    """
    Prüft, ob eine E-Mail-Adresse grundlegend gültig ist.

    Args:
        email: E-Mail-Adresse als String

    Returns:
        tuple: (ist_gueltig: bool, nachricht: str)
    """
    # Prüfung 1: Enthält genau ein @-Zeichen
    if email.count("@") != 1:
        return (False, "E-Mail muss genau ein @-Zeichen enthalten")

    # In lokalen Teil und Domain aufteilen
    lokaler_teil, domain = email.split("@")

    # Prüfung 2: Lokaler Teil darf nicht leer sein
    if not lokaler_teil:
        return (False, "Vor dem @ muss ein Name stehen")

    # Prüfung 3: Domain darf nicht leer sein
    if not domain:
        return (False, "Nach dem @ muss eine Domain stehen")

    # Prüfung 4: Domain muss einen Punkt enthalten
    if "." not in domain:
        return (False, "Die Domain muss einen Punkt enthalten")

    return (True, "E-Mail-Adresse ist gültig")


# ============================================================
# PAAR 5: Ausgabeformatierung
# ============================================================

# SCHLECHTER PROMPT: "Zeig Daten an"
# WARUM SCHLECHT: Welche Daten? Welches Format? Wie anzeigen?


def zeig_daten(daten):
    for d in daten:
        print(d)


# GUTER PROMPT: "Schreibe eine Funktion zeige_tabelle(), die eine
#   Liste von Dictionaries erhält (jedes Dict hat 'name', 'alter',
#   'stadt') und sie als formatierte Tabelle mit Spaltenüberschriften
#   und Trennlinien ausgibt. Nutze f-Strings mit fester Breite."


def zeige_tabelle(personen):
    """
    Zeigt eine Liste von Personen als formatierte Tabelle an.

    Args:
        personen: Liste von Dicts mit 'name', 'alter', 'stadt'
    """
    # Spaltenbreiten definieren
    breite_name = 20
    breite_alter = 8
    breite_stadt = 15

    # Überschrift ausgeben
    print(
        f"{'Name':<{breite_name}} {'Alter':>{breite_alter}} {'Stadt':<{breite_stadt}}"
    )
    print("-" * (breite_name + breite_alter + breite_stadt + 2))

    # Datenzeilen ausgeben
    for person in personen:
        name = person.get("name", "Unbekannt")
        alter = person.get("alter", 0)
        stadt = person.get("stadt", "Unbekannt")
        print(f"{name:<{breite_name}} {alter:>{breite_alter}} {stadt:<{breite_stadt}}")

    # Zusammenfassung
    print("-" * (breite_name + breite_alter + breite_stadt + 2))
    print(f"Gesamt: {len(personen)} Personen")


# ============================================================
# Hauptprogramm
# ============================================================

if __name__ == "__main__":
    print("=" * 50)
    print("Prompt-Beispiele: Gut vs. Schlecht")
    print("=" * 50)

    # Beispiel 1: Durchschnitt
    print("\n--- Beispiel 1: Durchschnitt ---")
    noten = [5.5, 4.0, 6.0, 5.0, 4.5]
    print(f"Noten: {noten}")
    print(f"Durchschnitt: {berechne_durchschnitt(noten):.2f}")
    print(f"Leere Liste: {berechne_durchschnitt([])}")

    # Beispiel 2: Wörter zählen
    print("\n--- Beispiel 2: Wörter zählen ---")
    text = "Python ist toll und Python macht Spass und Python ist einfach"
    ergebnis = zaehle_woerter(text)
    for wort, anzahl in ergebnis.items():
        print(f"  '{wort}': {anzahl}x")

    # Beispiel 3: Gerade Zahlen filtern
    print("\n--- Beispiel 3: Gerade Zahlen ---")
    alle_zahlen = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    gerade = filtere_gerade_zahlen(alle_zahlen)
    print(f"Alle Zahlen: {alle_zahlen}")
    print(f"Gerade Zahlen: {gerade}")

    # Beispiel 4: E-Mail prüfen
    print("\n--- Beispiel 4: E-Mail-Validierung ---")
    test_emails = ["anna@example.com", "ungueltig", "test@", "@domain.ch"]
    for email in test_emails:
        gueltig, nachricht = pruefe_email(email)
        symbol = "✅" if gueltig else "❌"
        print(f"  {symbol} '{email}': {nachricht}")

    # Beispiel 5: Tabelle anzeigen
    print("\n--- Beispiel 5: Formatierte Tabelle ---")
    personen = [
        {"name": "Anna Müller", "alter": 28, "stadt": "Zürich"},
        {"name": "Max Meier", "alter": 35, "stadt": "Bern"},
        {"name": "Lisa Weber", "alter": 22, "stadt": "Basel"},
    ]
    zeige_tabelle(personen)

    print("\n" + "=" * 50)
    print("Fazit: Spezifische Prompts → besserer Code!")
    print("=" * 50)
