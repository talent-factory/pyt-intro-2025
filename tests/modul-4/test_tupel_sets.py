"""
Tests für tupel_sets.py
Testet Tupel und Set-Operationen
"""

import sys
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
        import tupel_sets

        assert True
    except ImportError as e:
        pytest.fail(f"Import fehlgeschlagen: {e}")


@pytest.mark.modul4
@pytest.mark.parametrize(
    "punkt1,punkt2,erwartete_distanz",
    [
        ((0, 0), (3, 4), 5.0),
        ((0, 0), (0, 0), 0.0),
        ((1, 1), (1, 1), 0.0),
        ((0, 0), (1, 0), 1.0),
        ((0, 0), (0, 1), 1.0),
    ],
)
def test_berechne_distanz(punkt1, punkt2, erwartete_distanz):
    """Test: berechne_distanz() berechnet Distanz korrekt."""
    import tupel_sets

    distanz = tupel_sets.berechne_distanz(punkt1, punkt2)

    assert abs(distanz - erwartete_distanz) < 0.0001


@pytest.mark.modul4
def test_berechne_distanz_pythagoras():
    """Test: berechne_distanz() nutzt Pythagoras korrekt."""
    import tupel_sets

    # 3-4-5 Dreieck
    distanz = tupel_sets.berechne_distanz((0, 0), (3, 4))
    assert abs(distanz - 5.0) < 0.0001

    # 5-12-13 Dreieck
    distanz = tupel_sets.berechne_distanz((0, 0), (5, 12))
    assert abs(distanz - 13.0) < 0.0001


@pytest.mark.modul4
def test_eindeutige_woerter_einfach():
    """Test: eindeutige_woerter() findet eindeutige Wörter."""
    import tupel_sets

    text = "Python ist toll Python macht Spass"
    woerter = tupel_sets.eindeutige_woerter(text)

    assert isinstance(woerter, set)
    assert "python" in woerter
    assert "ist" in woerter
    assert "toll" in woerter
    assert "macht" in woerter
    assert "spass" in woerter


@pytest.mark.modul4
@pytest.mark.parametrize(
    "text,erwartete_anzahl",
    [
        ("eins zwei drei", 3),
        ("test test test", 1),
        ("a b c d e", 5),
        ("Python Python", 1),
    ],
)
def test_eindeutige_woerter_anzahl(text, erwartete_anzahl):
    """Test: eindeutige_woerter() zählt korrekt."""
    import tupel_sets

    woerter = tupel_sets.eindeutige_woerter(text)

    assert len(woerter) == erwartete_anzahl


@pytest.mark.modul4
def test_eindeutige_woerter_lowercase():
    """Test: eindeutige_woerter() konvertiert zu lowercase."""
    import tupel_sets

    text = "Python PYTHON python"
    woerter = tupel_sets.eindeutige_woerter(text)

    assert len(woerter) == 1
    assert "python" in woerter


@pytest.mark.modul4
def test_gemeinsame_elemente():
    """Test: gemeinsame_elemente() findet Schnittmenge."""
    import tupel_sets

    set1 = {"Anna", "Max", "Lisa"}
    set2 = {"Lisa", "Tom", "Sara"}

    gemeinsam = tupel_sets.gemeinsame_elemente(set1, set2)

    assert isinstance(gemeinsam, set)
    assert gemeinsam == {"Lisa"}


@pytest.mark.modul4
@pytest.mark.parametrize(
    "set1,set2,erwartet",
    [
        ({"a", "b"}, {"b", "c"}, {"b"}),
        ({"a", "b", "c"}, {"a", "b", "c"}, {"a", "b", "c"}),
        ({"a"}, {"b"}, set()),
        (set(), {"a"}, set()),
    ],
)
def test_gemeinsame_elemente_verschiedene_sets(set1, set2, erwartet):
    """Test: gemeinsame_elemente() mit verschiedenen Sets."""
    import tupel_sets

    gemeinsam = tupel_sets.gemeinsame_elemente(set1, set2)

    assert gemeinsam == erwartet


@pytest.mark.modul4
def test_berechne_distanz_negative_koordinaten():
    """Test: berechne_distanz() funktioniert mit negativen Koordinaten."""
    import tupel_sets

    distanz = tupel_sets.berechne_distanz((-3, -4), (0, 0))

    assert abs(distanz - 5.0) < 0.0001
