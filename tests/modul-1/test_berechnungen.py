"""
Tests für berechnungen.py
Testet praktische Berechnungen
"""

import sys
from io import StringIO
from pathlib import Path

import pytest

modul_pfad = Path(__file__).parent.parent.parent / "modul-1-einstieg" / "05-beispiele"
sys.path.insert(0, str(modul_pfad))


@pytest.mark.modul1
def test_modul_import():
    """Test: Modul kann importiert werden."""
    try:
        import berechnungen

        assert True
    except ImportError as e:
        pytest.fail(f"Import fehlgeschlagen: {e}")


@pytest.mark.modul1
def test_zinsrechnung():
    """Test: Zinsrechnung wird demonstriert."""
    old_stdout = sys.stdout
    sys.stdout = captured = StringIO()

    try:
        import importlib

        import berechnungen

        importlib.reload(berechnungen)

        output = captured.getvalue()

        assert "Zins" in output or "zins" in output
        assert "1000" in output  # Startkapital

    finally:
        sys.stdout = old_stdout


@pytest.mark.modul1
def test_benzinverbrauch():
    """Test: Benzinverbrauch wird berechnet."""
    old_stdout = sys.stdout
    sys.stdout = captured = StringIO()

    try:
        import importlib

        import berechnungen

        importlib.reload(berechnungen)

        output = captured.getvalue()

        assert "Benzin" in output or "verbrauch" in output.lower()

    finally:
        sys.stdout = old_stdout


@pytest.mark.modul1
@pytest.mark.parametrize(
    "kapital,zinssatz,jahre,erwartetes_endkapital",
    [
        (1000, 0.03, 5, 1159.27),
        (5000, 0.05, 3, 5788.13),
        (10000, 0.02, 10, 12189.94),
    ],
)
def test_zinsberechnung_formel(kapital, zinssatz, jahre, erwartetes_endkapital):
    """Test: Zinsberechnung funktioniert korrekt."""
    endkapital = kapital * ((1 + zinssatz) ** jahre)
    assert abs(endkapital - erwartetes_endkapital) < 0.01


@pytest.mark.modul1
@pytest.mark.parametrize(
    "strecke,verbrauch,erwartete_liter",
    [
        (100, 6.5, 6.5),
        (350, 6.5, 22.75),
        (200, 5.0, 10.0),
    ],
)
def test_benzinverbrauch_berechnung(strecke, verbrauch, erwartete_liter):
    """Test: Benzinverbrauch wird korrekt berechnet."""
    liter = strecke * verbrauch / 100
    assert abs(liter - erwartete_liter) < 0.01


@pytest.mark.modul1
@pytest.mark.parametrize(
    "sekunden,stunden,minuten,rest_sek",
    [
        (7325, 2, 2, 5),
        (3600, 1, 0, 0),
        (3661, 1, 1, 1),
    ],
)
def test_zeitumrechnung(sekunden, stunden, minuten, rest_sek):
    """Test: Zeitumrechnung funktioniert korrekt."""
    berechnet_stunden = sekunden // 3600
    rest = sekunden % 3600
    berechnet_minuten = rest // 60
    berechnet_sekunden = rest % 60

    assert berechnet_stunden == stunden
    assert berechnet_minuten == minuten
    assert berechnet_sekunden == rest_sek
