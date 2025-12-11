"""
Pytest Konfiguration und gemeinsame Fixtures
Für alle Test-Module
"""

import sys
from collections.abc import Callable, Generator
from io import StringIO
from pathlib import Path

import pytest

# Projekt-Root zum Python-Path hinzufügen
projekt_root = Path(__file__).parent.parent
sys.path.insert(0, str(projekt_root))


@pytest.fixture
def captured_output() -> Generator[StringIO, None, None]:
    """
    Fixture zum Erfassen von print()-Ausgaben.

    Yields:
        StringIO-Objekt mit der erfassten Ausgabe
    """
    import sys
    from io import StringIO

    old_stdout = sys.stdout
    sys.stdout = mystdout = StringIO()

    yield mystdout

    sys.stdout = old_stdout


@pytest.fixture
def mock_input(monkeypatch: pytest.MonkeyPatch) -> Callable[[list[str]], None]:
    """
    Fixture zum Mocken von input()-Aufrufen.

    Usage:
        def test_example(mock_input):
            mock_input(["Wert1", "Wert2"])
            # Code der input() aufruft
    """

    def _mock_input(values: list[str]) -> None:
        """
        Setzt eine Liste von Werten für aufeinanderfolgende input()-Aufrufe.

        Args:
            values: Liste der Eingabewerte
        """
        input_iterator = iter(values)
        monkeypatch.setattr("builtins.input", lambda _: next(input_iterator))

    return _mock_input


@pytest.fixture
def temp_file(tmp_path: Path) -> Callable[[str, str], Path]:
    """
    Fixture für temporäre Dateien.

    Args:
        tmp_path: Pytest's tmp_path fixture

    Returns:
        Funktion zum Erstellen temporärer Dateien
    """

    def _create_temp_file(content: str, filename: str = "test.txt") -> Path:
        """
        Erstellt eine temporäre Datei.

        Args:
            content: Dateiinhalt
            filename: Dateiname

        Returns:
            Path zur temporären Datei
        """
        file_path = tmp_path / filename
        file_path.write_text(content, encoding="utf-8")
        return file_path

    return _create_temp_file
