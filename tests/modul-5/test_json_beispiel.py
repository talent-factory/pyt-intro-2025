"""
Tests für json_beispiel.py
Testet JSON-Operationen mit temporären Dateien
"""

import json
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
        import json_beispiel

        assert True
    except ImportError as e:
        pytest.fail(f"Import fehlgeschlagen: {e}")


@pytest.mark.modul5
def test_config_erstellen(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    """Test: config_erstellen() erstellt JSON-Datei."""
    import json_beispiel

    monkeypatch.chdir(tmp_path)

    old_stdout = sys.stdout
    sys.stdout = StringIO()

    try:
        json_beispiel.config_erstellen()

        datei = tmp_path / "config.json"
        assert datei.exists()

    finally:
        sys.stdout = old_stdout


@pytest.mark.modul5
def test_config_erstellen_struktur(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    """Test: config_erstellen() erstellt korrekte Struktur."""
    import json_beispiel

    monkeypatch.chdir(tmp_path)

    old_stdout = sys.stdout
    sys.stdout = StringIO()

    try:
        json_beispiel.config_erstellen()

        datei = tmp_path / "config.json"
        with open(datei) as f:
            config = json.load(f)

        assert "app" in config
        assert "einstellungen" in config
        assert "benutzer" in config

    finally:
        sys.stdout = old_stdout


@pytest.mark.modul5
def test_config_erstellen_werte(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    """Test: config_erstellen() setzt korrekte Werte."""
    import json_beispiel

    monkeypatch.chdir(tmp_path)

    old_stdout = sys.stdout
    sys.stdout = StringIO()

    try:
        json_beispiel.config_erstellen()

        datei = tmp_path / "config.json"
        with open(datei) as f:
            config = json.load(f)

        assert config["app"]["name"] == "Meine App"
        assert config["app"]["version"] == "1.0.0"
        assert config["einstellungen"]["sprache"] == "de"
        assert config["einstellungen"]["theme"] == "hell"
        assert config["einstellungen"]["benachrichtigungen"] is True

    finally:
        sys.stdout = old_stdout


@pytest.mark.modul5
def test_config_laden(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    """Test: config_laden() lädt Konfiguration."""
    import json_beispiel

    monkeypatch.chdir(tmp_path)

    old_stdout = sys.stdout
    sys.stdout = StringIO()

    try:
        json_beispiel.config_erstellen()

    finally:
        sys.stdout = old_stdout

    config = json_beispiel.config_laden()

    assert config is not None
    assert "app" in config
    assert "einstellungen" in config


@pytest.mark.modul5
def test_config_laden_nicht_vorhanden(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    """Test: config_laden() gibt None wenn Datei fehlt."""
    import json_beispiel

    monkeypatch.chdir(tmp_path)

    config = json_beispiel.config_laden()

    assert config is None


@pytest.mark.modul5
def test_config_anzeigen(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    """Test: config_anzeigen() zeigt Konfiguration."""
    import json_beispiel

    monkeypatch.chdir(tmp_path)

    old_stdout = sys.stdout
    sys.stdout = StringIO()

    try:
        json_beispiel.config_erstellen()

    finally:
        sys.stdout = old_stdout

    old_stdout = sys.stdout
    sys.stdout = captured = StringIO()

    try:
        json_beispiel.config_anzeigen()
        output = captured.getvalue()

        assert "KONFIGURATION" in output or "=" in output
        assert "Meine App" in output or "app" in output

    finally:
        sys.stdout = old_stdout


@pytest.mark.modul5
def test_einstellung_aendern(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    """Test: einstellung_aendern() ändert Einstellung."""
    import json_beispiel

    monkeypatch.chdir(tmp_path)

    old_stdout = sys.stdout
    sys.stdout = StringIO()

    try:
        json_beispiel.config_erstellen()
        json_beispiel.einstellung_aendern("einstellungen", "sprache", "en")

    finally:
        sys.stdout = old_stdout

    # Laden und prüfen
    with open(tmp_path / "config.json") as f:
        config = json.load(f)

    assert config["einstellungen"]["sprache"] == "en"


@pytest.mark.modul5
def test_einstellung_aendern_verschiedene_werte(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    """Test: einstellung_aendern() mit verschiedenen Werten."""
    import json_beispiel

    monkeypatch.chdir(tmp_path)

    old_stdout = sys.stdout
    sys.stdout = StringIO()

    try:
        json_beispiel.config_erstellen()
        json_beispiel.einstellung_aendern("einstellungen", "theme", "dunkel")
        json_beispiel.einstellung_aendern("einstellungen", "benachrichtigungen", False)

    finally:
        sys.stdout = old_stdout

    with open(tmp_path / "config.json") as f:
        config = json.load(f)

    assert config["einstellungen"]["theme"] == "dunkel"
    assert config["einstellungen"]["benachrichtigungen"] is False


@pytest.mark.modul5
def test_json_formatierung(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    """Test: JSON-Datei ist lesbar formatiert (indent)."""
    import json_beispiel

    monkeypatch.chdir(tmp_path)

    old_stdout = sys.stdout
    sys.stdout = StringIO()

    try:
        json_beispiel.config_erstellen()

    finally:
        sys.stdout = old_stdout

    datei = tmp_path / "config.json"
    inhalt = datei.read_text()

    # Sollte mehrzeilig sein (indent)
    assert "\n" in inhalt
    assert inhalt.count("\n") > 5  # Mehrere Zeilen
