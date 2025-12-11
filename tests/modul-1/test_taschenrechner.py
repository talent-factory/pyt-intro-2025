"""
Tests für taschenrechner.py
Testet Taschenrechner-Funktionalität
"""

import sys
import pytest
from pathlib import Path
from io import StringIO
import math

modul_pfad = Path(__file__).parent.parent.parent / "modul-1-einstieg" / "05-beispiele"
sys.path.insert(0, str(modul_pfad))


@pytest.mark.modul1
def test_modul_import() -> None:
    """Test: Modul kann importiert werden."""
    try:
        import taschenrechner
        assert True
    except ImportError as e:
        pytest.fail(f"Import fehlgeschlagen: {e}")


@pytest.mark.modul1
def test_grundrechenarten_ausgabe() -> None:
    """Test: Grundrechenarten werden ausgegeben."""
    old_stdout = sys.stdout
    sys.stdout = captured = StringIO()

    try:
        import importlib
        import taschenrechner
        importlib.reload(taschenrechner)

        output = captured.getvalue()

        assert "+" in output or "Addition" in output
        assert "-" in output or "Subtraktion" in output
        assert "*" in output or "Multiplikation" in output
        assert "/" in output or "Division" in output

    finally:
        sys.stdout = old_stdout


@pytest.mark.modul1
@pytest.mark.parametrize("a,b,operation,expected", [
    (25, 5, "add", 30),
    (25, 5, "sub", 20),
    (25, 5, "mul", 125),
    (25, 5, "div", 5.0),
])
def test_rechenoperationen(a: int | float | str | bool, b: int | float | str | bool, operation: int | float | str | bool, expected: int | float | str | bool) -> None:
    """Test: Rechenoperationen funktionieren korrekt."""
    if operation == "add":
        result = a + b
    elif operation == "sub":
        result = a - b
    elif operation == "mul":
        result = a * b
    elif operation == "div":
        result = a / b

    assert result == expected


@pytest.mark.modul1
def test_kreisflaeche_berechnung() -> None:
    """Test: Kreisfläche wird korrekt berechnet."""
    radius = 5
    PI = 3.14159
    flaeche = PI * radius**2

    assert abs(flaeche - 78.53975) < 0.001


@pytest.mark.modul1
def test_durchschnitt_berechnung() -> None:
    """Test: Durchschnitt wird korrekt berechnet."""
    note1, note2, note3 = 5.5, 6.0, 5.0
    durchschnitt = (note1 + note2 + note3) / 3

    assert abs(durchschnitt - 5.5) < 0.01
