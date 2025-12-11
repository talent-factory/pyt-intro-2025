#!/usr/bin/env python3
import subprocess
import sys

# Git add
subprocess.run(["git", "add", "-A"], check=True)

# Git commit
msg = """🔧 fix: Type Hints in Tests korrigiert

- 75+ Type Hints von 'int | float | str | bool' zu spezifischen Types korrigiert
- Mathematische Operationen: int | float
- String-Parameter: str
- Boolean-Parameter: bool

Betroffene Dateien:
- 17 Test-Dateien in modul-1 bis modul-4
- fix_test_type_hints.py: Automatisierungs-Skript
- commit_changes.py: Commit-Skript

Alle Type Hints sind nun korrekt und spezifisch!"""

result = subprocess.run(["git", "commit", "-m", msg], capture_output=True, text=True)
print(result.stdout)
print(result.stderr)

if result.returncode == 0:
    # Git push
    result = subprocess.run(["git", "push", "origin", "develop"], capture_output=True, text=True)
    print(result.stdout)
    print(result.stderr)
    
    # Git log
    result = subprocess.run(["git", "log", "--oneline", "-3"], capture_output=True, text=True)
    print("\nLetzte 3 Commits:")
    print(result.stdout)
    print("\n✅ Erfolgreich!")
else:
    print("\n❌ Commit fehlgeschlagen")
    sys.exit(1)

