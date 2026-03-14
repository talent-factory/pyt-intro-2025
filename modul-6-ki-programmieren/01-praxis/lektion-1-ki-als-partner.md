# Lektion 1: KI als Programmierpartner

**Dauer:** 50 Minuten
**Format:** 15 Min Theorie + 20 Min Live-Demo + 15 Min Übung

## 🎯 Lernziele

- Verstehen, was KI-gestütztes Programmieren bedeutet
- Die drei Kategorien (Chat, IDE, CLI) unterscheiden können
- Erste Prompts formulieren können

## 📖 Theorie (15 Min)

### Was ist KI-gestütztes Programmieren?

KI-gestütztes Programmieren bedeutet, dass Sie eine künstliche Intelligenz als **Werkzeug** nutzen, um schneller und effektiver zu programmieren. Stellen Sie sich die KI als einen erfahrenen Kollegen vor, der neben Ihnen sitzt:

- Sie können **Fragen stellen**: "Wie funktioniert eine for-Schleife?"
- Sie können um **Hilfe bitten**: "Finde den Fehler in meinem Code"
- Sie können **Aufgaben delegieren**: "Schreibe eine Funktion, die Zahlen sortiert"

> **Wichtig:** Die KI ist ein Werkzeug, kein Ersatz für Ihr Verständnis. Sie müssen den Code, den die KI liefert, **verstehen und prüfen** können.

### Drei Kategorien von KI-Programmierwerkzeugen

| Kategorie | Beispiele | Wie es funktioniert |
|-----------|-----------|---------------------|
| **Chat** | Claude.ai, ChatGPT | Im Browser, Copy-Paste von Code |
| **IDE-Integration** | GitHub Copilot | Direkt in VS Code, automatische Vorschläge |
| **CLI** | Claude Code, Gemini CLI | Im Terminal, kennt Ihr Projekt |

#### Chat (Claude.ai, ChatGPT)

Sie schreiben eine Frage in den Browser und erhalten eine Antwort mit Code:

**Stärken:**
- Einfach zu bedienen, keine Installation
- Gut für einzelne Fragen und Erklärungen
- Ideal zum Lernen und Verstehen

**Schwächen:**
- Kein Zugriff auf Ihr Projekt
- Code muss manuell kopiert werden
- Kein Kontext über Ihre bisherige Arbeit

#### IDE-Integration (GitHub Copilot)

Die KI ist direkt in Ihren Editor eingebaut und schlägt Code vor, während Sie tippen:

**Stärken:**
- Nahtlose Integration in den Arbeitsfluss
- Schnelle Inline-Vorschläge
- Sieht die aktuell geöffnete Datei

**Schwächen:**
- Vorschläge manchmal unpassend
- Sieht nur begrenzt den Projektkontext
- Kann zu unkritischem Übernehmen verleiten

#### CLI (Claude Code, Gemini CLI)

Die KI läuft im Terminal und hat Zugriff auf Ihr gesamtes Projekt:

**Stärken:**
- Kennt das gesamte Projekt (alle Dateien)
- Kann Dateien lesen, erstellen und bearbeiten
- Volle Kontrolle, Terminal-Nähe
- Versteht Projektkontext durch CLAUDE.md

**Schwächen:**
- Erfordert Terminal-Kenntnisse
- Installation notwendig
- Höhere Einstiegshürde

### Warum CLI?

In diesem Modul konzentrieren wir uns auf **Claude Code** (CLI), weil:

1. **Volle Kontrolle:** Sie sehen genau, was die KI tut
2. **Projektkontext:** Die KI kennt Ihr gesamtes Projekt
3. **Terminal-Nähe:** Sie arbeiten dort, wo Python läuft
4. **Transparenz:** Jede Aktion wird angezeigt und kann bestätigt oder abgelehnt werden

## 💻 Live-Demo (20 Min)

### Demo 1: Chat-basiert (Claude.ai)

**Aufgabe:** "Schreibe eine Funktion berechne_durchschnitt"

Im Browser auf claude.ai eingeben:

```
Schreibe eine Python-Funktion berechne_durchschnitt,
die eine Liste von Zahlen nimmt und den Durchschnitt berechnet.
```

**Typische Antwort der KI:**

```python
def berechne_durchschnitt(zahlen):
    """Berechnet den Durchschnitt einer Liste von Zahlen."""
    if not zahlen:
        return 0
    return sum(zahlen) / len(zahlen)
```

**Diskussion:**
- ✅ Die Funktion ist korrekt und kompakt
- ⚠️ Aber: Die KI kennt unseren Kurs-Stil nicht (wir verwenden ausführlichere Schleifen statt `sum()`)
- ⚠️ Code muss manuell in das Projekt kopiert werden

### Demo 2: IDE-Integration (Copilot in VS Code)

**Aufgabe:** In VS Code eine neue Datei öffnen und tippen:

```python
def berechne_durchschnitt(zahlen):
    """Berechnet den Durchschnitt einer Liste von Zahlen."""
```

Copilot schlägt automatisch den Rest vor (graue Schrift):

```python
    summe = sum(zahlen)
    return summe / len(zahlen)
```

**Diskussion:**
- ✅ Schnell, direkt im Editor
- ⚠️ Vorschlag passt nicht immer zum gewünschten Stil
- ⚠️ Sieht nicht die anderen Dateien im Projekt

### Demo 3: CLI (Claude Code)

**Aufgabe:** Im Terminal, im Kurs-Repository:

```bash
claude
```

Dann eingeben:

```
Erkläre mir die Funktion berechne_durchschnitt aus Modul 4
```

**Was passiert:**
- Claude Code **durchsucht** das Projekt nach der Funktion
- Claude Code **liest** die Datei und den umgebenden Code
- Claude Code **erklärt** im Kontext des Kurses

**Diskussion:**
- ✅ Die KI kennt das Projekt und findet die Datei selbst
- ✅ Erklärung passt zum Kurs-Kontext
- ✅ Kein Copy-Paste nötig
- Das ist der **grosse Unterschied:** Projektkontext!

## ✏️ Übungen (15 Min)

### Übung 1: Prompts formulieren

Formulieren Sie **3 verschiedene Prompts** für folgende Aufgabe:

> "Erstelle ein Programm, das prüft ob eine Zahl eine Primzahl ist"

Variieren Sie Ihre Prompts:
- Einen kurzen, vagen Prompt
- Einen mittleren Prompt mit mehr Details
- Einen ausführlichen Prompt mit genauen Anforderungen

**Beispiel für einen ausführlichen Prompt:**

```
Schreibe eine Python-Funktion ist_primzahl(zahl), die einen
Integer als Parameter nimmt und True zurückgibt, wenn die Zahl
eine Primzahl ist, sonst False. Verwende eine for-Schleife.
Füge einen Docstring und deutsche Kommentare hinzu.
```

### Übung 2: Prompt-Qualität bewerten

Welcher Prompt ist besser? Begründen Sie Ihre Antwort.

**(A)** "Schreibe Code"

**(B)** "Schreibe eine Python-Funktion `ist_primzahl(zahl)`, die `True` zurückgibt, wenn die übergebene Zahl eine Primzahl ist, und `False` sonst. Verwende deutsche Variablennamen und Kommentare."

**Lösung:**
- Prompt (B) ist deutlich besser, weil er **spezifisch** ist:
  - Sprache: Python
  - Funktionsname: `ist_primzahl`
  - Parameter: `zahl`
  - Rückgabewert: `True`/`False`
  - Stil: Deutsche Namen und Kommentare
- Prompt (A) gibt der KI keine Richtung — das Ergebnis ist unvorhersehbar

## 📝 Zusammenfassung

| Kategorie | Wann verwenden? |
|-----------|-----------------|
| **Chat** | Einzelne Fragen, Lernen, Erklärungen |
| **IDE** | Schnelle Ergänzungen beim Tippen |
| **CLI** | Projektweites Arbeiten, komplexe Aufgaben |

### Wichtige Punkte

✅ **DO:**
- KI als Werkzeug verstehen, nicht als Ersatz
- Spezifische, klare Prompts formulieren
- Code der KI immer prüfen und verstehen

❌ **DON'T:**
- Code blind übernehmen ohne Verständnis
- Vage Prompts wie "Schreibe Code" verwenden
- KI-Antworten als immer korrekt annehmen

## 🔗 Weiter

[Lektion 2: Claude Code — Erste Schritte](./lektion-2-claude-code-einstieg.md)
