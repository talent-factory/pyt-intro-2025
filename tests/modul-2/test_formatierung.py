"""
Tests für formatierung.py
Testet String-Formatierung
"""

import sys
import pytest
from pathlib import Path

modul_pfad = Path(__file__).parent.parent.parent / "modul-2-datentypen" / "05-beispiele"
sys.path.insert(0, str(modul_pfad))


@pytest.mark.modul2
def test_modul_import() -> None:
    """Test: Modul kann importiert werden."""
    try:
        import formatierung
        assert True
    except ImportError as e:
        pytest.fail(f"Import fehlgeschlagen: {e}")


@pytest.mark.modul2
def test_f_string_basic() -> None:
    """Test: Einfache F-Strings funktionieren."""
    name = "Anna"
    alter = 25
    result = f"Ich heisse {name} und bin {alter} Jahre alt"
    assert "Anna" in result
    assert "25" in result


@pytest.mark.modul2
def test_f_string_mit_berechnungen() -> None:
    """Test: F-Strings mit Berechnungen."""
    a = 10
    b = 20
    result = f"Die Summe ist {a + b}"
    assert "30" in result


@pytest.mark.modul2
@pytest.mark.parametrize("zahl,dezimalstellen,expected", [
    (19.99, 2, "19.99"),
    (19.99, 1, "20.0"),
    (3.14159, 2, "3.14"),
])
def test_formatierung_dezimalstellen(zahl: int | float | str | bool, dezimalstellen: int | float | str | bool, expected: int | float | str | bool) -> None:
    """Test: Formatierung mit Dezimalstellen."""
    result = f"{zahl:.{dezimalstellen}f}"
    assert result == expected


@pytest.mark.modul2
@pytest.mark.parametrize("prozent,expected", [
    (0.75, "75%"),
    (0.5, "50%"),
    (1.0, "100%"),
])
def test_prozent_formatierung(prozent: int | float | str | bool, expected: int | float | str | bool) -> None:
    """Test: Prozent-Formatierung."""
    result = f"{prozent:.0%}"
    assert result == expected


@pytest.mark.modul2
def test_formatierung_ausrichtung() -> None:
    """Test: Text-Ausrichtung funktioniert."""
    text = "Test"

    # Rechtsbündig
    result_rechts = f"{text:>10}"
    assert len(result_rechts) == 10
    assert result_rechts.endswith("Test")

    # Linksbündig
    result_links = f"{text:<10}"
    assert len(result_links) == 10
    assert result_links.startswith("Test")

    # Zentriert
    result_mitte = f"{text:^10}"
    assert len(result_mitte) == 10


@pytest.mark.modul2
def test_formatierung_tausender_trennzeichen() -> None:
    """Test: Tausender-Trennzeichen."""
    zahl = 1234567.89
    result = f"{zahl:,.2f}"
    assert "," in result
    assert "1,234,567.89" == result


@pytest.mark.modul2
def test_mehrzeilige_f_strings() -> None:
    """Test: Mehrzeilige F-Strings."""
    name = "Anna"
    alter = 25

    text = f"""
Name: {name}
Alter: {alter}
"""
    assert "Anna" in text
    assert "25" in text


@pytest.mark.modul2
def test_format_methode() -> None:
    """Test: format()-Methode funktioniert."""
    name = "Anna"
    alter = 25
    result = "Ich heisse {} und bin {} Jahre alt".format(name, alter)
    assert "Anna" in result
    assert "25" in result


@pytest.mark.modul2
def test_prozent_formatierung_alt() -> None:
    """Test: Alte %-Formatierung."""
    name = "Anna"
    alter = 25
    result = "Ich heisse %s und bin %d Jahre alt" % (name, alter)
    assert "Anna" in result
    assert "25" in result


@pytest.mark.modul2
def test_tabellen_formatierung() -> None:
    """Test: Tabellen mit Formatierung."""
    # Kopfzeile
    header = f"{'Name':<15} {'Alter':>5} {'Preis':>10}"
    assert len(header.replace(" ", "X")) >= 30

    # Datenzeile
    zeile = f"{'Anna':<15} {25:>5} {19.99:>10.2f}"
    assert "Anna" in zeile
    assert "25" in zeile
    assert "19.99" in zeile
