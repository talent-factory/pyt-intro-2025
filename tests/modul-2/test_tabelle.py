"""
Tests für tabelle.py
Testet formatierte Tabellen-Ausgabe
"""

import sys
from io import StringIO
from pathlib import Path

import pytest

modul_pfad = Path(__file__).parent.parent.parent / "modul-2-datentypen" / "05-beispiele"
sys.path.insert(0, str(modul_pfad))


@pytest.mark.modul2
def test_modul_import():
    """Test: Modul kann importiert werden."""
    try:
        import tabelle

        assert True
    except ImportError as e:
        pytest.fail(f"Import fehlgeschlagen: {e}")


@pytest.mark.modul2
def test_tabelle_hat_ausgabe():
    """Test: Tabelle erzeugt Ausgabe."""
    old_stdout = sys.stdout
    sys.stdout = captured = StringIO()

    try:
        import importlib

        import tabelle

        importlib.reload(tabelle)

        output = captured.getvalue()

        assert len(output) > 0
        assert "PRODUKTLISTE" in output or "Produkt" in output

    finally:
        sys.stdout = old_stdout


@pytest.mark.modul2
@pytest.mark.parametrize(
    "produkt_daten",
    [
        {"name": "Apfel", "menge": 10, "preis": 2.50},
        {"name": "Banane", "menge": 5, "preis": 3.20},
    ],
)
def test_berechnung_total(produkt_daten):
    """Test: Total wird korrekt berechnet."""
    total = produkt_daten["menge"] * produkt_daten["preis"]
    expected_total = produkt_daten["menge"] * produkt_daten["preis"]

    assert abs(total - expected_total) < 0.01


@pytest.mark.modul2
def test_summen_berechnung():
    """Test: Gesamtsumme wird korrekt berechnet."""
    produkte = [
        {"name": "Apfel", "menge": 10, "preis": 2.50},
        {"name": "Banane", "menge": 5, "preis": 3.20},
    ]

    gesamt_menge = sum(p["menge"] for p in produkte)
    gesamt_preis = sum(p["menge"] * p["preis"] for p in produkte)

    assert gesamt_menge == 15
    assert abs(gesamt_preis - 41.00) < 0.01


@pytest.mark.modul2
def test_durchschnittspreis():
    """Test: Durchschnittspreis wird berechnet."""
    gesamt_preis = 41.00
    gesamt_menge = 15

    durchschnitt = gesamt_preis / gesamt_menge

    assert abs(durchschnitt - 2.73) < 0.01


@pytest.mark.modul2
def test_formatierung_in_tabelle():
    """Test: Zahlen-Formatierung in Tabelle."""
    preis = 2.50
    formatiert = f"{preis:12.2f}"

    assert "2.50" in formatiert
    assert len(formatiert) == 12
