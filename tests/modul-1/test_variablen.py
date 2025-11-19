"""
Tests für variablen.py
Testet Arbeiten mit Variablen
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
        import variablen
        assert True
    except ImportError as e:
        pytest.fail(f"Import fehlgeschlagen: {e}")


@pytest.mark.modul1
def test_variablen_ausgabe():
    """Test: Variablen werden korrekt ausgegeben."""
    old_stdout = sys.stdout
    sys.stdout = captured = StringIO()

    try:
        import importlib
        import variablen
        importlib.reload(variablen)

        output = captured.getvalue()

        # Prüfe erwartete Inhalte
        assert "Anna" in output
        assert "25" in output or "26" in output
        assert "Zürich" in output

    finally:
        sys.stdout = old_stdout


@pytest.mark.modul1
def test_berechnungen():
    """Test: Berechnungen werden durchgeführt."""
    old_stdout = sys.stdout
    sys.stdout = captured = StringIO()

    try:
        import importlib
        import variablen
        importlib.reload(variablen)

        output = captured.getvalue()

        # Prüfe mathematische Operationen
        assert "Summe" in output or "summe" in output
        assert "15" in output  # 10 + 5
        assert "5" in output   # 10 - 5
        assert "50" in output  # 10 * 5

    finally:
        sys.stdout = old_stdout
