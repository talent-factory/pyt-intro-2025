"""
Tests für csv_beispiel.py
Testet CSV-Operationen mit temporären Dateien
"""

import csv
import sys
from io import StringIO
from pathlib import Path
from typing import Any

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
        import csv_beispiel

        assert True
    except ImportError as e:
        pytest.fail(f"Import fehlgeschlagen: {e}")


@pytest.mark.modul5
def test_kontakte_erstellen(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    """Test: kontakte_erstellen() erstellt CSV-Datei."""
    import csv_beispiel

    monkeypatch.chdir(tmp_path)

    old_stdout = sys.stdout
    sys.stdout = StringIO()

    try:
        csv_beispiel.kontakte_erstellen()

        datei = tmp_path / "kontakte.csv"
        assert datei.exists()

    finally:
        sys.stdout = old_stdout


@pytest.mark.modul5
def test_kontakte_erstellen_inhalt(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    """Test: kontakte_erstellen() schreibt korrekte Daten."""
    import csv_beispiel

    monkeypatch.chdir(tmp_path)

    old_stdout = sys.stdout
    sys.stdout = StringIO()

    try:
        csv_beispiel.kontakte_erstellen()

        datei = tmp_path / "kontakte.csv"
        with open(datei) as f:
            reader = csv.DictReader(f)
            kontakte = list(reader)

        assert len(kontakte) == 3
        assert kontakte[0]["name"] == "Anna Muster"
        assert kontakte[1]["name"] == "Max Meier"
        assert kontakte[2]["name"] == "Lisa Schmidt"

    finally:
        sys.stdout = old_stdout


@pytest.mark.modul5
def test_kontakte_erstellen_hat_header(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    """Test: CSV-Datei hat korrekten Header."""
    import csv_beispiel

    monkeypatch.chdir(tmp_path)

    old_stdout = sys.stdout
    sys.stdout = StringIO()

    try:
        csv_beispiel.kontakte_erstellen()

        datei = tmp_path / "kontakte.csv"
        with open(datei) as f:
            reader = csv.DictReader(f)
            fieldnames = reader.fieldnames

        assert fieldnames is not None
        assert "name" in fieldnames
        assert "email" in fieldnames
        assert "telefon" in fieldnames

    finally:
        sys.stdout = old_stdout


@pytest.mark.modul5
def test_kontakte_anzeigen(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    """Test: kontakte_anzeigen() zeigt alle Kontakte."""
    import csv_beispiel

    monkeypatch.chdir(tmp_path)

    old_stdout = sys.stdout
    sys.stdout = StringIO()

    try:
        csv_beispiel.kontakte_erstellen()

    finally:
        sys.stdout = old_stdout

    old_stdout = sys.stdout
    sys.stdout = captured = StringIO()

    try:
        csv_beispiel.kontakte_anzeigen()
        output = captured.getvalue()

        assert "Anna Muster" in output
        assert "Max Meier" in output
        assert "Lisa Schmidt" in output
        assert "KONTAKTE" in output or "=" in output

    finally:
        sys.stdout = old_stdout


@pytest.mark.modul5
def test_kontakt_suchen_findet_exakt(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    """Test: kontakt_suchen() findet exakten Kontakt."""
    import csv_beispiel

    monkeypatch.chdir(tmp_path)

    old_stdout = sys.stdout
    sys.stdout = StringIO()

    try:
        csv_beispiel.kontakte_erstellen()

    finally:
        sys.stdout = old_stdout

    gefunden = csv_beispiel.kontakt_suchen("Max")

    assert gefunden is not None
    assert "Max" in gefunden["name"]
    assert gefunden["email"] == "max@example.com"


@pytest.mark.modul5
def test_kontakt_suchen_case_insensitive(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    """Test: kontakt_suchen() ist case-insensitive."""
    import csv_beispiel

    monkeypatch.chdir(tmp_path)

    old_stdout = sys.stdout
    sys.stdout = StringIO()

    try:
        csv_beispiel.kontakte_erstellen()

    finally:
        sys.stdout = old_stdout

    # Verschiedene Schreibweisen
    assert csv_beispiel.kontakt_suchen("anna") is not None
    assert csv_beispiel.kontakt_suchen("ANNA") is not None
    assert csv_beispiel.kontakt_suchen("Anna") is not None


@pytest.mark.modul5
def test_kontakt_suchen_nicht_gefunden(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    """Test: kontakt_suchen() gibt None wenn nicht gefunden."""
    import csv_beispiel

    monkeypatch.chdir(tmp_path)

    old_stdout = sys.stdout
    sys.stdout = StringIO()

    try:
        csv_beispiel.kontakte_erstellen()

    finally:
        sys.stdout = old_stdout

    gefunden = csv_beispiel.kontakt_suchen("Nicht Existent")

    assert gefunden is None


@pytest.mark.modul5
def test_kontakt_suchen_teilstring(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    """Test: kontakt_suchen() findet Teilstring."""
    import csv_beispiel

    monkeypatch.chdir(tmp_path)

    old_stdout = sys.stdout
    sys.stdout = StringIO()

    try:
        csv_beispiel.kontakte_erstellen()

    finally:
        sys.stdout = old_stdout

    # Sollte "Anna Muster" finden
    gefunden = csv_beispiel.kontakt_suchen("Muster")

    assert gefunden is not None
    assert "Muster" in gefunden["name"]
