"""
Konfigurationsverwaltung mit JSON

Dieses Programm zeigt, wie man JSON-Konfigurationsdateien einliest
und die Daten in einer Klasse strukturiert verwaltet.

Autor: Talent Factory
Datum: 2025
"""

import json
from pathlib import Path
from typing import Any


class VSCodeEinstellungen:
    """
    Klasse zur Verwaltung von VS Code Einstellungen.

    Diese Klasse liest die settings.json ein und stellt die
    Einstellungen über Eigenschaften zur Verfügung.
    """

    def __init__(self, config_pfad: str | Path):
        """
        Initialisiert die Einstellungen aus einer JSON-Datei.

        Args:
            config_pfad: Pfad zur settings.json Datei
        """
        self.config_pfad = Path(config_pfad)
        self.einstellungen: dict[str, Any] = {}
        self.lade_einstellungen()

    def lade_einstellungen(self) -> None:
        """Lädt die Einstellungen aus der JSON-Datei."""
        try:
            with open(self.config_pfad, encoding="utf-8") as datei:
                inhalt = datei.read()
                # Entferne Kommentare aus JSON (VS Code erlaubt Kommentare)
                inhalt_bereinigt = self._entferne_json_kommentare(inhalt)
                self.einstellungen = json.loads(inhalt_bereinigt)
            print(f"✓ Einstellungen erfolgreich geladen aus: {self.config_pfad}")
        except FileNotFoundError:
            print(f"✗ Fehler: Datei nicht gefunden: {self.config_pfad}")
            self.einstellungen = {}
        except json.JSONDecodeError as e:
            print(f"✗ Fehler beim Parsen der JSON-Datei: {e}")
            self.einstellungen = {}

    def _entferne_json_kommentare(self, text: str) -> str:
        """
        Entfernt Kommentare aus JSON-Text (VS Code erlaubt // Kommentare).

        Args:
            text: JSON-Text mit möglichen Kommentaren

        Returns:
            Bereinigter JSON-Text ohne Kommentare
        """
        zeilen = text.split("\n")
        bereinigte_zeilen = []

        for zeile in zeilen:
            # Entferne // Kommentare (aber nicht in Strings)
            if "//" in zeile:
                # Einfache Lösung: Entferne alles nach //
                # (funktioniert nicht perfekt bei // in Strings, aber für VS Code Settings OK)
                zeile = zeile.split("//")[0]
            bereinigte_zeilen.append(zeile)

        return "\n".join(bereinigte_zeilen)

    def hole_wert(self, schluessel: str, standard: Any = None) -> Any:
        """
        Holt einen Wert aus den Einstellungen.

        Args:
            schluessel: Der Schlüssel der Einstellung
            standard: Standardwert, falls Schlüssel nicht existiert

        Returns:
            Der Wert der Einstellung oder der Standardwert
        """
        return self.einstellungen.get(schluessel, standard)

    # Python-spezifische Einstellungen
    @property
    def python_interpreter(self) -> str:
        """Gibt den Python Interpreter Pfad zurück."""
        return self.hole_wert("python.defaultInterpreterPath", "")

    @property
    def python_testing_enabled(self) -> bool:
        """Prüft, ob pytest aktiviert ist."""
        return self.hole_wert("python.testing.pytestEnabled", False)

    @property
    def pytest_args(self) -> list[str]:
        """Gibt die pytest Argumente zurück."""
        return self.hole_wert("python.testing.pytestArgs", [])

    # Editor-Einstellungen
    @property
    def editor_tab_size(self) -> int:
        """Gibt die Tab-Grösse zurück."""
        return self.hole_wert("editor.tabSize", 4)

    @property
    def editor_rulers(self) -> list[int]:
        """Gibt die Editor-Lineale zurück."""
        return self.hole_wert("editor.rulers", [])

    @property
    def format_on_save(self) -> bool:
        """Prüft, ob Format-on-Save aktiviert ist."""
        python_settings = self.hole_wert("[python]", {})
        return python_settings.get("editor.formatOnSave", False)

    # Ruff-Einstellungen
    @property
    def ruff_enabled(self) -> bool:
        """Prüft, ob Ruff aktiviert ist."""
        return self.hole_wert("ruff.enable", False)

    @property
    def ruff_path(self) -> list[str]:
        """Gibt den Ruff-Pfad zurück."""
        return self.hole_wert("ruff.path", [])

    def zeige_zusammenfassung(self) -> None:
        """Zeigt eine Zusammenfassung der wichtigsten Einstellungen."""
        print("\n" + "=" * 60)
        print("VS CODE EINSTELLUNGEN - ZUSAMMENFASSUNG")
        print("=" * 60)

        print("\n📁 PYTHON-KONFIGURATION:")
        print(f"  • Interpreter: {self.python_interpreter}")
        print(f"  • Pytest aktiviert: {self.python_testing_enabled}")
        print(f"  • Pytest Args: {', '.join(self.pytest_args)}")

        print("\n✏️  EDITOR-EINSTELLUNGEN:")
        print(f"  • Tab-Grösse: {self.editor_tab_size}")
        print(f"  • Lineale bei: {self.editor_rulers}")
        print(f"  • Format on Save: {self.format_on_save}")

        print("\n🔧 CODE-QUALITÄT (RUFF):")
        print(f"  • Ruff aktiviert: {self.ruff_enabled}")
        if self.ruff_path:
            print(f"  • Ruff Pfad: {self.ruff_path[0]}")

        print("\n" + "=" * 60)


if __name__ == "__main__":
    # Pfad zur VS Code Settings-Datei
    # Annahme: Das Skript liegt in modul-5-dateien-module/05-beispiele/
    # und die settings.json in .vscode/settings.json
    projekt_root = Path(__file__).parent.parent.parent
    settings_pfad = projekt_root / ".vscode" / "settings.json"

    print("=" * 60)
    print("KONFIGURATIONSVERWALTUNG MIT JSON")
    print("=" * 60)

    # Einstellungen laden
    config = VSCodeEinstellungen(settings_pfad)

    # Zusammenfassung anzeigen
    config.zeige_zusammenfassung()

    # Einzelne Werte abfragen
    print("\n📋 EINZELNE WERTE ABFRAGEN:")
    print(
        f"  • Terminal (macOS): {config.hole_wert('terminal.integrated.defaultProfile.osx', 'nicht gesetzt')}"
    )
    print(f"  • Minimap aktiviert: {config.hole_wert('editor.minimap.enabled', False)}")
    print(
        f"  • Bracket Colorization: {config.hole_wert('editor.bracketPairColorization.enabled', False)}"
    )
    print(
        f"  • Whitespace Rendering: {config.hole_wert('editor.renderWhitespace', 'none')}"
    )
    print(
        f"  • Auto-Import: {config.hole_wert('python.analysis.autoImportCompletions', False)}"
    )

    # Alle Einstellungen anzeigen (optional)
    print("\n🔍 ANZAHL GELADENER EINSTELLUNGEN:")
    print(f"  • Gesamt: {len(config.einstellungen)} Einstellungen")

    # Beispiel: Alle Python-bezogenen Einstellungen finden
    print("\n🐍 ALLE PYTHON-EINSTELLUNGEN:")
    python_keys = [
        key for key in config.einstellungen.keys() if key.startswith("python.")
    ]
    for key in sorted(python_keys):
        wert = config.einstellungen[key]
        # Kürze lange Werte für bessere Lesbarkeit
        if isinstance(wert, list | dict) and len(str(wert)) > 50:
            print(f"  • {key}: {type(wert).__name__} mit {len(wert)} Elementen")
        else:
            print(f"  • {key}: {wert}")
