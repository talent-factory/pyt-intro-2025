"""
Tests für notizen_app.py
Testet die reine Formatierungs-Logik der Notizen-App.
"""

import sys
from datetime import datetime
from pathlib import Path

import pytest

# Modul importieren
modul_pfad = (
    Path(__file__).parent.parent.parent / "modul-5-dateien-module" / "05-beispiele"
)
sys.path.insert(0, str(modul_pfad))


@pytest.mark.modul5
def test_modul_kann_importiert_werden() -> None:
    """Test: Modul kann ohne Fehler importiert werden."""
    try:
        import notizen_app

        assert True
    except ImportError as e:
        pytest.fail(f"Import fehlgeschlagen: {e}")


@pytest.mark.modul5
def test_formatiere_notiz_mit_zeitpunkt() -> None:
    """Test: formatiere_notiz() erzeugt korrekte Zeile mit gegebenem Zeitpunkt."""
    import notizen_app

    zeitpunkt = datetime(2026, 6, 2, 14, 30)
    ergebnis = notizen_app.formatiere_notiz("Einkaufen gehen", zeitpunkt)

    assert ergebnis == "[2026-06-02 14:30] Einkaufen gehen"


@pytest.mark.modul5
def test_formatiere_notiz_ohne_zeitpunkt() -> None:
    """Test: formatiere_notiz() ohne Zeitpunkt nutzt aktuelle Zeit und enthält Text."""
    import notizen_app

    ergebnis = notizen_app.formatiere_notiz("Test")

    assert ergebnis.startswith("[")
    assert ergebnis.endswith("Test")
    assert "] " in ergebnis
