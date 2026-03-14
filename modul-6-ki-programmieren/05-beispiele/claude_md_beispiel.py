"""
CLAUDE.md Einfluss auf KI-generierten Code

Dieses Skript demonstriert, wie eine CLAUDE.md-Datei
das Verhalten der KI beim Code-Generieren beeinflusst.

Konzepte:
- CLAUDE.md als Projekt-Konfiguration
- Einfluss auf Namensgebung
- Einfluss auf Code-Stil
- Konsistenz durch Vorgaben
"""


# ============================================================
# OHNE CLAUDE.md: KI verwendet Standard-Englisch
# ============================================================
# Die KI wurde gefragt: "Write a function to calculate the average"
# Ohne CLAUDE.md verwendet die KI englische Namen und minimale Doku.


def calculate_average(numbers):
    """Calculate the average of a list of numbers."""
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)


def is_valid_email(email):
    """Check if email is valid."""
    return "@" in email and "." in email


def find_max(lst):
    """Find maximum value."""
    if not lst:
        return None
    max_val = lst[0]
    for item in lst:
        if item > max_val:
            max_val = item
    return max_val


# ============================================================
# MIT CLAUDE.md: KI folgt den Projektvorgaben
# ============================================================
# Dieselbe Frage, aber mit CLAUDE.md im Projekt.
# Die CLAUDE.md enthielt folgende relevante Regeln:
#
# ┌─────────────────────────────────────────────────────┐
# │ Auszug aus der CLAUDE.md:                           │
# │                                                     │
# │ ## Code-Stil Richtlinien                            │
# │ - Variablennamen: Deutsche Namen, snake_case        │
# │ - Funktionen: Deutsche Namen, snake_case            │
# │ - Kommentare: Deutsch, ausführlich für Lernzwecke   │
# │ - Docstrings: In allen Funktionen/Modulen           │
# │ - Ausgabe: Trennlinien mit print("=" * 40)          │
# │                                                     │
# │ ## Didaktischer Code                                │
# │ - Code-Klarheit > Kompaktheit                       │
# │ - Explizite Schleifen statt Comprehensions          │
# │ - Ausführliche Kommentare                           │
# └─────────────────────────────────────────────────────┘


def berechne_durchschnitt(zahlen):
    """
    Berechnet den Durchschnitt einer Liste von Zahlen.

    Args:
        zahlen: Liste von Zahlen (int oder float)

    Returns:
        float: Durchschnittswert, 0.0 bei leerer Liste
    """
    # Leere Liste abfangen
    if not zahlen:
        return 0.0

    # Summe schrittweise berechnen (didaktisch klar)
    summe = 0.0
    for zahl in zahlen:
        summe += zahl

    # Durchschnitt berechnen und zurückgeben
    durchschnitt = summe / len(zahlen)
    return durchschnitt


def ist_gueltige_email(email):
    """
    Prüft, ob eine E-Mail-Adresse gültig ist.

    Prüft grundlegende Kriterien:
    - Enthält genau ein @-Zeichen
    - Hat Text vor und nach dem @
    - Domain enthält einen Punkt

    Args:
        email: E-Mail-Adresse als String

    Returns:
        bool: True wenn die E-Mail gültig erscheint
    """
    # Prüfung 1: Genau ein @ enthalten
    if email.count("@") != 1:
        return False

    # In Teile aufteilen
    lokaler_teil, domain = email.split("@")

    # Prüfung 2: Beide Teile nicht leer
    if not lokaler_teil or not domain:
        return False

    # Prüfung 3: Domain hat einen Punkt
    if "." not in domain:
        return False

    return True


def finde_maximum(zahlen):
    """
    Findet die grösste Zahl in einer Liste.

    Verwendet eine einfache Schleife statt der
    eingebauten max()-Funktion (didaktisch).

    Args:
        zahlen: Liste von Zahlen

    Returns:
        Die grösste Zahl oder None bei leerer Liste
    """
    # Leere Liste abfangen
    if not zahlen:
        return None

    # Erste Zahl als Startwert nehmen
    maximum = zahlen[0]

    # Alle weiteren Zahlen vergleichen
    for zahl in zahlen:
        if zahl > maximum:
            maximum = zahl

    return maximum


# ============================================================
# Vergleich der Unterschiede
# ============================================================


def zeige_vergleich():
    """Zeigt den direkten Vergleich zwischen den Versionen."""

    print("=" * 55)
    print("Vergleich: Ohne vs. Mit CLAUDE.md")
    print("=" * 55)

    print(
        """
    ┌────────────────┬──────────────────┬──────────────────────┐
    │ Aspekt         │ Ohne CLAUDE.md   │ Mit CLAUDE.md        │
    ├────────────────┼──────────────────┼──────────────────────┤
    │ Sprache        │ Englisch         │ Deutsch              │
    │ Funktionsname  │ calculate_average│ berechne_durchschnitt│
    │ Parameter      │ numbers          │ zahlen               │
    │ Docstring      │ 1 Zeile, EN     │ Mehrzeilig, DE       │
    │ Kommentare     │ Kaum/Keine       │ Ausführlich          │
    │ Fehlerhandling │ Minimal          │ Explizit             │
    │ Code-Stil      │ Kompakt          │ Didaktisch klar      │
    └────────────────┴──────────────────┴──────────────────────┘
    """
    )


# ============================================================
# Beispiel einer CLAUDE.md-Datei
# ============================================================

BEISPIEL_CLAUDE_MD = """
# CLAUDE.md - Projekt-Konfiguration

## Code-Stil
- **Variablennamen:** Deutsche Namen, snake_case
- **Funktionen:** Deutsche Namen, snake_case
- **Kommentare:** Deutsch, ausführlich
- **Docstrings:** In allen Funktionen mit Args und Returns

## Didaktik
- Code-Klarheit wichtiger als Kompaktheit
- Explizite for-Schleifen statt List Comprehensions
- Jeden Schritt kommentieren

## Ausgabe
- Trennlinien: print("=" * 40)
- Titel in Grossbuchstaben
- Leerzeilen zwischen Abschnitten
"""


# ============================================================
# Hauptprogramm
# ============================================================

if __name__ == "__main__":
    print("=" * 55)
    print("CLAUDE.md Einfluss auf KI-Code")
    print("=" * 55)

    # Test-Daten
    test_zahlen = [4.5, 5.0, 6.0, 3.5, 5.5]

    # Ohne CLAUDE.md
    print("\n--- Ohne CLAUDE.md (Englisch, kompakt) ---")
    print(f"calculate_average({test_zahlen})")
    print(f"  → {calculate_average(test_zahlen)}")
    print(f"is_valid_email('test@mail.ch') → {is_valid_email('test@mail.ch')}")
    print(f"find_max({test_zahlen}) → {find_max(test_zahlen)}")

    # Mit CLAUDE.md
    print("\n--- Mit CLAUDE.md (Deutsch, didaktisch) ---")
    print(f"berechne_durchschnitt({test_zahlen})")
    print(f"  → {berechne_durchschnitt(test_zahlen)}")
    print(f"ist_gueltige_email('test@mail.ch') → {ist_gueltige_email('test@mail.ch')}")
    print(f"finde_maximum({test_zahlen}) → {finde_maximum(test_zahlen)}")

    # Vergleich anzeigen
    print()
    zeige_vergleich()

    # CLAUDE.md Beispiel anzeigen
    print("--- Beispiel CLAUDE.md ---")
    print(BEISPIEL_CLAUDE_MD)

    print("=" * 55)
    print("Fazit: CLAUDE.md sorgt für konsistenten Code-Stil!")
    print("=" * 55)
