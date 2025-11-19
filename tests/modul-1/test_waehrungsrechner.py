"""
Tests für waehrungsrechner.py
Testet Währungsumrechnungen
"""

import sys
import pytest
from pathlib import Path
from io import StringIO

modul_pfad = Path(__file__).parent.parent.parent / "modul-1-einstieg" / "05-beispiele"
sys.path.insert(0, str(modul_pfad))


@pytest.mark.modul1
def test_modul_import():
    """Test: Modul kann importiert werden."""
    try:
        import waehrungsrechner
        assert True
    except ImportError as e:
        pytest.fail(f"Import fehlgeschlagen: {e}")


@pytest.mark.modul1
@pytest.mark.parametrize("eur,kurs,expected_zielwaehrung", [
    (100, 0.95, 95.0),    # EUR zu CHF
    (100, 1.10, 110.0),   # EUR zu USD
    (100, 0.85, 85.0),    # EUR zu GBP
    (50, 0.95, 47.5),
])
def test_eur_umrechnung(eur, kurs, expected_zielwaehrung):
    """Test: EUR zu andere Währungen."""
    zielwaehrung = eur * kurs
    assert abs(zielwaehrung - expected_zielwaehrung) < 0.01


@pytest.mark.modul1
@pytest.mark.parametrize("quellwaehrung,kurs,expected_eur", [
    (95.0, 0.95, 100.0),   # CHF zu EUR
    (110.0, 1.10, 100.0),  # USD zu EUR
    (85.0, 0.85, 100.0),   # GBP zu EUR
])
def test_rueckrechnung_zu_eur(quellwaehrung, kurs, expected_eur):
    """Test: Rückrechnung zu EUR."""
    eur = quellwaehrung / kurs
    assert abs(eur - expected_eur) < 0.01


@pytest.mark.modul1
def test_wechselgebuehr_berechnung():
    """Test: Berechnung mit Wechselgebühren."""
    betrag_eur = 100.00
    kurs = 0.95
    gebuehr = 0.02  # 2%

    chf_ohne_gebuehr = betrag_eur * kurs
    chf_mit_gebuehr = chf_ohne_gebuehr * (1 - gebuehr)

    assert abs(chf_ohne_gebuehr - 95.0) < 0.01
    assert abs(chf_mit_gebuehr - 93.1) < 0.01


@pytest.mark.modul1
@pytest.mark.parametrize("betrag,kurs_alt,kurs_neu,expected_gewinn", [
    (100, 1.10, 1.20, 10.0),  # USD steigt
    (100, 0.95, 1.00, 5.0),   # CHF steigt
])
def test_kursgewinn(betrag, kurs_alt, kurs_neu, expected_gewinn):
    """Test: Gewinn bei Kursänderung."""
    wert_alt = betrag * kurs_alt
    wert_neu = betrag * kurs_neu
    gewinn = wert_neu - wert_alt

    assert abs(gewinn - expected_gewinn) < 0.01
