"""
Tests für dictionaries.py
Testet Dictionary-Operationen und Funktionen
"""

import sys
import pytest
from pathlib import Path
from io import StringIO

# Modul importieren
modul_pfad = Path(__file__).parent.parent.parent / "modul-4-funktionen-datenstrukturen" / "05-beispiele"
sys.path.insert(0, str(modul_pfad))


@pytest.mark.modul4
def test_modul_kann_importiert_werden():
    """Test: Modul kann ohne Fehler importiert werden."""
    try:
        import dictionaries
        assert True
    except ImportError as e:
        pytest.fail(f"Import fehlgeschlagen: {e}")


@pytest.mark.modul4
def test_zeige_person_funktion():
    """Test: zeige_person() zeigt Person formatiert an."""
    import dictionaries

    old_stdout = sys.stdout
    sys.stdout = captured = StringIO()

    try:
        person = {"name": "Test Person", "email": "test@example.com"}
        dictionaries.zeige_person(person)
        output = captured.getvalue()

        assert "Test Person" in output
        assert "test@example.com" in output
        assert "Person" in output or "name" in output

    finally:
        sys.stdout = old_stdout


@pytest.mark.modul4
def test_erstelle_kontakt():
    """Test: erstelle_kontakt() erstellt Dictionary korrekt."""
    import dictionaries

    kontakt = dictionaries.erstelle_kontakt(
        "Anna Muster",
        "anna@example.com",
        "079 123 45 67"
    )

    assert isinstance(kontakt, dict)
    assert kontakt["name"] == "Anna Muster"
    assert kontakt["email"] == "anna@example.com"
    assert kontakt["telefon"] == "079 123 45 67"


@pytest.mark.modul4
def test_erstelle_kontakt_hat_richtige_keys():
    """Test: erstelle_kontakt() hat die richtigen Keys."""
    import dictionaries

    kontakt = dictionaries.erstelle_kontakt("Test", "test@test.com", "123")

    assert "name" in kontakt
    assert "email" in kontakt
    assert "telefon" in kontakt
    assert len(kontakt) == 3


@pytest.mark.modul4
def test_suche_kontakt_findet_exakt():
    """Test: suche_kontakt() findet exakten Namen."""
    import dictionaries

    kontakte = [
        dictionaries.erstelle_kontakt("Anna Muster", "anna@example.com", "079 123"),
        dictionaries.erstelle_kontakt("Max Meier", "max@example.com", "078 987"),
    ]

    gefunden = dictionaries.suche_kontakt(kontakte, "Max Meier")

    assert gefunden is not None
    assert gefunden["name"] == "Max Meier"
    assert gefunden["email"] == "max@example.com"


@pytest.mark.modul4
def test_suche_kontakt_case_insensitive():
    """Test: suche_kontakt() ist case-insensitive bei exakter Suche."""
    import dictionaries

    kontakte = [
        dictionaries.erstelle_kontakt("Anna Muster", "anna@example.com", "079 123"),
    ]

    # Verschiedene Schreibweisen testen - exakter Name erforderlich
    assert dictionaries.suche_kontakt(kontakte, "anna muster") is not None
    assert dictionaries.suche_kontakt(kontakte, "ANNA MUSTER") is not None
    assert dictionaries.suche_kontakt(kontakte, "Anna Muster") is not None


@pytest.mark.modul4
def test_suche_kontakt_nicht_gefunden():
    """Test: suche_kontakt() gibt None wenn nicht gefunden."""
    import dictionaries

    kontakte = [
        dictionaries.erstelle_kontakt("Anna Muster", "anna@example.com", "079 123"),
    ]

    gefunden = dictionaries.suche_kontakt(kontakte, "Nicht Existent")

    assert gefunden is None


@pytest.mark.modul4
def test_suche_kontakt_leere_liste():
    """Test: suche_kontakt() funktioniert mit leerer Liste."""
    import dictionaries

    kontakte = []

    gefunden = dictionaries.suche_kontakt(kontakte, "Test")

    assert gefunden is None
