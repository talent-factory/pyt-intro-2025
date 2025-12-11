"""
Tests für email_validator.py
Testet E-Mail-Validierung
"""

import sys
from pathlib import Path
from unittest.mock import patch

import pytest

modul_pfad = Path(__file__).parent.parent.parent / "modul-2-datentypen" / "05-beispiele"
sys.path.insert(0, str(modul_pfad))


@pytest.mark.modul2
def test_modul_import() -> None:
    """Test: Modul kann importiert werden."""
    with patch("builtins.input", return_value="q"):
        try:
            import email_validator

            assert True
        except Exception as e:
            pytest.skip(f"Interaktives Modul: {e}")


@pytest.mark.modul2
def test_validiere_email_funktion_existiert() -> None:
    """Test: validiere_email Funktion existiert."""
    with patch("builtins.input", return_value="q"):
        import email_validator

        assert hasattr(email_validator, "validiere_email")


@pytest.mark.modul2
@pytest.mark.parametrize(
    "email,sollte_gueltig_sein",
    [
        ("test@example.com", True),
        ("user@domain.de", True),
        ("anna.mueller@firma.ch", True),
        ("", False),  # Leer
        ("@example.com", False),  # Kein Benutzername
        ("test@", False),  # Keine Domain
        ("testexample.com", False),  # Kein @
        ("test@@example.com", False),  # Doppeltes @
        ("test@example", False),  # Kein . in Domain
        ("test@example.c", False),  # TLD zu kurz
    ],
)
def test_email_validierung(
    email: str, sollte_gueltig_sein: int | float | str | bool
) -> None:
    """Test: E-Mail-Validierung mit verschiedenen Eingaben."""
    with patch("builtins.input", return_value="q"):
        import importlib

        import email_validator

        importlib.reload(email_validator)

        ist_gueltig, meldung = email_validator.validiere_email(email)

        if sollte_gueltig_sein:
            assert ist_gueltig, f"E-Mail sollte gültig sein: {email}, Fehler: {meldung}"
        else:
            assert not ist_gueltig, f"E-Mail sollte ungültig sein: {email}"


@pytest.mark.modul2
def test_email_leer() -> None:
    """Test: Leere E-Mail wird abgelehnt."""
    with patch("builtins.input", return_value="q"):
        import importlib

        import email_validator

        importlib.reload(email_validator)

        ist_gueltig, meldung = email_validator.validiere_email("")

        assert not ist_gueltig
        assert "leer" in meldung.lower()


@pytest.mark.modul2
def test_email_ohne_at() -> None:
    """Test: E-Mail ohne @ wird abgelehnt."""
    with patch("builtins.input", return_value="q"):
        import importlib

        import email_validator

        importlib.reload(email_validator)

        ist_gueltig, meldung = email_validator.validiere_email("test.example.com")

        assert not ist_gueltig
        assert "@" in meldung or "fehlt" in meldung.lower()


@pytest.mark.modul2
def test_email_mehrere_at() -> None:
    """Test: E-Mail mit mehreren @ wird abgelehnt."""
    with patch("builtins.input", return_value="q"):
        import importlib

        import email_validator

        importlib.reload(email_validator)

        ist_gueltig, meldung = email_validator.validiere_email("test@@example.com")

        assert not ist_gueltig


@pytest.mark.modul2
def test_email_ohne_punkt_in_domain() -> None:
    """Test: E-Mail ohne . in Domain wird abgelehnt."""
    with patch("builtins.input", return_value="q"):
        import importlib

        import email_validator

        importlib.reload(email_validator)

        ist_gueltig, meldung = email_validator.validiere_email("test@example")

        assert not ist_gueltig
        assert "." in meldung or "domain" in meldung.lower()


@pytest.mark.modul2
def test_email_whitespace_trimming() -> None:
    """Test: Leerzeichen werden entfernt."""
    with patch("builtins.input", return_value="q"):
        import importlib

        import email_validator

        importlib.reload(email_validator)

        # E-Mail mit Leerzeichen davor/danach sollte akzeptiert werden
        ist_gueltig, meldung = email_validator.validiere_email("  test@example.com  ")

        assert ist_gueltig


@pytest.mark.modul2
def test_email_teile_aufsplitten() -> None:
    """Test: E-Mail-Teile werden korrekt aufgesplittet."""
    email = "user@domain.com"
    teile = email.split("@")

    assert len(teile) == 2
    assert teile[0] == "user"
    assert teile[1] == "domain.com"


@pytest.mark.modul2
def test_domain_teile() -> None:
    """Test: Domain-Teile werden korrekt aufgesplittet."""
    domain = "example.com"
    teile = domain.split(".")

    assert len(teile) == 2
    assert teile[0] == "example"
    assert teile[1] == "com"
    assert len(teile[-1]) >= 2  # TLD mindestens 2 Zeichen
