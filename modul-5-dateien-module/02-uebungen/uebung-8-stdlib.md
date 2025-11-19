# Übung: Standard-Module

**Dauer:** 15 Minuten

Verwenden Sie Standard-Module:

1. `datetime` - Zeigen Sie aktuelles Datum und Zeit
2. `random` - Generieren Sie 5 Zufallszahlen zwischen 1-100
3. `os` - Listen Sie alle .txt Dateien im aktuellen Verzeichnis

**Lösung:**
```python
import datetime
import random
import os

# Datum und Zeit
jetzt = datetime.datetime.now()
print(f"Jetzt: {jetzt.strftime('%d.%m.%Y %H:%M:%S')}")

# Zufallszahlen
zahlen = [random.randint(1, 100) for _ in range(5)]
print(f"Zufallszahlen: {zahlen}")

# Dateien
txt_dateien = [f for f in os.listdir('.') if f.endswith('.txt')]
print(f"TXT-Dateien: {txt_dateien}")
```

