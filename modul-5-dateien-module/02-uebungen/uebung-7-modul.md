# Übung: Eigenes Modul

**Dauer:** 15 Minuten

Erstellen Sie ein Modul `string_utils.py` mit:
- `ist_palindrom(text)` - Prüft ob Text ein Palindrom ist
- `woerter_zaehlen(text)` - Zählt Wörter
- `umkehren(text)` - Kehrt Text um

**Lösung:**
```python
# string_utils.py
def ist_palindrom(text):
    text = text.lower().replace(" ", "")
    return text == text[::-1]

def woerter_zaehlen(text):
    return len(text.split())

def umkehren(text):
    return text[::-1]

if __name__ == "__main__":
    print(ist_palindrom("Anna"))  # True
    print(woerter_zaehlen("Hallo Welt"))  # 2
    print(umkehren("Python"))  # nohtyP
```

