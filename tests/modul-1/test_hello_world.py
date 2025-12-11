"""
Tests für hello_world.py
Testet grundlegende print-Ausgaben und String-Formatierung
"""

import sys
from io import StringIO
from pathlib import Path

import pytest

# Modul importieren
modul_pfad = Path(__file__).parent.parent.parent / "modul-1-einstieg" / "05-beispiele"
sys.path.insert(0, str(modul_pfad))


@pytest.mark.modul1
def test_modul_kann_importiert_werden() -> None:
    """Test: Modul kann ohne Fehler importiert werden."""
    try:
        import hello_world

        assert True
    except ImportError as e:
        pytest.fail(f"Import fehlgeschlagen: {e}")


@pytest.mark.modul1
def test_modul_hat_ausgaben() -> None:
    """Test: Modul erzeugt Ausgaben beim Import."""
    old_stdout = sys.stdout
    sys.stdout = captured = StringIO()

    try:
        # Modul neu importieren um Ausgaben zu erfassen
        import importlib

        import hello_world

        importlib.reload(hello_world)

        output = captured.getvalue()

        # Prüfe ob bestimmte Ausgaben vorhanden sind
        assert "Hello" in output or "Hallo" in output
        assert len(output) > 0

    finally:
        sys.stdout = old_stdout


@pytest.mark.modul1
def test_ausgabe_enthaelt_erwartete_begriffe() -> None:
    """Test: Ausgabe enthält erwartete Begriffe."""
    old_stdout = sys.stdout
    sys.stdout = captured = StringIO()

    try:
        import importlib

        import hello_world

        importlib.reload(hello_world)

        output = captured.getvalue()

        # Prüfe erwartete Inhalte
        assert "Python" in output
        assert "Anna" in output or "Müller" in output

    finally:
        sys.stdout = old_stdout


@pytest.mark.modul1
def test_ausgabe_hat_mehrere_zeilen() -> None:
    """Test: Ausgabe besteht aus mehreren Zeilen."""
    old_stdout = sys.stdout
    sys.stdout = captured = StringIO()

    try:
        import importlib

        import hello_world

        importlib.reload(hello_world)

        output = captured.getvalue()
        zeilen = output.strip().split("\n")

        # Sollte mehrere Zeilen haben
        assert len(zeilen) >= 5

    finally:
        sys.stdout = old_stdout
