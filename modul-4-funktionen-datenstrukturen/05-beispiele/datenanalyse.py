"""
Beispiel: Datenanalyse

Analysiert eine feste Liste von Tagestemperaturen und eine Liste
von Messungen (Dictionaries) mit eigenen Funktionen:
- Minimum, Maximum, Durchschnitt, Median
- Zählen (wie viele Werte über einem Grenzwert)
- Häufigkeiten pro Ort mit einem Dictionary

Das Programm läuft mit festen Daten (keine Eingaben nötig).
"""


def minimum(werte: list) -> float:
    """
    Findet den kleinsten Wert einer Liste.

    Args:
        werte: Liste von Zahlen (nicht leer)

    Returns:
        Kleinster Wert
    """
    kleinster = werte[0]
    for wert in werte:
        if wert < kleinster:
            kleinster = wert
    return kleinster


def maximum(werte: list) -> float:
    """
    Findet den grössten Wert einer Liste.

    Args:
        werte: Liste von Zahlen (nicht leer)

    Returns:
        Grösster Wert
    """
    groesster = werte[0]
    for wert in werte:
        if wert > groesster:
            groesster = wert
    return groesster


def mittelwert(werte: list) -> float:
    """
    Berechnet den Durchschnitt einer Liste.

    Args:
        werte: Liste von Zahlen (nicht leer)

    Returns:
        Durchschnitt als float
    """
    summe = 0
    for wert in werte:
        summe += wert
    return summe / len(werte)


def median(werte: list) -> float:
    """
    Berechnet den Median (mittlerer Wert der sortierten Liste).

    Args:
        werte: Liste von Zahlen (nicht leer)

    Returns:
        Median als float
    """
    sortiert = sorted(werte)
    anzahl = len(sortiert)
    mitte = anzahl // 2

    if anzahl % 2 == 1:
        return sortiert[mitte]
    return (sortiert[mitte - 1] + sortiert[mitte]) / 2


def zaehle_ueber(werte: list, grenze: float) -> int:
    """
    Zählt, wie viele Werte über einer Grenze liegen.

    Args:
        werte: Liste von Zahlen
        grenze: Grenzwert (der Wert selbst zählt nicht mit)

    Returns:
        Anzahl Werte grösser als die Grenze
    """
    anzahl = 0
    for wert in werte:
        if wert > grenze:
            anzahl += 1
    return anzahl


def zaehle_pro_ort(messungen: list) -> dict:
    """
    Zählt, wie viele Messungen es pro Ort gibt.

    Args:
        messungen: Liste von Dictionaries mit Schlüssel "ort"

    Returns:
        Dictionary Ort -> Anzahl
    """
    zaehler = {}
    for messung in messungen:
        ort = messung["ort"]
        if ort in zaehler:
            zaehler[ort] += 1
        else:
            zaehler[ort] = 1
    return zaehler


def durchschnitt_pro_ort(messungen: list) -> dict:
    """
    Berechnet die Durchschnittstemperatur pro Ort.

    Args:
        messungen: Liste von Dictionaries mit "ort" und "temperatur"

    Returns:
        Dictionary Ort -> Durchschnittstemperatur
    """
    temperaturen_pro_ort = {}
    for messung in messungen:
        ort = messung["ort"]
        if ort not in temperaturen_pro_ort:
            temperaturen_pro_ort[ort] = []
        temperaturen_pro_ort[ort].append(messung["temperatur"])

    durchschnitte = {}
    for ort in temperaturen_pro_ort:
        durchschnitte[ort] = mittelwert(temperaturen_pro_ort[ort])
    return durchschnitte


if __name__ == "__main__":
    print("=" * 40)
    print("DEMO: DATENANALYSE")
    print("=" * 40)

    # Teil 1: Einfache Zahlenliste (Tagestemperaturen einer Woche)
    temperaturen = [14.5, 17.0, 12.5, 19.0, 21.5, 16.0, 18.5]

    print("\n--- Tagestemperaturen ---")
    print(f"Werte:        {temperaturen}")
    print(f"Anzahl:       {len(temperaturen)}")
    print(f"Minimum:      {minimum(temperaturen)}")
    print(f"Maximum:      {maximum(temperaturen)}")
    print(f"Mittelwert:   {mittelwert(temperaturen):.2f}")
    print(f"Median:       {median(temperaturen)}")
    print(f"Über 18 Grad: {zaehle_ueber(temperaturen, 18)} Tage")

    # Teil 2: Liste von Dictionaries (Messungen an verschiedenen Orten)
    messungen = [
        {"ort": "Zürich", "temperatur": 15.0},
        {"ort": "Bern", "temperatur": 14.0},
        {"ort": "Zürich", "temperatur": 17.0},
        {"ort": "Basel", "temperatur": 18.0},
        {"ort": "Bern", "temperatur": 16.0},
        {"ort": "Zürich", "temperatur": 16.0},
    ]

    print("\n--- Messungen pro Ort ---")
    anzahl_pro_ort = zaehle_pro_ort(messungen)
    for ort in anzahl_pro_ort:
        print(f"{ort}: {anzahl_pro_ort[ort]} Messungen")

    print("\n--- Durchschnitt pro Ort ---")
    schnitt_pro_ort = durchschnitt_pro_ort(messungen)
    for ort in schnitt_pro_ort:
        print(f"{ort}: {schnitt_pro_ort[ort]:.1f} Grad")
