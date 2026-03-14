# Cheatsheet: Claude Code

## Installation

```bash
npm install -g @anthropic-ai/claude-code
```

## Starten

```bash
# Im Projektverzeichnis starten
cd mein-projekt
claude
```

## Wichtigste Slash-Commands

| Command | Beschreibung |
|---------|-------------|
| `/help` | Hilfe anzeigen |
| `/clear` | Konversation zurücksetzen |
| `/compact` | Kontext komprimieren |
| `/cost` | Bisherige Kosten anzeigen |

## Tastenkürzel

| Kürzel | Aktion |
|--------|--------|
| `Tab` | Autocomplete / Vorschlag annehmen |
| `Ctrl+C` | Aktuelle Aktion abbrechen |
| `Escape` | Zurück / Abbrechen |
| `Enter` | Nachricht senden |
| `Shift+Enter` | Neue Zeile (mehrzeilig) |

## CLAUDE.md — Projektkontext

Erstellen Sie eine `CLAUDE.md`-Datei im Projektverzeichnis:

```markdown
# CLAUDE.md
Dieses Projekt ist ein Python-Programm für ...
- Sprache: Python 3.11
- Stil: Deutsche Variablennamen
- Kommentare: Deutsch
```

Claude Code liest diese Datei automatisch und kennt so den Projektkontext.

## Häufige Prompts

```
# Code erklären
"Erkläre mir, was dieser Code macht."

# Fehler finden
"Mein Code gibt folgenden Fehler: [Fehlermeldung]"

# Code generieren
"Erstelle eine Funktion, die [Beschreibung]."

# Code verbessern
"Verbessere diesen Code hinsichtlich Lesbarkeit."

# Tests schreiben
"Schreibe Tests für diese Funktion."
```

## Tipps für Anfänger

1. **Spezifisch fragen** — Je genauer der Prompt, desto besser die Antwort
2. **Ergebnis prüfen** — KI-Code immer testen, nicht blind übernehmen
3. **Iterativ arbeiten** — Auf Antworten aufbauen und verfeinern
4. **Kontext geben** — Relevanten Code oder Fehlermeldungen mitschicken
5. **Nachfragen** — Bei Unklarheiten um Erklärung bitten

## Workflow

```
1. Projekt öffnen    →  cd mein-projekt
2. Claude starten    →  claude
3. Aufgabe stellen   →  "Erstelle eine Funktion, die ..."
4. Ergebnis prüfen   →  Code lesen und verstehen
5. Testen            →  python mein_skript.py
6. Verfeinern        →  "Füge bitte ... hinzu"
```

## Gut zu wissen

- Claude Code arbeitet direkt mit Ihren Dateien im Projektverzeichnis
- Änderungen an Dateien werden erst nach Ihrer Bestätigung gemacht
- Sie können jederzeit mit `/clear` einen neuen Dialog starten
- Die `CLAUDE.md`-Datei hilft Claude, Ihr Projekt zu verstehen
