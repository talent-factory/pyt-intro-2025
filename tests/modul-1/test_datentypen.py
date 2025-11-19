"""
Tests für datentypen.py
Testet grundlegende Datentypen in Python
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
        import datentypen
        assert True
    except ImportError as e:
        pytest.fail(f"Import fehlgeschlagen: {e}")


@pytest.mark.modul1
def test_datentypen_ausgabe():
    """Test: Verschiedene Datentypen werden ausgegeben."""
    old_stdout = sys.stdout
    sys.stdout = captured = StringIO()

    try:
        import importlib
        import datentypen
        importlib.reload(datentypen)

        output = captured.getvalue()

        # Prüfe ob alle Typen erwähnt werden
        assert "int" in output
        assert "float" in output
        assert "str" in output
        assert "bool" in output

    finally:
        sys.stdout = old_stdout


@pytest.mark.modul1
def test_typkonvertierung():
    """Test: Typkonvertierung wird demonstriert."""
    old_stdout = sys.stdout
    sys.stdout = captured = StringIO()

    try:
        import importlib
        import datentypen
        importlib.reload(datentypen)

        output = captured.getvalue()

        # Prüfe Konvertierung
        assert "42" in output
        assert "Typkonvertierung" in output or "konvertierung" in output.lower()

    finally:
        sys.stdout = old_stdout
