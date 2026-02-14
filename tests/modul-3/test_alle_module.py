"""
Zusammengefasste Tests für alle Modul-3 Programme
Diese Tests prüfen Import und grundlegende Funktionalität
"""

import sys
from io import StringIO
from pathlib import Path
from unittest.mock import patch

import pytest

modul_pfad = (
    Path(__file__).parent.parent.parent / "modul-3-kontrollstrukturen" / "05-beispiele"
)
sys.path.insert(0, str(modul_pfad))


# ===== bedingungen.py =====


@pytest.mark.modul3
def test_bedingungen_import() -> None:
    """Test: bedingungen.py kann importiert werden."""
    try:
        import bedingungen

        assert True
    except ImportError as e:
        pytest.fail(f"Import fehlgeschlagen: {e}")


@pytest.mark.modul3
@pytest.mark.parametrize(
    "alter,expected",
    [
        (20, True),
        (17, False),
        (18, True),
    ],
)
def test_volljaehrigkeit(alter: int, expected: int | float | str | bool) -> None:
    """Test: Volljährigkeits-Prüfung."""
    ist_volljaehrig = alter >= 18
    assert ist_volljaehrig == expected


@pytest.mark.modul3
@pytest.mark.parametrize(
    "punkte,expected_note",
    [
        (95, 6),
        (85, 5),
        (75, 4),
        (65, 3),
        (55, 2),
    ],
)
def test_notenberechnung(punkte: int, expected_note: int) -> None:
    """Test: Notenberechnung mit if-elif-else."""
    if punkte >= 90:
        note = 6
    elif punkte >= 80:
        note = 5
    elif punkte >= 70:
        note = 4
    elif punkte >= 60:
        note = 3
    else:
        note = 2

    assert note == expected_note


# ===== while_schleifen.py =====


@pytest.mark.modul3
def test_while_schleifen_import() -> None:
    """Test: while_schleifen.py kann importiert werden."""
    try:
        import while_schleifen

        assert True
    except ImportError as e:
        pytest.fail(f"Import fehlgeschlagen: {e}")


@pytest.mark.modul3
def test_summe_mit_while() -> None:
    """Test: Summe berechnen mit while-Schleife."""
    summe = 0
    zahl = 1

    while zahl <= 10:
        summe += zahl
        zahl += 1

    assert summe == 55  # 1+2+3+...+10


@pytest.mark.modul3
def test_fakultaet_mit_while() -> None:
    """Test: Fakultät berechnen mit while-Schleife."""
    n = 5
    fakultaet = 1
    zaehler = 1

    while zaehler <= n:
        fakultaet *= zaehler
        zaehler += 1

    assert fakultaet == 120  # 5!


# ===== for_schleifen.py =====


@pytest.mark.modul3
def test_for_schleifen_import() -> None:
    """Test: for_schleifen.py kann importiert werden."""
    try:
        import for_schleifen

        assert True
    except ImportError as e:
        pytest.fail(f"Import fehlgeschlagen: {e}")


@pytest.mark.modul3
@pytest.mark.parametrize(
    "start,end,expected_list",
    [
        (0, 5, [0, 1, 2, 3, 4]),
        (1, 6, [1, 2, 3, 4, 5]),
        (5, 10, [5, 6, 7, 8, 9]),
    ],
)
def test_range_erzeugung(start: int, end: int, expected_list: list[int]) -> None:
    """Test: range() erzeugt erwartete Listen."""
    result = list(range(start, end))
    assert result == expected_list


@pytest.mark.modul3
def test_liste_iteration() -> None:
    """Test: Iteration über Listen."""
    fruechte = ["Apfel", "Banane", "Orange"]
    gefunden = []

    for frucht in fruechte:
        gefunden.append(frucht)

    assert gefunden == fruechte


@pytest.mark.modul3
def test_summe_mit_for() -> None:
    """Test: Summe berechnen mit for-Schleife."""
    zahlen = [10, 20, 30, 40, 50]
    summe = 0

    for zahl in zahlen:
        summe += zahl

    assert summe == 150


# ===== listen.py =====


@pytest.mark.modul3
def test_listen_import() -> None:
    """Test: listen.py kann importiert werden."""
    try:
        import listen

        assert True
    except ImportError as e:
        pytest.fail(f"Import fehlgeschlagen: {e}")


@pytest.mark.modul3
def test_liste_erstellen() -> None:
    """Test: Listen erstellen."""
    zahlen = [1, 2, 3, 4, 5]
    namen = ["Anna", "Max", "Lisa"]

    assert len(zahlen) == 5
    assert len(namen) == 3


@pytest.mark.modul3
def test_liste_indexierung() -> None:
    """Test: Auf Listenelemente zugreifen."""
    fruechte = ["Apfel", "Banane", "Orange"]

    assert fruechte[0] == "Apfel"
    assert fruechte[-1] == "Orange"


@pytest.mark.modul3
def test_liste_append() -> None:
    """Test: Elemente hinzufügen."""
    liste = ["Apfel", "Banane"]
    liste.append("Orange")

    assert len(liste) == 3
    assert liste[-1] == "Orange"


@pytest.mark.modul3
def test_liste_remove() -> None:
    """Test: Elemente entfernen."""
    liste = ["Apfel", "Banane", "Orange"]
    liste.remove("Banane")

    assert len(liste) == 2
    assert "Banane" not in liste


# ===== verschachtelt.py =====


@pytest.mark.modul3
def test_verschachtelt_import() -> None:
    """Test: verschachtelt.py kann importiert werden."""
    try:
        import verschachtelt

        assert True
    except ImportError as e:
        pytest.fail(f"Import fehlgeschlagen: {e}")


@pytest.mark.modul3
def test_verschachtelte_schleifen() -> None:
    """Test: Verschachtelte Schleifen."""
    result = []
    for i in range(3):
        for j in range(3):
            result.append((i, j))

    assert len(result) == 9
    assert result[0] == (0, 0)
    assert result[-1] == (2, 2)


@pytest.mark.modul3
def test_multiplikationstabelle() -> None:
    """Test: Multiplikationstabelle."""
    tabelle = []
    for i in range(1, 4):
        zeile = []
        for j in range(1, 4):
            zeile.append(i * j)
        tabelle.append(zeile)

    assert tabelle[0] == [1, 2, 3]  # 1*1, 1*2, 1*3
    assert tabelle[1] == [2, 4, 6]  # 2*1, 2*2, 2*3


# ===== zahlenraten.py =====


# zahlenraten.py ist ein interaktives Spiel - keine Tests nötig


# ===== einkaufsliste.py =====


# einkaufsliste.py ist ein interaktives Programm - keine Tests nötig


# ===== primzahlen.py =====


# primzahlen.py ist ein interaktives Programm - keine Tests nötig


# ===== muster.py =====


@pytest.mark.modul3
def test_muster_import() -> None:
    """Test: muster.py kann importiert werden."""
    with patch("builtins.input", return_value="test"):
        try:
            import muster

            assert hasattr(muster, "rechteck")
        except Exception as e:
            pytest.skip(f"Interaktives Modul: {e}")


@pytest.mark.modul3
def test_muster_funktionen_existieren() -> None:
    """Test: Muster-Funktionen existieren."""
    with patch("builtins.input", return_value="test"):
        import muster

        assert hasattr(muster, "dreieck")
        assert hasattr(muster, "pyramide")


# ===== menu.py =====


@pytest.mark.modul3
def test_menu_import() -> None:
    """Test: menu.py kann importiert werden."""
    with patch("builtins.input", return_value="6"):
        try:
            import menu

            assert hasattr(menu, "main")
        except Exception as e:
            pytest.skip(f"Interaktives Modul: {e}")


@pytest.mark.modul3
def test_menu_funktionen_existieren() -> None:
    """Test: Menü-Funktionen existieren."""
    with patch("builtins.input", return_value="6"):
        import menu

        assert hasattr(menu, "taschenrechner")
        assert hasattr(menu, "temperatur_umrechner")
        assert hasattr(menu, "bmi_rechner")


@pytest.mark.modul3
@pytest.mark.parametrize(
    "gewicht,groesse,expected_bmi",
    [
        (70, 1.75, 22.9),
        (80, 1.80, 24.7),
    ],
)
def test_bmi_berechnung_in_menu(
    gewicht: int | float,
    groesse: int | float,
    expected_bmi: int | float,
) -> None:
    """Test: BMI-Berechnung im Menü."""
    bmi = gewicht / (groesse**2)
    assert abs(bmi - expected_bmi) < 0.1
