"""
Tests für parameter.py
Testet Funktionen mit Parametern und Rückgabewerten
"""

import sys
from io import StringIO
from pathlib import Path

import pytest

# Modul importieren
modul_pfad = (
    Path(__file__).parent.parent.parent
    / "modul-4-funktionen-datenstrukturen"
    / "05-beispiele"
)
sys.path.insert(0, str(modul_pfad))


@pytest.mark.modul4
def test_modul_kann_importiert_werden():
    """Test: Modul kann ohne Fehler importiert werden."""
    try:
        import parameter

        assert True
    except ImportError as e:
        pytest.fail(f"Import fehlgeschlagen: {e}")


@pytest.mark.modul4
def test_gruesse_funktion():
    """Test: gruesse() gibt Begrüßung mit Namen aus."""
    import parameter

    old_stdout = sys.stdout
    sys.stdout = captured = StringIO()

    try:
        parameter.gruesse("Anna")
        output = captured.getvalue()

        assert "Anna" in output
        assert "Hallo" in output or "hallo" in output

    finally:
        sys.stdout = old_stdout


@pytest.mark.modul4
@pytest.mark.parametrize(
    "a,b,erwartet",
    [
        (5, 3, 8),
        (0, 0, 0),
        (-5, 5, 0),
        (10, 20, 30),
        (100, 200, 300),
    ],
)
def test_addiere_funktion(a, b, erwartet):
    """Test: addiere() berechnet Summe korrekt."""
    import parameter

    result = parameter.addiere(a, b)
    assert result == erwartet


@pytest.mark.modul4
@pytest.mark.parametrize(
    "betrag,waehrung,erwartet",
    [
        (19.99, "CHF", "19.99 CHF"),
        (29.50, "EUR", "29.50 EUR"),
        (100, "USD", "100.00 USD"),
        (0, "CHF", "0.00 CHF"),
    ],
)
def test_formatiere_preis_mit_waehrung(betrag, waehrung, erwartet):
    """Test: formatiere_preis() formatiert mit Währung."""
    import parameter

    result = parameter.formatiere_preis(betrag, waehrung)
    assert result == erwartet


@pytest.mark.modul4
def test_formatiere_preis_default_waehrung():
    """Test: formatiere_preis() nutzt CHF als Standard."""
    import parameter

    result = parameter.formatiere_preis(19.99)
    assert result == "19.99 CHF"
    assert "CHF" in result


@pytest.mark.modul4
@pytest.mark.parametrize(
    "laenge,breite,erwartete_flaeche,erwarteter_umfang",
    [
        (5, 3, 15, 16),
        (10, 10, 100, 40),
        (1, 1, 1, 4),
        (7, 4, 28, 22),
    ],
)
def test_berechne_rechteck(laenge, breite, erwartete_flaeche, erwarteter_umfang):
    """Test: berechne_rechteck() berechnet Fläche und Umfang."""
    import parameter

    flaeche, umfang = parameter.berechne_rechteck(laenge, breite)
    assert flaeche == erwartete_flaeche
    assert umfang == erwarteter_umfang


@pytest.mark.modul4
def test_berechne_rechteck_gibt_tupel_zurueck():
    """Test: berechne_rechteck() gibt Tupel zurück."""
    import parameter

    result = parameter.berechne_rechteck(5, 3)
    assert isinstance(result, tuple)
    assert len(result) == 2


@pytest.mark.modul4
def test_addiere_mit_floats():
    """Test: addiere() funktioniert auch mit Floats."""
    import parameter

    result = parameter.addiere(3.5, 2.7)
    assert abs(result - 6.2) < 0.0001  # Float-Vergleich mit Toleranz
