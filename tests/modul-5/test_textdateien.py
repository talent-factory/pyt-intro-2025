"""
Tests für textdateien.py
Testet Textdatei-Operationen mit temporären Dateien
"""

import sys
import pytest
from pathlib import Path
from io import StringIO
from unittest.mock import patch
import os

# Modul importieren
modul_pfad = Path(__file__).parent.parent.parent / "modul-5-dateien-module" / "05-beispiele"
sys.path.insert(0, str(modul_pfad))


@pytest.mark.modul5
def test_modul_kann_importiert_werden():
    """Test: Modul kann ohne Fehler importiert werden."""
    try:
        import textdateien
        assert True
    except ImportError as e:
        pytest.fail(f"Import fehlgeschlagen: {e}")


@pytest.mark.modul5
def test_tagebuch_eintrag_erstellt_datei(tmp_path, monkeypatch):
    """Test: tagebuch_eintrag() erstellt Datei."""
    import textdateien

    # Wechsle in temporäres Verzeichnis
    monkeypatch.chdir(tmp_path)

    old_stdout = sys.stdout
    sys.stdout = StringIO()

    try:
        textdateien.tagebuch_eintrag("Test-Eintrag")

        datei = tmp_path / "tagebuch.txt"
        assert datei.exists()

    finally:
        sys.stdout = old_stdout


@pytest.mark.modul5
def test_tagebuch_eintrag_schreibt_inhalt(tmp_path, monkeypatch):
    """Test: tagebuch_eintrag() schreibt korrekten Inhalt."""
    import textdateien

    monkeypatch.chdir(tmp_path)

    old_stdout = sys.stdout
    sys.stdout = StringIO()

    try:
        textdateien.tagebuch_eintrag("Heute war ein guter Tag!")

        datei = tmp_path / "tagebuch.txt"
        inhalt = datei.read_text()

        assert "Heute war ein guter Tag!" in inhalt
        # Sollte Zeitstempel enthalten
        assert "[" in inhalt
        assert "]" in inhalt

    finally:
        sys.stdout = old_stdout


@pytest.mark.modul5
def test_tagebuch_eintrag_append_modus(tmp_path, monkeypatch):
    """Test: tagebuch_eintrag() hängt an (append mode)."""
    import textdateien

    monkeypatch.chdir(tmp_path)

    old_stdout = sys.stdout
    sys.stdout = StringIO()

    try:
        textdateien.tagebuch_eintrag("Erster Eintrag")
        textdateien.tagebuch_eintrag("Zweiter Eintrag")

        datei = tmp_path / "tagebuch.txt"
        inhalt = datei.read_text()

        assert "Erster Eintrag" in inhalt
        assert "Zweiter Eintrag" in inhalt
        assert inhalt.count("[") == 2  # Zwei Zeitstempel

    finally:
        sys.stdout = old_stdout


@pytest.mark.modul5
def test_tagebuch_anzeigen_ohne_datei(tmp_path, monkeypatch):
    """Test: tagebuch_anzeigen() behandelt fehlende Datei."""
    import textdateien

    monkeypatch.chdir(tmp_path)

    old_stdout = sys.stdout
    sys.stdout = captured = StringIO()

    try:
        textdateien.tagebuch_anzeigen()
        output = captured.getvalue()

        assert "Noch keine Einträge" in output or "nicht" in output

    finally:
        sys.stdout = old_stdout


@pytest.mark.modul5
def test_tagebuch_anzeigen_mit_eintraegen(tmp_path, monkeypatch):
    """Test: tagebuch_anzeigen() zeigt Einträge."""
    import textdateien

    monkeypatch.chdir(tmp_path)

    # Erstelle Einträge
    old_stdout = sys.stdout
    sys.stdout = StringIO()

    try:
        textdateien.tagebuch_eintrag("Test 1")
        textdateien.tagebuch_eintrag("Test 2")

    finally:
        sys.stdout = old_stdout

    # Zeige Einträge
    old_stdout = sys.stdout
    sys.stdout = captured = StringIO()

    try:
        textdateien.tagebuch_anzeigen()
        output = captured.getvalue()

        assert "Test 1" in output
        assert "Test 2" in output
        assert "TAGEBUCH" in output or "=" in output

    finally:
        sys.stdout = old_stdout


@pytest.mark.modul5
def test_datei_analysieren(tmp_path):
    """Test: datei_analysieren() analysiert Datei korrekt."""
    import textdateien

    # Erstelle Testdatei
    test_datei = tmp_path / "test.txt"
    test_datei.write_text("Zeile 1\nZeile 2\nZeile 3")

    old_stdout = sys.stdout
    sys.stdout = captured = StringIO()

    try:
        textdateien.datei_analysieren(str(test_datei))
        output = captured.getvalue()

        assert "3" in output  # 3 Zeilen
        assert "Zeilen" in output
        assert "Wörter" in output or "Zeichen" in output

    finally:
        sys.stdout = old_stdout


@pytest.mark.modul5
def test_datei_analysieren_zaehlt_korrekt(tmp_path):
    """Test: datei_analysieren() zählt Zeilen, Wörter, Zeichen."""
    import textdateien

    test_datei = tmp_path / "test.txt"
    test_datei.write_text("ein zwei drei\nvier fünf")

    old_stdout = sys.stdout
    sys.stdout = captured = StringIO()

    try:
        textdateien.datei_analysieren(str(test_datei))
        output = captured.getvalue()

        # 2 Zeilen
        assert "2" in output

    finally:
        sys.stdout = old_stdout
