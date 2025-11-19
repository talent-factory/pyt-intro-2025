"""
Tests für funktionen_basis.py
Testet grundlegende Funktionen und deren Ausgaben
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
        import funktionen_basis
        assert True
    except ImportError as e:
        pytest.fail(f"Import fehlgeschlagen: {e}")


@pytest.mark.modul4
def test_zeige_header_funktion():
    """Test: zeige_header() erzeugt korrekte Ausgabe."""
    import funktionen_basis

    old_stdout = sys.stdout
    sys.stdout = captured = StringIO()

    try:
        funktionen_basis.zeige_header()
        output = captured.getvalue()

        # Prüfe auf erwartete Inhalte
        assert "=" in output
        assert "FUNKTIONEN DEMO" in output or "DEMO" in output
        zeilen = output.strip().split('\n')
        assert len(zeilen) >= 3  # Header sollte mehrere Zeilen haben

    finally:
        sys.stdout = old_stdout


@pytest.mark.modul4
def test_zeige_menu_funktion():
    """Test: zeige_menu() zeigt Menüoptionen."""
    import funktionen_basis

    old_stdout = sys.stdout
    sys.stdout = captured = StringIO()

    try:
        funktionen_basis.zeige_menu()
        output = captured.getvalue()

        # Prüfe auf Menüeinträge
        assert "1." in output or "2." in output or "3." in output
        assert len(output) > 0

    finally:
        sys.stdout = old_stdout


@pytest.mark.modul4
def test_begruessung_funktion():
    """Test: begruessung() gibt Willkommensnachricht aus."""
    import funktionen_basis

    old_stdout = sys.stdout
    sys.stdout = captured = StringIO()

    try:
        funktionen_basis.begruessung()
        output = captured.getvalue()

        # Prüfe auf Begrüßung
        assert "Willkommen" in output or "Python" in output
        assert len(output) > 0

    finally:
        sys.stdout = old_stdout


@pytest.mark.modul4
def test_zeige_footer_funktion():
    """Test: zeige_footer() zeigt Footer."""
    import funktionen_basis

    old_stdout = sys.stdout
    sys.stdout = captured = StringIO()

    try:
        funktionen_basis.zeige_footer()
        output = captured.getvalue()

        # Prüfe auf Footer-Elemente
        assert "-" in output or "=" in output
        assert "2025" in output or "Python" in output or "©" in output

    finally:
        sys.stdout = old_stdout


@pytest.mark.modul4
def test_alle_funktionen_sind_aufrufbar():
    """Test: Alle definierten Funktionen können aufgerufen werden."""
    import funktionen_basis

    # Prüfe ob Funktionen existieren
    assert hasattr(funktionen_basis, 'zeige_header')
    assert hasattr(funktionen_basis, 'zeige_menu')
    assert hasattr(funktionen_basis, 'begruessung')
    assert hasattr(funktionen_basis, 'zeige_footer')

    # Prüfe ob es aufrufbare Funktionen sind
    assert callable(funktionen_basis.zeige_header)
    assert callable(funktionen_basis.zeige_menu)
    assert callable(funktionen_basis.begruessung)
    assert callable(funktionen_basis.zeige_footer)
