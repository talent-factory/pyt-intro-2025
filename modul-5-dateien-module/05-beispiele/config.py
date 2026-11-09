"""
Konfigurationsverwaltung mit JSON

Dieses Programm zeigt, wie man eine JSON-Konfigurationsdatei einliest
und die Einstellungen in einem Dictionary auswertet.

Zeigt:
- JSON-Datei lesen (mit Kommentaren, wie sie VS Code erlaubt)
- Fehlerbehandlung mit try / except (FileNotFoundError, JSONDecodeError)
- Werte mit .get() und Standardwerten abfragen
- Pfade mit dem Modul os.path zusammensetzen

Autor: Talent Factory
Datum: 2025
"""

import json
import os


def entferne_json_kommentare(text):
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


def lade_einstellungen(config_pfad):
    """
    Lädt die Einstellungen aus einer JSON-Datei.

    Args:
        config_pfad: Pfad zur settings.json Datei

    Returns:
        Dictionary mit den Einstellungen (leer, wenn das Laden fehlschlägt)
    """
    try:
        with open(config_pfad, encoding="utf-8") as datei:
            inhalt = datei.read()
        # Entferne Kommentare aus JSON (VS Code erlaubt Kommentare)
        inhalt_bereinigt = entferne_json_kommentare(inhalt)
        einstellungen = json.loads(inhalt_bereinigt)
        print(f"✓ Einstellungen erfolgreich geladen aus: {config_pfad}")
        return einstellungen
    except FileNotFoundError:
        print(f"✗ Fehler: Datei nicht gefunden: {config_pfad}")
        return {}
    except json.JSONDecodeError as fehler:
        print(f"✗ Fehler beim Parsen der JSON-Datei: {fehler}")
        return {}


def hole_wert(einstellungen, schluessel, standard=None):
    """
    Holt einen Wert aus den Einstellungen.

    Args:
        einstellungen: Dictionary mit den Einstellungen
        schluessel: Der Schlüssel der Einstellung
        standard: Standardwert, falls der Schlüssel nicht existiert

    Returns:
        Der Wert der Einstellung oder der Standardwert
    """
    return einstellungen.get(schluessel, standard)


def zeige_zusammenfassung(einstellungen):
    """Zeigt eine Zusammenfassung der wichtigsten Einstellungen."""
    interpreter = hole_wert(einstellungen, "python.defaultInterpreterPath", "")
    pytest_aktiv = hole_wert(einstellungen, "python.testing.pytestEnabled", False)
    pytest_args = hole_wert(einstellungen, "python.testing.pytestArgs", [])

    tab_groesse = hole_wert(einstellungen, "editor.tabSize", 4)
    lineale = hole_wert(einstellungen, "editor.rulers", [])
    python_einstellungen = hole_wert(einstellungen, "[python]", {})
    format_on_save = python_einstellungen.get("editor.formatOnSave", False)

    ruff_aktiv = hole_wert(einstellungen, "ruff.enable", False)
    ruff_pfad = hole_wert(einstellungen, "ruff.path", [])

    print("\n" + "=" * 60)
    print("VS CODE EINSTELLUNGEN - ZUSAMMENFASSUNG")
    print("=" * 60)

    print("\n📁 PYTHON-KONFIGURATION:")
    print(f"  • Interpreter: {interpreter}")
    print(f"  • Pytest aktiviert: {pytest_aktiv}")
    print(f"  • Pytest Args: {', '.join(pytest_args)}")

    print("\n✏️  EDITOR-EINSTELLUNGEN:")
    print(f"  • Tab-Grösse: {tab_groesse}")
    print(f"  • Lineale bei: {lineale}")
    print(f"  • Format on Save: {format_on_save}")

    print("\n🔧 CODE-QUALITÄT (RUFF):")
    print(f"  • Ruff aktiviert: {ruff_aktiv}")
    if ruff_pfad:
        print(f"  • Ruff Pfad: {ruff_pfad[0]}")

    print("\n" + "=" * 60)


if __name__ == "__main__":
    # Pfad zur VS Code Settings-Datei
    # Annahme: Das Skript liegt in modul-5-dateien-module/05-beispiele/
    # und die settings.json in .vscode/settings.json
    skript_ordner = os.path.dirname(os.path.abspath(__file__))
    projekt_root = os.path.join(skript_ordner, "..", "..")
    settings_pfad = os.path.join(projekt_root, ".vscode", "settings.json")

    print("=" * 60)
    print("KONFIGURATIONSVERWALTUNG MIT JSON")
    print("=" * 60)

    # Einstellungen laden
    einstellungen = lade_einstellungen(settings_pfad)

    # Zusammenfassung anzeigen
    zeige_zusammenfassung(einstellungen)

    # Einzelne Werte abfragen
    print("\n📋 EINZELNE WERTE ABFRAGEN:")
    terminal = hole_wert(
        einstellungen, "terminal.integrated.defaultProfile.osx", "nicht gesetzt"
    )
    minimap = hole_wert(einstellungen, "editor.minimap.enabled", False)
    klammern = hole_wert(einstellungen, "editor.bracketPairColorization.enabled", False)
    leerzeichen = hole_wert(einstellungen, "editor.renderWhitespace", "none")
    auto_import = hole_wert(
        einstellungen, "python.analysis.autoImportCompletions", False
    )

    print(f"  • Terminal (macOS): {terminal}")
    print(f"  • Minimap aktiviert: {minimap}")
    print(f"  • Bracket Colorization: {klammern}")
    print(f"  • Whitespace Rendering: {leerzeichen}")
    print(f"  • Auto-Import: {auto_import}")

    # Alle Einstellungen anzeigen (optional)
    print("\n🔍 ANZAHL GELADENER EINSTELLUNGEN:")
    print(f"  • Gesamt: {len(einstellungen)} Einstellungen")

    # Beispiel: Alle Python-bezogenen Einstellungen finden
    print("\n🐍 ALLE PYTHON-EINSTELLUNGEN:")
    python_keys = []
    for key in einstellungen:
        if key.startswith("python."):
            python_keys.append(key)

    for key in sorted(python_keys):
        wert = einstellungen[key]
        # Kürze lange Werte für bessere Lesbarkeit
        if len(str(wert)) > 50:
            print(f"  • {key}: (langer Wert, {len(str(wert))} Zeichen)")
        else:
            print(f"  • {key}: {wert}")
