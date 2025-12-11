#!/usr/bin/env python3
"""
Skript zum Korrigieren der Type Hints in Test-Dateien.

Ersetzt zu weit gefasste Type Hints (int | float | str | bool) durch
spezifischere Type Hints basierend auf dem Kontext der Verwendung.
"""

import re
from pathlib import Path


def analyze_parameter_usage(content: str, param_name: str) -> str:
    """
    Analysiert, wie ein Parameter verwendet wird und bestimmt den korrekten Type Hint.

    Args:
        content: Der Funktionsinhalt
        param_name: Der Name des Parameters

    Returns:
        Der korrekte Type Hint
    """
    # Mathematische Operationen: nur int | float
    math_ops = [r"\*\*", r"\*", r"/", r"\+", r"-", r"abs\(", r"round\("]
    for op in math_ops:
        if re.search(rf"{param_name}\s*{op}|{op}\s*{param_name}", content):
            return "int | float"

    # Vergleichsoperationen mit Zahlen: int | float
    if re.search(rf"{param_name}\s*[<>=]+\s*\d+|\d+\s*[<>=]+\s*{param_name}", content):
        return "int | float"

    # String-Operationen
    if re.search(rf'"{param_name}"|f".*{{{param_name}', content):
        return "str"

    # Boolean-Vergleiche
    if re.search(
        rf"{param_name}\s*==\s*(True|False)|(True|False)\s*==\s*{param_name}", content
    ):
        return "bool"

    # Tuple/Set basierend auf Parametrize-Werten
    if "tuple" in param_name.lower() or "punkt" in param_name.lower():
        return "tuple[int, int]"
    if "set" in param_name.lower():
        return "set[int]"

    # Default: behalte original
    return "int | float | str | bool"


def fix_type_hints_in_file(filepath: Path) -> tuple[int, list[str]]:
    """
    Korrigiert Type Hints in einer Test-Datei.

    Args:
        filepath: Pfad zur Test-Datei

    Returns:
        Tuple aus (Anzahl Änderungen, Liste der Änderungen)
    """
    content = filepath.read_text()
    original_content = content
    changes = []

    # Finde alle Funktionen mit problematischen Type Hints
    pattern = r"def (test_\w+)\((.*?)\) -> None:"
    matches = re.finditer(pattern, content, re.DOTALL)

    for match in matches:
        func_name = match.group(1)
        params = match.group(2)

        # Überspringe Funktionen ohne Parameter
        if not params.strip() or params.strip() == "":
            continue

        # Parse Parameter
        param_list = [p.strip() for p in params.split(",") if p.strip()]

        for param in param_list:
            # Überspringe spezielle Parameter (tmp_path, etc.)
            if ":" not in param:
                continue

            param_parts = param.split(":")
            if len(param_parts) != 2:
                continue

            param_name = param_parts[0].strip()
            param_type = param_parts[1].strip()

            # Nur Type Hints mit "int | float | str | bool" korrigieren
            if param_type != "int | float | str | bool":
                continue

            # Bestimme korrekten Type Hint basierend auf Verwendung
            # Hole Funktionsinhalt
            func_start = match.end()
            # Finde nächste Funktion oder Ende der Datei
            next_func = re.search(r"\ndef ", content[func_start:])
            if next_func:
                func_end = func_start + next_func.start()
            else:
                func_end = len(content)

            func_content = content[func_start:func_end]

            # Spezielle Regeln basierend auf Parameter-Namen
            new_type = None

            # String-Parameter
            if any(
                x in param_name.lower()
                for x in ["string", "str", "text", "msg", "operation", "expected_msg"]
            ):
                new_type = "str"

            # Boolean-Parameter
            elif (
                any(x in param_name.lower() for x in ["expected_bool", "expected"])
                and "bool" in func_content
            ):
                new_type = "bool"

            # Integer-Parameter
            elif any(
                x in param_name.lower()
                for x in [
                    "alter",
                    "punkte",
                    "note",
                    "dezimalstellen",
                    "expected_int",
                    "expected_note",
                ]
            ):
                new_type = "int"

            # Float-Parameter
            elif any(
                x in param_name.lower()
                for x in [
                    "expected_float",
                    "zahl",
                    "prozent",
                    "expected_bmi",
                    "erwartete_distanz",
                ]
            ):
                if "expected_float" in param_name.lower():
                    new_type = "float"
                else:
                    new_type = "int | float"

            # Mathematische Operationen
            elif re.search(
                rf"{param_name}\s*[\*\+\-/]|[\*\+\-/]\s*{param_name}|\*\*|abs\(|round\(",
                func_content,
            ):
                new_type = "int | float"

            # Tuple/Set
            elif "punkt" in param_name.lower():
                new_type = "tuple[int, int]"
            elif "set" in param_name.lower() and "erwartet" in param_name.lower():
                new_type = "set[int]"

            # Wenn kein spezifischer Type gefunden wurde, analysiere Verwendung
            if new_type is None:
                new_type = analyze_parameter_usage(func_content, param_name)

            # Ersetze Type Hint nur wenn sich etwas ändert
            if new_type != param_type and new_type != "int | float | str | bool":
                old_param = f"{param_name}: {param_type}"
                new_param = f"{param_name}: {new_type}"
                content = content.replace(old_param, new_param)
                changes.append(
                    f"  - {func_name}: {param_name}: {param_type} → {new_type}"
                )

    # Schreibe nur wenn Änderungen vorgenommen wurden
    if content != original_content:
        filepath.write_text(content)
        return len(changes), changes

    return 0, []


def main() -> None:
    """Hauptfunktion."""
    test_dir = Path("tests")
    total_changes = 0
    all_changes = []

    print("🔍 Suche nach Test-Dateien mit problematischen Type Hints...\n")

    for test_file in sorted(test_dir.rglob("test_*.py")):
        num_changes, changes = fix_type_hints_in_file(test_file)
        if num_changes > 0:
            total_changes += num_changes
            print(f"✅ {test_file.relative_to(test_dir)}: {num_changes} Änderungen")
            all_changes.extend(changes)

    print(f"\n{'=' * 60}")
    print(f"✅ Insgesamt {total_changes} Type Hints korrigiert!")
    print(f"{'=' * 60}")

    if all_changes:
        print("\n📝 Detaillierte Änderungen:")
        for change in all_changes[:20]:  # Zeige erste 20
            print(change)
        if len(all_changes) > 20:
            print(f"  ... und {len(all_changes) - 20} weitere")


if __name__ == "__main__":
    main()
