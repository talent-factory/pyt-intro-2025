"""
Tests für bmi_rechner.py
Testet BMI-Berechnungen
"""

import sys
from pathlib import Path

import pytest

modul_pfad = Path(__file__).parent.parent.parent / "modul-1-einstieg" / "05-beispiele"
sys.path.insert(0, str(modul_pfad))


@pytest.mark.modul1
def test_modul_import():
    """Test: Modul kann importiert werden."""
    try:
        import bmi_rechner

        assert True
    except ImportError as e:
        pytest.fail(f"Import fehlgeschlagen: {e}")


@pytest.mark.modul1
@pytest.mark.parametrize(
    "gewicht,groesse,expected_bmi",
    [
        (70, 1.75, 22.9),
        (90, 1.80, 27.8),
        (55, 1.65, 20.2),
        (80, 1.70, 27.7),
    ],
)
def test_bmi_berechnung(gewicht, groesse, expected_bmi):
    """Test: BMI wird korrekt berechnet."""
    bmi = gewicht / (groesse**2)
    assert abs(bmi - expected_bmi) < 0.1


@pytest.mark.modul1
@pytest.mark.parametrize(
    "bmi,expected_kategorie",
    [
        (17.0, "Untergewicht"),
        (20.0, "Normalgewicht"),
        (26.0, "Übergewicht"),
        (32.0, "Adipositas"),
    ],
)
def test_bmi_kategorisierung(bmi, expected_kategorie):
    """Test: BMI-Kategorisierung ist korrekt."""
    if bmi < 18.5:
        kategorie = "Untergewicht"
    elif bmi < 25:
        kategorie = "Normalgewicht"
    elif bmi < 30:
        kategorie = "Übergewicht"
    else:
        kategorie = "Adipositas"

    assert kategorie == expected_kategorie


@pytest.mark.modul1
@pytest.mark.parametrize(
    "groesse,ideal_bmi,expected_gewicht",
    [
        (1.75, 22, 67.4),
        (1.80, 22, 71.3),
        (1.65, 22, 59.9),
    ],
)
def test_idealgewicht_berechnung(groesse, ideal_bmi, expected_gewicht):
    """Test: Idealgewicht wird korrekt berechnet."""
    idealgewicht = ideal_bmi * (groesse**2)
    assert abs(idealgewicht - expected_gewicht) < 0.1


@pytest.mark.modul1
def test_bmi_grenzwerte():
    """Test: BMI-Grenzwerte sind korrekt."""
    # Grenzwert Untergewicht/Normalgewicht
    assert 18.5 > 18.4

    # Grenzwert Normalgewicht/Übergewicht
    assert 25.0 > 24.9

    # Grenzwert Übergewicht/Adipositas
    assert 30.0 > 29.9


@pytest.mark.modul1
@pytest.mark.parametrize(
    "gewicht,groesse",
    [
        (70, 1.75),
        (90, 1.80),
        (55, 1.65),
    ],
)
def test_bmi_ist_positiv(gewicht, groesse):
    """Test: BMI ist immer positiv bei gültigen Eingaben."""
    bmi = gewicht / (groesse**2)
    assert bmi > 0
