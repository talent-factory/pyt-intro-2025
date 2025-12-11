"""
Tests für listen_operationen.py
Testet List Comprehensions und Listen-Funktionen
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
        import listen_operationen

        assert True
    except ImportError as e:
        pytest.fail(f"Import fehlgeschlagen: {e}")


@pytest.mark.modul4
def test_zeige_liste_funktion():
    """Test: zeige_liste() zeigt Liste formatiert an."""
    import listen_operationen

    old_stdout = sys.stdout
    sys.stdout = captured = StringIO()

    try:
        listen_operationen.zeige_liste([1, 2, 3], "Testliste")
        output = captured.getvalue()

        assert "Testliste" in output
        assert "[1, 2, 3]" in output
        assert "Länge" in output or "3" in output

    finally:
        sys.stdout = old_stdout


@pytest.mark.modul4
@pytest.mark.parametrize(
    "eingabe,erwartet",
    [
        ([1, 2, 3, 4, 5, 6], [2, 4, 6]),
        ([10, 11, 12, 13], [10, 12]),
        ([1, 3, 5, 7, 9], []),
        ([2, 4, 6, 8], [2, 4, 6, 8]),
        ([], []),
    ],
)
def test_nur_gerade(eingabe, erwartet):
    """Test: nur_gerade() filtert gerade Zahlen korrekt."""
    import listen_operationen

    result = listen_operationen.nur_gerade(eingabe)
    assert result == erwartet


@pytest.mark.modul4
@pytest.mark.parametrize(
    "eingabe,erwartet",
    [
        ([1, 2, 3], [2, 4, 6]),
        ([5, 10, 15], [10, 20, 30]),
        ([0], [0]),
        ([], []),
        ([-1, -2, -3], [-2, -4, -6]),
    ],
)
def test_verdopple(eingabe, erwartet):
    """Test: verdopple() verdoppelt alle Werte."""
    import listen_operationen

    result = listen_operationen.verdopple(eingabe)
    assert result == erwartet


@pytest.mark.modul4
def test_statistik_einfache_liste():
    """Test: statistik() berechnet Statistiken korrekt."""
    import listen_operationen

    zahlen = [1, 2, 3, 4, 5]
    stats = listen_operationen.statistik(zahlen)

    assert stats["min"] == 1
    assert stats["max"] == 5
    assert stats["summe"] == 15
    assert stats["durchschnitt"] == 3.0


@pytest.mark.modul4
@pytest.mark.parametrize(
    "zahlen,min_val,max_val,summe,durchschnitt",
    [
        ([10, 20, 30], 10, 30, 60, 20.0),
        ([5], 5, 5, 5, 5.0),
        ([1, 1, 1, 1], 1, 1, 4, 1.0),
        ([-5, 0, 5], -5, 5, 0, 0.0),
    ],
)
def test_statistik_verschiedene_listen(zahlen, min_val, max_val, summe, durchschnitt):
    """Test: statistik() funktioniert mit verschiedenen Listen."""
    import listen_operationen

    stats = listen_operationen.statistik(zahlen)

    assert stats["min"] == min_val
    assert stats["max"] == max_val
    assert stats["summe"] == summe
    assert abs(stats["durchschnitt"] - durchschnitt) < 0.0001


@pytest.mark.modul4
def test_statistik_gibt_dict_zurueck():
    """Test: statistik() gibt Dictionary zurück."""
    import listen_operationen

    stats = listen_operationen.statistik([1, 2, 3])

    assert isinstance(stats, dict)
    assert "min" in stats
    assert "max" in stats
    assert "summe" in stats
    assert "durchschnitt" in stats


@pytest.mark.modul4
def test_nur_gerade_aendert_original_nicht():
    """Test: nur_gerade() ändert Original-Liste nicht."""
    import listen_operationen

    original = [1, 2, 3, 4, 5]
    kopie = original.copy()

    listen_operationen.nur_gerade(original)

    assert original == kopie  # Original unverändert
