# Lektion 2: Claude Code — Erste Schritte

**Dauer:** 50 Minuten
**Format:** 10 Min Theorie + 25 Min Geführte Praxis + 15 Min Übung

## 🎯 Lernziele

- Claude Code installieren können
- Erste Interaktion mit Claude Code durchführen
- CLAUDE.md als Projektkontext verstehen

## 📖 Theorie (10 Min)

### Was ist Claude Code?

Claude Code ist ein **CLI-Tool** (Command Line Interface) von Anthropic. Es läuft direkt im Terminal und kann:

- Ihr gesamtes Projekt lesen und verstehen
- Dateien erstellen, bearbeiten und löschen
- Code erklären, debuggen und generieren
- Auf die Projektstruktur und den Kontext zugreifen

### Voraussetzungen

| Was | Warum |
|-----|-------|
| **Node.js** (v18+) | Claude Code ist ein Node.js-Paket |
| **Account** | Anthropic-Account oder GitHub-Login |
| **Terminal** | VS Code Terminal oder System-Terminal |

### CLAUDE.md — Die Bedienungsanleitung für die KI

Die Datei `CLAUDE.md` ist wie eine **Bedienungsanleitung**, die Sie der KI mitgeben:

```markdown
# CLAUDE.md

## Projektübersicht
Dieses Projekt ist ein Python-Einführungskurs...

## Code-Stil
- Deutsche Variablennamen (snake_case)
- Ausführliche Kommentare
- Docstrings in allen Funktionen
```

**Was passiert damit?**
- Claude Code liest diese Datei **automatisch** beim Start
- Die KI versteht dadurch den **Kontext** Ihres Projekts
- Antworten passen zum **Stil** und zur **Struktur** des Projekts

**Beispiel:** Die CLAUDE.md dieses Kursprojekts enthält:
- Projektstruktur (5 Module + Zusatzmodul)
- Naming Conventions (deutsche Namen, snake_case)
- Code-Stil Richtlinien (didaktischer Code)
- Git Workflow (Emoji Conventional Commits)

## 💻 Geführte Praxis (25 Min)

### Schritt 1: Installation (5 Min)

Öffnen Sie Ihr Terminal und führen Sie aus:

```bash
npm install -g @anthropic-ai/claude-code
```

**Häufige Fehlermeldungen und Lösungen:**

| Fehler | Lösung |
|--------|--------|
| `npm: command not found` | Node.js muss installiert werden |
| `EACCES permission denied` | Mit `sudo` ausführen (Mac/Linux) |
| `node version too old` | Node.js auf v18+ aktualisieren |

**Prüfen, ob es funktioniert:**

```bash
claude --version
```

### Schritt 2: Erster Start (5 Min)

Navigieren Sie zum Kurs-Repository und starten Sie Claude Code:

```bash
cd pfad/zum/pyt-intro-2025
claude
```

**Was Sie sehen:**
- Claude Code startet und zeigt eine Eingabeaufforderung
- Die KI liest automatisch die CLAUDE.md

**Erste Eingabe:**

```
Erkläre mir dieses Projekt in 3 Sätzen.
```

**Erwartete Antwort:** Claude Code beschreibt den Python-Einführungskurs, die Module, die Zielgruppe (Anfänger) — alles basierend auf der CLAUDE.md und der Projektstruktur.

### Schritt 3: CLAUDE.md erkunden (5 Min)

Öffnen Sie die Datei `CLAUDE.md` im Editor:

```bash
code CLAUDE.md
```

Gehen Sie gemeinsam durch:
1. **Projektübersicht** — Was erfährt die KI über den Kurs?
2. **Projektstruktur** — Wie findet die KI sich zurecht?
3. **Code-Stil** — Warum schreibt die KI deutschen Code?
4. **Naming Conventions** — Woher kennt die KI `snake_case`?

**Erkenntnis:** Die Qualität der CLAUDE.md bestimmt die Qualität der KI-Antworten.

### Schritt 4: Erste Aufgabe (10 Min)

Geben Sie in Claude Code ein:

```
Erkläre mir die Funktion berechne_durchschnitt aus Modul 4.
Erkläre für Anfänger, Zeile für Zeile.
```

**Was passiert:**
1. Claude Code **sucht** die Datei im Projekt
2. Claude Code **liest** den Code
3. Claude Code **erklärt** verständlich für Anfänger

**Gemeinsam besprechen:**
- Stimmt die Erklärung?
- Hat die KI den Code richtig verstanden?
- Ist die Erklärung für Anfänger verständlich?

**Weitere Aufgabe ausprobieren:**

```
Welche Python-Konzepte werden in Modul 3 behandelt?
```

Die KI durchsucht die Dateien von Modul 3 und fasst die Themen zusammen.

## ✏️ Übungen (15 Min)

### Übung 1: Eigenen Code erklären lassen

Wählen Sie eine **eigene Lösung** aus Modul 3 oder 4 und lassen Sie Claude Code diese erklären:

```
Erkläre mir den Code in [Dateiname].
Was macht jede Zeile?
```

**Aufgabe:** Notieren Sie:
- Was hat die KI **richtig** erkannt?
- Was hat die KI **nicht erwähnt** oder falsch erklärt?
- Welche Erklärung hat Ihnen am meisten geholfen?

### Übung 2: Projektfrage stellen

Stellen Sie Claude Code eine Frage zu diesem Kursprojekt:

Mögliche Fragen:
- "Wie viele Python-Dateien gibt es in Modul 2?"
- "Welche Übungen gibt es in Modul 3?"
- "Was steht in der README von Modul 1?"

**Aufgabe:** Vergleichen Sie die Antwort mit Ihrem eigenen Wissen:
- Ist die Antwort korrekt?
- Hat die KI die Information schneller gefunden als Sie?
- Wo könnte die KI falsch liegen?

## 📝 Zusammenfassung

| Schritt | Befehl |
|---------|--------|
| Installation | `npm install -g @anthropic-ai/claude-code` |
| Starten | `claude` (im Projektverzeichnis) |
| Beenden | `/exit` oder `Ctrl+C` |
| Projektkontext | Wird über `CLAUDE.md` bereitgestellt |

### Wichtige Punkte

✅ **DO:**
- Claude Code immer im Projektverzeichnis starten
- CLAUDE.md pflegen für bessere Antworten
- KI-Antworten kritisch prüfen

❌ **DON'T:**
- Claude Code ohne Projektkontext verwenden
- Antworten ungeprüft übernehmen
- Sensible Daten (Passwörter, API-Keys) eingeben

## 🔗 Weiter

[Lektion 3: Effektiv mit Claude Code arbeiten](./lektion-3-effektiv-arbeiten.md)
