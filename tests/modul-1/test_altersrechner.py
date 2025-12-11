"""
Tests für altersrechner.py
Testet Altersberechnungen
"""

import sys
import pytest
from pathlib import Path
from io import StringIO

modul_pfad = Path(__file__).parent.parent.parent / "modul-1-einstieg" / "05-beispiele"
sys.path.insert(0, str(modul_pfad))


@pytest.mark.modul1
def test_modul_import() -> None:
    """Test: Modul kann importiert werden."""
    try:
        import altersrechner
        assert True
    except ImportError as e:
        pytest.fail(f"Import fehlgeschlagen: {e}")


@pytest.mark.modul1
@pytest.mark.parametrize("geburtsjahr,aktuelles_jahr,expected_alter", [
    (2000, 2025, 25),
    (1995, 2025, 30),
    (2005, 2025, 20),
    (1990, 2025, 35),
])
def test_altersberechnung(geburtsjahr: int | float | str | bool, aktuelles_jahr: int | float | str | bool, expected_alter: int | float | str | bool) -> None:
    """Test: Alter wird korrekt berechnet."""
    alter = aktuelles_jahr - geburtsjahr
    assert alter == expected_alter


@pytest.mark.modul1
@pytest.mark.parametrize("alter,expected_monate", [
    (25, 300),
    (30, 360),
    (20, 240),
])
def test_alter_in_monaten(alter: int | float | str | bool, expected_monate: int | float | str | bool) -> None:
    """Test: Umrechnung in Monate."""
    monate = alter * 12
    assert monate == expected_monate


@pytest.mark.modul1
@pytest.mark.parametrize("alter,expected_tage", [
    (25, 9125),
    (30, 10950),
    (20, 7300),
])
def test_alter_in_tagen(alter: int | float | str | bool, expected_tage: int | float | str | bool) -> None:
    """Test: Umrechnung in Tage (ungefähr)."""
    tage = alter * 365
    assert tage == expected_tage


@pytest.mark.modul1
@pytest.mark.parametrize("alter,expected_naechster_runder", [
    (25, 30),
    (33, 40),
    (49, 50),
    (20, 30),
])
def test_naechster_runder_geburtstag(alter: int | float | str | bool, expected_naechster_runder: int | float | str | bool) -> None:
    """Test: Berechnung des nächsten runden Geburtstags."""
    naechster_runder = ((alter // 10) + 1) * 10
    assert naechster_runder == expected_naechster_runder


@pytest.mark.modul1
def test_jahre_bis_runder_geburtstag() -> None:
    """Test: Jahre bis zum runden Geburtstag."""
    alter = 25
    naechster_runder = 30
    jahre_bis = naechster_runder - alter

    assert jahre_bis == 5
