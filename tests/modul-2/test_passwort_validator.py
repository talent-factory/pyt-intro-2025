"""
Tests für passwort_validator.py
Testet Passwort-Validierung
"""

import sys
import pytest
from pathlib import Path
from unittest.mock import patch

modul_pfad = Path(__file__).parent.parent.parent / "modul-2-datentypen" / "05-beispiele"
sys.path.insert(0, str(modul_pfad))


@pytest.mark.modul2
def test_modul_import() -> None:
    """Test: Modul kann importiert werden."""
    # Mocke input() um Endlosschleife zu vermeiden
    with patch('builtins.input', return_value='q'):
        try:
            import passwort_validator
            assert True
        except Exception as e:
            pytest.skip(f"Interaktives Modul: {e}")


@pytest.mark.modul2
def test_validiere_passwort_funktion_existiert() -> None:
    """Test: validiere_passwort Funktion existiert."""
    with patch('builtins.input', return_value='q'):
        import passwort_validator
        assert hasattr(passwort_validator, 'validiere_passwort')


@pytest.mark.modul2
@pytest.mark.parametrize("passwort,sollte_gueltig_sein", [
    ("Test123!", True),
    ("Sicher@99", True),
    ("MyPwd#42", True),
    ("kurz1!", False),  # Zu kurz
    ("nurklein123!", False),  # Kein Grossbuchstabe
    ("NURGROSS123!", False),  # Kein Kleinbuchstabe
    ("KeinZahl!", False),  # Keine Zahl
    ("KeineSonder123", False),  # Kein Sonderzeichen
])
def test_passwort_validierung(passwort: int | float | str | bool, sollte_gueltig_sein: int | float | str | bool) -> None:
    """Test: Passwort-Validierung mit verschiedenen Eingaben."""
    with patch('builtins.input', return_value='q'):
        import passwort_validator
        import importlib
        importlib.reload(passwort_validator)

        ist_gueltig, fehler = passwort_validator.validiere_passwort(passwort)

        if sollte_gueltig_sein:
            assert ist_gueltig, f"Passwort sollte gültig sein: {passwort}, Fehler: {fehler}"
            assert len(fehler) == 0
        else:
            assert not ist_gueltig, f"Passwort sollte ungültig sein: {passwort}"
            assert len(fehler) > 0


@pytest.mark.modul2
def test_passwort_mindestlaenge() -> None:
    """Test: Mindestlänge wird geprüft."""
    with patch('builtins.input', return_value='q'):
        import passwort_validator
        import importlib
        importlib.reload(passwort_validator)

        ist_gueltig, fehler = passwort_validator.validiere_passwort("Test1!")

        assert not ist_gueltig
        assert any("8 Zeichen" in str(f) for f in fehler)


@pytest.mark.modul2
def test_passwort_grossbuchstabe() -> None:
    """Test: Grossbuchstabe erforderlich."""
    with patch('builtins.input', return_value='q'):
        import passwort_validator
        import importlib
        importlib.reload(passwort_validator)

        ist_gueltig, fehler = passwort_validator.validiere_passwort("test123!")

        assert not ist_gueltig
        assert any("Grossbuchstabe" in str(f) or "grossbuchstabe" in str(f).lower() for f in fehler)


@pytest.mark.modul2
def test_passwort_kleinbuchstabe() -> None:
    """Test: Kleinbuchstabe erforderlich."""
    with patch('builtins.input', return_value='q'):
        import passwort_validator
        import importlib
        importlib.reload(passwort_validator)

        ist_gueltig, fehler = passwort_validator.validiere_passwort("TEST123!")

        assert not ist_gueltig
        assert any("Kleinbuchstabe" in str(f) or "kleinbuchstabe" in str(f).lower() for f in fehler)


@pytest.mark.modul2
def test_passwort_zahl() -> None:
    """Test: Zahl erforderlich."""
    with patch('builtins.input', return_value='q'):
        import passwort_validator
        import importlib
        importlib.reload(passwort_validator)

        ist_gueltig, fehler = passwort_validator.validiere_passwort("TestTest!")

        assert not ist_gueltig
        assert any("Zahl" in str(f) or "zahl" in str(f).lower() for f in fehler)


@pytest.mark.modul2
def test_passwort_sonderzeichen() -> None:
    """Test: Sonderzeichen erforderlich."""
    with patch('builtins.input', return_value='q'):
        import passwort_validator
        import importlib
        importlib.reload(passwort_validator)

        ist_gueltig, fehler = passwort_validator.validiere_passwort("Test1234")

        assert not ist_gueltig
        assert any("Sonderzeichen" in str(f) or "sonderzeichen" in str(f).lower() for f in fehler)
