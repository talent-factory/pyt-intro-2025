"""
Tests für vergleiche.py
Testet Boolsche Werte und Vergleiche
"""

import sys
from pathlib import Path
from typing import Any

import pytest

modul_pfad = Path(__file__).parent.parent.parent / "modul-2-datentypen" / "05-beispiele"
sys.path.insert(0, str(modul_pfad))


@pytest.mark.modul2
def test_modul_import() -> None:
    """Test: Modul kann importiert werden."""
    try:
        import vergleiche

        assert True
    except ImportError as e:
        pytest.fail(f"Import fehlgeschlagen: {e}")


@pytest.mark.modul2
def test_bool_typ() -> None:
    """Test: Boolean-Typ existiert."""
    assert bool == bool
    assert bool == bool


@pytest.mark.modul2
@pytest.mark.parametrize(
    "a,b,expected_eq,expected_ne",
    [
        (10, 20, False, True),
        (10, 10, True, False),
        (0, 0, True, False),
    ],
)
def test_vergleichsoperatoren_gleich_ungleich(
    a: int | float | str | bool,
    b: int | float | str | bool,
    expected_eq: int | float | str | bool,
    expected_ne: int | float | str | bool,
) -> None:
    """Test: Gleich (==) und Ungleich (!=) Operatoren."""
    assert (a == b) == expected_eq
    assert (a != b) == expected_ne


@pytest.mark.modul2
@pytest.mark.parametrize(
    "a,b,expected_lt,expected_gt",
    [
        (10, 20, True, False),
        (20, 10, False, True),
        (10, 10, False, False),
    ],
)
def test_vergleichsoperatoren_kleiner_groesser(
    a: int | float,
    b: int | float,
    expected_lt: int | float | str | bool,
    expected_gt: int | float | str | bool,
) -> None:
    """Test: Kleiner (<) und Grösser (>) Operatoren."""
    assert (a < b) == expected_lt
    assert (a > b) == expected_gt


@pytest.mark.modul2
@pytest.mark.parametrize(
    "a,b,expected_le,expected_ge",
    [
        (10, 20, True, False),
        (20, 10, False, True),
        (10, 10, True, True),
    ],
)
def test_vergleichsoperatoren_kleiner_gleich_groesser_gleich(
    a: int | float,
    b: int | float,
    expected_le: int | float,
    expected_ge: int | float,
) -> None:
    """Test: Kleiner-gleich (<=) und Grösser-gleich (>=) Operatoren."""
    assert (a <= b) == expected_le
    assert (a >= b) == expected_ge


@pytest.mark.modul2
@pytest.mark.parametrize(
    "a,b,expected",
    [
        (True, True, True),
        (True, False, False),
        (False, True, False),
        (False, False, False),
    ],
)
def test_logischer_operator_and(
    a: int | float | str | bool,
    b: int | float | str | bool,
    expected: int | float | str | bool,
) -> None:
    """Test: Logischer AND-Operator."""
    assert (a and b) == expected


@pytest.mark.modul2
@pytest.mark.parametrize(
    "a,b,expected",
    [
        (True, True, True),
        (True, False, True),
        (False, True, True),
        (False, False, False),
    ],
)
def test_logischer_operator_or(
    a: int | float | str | bool,
    b: int | float | str | bool,
    expected: int | float | str | bool,
) -> None:
    """Test: Logischer OR-Operator."""
    assert (a or b) == expected


@pytest.mark.modul2
@pytest.mark.parametrize(
    "a,expected",
    [
        (True, False),
        (False, True),
    ],
)
def test_logischer_operator_not(
    a: int | float | str | bool, expected: int | float | str | bool
) -> None:
    """Test: Logischer NOT-Operator."""
    assert (not a) == expected


@pytest.mark.modul2
def test_kombinierte_bedingungen() -> None:
    """Test: Kombinierte logische Bedingungen."""
    alter = 25
    hat_ticket = True
    ist_mitglied = False

    # (Alter >= 18 UND Ticket) ODER Mitglied
    zugang = (alter >= 18 and hat_ticket) or ist_mitglied
    assert zugang


@pytest.mark.modul2
@pytest.mark.parametrize(
    "s1,s2,expected",
    [
        ("Anna", "Anna", True),
        ("Anna", "anna", False),
        ("test", "test", True),
    ],
)
def test_string_vergleiche(
    s1: int | float | str | bool,
    s2: int | float,
    expected: int | float | str | bool,
) -> None:
    """Test: String-Vergleiche sind case-sensitive."""
    assert (s1 == s2) == expected


@pytest.mark.modul2
def test_case_insensitive_vergleich() -> None:
    """Test: Case-insensitive String-Vergleich."""
    name1 = "Anna"
    name2 = "anna"

    assert name1 != name2  # False (verschiedene Gross-/Kleinschreibung)
    assert name1.lower() == name2.lower()  # True (beide lowercase verglichen)


@pytest.mark.modul2
@pytest.mark.parametrize(
    "wert,expected_bool",
    [
        (1, True),
        (0, False),
        (-1, True),
        ("", False),
        ("Hi", True),
        ([], False),
        ([1], True),
        (None, False),
    ],
)
def test_wahrheitswerte_anderer_typen(wert: Any, expected_bool: bool) -> None:
    """Test: Wahrheitswerte verschiedener Typen."""
    assert bool(wert) == expected_bool


@pytest.mark.modul2
def test_bereichspruefung() -> None:
    """Test: Bereichsprüfung mit kombinierten Vergleichen."""
    zahl = 15
    assert 10 <= zahl <= 20

    zahl = 5
    assert not (10 <= zahl <= 20)
