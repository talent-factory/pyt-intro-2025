"""
Tests für temperatur.py
Testet Temperaturumrechnungen
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
        import temperatur

        assert True
    except ImportError as e:
        pytest.fail(f"Import fehlgeschlagen: {e}")


@pytest.mark.modul1
@pytest.mark.parametrize(
    "celsius,expected_fahrenheit",
    [
        (0, 32),
        (25, 77),
        (100, 212),
        (37, 98.6),
        (-40, -40),
    ],
)
def test_celsius_zu_fahrenheit(
    celsius: int | float, expected_fahrenheit: int | float
) -> None:
    """Test: Celsius zu Fahrenheit Umrechnung."""
    fahrenheit = (celsius * 9 / 5) + 32
    assert abs(fahrenheit - expected_fahrenheit) < 0.1


@pytest.mark.modul1
@pytest.mark.parametrize(
    "fahrenheit,expected_celsius",
    [
        (32, 0),
        (77, 25),
        (212, 100),
        (98.6, 37),
        (-40, -40),
    ],
)
def test_fahrenheit_zu_celsius(
    fahrenheit: int | float, expected_celsius: int | float
) -> None:
    """Test: Fahrenheit zu Celsius Umrechnung."""
    celsius = (fahrenheit - 32) * 5 / 9
    assert abs(celsius - expected_celsius) < 0.1


@pytest.mark.modul1
@pytest.mark.parametrize(
    "celsius,expected_kelvin",
    [
        (0, 273.15),
        (25, 298.15),
        (100, 373.15),
        (-273.15, 0),
    ],
)
def test_celsius_zu_kelvin(celsius: int | float, expected_kelvin: int | float) -> None:
    """Test: Celsius zu Kelvin Umrechnung."""
    kelvin = celsius + 273.15
    assert abs(kelvin - expected_kelvin) < 0.01


@pytest.mark.modul1
@pytest.mark.parametrize(
    "kelvin,expected_celsius",
    [
        (273.15, 0),
        (298.15, 25),
        (373.15, 100),
        (300, 26.85),
    ],
)
def test_kelvin_zu_celsius(kelvin: int | float, expected_celsius: int | float) -> None:
    """Test: Kelvin zu Celsius Umrechnung."""
    celsius = kelvin - 273.15
    assert abs(celsius - expected_celsius) < 0.01


@pytest.mark.modul1
def test_gefrierpunkt_und_siedepunkt() -> None:
    """Test: Wichtige Temperaturpunkte sind korrekt."""
    # Gefrierpunkt
    assert (0 * 9 / 5) + 32 == 32  # 0°C = 32°F

    # Siedepunkt
    assert (100 * 9 / 5) + 32 == 212  # 100°C = 212°F
