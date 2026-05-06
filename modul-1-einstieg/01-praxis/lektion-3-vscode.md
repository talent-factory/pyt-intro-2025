# Lektion 3: VS Code Entwicklungsumgebung

**Dauer:** 50 Minuten  
**Format:** Theorie (15 Min.) + Live-Coding (20 Min.) + Übung (15 Min.)

## 🎯 Lernziele

Nach dieser Lektion können Sie:

- VS Code öffnen und navigieren
- Python-Dateien erstellen und speichern
- Code ausführen
- Grundlegende Debugging-Techniken anwenden

---

## 📖 Theorie (15 Min.)

### 1. Was ist VS Code?

**Visual Studio Code** = Professioneller Code-Editor von Microsoft

**Vorteile:**

- ✅ Kostenlos und Open Source
- ✅ Viele Extensions
- ✅ Syntax-Highlighting
- ✅ IntelliSense (Auto-Vervollständigung)
- ✅ Integriertes Terminal
- ✅ Git-Integration

### 2. VS Code Oberfläche

```text
┌─────────────────────────────────────────┐
│  Menü                                   │
├──────┬──────────────────────────────────┤
│      │                                  │
│ Ex-  │        Editor                    │
│ plo- │        (Code schreiben)          │
│ rer  │                                  │
│      │                                  │
├──────┴──────────────────────────────────┤
│  Terminal                               │
└─────────────────────────────────────────┘
```

**Wichtige Bereiche:**

- **Explorer:** Dateien und Ordner (links)
- **Editor:** Code schreiben (Mitte)
- **Terminal:** Befehle ausführen (unten)

### 3. Python-Datei vs. Shell

**Shell (REPL):**

- Interaktiv
- Sofortige Ergebnisse
- Nicht gespeichert

**Python-Datei (.py):**

- Gespeichert
- Wiederverwendbar
- Professionell

---

## 💻 Live-Coding (20 Min.)

### Demo 1: VS Code öffnen und einrichten (5 Min.)

1. **VS Code starten**
2. **Ordner öffnen:** `File` → `Open Folder`
3. **Neuen Ordner erstellen:** `python-kurs`
4. **Python-Extension prüfen:** Extensions-Symbol → "Python" suchen

### Demo 2: Erste Python-Datei (7 Min.)

1. **Neue Datei:** `File` → `New File` oder `Ctrl+N`
2. **Speichern als:** `hello.py`
3. **Code schreiben:**

```python
# Mein erstes Python-Programm
print("Hello, VS Code!")

name = "Python"
print(f"Ich lerne {name}")

# Einfache Berechnung
x = 10
y = 5
summe = x + y
print(f"{x} + {y} = {summe}")
```

4. **Speichern:** `Ctrl+S` / `Cmd+S`

### Demo 3: Code ausführen (4 Min.)

#### Methode 1: Run-Button

- Klick auf ▶️ (oben rechts)

#### Methode 2: Terminal

```bash
python hello.py
```

#### Methode 3: Rechtsklick

- Rechtsklick im Editor → "Run Python File in Terminal"

**Ausgabe im Terminal:**

```text
Hello, VS Code!
Ich lerne Python
10 + 5 = 15
```

### Demo 4: Debugging-Grundlagen (4 Min.)

**Absichtlicher Fehler:**

```python
print("Hallo"  # Klammer vergessen
```

**VS Code zeigt:**

- Rote Wellenlinie
- Fehlermeldung beim Ausführen

**Korrigieren:**

```python
print("Hallo")  # Klammer hinzugefügt
```

**Erklären:**

- VS Code hilft Fehler zu finden
- Rote Wellenlinien = Syntaxfehler
- Fehler vor dem Ausführen sichtbar

---

## ✏️ Übung (15 Min.)

### [Übung 3: Altersrechner](../02-uebungen/uebung-3-altersrechner.md)

**Aufgabe:**

Erstellen Sie eine Datei `altersrechner.py`:

```python
# Altersrechner
geburtsjahr = 2000
aktuelles_jahr = 2025
alter = aktuelles_jahr - geburtsjahr
print(f"Sie sind {alter} Jahre alt")
```

**Erweitern Sie:**

- Verschiedene Geburtsjahre testen
- Ausgabe formatieren
- Kommentare hinzufügen

---

## 🎨 VS Code Tipps

### Wichtige Shortcuts

**Windows/Linux:**

- `Ctrl+S` - Speichern
- `Ctrl+N` - Neue Datei
- Ctrl+` - Terminal öffnen/schliessen
- `Ctrl+/` - Kommentar ein/aus

**macOS:**

- `Cmd+S` - Speichern
- `Cmd+N` - Neue Datei
- Cmd+` - Terminal öffnen/schliessen
- `Cmd+/` - Kommentar ein/aus

### Nützliche Features

**Auto-Vervollständigung:**

- Tippen Sie `pri` → VS Code schlägt `print()` vor
- `Tab` zum Akzeptieren

**Mehrere Zeilen kommentieren:**

- Zeilen markieren
- `Ctrl+/` / `Cmd+/`

**Code formatieren:**

- `Shift+Alt+F` (Windows/Linux)
- `Shift+Option+F` (macOS)

---

## 📝 Zusammenfassung

**Wichtigste Punkte:**

1. VS Code = Professioneller Editor
2. Python-Dateien enden mit `.py`
3. Code ausführen: Run-Button oder Terminal
4. VS Code hilft Fehler zu finden
5. Shortcuts sparen Zeit

**Ausblick auf Lektion 4:**

- Variablen vertiefen
- Datentypen int und float
- Operatoren und Berechnungen
- Best Practices

---

## 🎓 Für Dozenten

### Vorbereitung

- [ ] VS Code geöffnet
- [ ] Python-Extension installiert
- [ ] Beispiel-Ordner vorbereitet

### Tipps

- **Langsam navigieren** - Zeigen Sie jeden Klick
- **Shortcuts erwähnen** - Aber nicht erzwingen
- **Terminal erklären** - Viele kennen es nicht
- **Fehler zeigen** - Nimmt Angst

### Häufige Probleme

**Python nicht gefunden:**

- `Ctrl+Shift+P` → "Python: Select Interpreter"
- Python-Installation wählen

**Terminal öffnet nicht:**

- `View` → `Terminal`
- Oder Ctrl+`

---

**Nächste Lektion:** [Lektion 4: Variablen und Zahlen](./lektion-4-variablen-zahlen.md)
