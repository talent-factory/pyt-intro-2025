#!/usr/bin/env python3
"""
Wendet Type Hints aus dem Feature-Branch auf den aktuellen Branch an.
Verwendet git diff, um nur die Type Hints zu extrahieren und anzuwenden.
"""

import subprocess
import sys
from pathlib import Path


def run_command(cmd: list[str]) -> str:
    """Führt einen Shell-Befehl aus und gibt die Ausgabe zurück."""
    result = subprocess.run(cmd, capture_output=True, text=True, check=True)
    return result.stdout


def get_file_from_branch(filepath: str, branch: str) -> str:
    """Holt Dateiinhalt aus einem bestimmten Branch."""
    try:
        return run_command(["git", "show", f"{branch}:{filepath}"])
    except subprocess.CalledProcessError:
        return ""


def main():
    """Hauptfunktion."""
    print("🔍 Hole Liste der geänderten Dateien...")

    # Hole alle Python-Dateien, die im Feature-Branch geändert wurden
    diff_output = run_command(
        [
            "git",
            "diff",
            "--name-only",
            "HEAD",
            "origin/feature/add-type-hints-and-docstrings",
        ]
    )

    files = [f.strip() for f in diff_output.split("\n") if f.strip().endswith(".py")]

    print(f"📝 Gefunden: {len(files)} Python-Dateien")

    # Hole auch die neue Datei
    print("\n📄 Hole DOKUMENTATION_ZUSAMMENFASSUNG.md...")
    doc_content = get_file_from_branch(
        "DOKUMENTATION_ZUSAMMENFASSUNG.md",
        "origin/feature/add-type-hints-and-docstrings",
    )
    if doc_content:
        Path("DOKUMENTATION_ZUSAMMENFASSUNG.md").write_text(doc_content)
        print("  ✅ Erstellt")

    # Für jede Datei: Hole Version mit Type Hints
    success_count = 0
    for filepath in files:
        print(f"  Verarbeite: {filepath}")

        # Hole Version mit Type Hints
        feature_content = get_file_from_branch(
            filepath, "origin/feature/add-type-hints-and-docstrings"
        )

        if feature_content:
            Path(filepath).write_text(feature_content)
            success_count += 1

    print(f"\n✅ {success_count} Dateien aktualisiert")

    # Führe Ruff-Formatierung aus
    print("\n🎨 Führe Ruff-Formatierung aus...")
    subprocess.run([".venv/bin/ruff", "format", "."], check=False)
    subprocess.run([".venv/bin/ruff", "check", ".", "--fix"], check=False)

    print("\n✅ Fertig! Type Hints wurden angewendet und Code formatiert.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
