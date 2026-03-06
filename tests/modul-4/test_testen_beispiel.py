"""
Tests fuer testen_beispiel.py

Diese Testdatei zeigt, wie man Funktionen mit pytest testet.
Sie dient als Lernbeispiel fuer Lektion 4 von Modul 4.
"""

import sys
from pathlib import Path

import pytest

# Modul-Pfad hinzufuegen
modul_pfad = (
    Path(__file__).parent.parent.parent
    / "modul-4-funktionen-datenstrukturen"
    / "05-beispiele"
)
sys.path.insert(0, str(modul_pfad))

from testen_beispiel import berechne_durchschnitt, erstelle_kontakt, ist_gerade

# ===== ist_gerade() =====


@pytest.mark.modul4
def test_ist_gerade_mit_gerader_zahl() -> None:
    """Gerade Zahlen ergeben True."""
    assert ist_gerade(4) is True
    assert ist_gerade(100) is True


@pytest.mark.modul4
def test_ist_gerade_mit_ungerader_zahl() -> None:
    """Ungerade Zahlen ergeben False."""
    assert ist_gerade(7) is False
    assert ist_gerade(1) is False


@pytest.mark.modul4
def test_ist_gerade_mit_null() -> None:
    """Null ist eine gerade Zahl."""
    assert ist_gerade(0) is True


@pytest.mark.modul4
def test_ist_gerade_mit_negativer_zahl() -> None:
    """Auch negative Zahlen koennen gerade sein."""
    assert ist_gerade(-2) is True
    assert ist_gerade(-3) is False


# ===== berechne_durchschnitt() =====


@pytest.mark.modul4
def test_durchschnitt_normale_liste() -> None:
    """Durchschnitt einer normalen Liste."""
    assert berechne_durchschnitt([10.0, 20.0, 30.0]) == 20.0


@pytest.mark.modul4
def test_durchschnitt_ein_element() -> None:
    """Durchschnitt mit nur einem Element."""
    assert berechne_durchschnitt([5.0]) == 5.0


@pytest.mark.modul4
def test_durchschnitt_gleiche_werte() -> None:
    """Durchschnitt bei gleichen Werten."""
    assert berechne_durchschnitt([3.0, 3.0, 3.0]) == 3.0


@pytest.mark.modul4
def test_durchschnitt_leere_liste() -> None:
    """Leere Liste ergibt 0.0."""
    assert berechne_durchschnitt([]) == 0.0


# ===== erstelle_kontakt() =====


@pytest.mark.modul4
def test_kontakt_hat_alle_felder() -> None:
    """Kontakt enthaelt name, email, telefon."""
    kontakt = erstelle_kontakt("Anna", "anna@example.com", "079 123 45 67")
    assert "name" in kontakt
    assert "email" in kontakt
    assert "telefon" in kontakt


@pytest.mark.modul4
def test_kontakt_werte_korrekt() -> None:
    """Kontakt-Werte stimmen mit Eingabe ueberein."""
    kontakt = erstelle_kontakt("Max", "max@example.com", "078 987 65 43")
    assert kontakt["name"] == "Max"
    assert kontakt["email"] == "max@example.com"
    assert kontakt["telefon"] == "078 987 65 43"
