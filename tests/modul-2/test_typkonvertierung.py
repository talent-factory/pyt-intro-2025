"""
Tests für typkonvertierung.py
Testet Typkonvertierung zwischen verschiedenen Datentypen
"""

import sys
import pytest
from pathlib import Path

modul_pfad = Path(__file__).parent.parent.parent / "modul-2-datentypen" / "05-beispiele"
sys.path.insert(0, str(modul_pfad))


@pytest.mark.modul2
def test_modul_import() -> None:
    """Test: Modul kann importiert werden."""
    try:
        import typkonvertierung
        assert True
    except ImportError as e:
        pytest.fail(f"Import fehlgeschlagen: {e}")


@pytest.mark.modul2
@pytest.mark.parametrize("string_zahl,expected_int", [
    ("42", 42),
    ("0", 0),
    ("-10", -10),
    ("999", 999),
])
def test_string_zu_int(string_zahl: int | float | str | bool, expected_int: int | float | str | bool) -> None:
    """Test: String zu Integer Konvertierung."""
    result = int(string_zahl)
    assert result == expected_int
    assert type(result) == int


@pytest.mark.modul2
@pytest.mark.parametrize("string_zahl,expected_float", [
    ("3.14", 3.14),
    ("19.99", 19.99),
    ("0.0", 0.0),
    ("-2.5", -2.5),
])
def test_string_zu_float(string_zahl: int | float | str | bool, expected_float: int | float | str | bool) -> None:
    """Test: String zu Float Konvertierung."""
    result = float(string_zahl)
    assert abs(result - expected_float) < 0.001
    assert type(result) == float


@pytest.mark.modul2
@pytest.mark.parametrize("zahl,expected_string", [
    (42, "42"),
    (0, "0"),
    (-10, "-10"),
    (3.14, "3.14"),
])
def test_zahl_zu_string(zahl: int | float | str | bool, expected_string: int | float | str | bool) -> None:
    """Test: Zahl zu String Konvertierung."""
    result = str(zahl)
    assert result == expected_string
    assert type(result) == str


@pytest.mark.modul2
def test_string_konkatenation_ohne_konvertierung() -> None:
    """Test: String-Konkatenation ohne Typkonvertierung."""
    zahl1_str = "10"
    zahl2_str = "20"

    # Ohne Konvertierung: String-Konkatenation
    result = zahl1_str + zahl2_str
    assert result == "1020"


@pytest.mark.modul2
def test_addition_mit_konvertierung() -> None:
    """Test: Addition nach Typkonvertierung."""
    zahl1_str = "10"
    zahl2_str = "20"

    # Mit Konvertierung: Addition
    zahl1 = int(zahl1_str)
    zahl2 = int(zahl2_str)
    result = zahl1 + zahl2

    assert result == 30


@pytest.mark.modul2
@pytest.mark.parametrize("float_zahl,expected_int", [
    (3.14159, 3),
    (19.99, 19),
    (5.9, 5),
    (-2.7, -2),
])
def test_float_zu_int(float_zahl: int | float | str | bool, expected_int: int | float | str | bool) -> None:
    """Test: Float zu Int (Nachkommastellen werden abgeschnitten)."""
    result = int(float_zahl)
    assert result == expected_int


@pytest.mark.modul2
@pytest.mark.parametrize("int_zahl,expected_float", [
    (42, 42.0),
    (0, 0.0),
    (-10, -10.0),
])
def test_int_zu_float(int_zahl: int | float | str | bool, expected_float: int | float | str | bool) -> None:
    """Test: Int zu Float Konvertierung."""
    result = float(int_zahl)
    assert result == expected_float
    assert type(result) == float


@pytest.mark.modul2
@pytest.mark.parametrize("wert,expected_bool", [
    (1, True),
    (0, False),
    (-1, True),
    (42, True),
    ("", False),
    ("Hi", True),
    ("0", True),  # Nicht-leerer String ist True!
    ("False", True),  # Nicht-leerer String ist True!
])
def test_zu_boolean(wert: int | float | str | bool, expected_bool: int | float | str | bool) -> None:
    """Test: Konvertierung zu Boolean."""
    result = bool(wert)
    assert result == expected_bool


@pytest.mark.modul2
def test_fehlerhafte_konvertierung_int() -> None:
    """Test: Fehlerhafte String zu Int Konvertierung."""
    with pytest.raises(ValueError):
        int("Hallo")

    with pytest.raises(ValueError):
        int("3.14")  # Direkt nicht möglich!


@pytest.mark.modul2
def test_fehlerhafte_konvertierung_float() -> None:
    """Test: Fehlerhafte String zu Float Konvertierung."""
    with pytest.raises(ValueError):
        float("abc")


@pytest.mark.modul2
def test_float_string_zu_int_korrekt() -> None:
    """Test: Korrekte Konvertierung von Float-String zu Int."""
    preis_str = "19.99"

    # Über float() als Zwischenschritt
    preis_float = float(preis_str)
    preis_int = int(preis_float)

    assert preis_int == 19


@pytest.mark.modul2
def test_typ_ermitteln() -> None:
    """Test: type() ermittelt den Typ korrekt."""
    assert type(42) == int
    assert type(3.14) == float
    assert type("Hallo") == str
    assert type(True) == bool
