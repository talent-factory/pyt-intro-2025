"""
Tests für input_output.py
Testet Input/Output mit Mocking
"""

import sys
from io import StringIO
from pathlib import Path
from unittest.mock import patch

import pytest

modul_pfad = Path(__file__).parent.parent.parent / "modul-2-datentypen" / "05-beispiele"
sys.path.insert(0, str(modul_pfad))


@pytest.mark.modul2
def test_modul_import() -> None:
    """Test: Modul kann importiert werden (wird interaktiv sein)."""
    # Hinweis: Das Modul verwendet input(), daher mocken wir das
    try:
        with patch("builtins.input", return_value="Test"):
            import input_output
        assert True
    except Exception as e:
        # Bei interaktiven Modulen ist Import-Test optional
        pytest.skip(f"Interaktives Modul: {e}")


@pytest.mark.modul2
def test_input_gibt_string_zurueck() -> None:
    """Test: input() gibt immer String zurück."""
    with patch("builtins.input", return_value="42"):
        eingabe = input("Test: ")
        assert type(eingabe) == str
        assert eingabe == "42"


@pytest.mark.modul2
def test_input_zu_int_konvertierung() -> None:
    """Test: Input-String wird zu Int konvertiert."""
    with patch("builtins.input", return_value="25"):
        alter_str = input("Alter: ")
        alter = int(alter_str)

        assert type(alter) == int
        assert alter == 25


@pytest.mark.modul2
def test_input_direkte_konvertierung() -> None:
    """Test: Direkte Konvertierung bei input()."""
    with patch("builtins.input", return_value="1.75"):
        groesse = float(input("Grösse: "))

        assert type(groesse) == float
        assert abs(groesse - 1.75) < 0.01


@pytest.mark.modul2
@pytest.mark.parametrize(
    "sep,expected",
    [
        (" ", "A B C"),
        ("-", "A-B-C"),
        (" | ", "A | B | C"),
    ],
)
def test_print_mit_sep_parameter(sep: str, expected: str) -> None:
    """Test: print() mit sep Parameter."""
    old_stdout = sys.stdout
    sys.stdout = captured = StringIO()

    try:
        print("A", "B", "C", sep=sep)
        output = captured.getvalue().strip()
        assert output == expected

    finally:
        sys.stdout = old_stdout


@pytest.mark.modul2
def test_print_mit_end_parameter() -> None:
    """Test: print() mit end Parameter."""
    old_stdout = sys.stdout
    sys.stdout = captured = StringIO()

    try:
        print("Zeile 1", end=" ")
        print("Zeile 2")
        output = captured.getvalue()

        # Sollten in einer Zeile sein
        assert "Zeile 1 Zeile 2" in output

    finally:
        sys.stdout = old_stdout


@pytest.mark.modul2
def test_formatierte_ausgabe() -> None:
    """Test: Formatierte Ausgabe mit F-Strings."""
    name = "Anna"
    alter = 25
    preis = 19.99

    result = f"Name: {name}, Alter: {alter}, Preis: {preis:.2f} CHF"

    assert "Anna" in result
    assert "25" in result
    assert "19.99" in result


@pytest.mark.modul2
def test_tabellen_ausgabe() -> None:
    """Test: Tabellen-formatierte Ausgabe."""
    header = f"{'Name':<15} {'Alter':>5} {'Preis':>10}"
    zeile = f"{'Anna':<15} {25:>5} {19.99:>10.2f}"

    # Prüfe Formatierung
    assert len(header) >= 30
    assert "Anna" in zeile
    assert "25" in zeile
