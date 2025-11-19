"""
Tests für vergleiche.py
Testet Boolsche Werte und Vergleiche
"""

import sys
import pytest
from pathlib import Path

modul_pfad = Path(__file__).parent.parent.parent / "modul-2-datentypen" / "05-beispiele"
sys.path.insert(0, str(modul_pfad))


@pytest.mark.modul2
def test_modul_import():
    """Test: Modul kann importiert werden."""
    try:
        import vergleiche
        assert True
    except ImportError as e:
        pytest.fail(f"Import fehlgeschlagen: {e}")


@pytest.mark.modul2
def test_bool_typ():
    """Test: Boolean-Typ existiert."""
    assert type(True) == bool
    assert type(False) == bool


@pytest.mark.modul2
@pytest.mark.parametrize("a,b,expected_eq,expected_ne", [
    (10, 20, False, True),
    (10, 10, True, False),
    (0, 0, True, False),
])
def test_vergleichsoperatoren_gleich_ungleich(a, b, expected_eq, expected_ne):
    """Test: Gleich (==) und Ungleich (!=) Operatoren."""
    assert (a == b) == expected_eq
    assert (a != b) == expected_ne


@pytest.mark.modul2
@pytest.mark.parametrize("a,b,expected_lt,expected_gt", [
    (10, 20, True, False),
    (20, 10, False, True),
    (10, 10, False, False),
])
def test_vergleichsoperatoren_kleiner_groesser(a, b, expected_lt, expected_gt):
    """Test: Kleiner (<) und Grösser (>) Operatoren."""
    assert (a < b) == expected_lt
    assert (a > b) == expected_gt


@pytest.mark.modul2
@pytest.mark.parametrize("a,b,expected_le,expected_ge", [
    (10, 20, True, False),
    (20, 10, False, True),
    (10, 10, True, True),
])
def test_vergleichsoperatoren_kleiner_gleich_groesser_gleich(a, b, expected_le, expected_ge):
    """Test: Kleiner-gleich (<=) und Grösser-gleich (>=) Operatoren."""
    assert (a <= b) == expected_le
    assert (a >= b) == expected_ge


@pytest.mark.modul2
@pytest.mark.parametrize("a,b,expected", [
    (True, True, True),
    (True, False, False),
    (False, True, False),
    (False, False, False),
])
def test_logischer_operator_and(a, b, expected):
    """Test: Logischer AND-Operator."""
    assert (a and b) == expected


@pytest.mark.modul2
@pytest.mark.parametrize("a,b,expected", [
    (True, True, True),
    (True, False, True),
    (False, True, True),
    (False, False, False),
])
def test_logischer_operator_or(a, b, expected):
    """Test: Logischer OR-Operator."""
    assert (a or b) == expected


@pytest.mark.modul2
@pytest.mark.parametrize("a,expected", [
    (True, False),
    (False, True),
])
def test_logischer_operator_not(a, expected):
    """Test: Logischer NOT-Operator."""
    assert (not a) == expected


@pytest.mark.modul2
def test_kombinierte_bedingungen():
    """Test: Kombinierte logische Bedingungen."""
    alter = 25
    hat_ticket = True
    ist_mitglied = False

    # (Alter >= 18 UND Ticket) ODER Mitglied
    zugang = (alter >= 18 and hat_ticket) or ist_mitglied
    assert zugang == True


@pytest.mark.modul2
@pytest.mark.parametrize("s1,s2,expected", [
    ("Anna", "Anna", True),
    ("Anna", "anna", False),
    ("test", "test", True),
])
def test_string_vergleiche(s1, s2, expected):
    """Test: String-Vergleiche sind case-sensitive."""
    assert (s1 == s2) == expected


@pytest.mark.modul2
def test_case_insensitive_vergleich():
    """Test: Case-insensitive String-Vergleich."""
    name1 = "Anna"
    name2 = "anna"

    assert name1 != name2  # False (verschiedene Gross-/Kleinschreibung)
    assert name1.lower() == name2.lower()  # True (beide lowercase verglichen)


@pytest.mark.modul2
@pytest.mark.parametrize("wert,expected_bool", [
    (1, True),
    (0, False),
    (-1, True),
    ("", False),
    ("Hi", True),
    ([], False),
    ([1], True),
    (None, False),
])
def test_wahrheitswerte_anderer_typen(wert, expected_bool):
    """Test: Wahrheitswerte verschiedener Typen."""
    assert bool(wert) == expected_bool


@pytest.mark.modul2
def test_bereichspruefung():
    """Test: Bereichsprüfung mit kombinierten Vergleichen."""
    zahl = 15
    assert 10 <= zahl <= 20

    zahl = 5
    assert not (10 <= zahl <= 20)
