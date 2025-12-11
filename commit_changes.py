#!/usr/bin/env python3
"""Commit und Push der Type Hint Korrekturen."""

import subprocess
import sys


def run_command(cmd: list[str]) -> tuple[int, str, str]:
    """Führt einen Befehl aus und gibt Returncode, stdout und stderr zurück."""
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.returncode, result.stdout, result.stderr


def main() -> None:
    """Hauptfunktion."""
    print("🔍 Prüfe Git-Status...")

    # Git add
    print("\n📦 Stage alle Änderungen...")
    returncode, stdout, stderr = run_command(["git", "add", "-A"])
    if returncode != 0:
        print(f"❌ Fehler beim Stagen: {stderr}")
        sys.exit(1)
    print("✅ Alle Änderungen gestaged")

    # Git status
    returncode, stdout, stderr = run_command(["git", "status", "--short"])
    if stdout.strip():
        print(f"\n📝 Geänderte Dateien:\n{stdout}")
        num_files = len(stdout.strip().split("\n"))
        print(f"Anzahl geänderter Dateien: {num_files}")
    else:
        print("\n✅ Keine Änderungen zum Committen")
        return

    # Git commit
    commit_msg = """🔧 fix: Type Hints in Tests korrigiert

- 75+ Type Hints von 'int | float | str | bool' zu spezifischen Types korrigiert
- Mathematische Operationen: int | float
- String-Parameter: str
- Boolean-Parameter: bool
- Integer-Parameter: int
- Float-Parameter: float

Betroffene Dateien:
- 17 Test-Dateien in modul-1 bis modul-4
- fix_test_type_hints.py: Automatisierungs-Skript hinzugefügt

Alle Type Hints sind nun korrekt und spezifisch!"""

    print("\n💾 Committe Änderungen...")
    returncode, stdout, stderr = run_command(["git", "commit", "-m", commit_msg])
    if returncode != 0:
        print(f"❌ Fehler beim Committen: {stderr}")
        sys.exit(1)
    print(f"✅ Commit erfolgreich:\n{stdout}")

    # Git log
    returncode, stdout, stderr = run_command(["git", "log", "--oneline", "-1"])
    print(f"\n📋 Letzter Commit:\n{stdout}")

    # Git push
    print("\n🚀 Pushe zu origin/develop...")
    returncode, stdout, stderr = run_command(["git", "push", "origin", "develop"])
    if returncode != 0:
        print(f"❌ Fehler beim Pushen: {stderr}")
        sys.exit(1)
    print("✅ Push erfolgreich!")

    # Final log
    returncode, stdout, stderr = run_command(["git", "log", "--oneline", "-3"])
    print(f"\n📜 Letzte 3 Commits:\n{stdout}")

    print("\n" + "=" * 60)
    print("✅ Alle Änderungen erfolgreich committed und gepusht!")
    print("=" * 60)


if __name__ == "__main__":
    main()
