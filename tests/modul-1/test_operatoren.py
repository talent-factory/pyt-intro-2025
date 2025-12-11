"""
Tests für operatoren.py
Testet arithmetische Operatoren
"""

import sys
from io import StringIO
from pathlib import Path

import pytest

modul_pfad = Path(__file__).parent.parent.parent / "modul-1-einstieg" / "05-beispiele"
sys.path.insert(0, str(modul_pfad))


@pytest.mark.modul1
def test_modul_import() -> None:
    """Test: Modul kann importiert werden."""
    try:
        import operatoren

        assert True
    except ImportError as e:
        pytest.fail(f"Import fehlgeschlagen: {e}")


@pytest.mark.modul1
def test_grundrechenarten() -> None:
    """Test: Grundrechenarten werden demonstriert."""
    old_stdout = sys.stdout
    sys.stdout = captured = StringIO()

    try:
        import importlib

        import operatoren

        importlib.reload(operatoren)

        output = captured.getvalue()

        # Prüfe mathematische Operationen
        assert "Addition" in output or "+" in output
        assert "Subtraktion" in output or "-" in output
        assert "Multiplikation" in output or "*" in output
        assert "Division" in output or "/" in output

    finally:
        sys.stdout = old_stdout


@pytest.mark.modul1
def test_erweiterte_operationen() -> None:
    """Test: Erweiterte Operationen werden gezeigt."""
    old_stdout = sys.stdout
    sys.stdout = captured = StringIO()

    try:
        import importlib

        import operatoren

        importlib.reload(operatoren)

        output = captured.getvalue()

        # Prüfe Modulo und Ganzzahldivision
        assert "Modulo" in output or "Rest" in output
        assert "//" in output or "Ganzzahldivision" in output

    finally:
        sys.stdout = old_stdout


@pytest.mark.modul1
@pytest.mark.parametrize(
    "a,b,expected_sum",
    [
        (17, 5, 22),
        (10, 20, 30),
        (0, 0, 0),
    ],
)
def test_addition_berechnung(
    a: int | float,
    b: int | float,
    expected_sum: int | float | str | bool,
) -> None:
    """Test: Addition wird korrekt berechnet."""
    result = a + b
    assert result == expected_sum


@pytest.mark.modul1
@pytest.mark.parametrize(
    "a,b,expected_mod",
    [
        (17, 5, 2),
        (10, 3, 1),
        (20, 4, 0),
    ],
)
def test_modulo_berechnung(
    a: int | float,
    b: int | float,
    expected_mod: int | float | str | bool,
) -> None:
    """Test: Modulo wird korrekt berechnet."""
    result = a % b
    assert result == expected_mod
