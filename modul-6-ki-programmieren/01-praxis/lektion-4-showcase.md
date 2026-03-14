# Lektion 4: Showcase — Was noch möglich ist

**Dauer:** 50 Minuten
**Format:** 10 Min Theorie + 30 Min Live-Demo durch Dozent + 10 Min Diskussion

## 🎯 Lernziele

- Das Claude Code Ökosystem kennen
- Fortgeschrittene Möglichkeiten einordnen können
- Ethik und Verantwortung beim KI-Einsatz reflektieren

## 📖 Theorie (10 Min)

### Das Claude Code Ökosystem

Claude Code ist mehr als ein einfaches Chat-Tool im Terminal. Es bietet ein ganzes Ökosystem an Erweiterungen:

| Feature | Erklärung | Beispiel |
|---------|-----------|---------|
| **Commands** | Eigene Befehle definieren, die wiederverwendbar sind | `/commit` erstellt automatisch einen Commit mit passender Nachricht |
| **Skills** | Komplexe Workflows als wiederverwendbare Anleitungen | Ein Skill für "Neue Lektion erstellen" führt alle Schritte durch |
| **Plugins** | Externe Dienste anbinden (MCP-Server) | Linear-Plugin zum Lesen und Erstellen von Issues |
| **Agenten** | KI arbeitet eigenständig an komplexen Aufgaben | Agent erstellt ein komplettes Modul mit allen Dateien |

> **Hinweis:** Diese Features sind fortgeschritten. Sie müssen sie heute nicht beherrschen — es geht darum, die **Möglichkeiten** zu kennen.

### Weiterführende Ressourcen

Auf der Talent Factory Website finden Sie eine kuratierte Übersicht aller Plugins und Erweiterungen:

🔗 [talent-factory.xyz/tools/claude-plugins/](https://talent-factory.xyz/tools/claude-plugins/)

## 💻 Live-Demo durch Dozent (30 Min)

> **Hinweis für Studierende:** In dieser Phase zeigt der Dozent fortgeschrittene Funktionen. Sie schauen zu und stellen Fragen. Ziel ist es, ein Gefühl dafür zu bekommen, was möglich ist.

### Demo 1: Plugin im Einsatz (10 Min)

Der Dozent zeigt 1-2 Plugins, die im Kurs verwendet wurden:

**Beispiel: Linear-Plugin**

```
Zeige mir alle offenen Issues im Projekt pyt-intro-2025.
```

Die KI verbindet sich mit Linear (Projektmanagement-Tool) und listet die Issues auf — direkt im Terminal, ohne Browser.

**Beispiel: Playwright-Plugin**

```
Öffne die Seite talent-factory.xyz und mache einen Screenshot.
```

Die KI steuert einen Browser, navigiert zur Seite und speichert einen Screenshot.

**Diskussion:**
- Was ist der Vorteil gegenüber manuellem Arbeiten?
- Wann macht ein Plugin Sinn, wann nicht?

### Demo 2: Skill-Workflow (10 Min)

Ein **Skill** ist eine gespeicherte Anleitung, die Claude Code Schritt für Schritt abarbeitet.

**Beispiel: Skill "Neue Lektion erstellen"**

Der Dozent zeigt, wie ein Skill den kompletten Workflow automatisiert:

1. **Brainstorming:** KI generiert Lernziele und Themenvorschläge
2. **Struktur:** KI erstellt die Markdown-Datei mit allen Abschnitten
3. **Inhalt:** KI füllt Theorie, Code-Beispiele und Übungen
4. **Review:** KI prüft auf Konsistenz mit den anderen Lektionen

```
/skill neue-lektion "Lektion über Dictionaries"
```

**Diskussion:**
- Wie viel Zeit spart das?
- Was muss der Mensch trotzdem prüfen?

### Demo 3: Autonomer Agent (10 Min)

Ein **Agent** ist Claude Code im autonomen Modus. Die KI plant und führt mehrere Schritte eigenständig aus.

**Beispiel:** Der Dozent gibt eine komplexe Aufgabe:

```
Erstelle ein Python-Programm, das:
1. Eine CSV-Datei mit Schülernoten einliest
2. Den Durchschnitt pro Schüler berechnet
3. Eine Zusammenfassung als Textdatei erstellt
4. Fehlerbehandlung für ungültige Dateien einbaut

Erstelle auch 3 Testfälle.
```

**Was passiert:**
- Claude Code **plant** die Aufgabe (welche Dateien, welche Struktur)
- Claude Code **erstellt** die Dateien Schritt für Schritt
- Claude Code **testet** den Code
- Der Dozent zeigt jeden Schritt und erklärt, was die KI tut

**Diskussion:**
- Würden Sie dem Ergebnis vertrauen?
- Was könnte schiefgehen?
- Wo braucht es menschliche Kontrolle?

## 🗣️ Diskussion (10 Min)

### Diskussionsfragen

Diskutieren Sie in der Gruppe:

**1. KI im Programmieralltag**
> Wie wird KI Ihren Programmieralltag verändern? Werden Programmierer überflüssig, oder werden sie produktiver?

**2. Risiken von blindem Übernehmen**
> Was kann passieren, wenn man KI-generierten Code ohne Prüfung übernimmt? Kennen Sie Beispiele für Fehler, die KI-Tools machen?

**3. Urheberrecht und Ethik**
> Wem gehört Code, den eine KI generiert? Darf man KI-Code in kommerziellen Projekten verwenden?

### Alternativen und Marktübersicht

| Tool | Typ | Stärke | Link |
|------|-----|--------|------|
| **Claude Code** | CLI | Projektkontext, Plugins | [claude.ai/download](https://claude.ai/download) |
| **GitHub Copilot** | IDE | Inline-Vorschläge in VS Code | [github.com/features/copilot](https://github.com/features/copilot) |
| **Codex CLI** | CLI | OpenAI-basiert, Open Source | [github.com/openai/codex](https://github.com/openai/codex) |
| **OpenCode CLI** | CLI | Leichtgewichtig, mehrere Anbieter | [github.com/opencode-ai/opencode](https://github.com/opencode-ai/opencode) |
| **Gemini CLI** | CLI | Google-basiert, grosses Kontextfenster | [github.com/google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli) |

## 📝 Zusammenfassung

### Was Sie heute gelernt haben

| Lektion | Kernaussage |
|---------|-------------|
| **Lektion 1** | KI-Tools gibt es in 3 Kategorien: Chat, IDE, CLI |
| **Lektion 2** | Claude Code installieren und erste Schritte |
| **Lektion 3** | Spezifisch, kontextreich und iterativ prompting |
| **Lektion 4** | Plugins, Skills und Agenten erweitern die Möglichkeiten |

### Drei Dinge zum Mitnehmen

1. **KI ist ein Werkzeug** — Sie bleiben der Fahrer, die KI ist das Navigationssystem
2. **Verstehen vor Verwenden** — Übernehmen Sie nur Code, den Sie verstehen
3. **Übung macht den Meister** — Je mehr Sie prompten, desto besser werden Ihre Ergebnisse

### Wichtige Punkte

✅ **DO:**
- KI-Tools als Produktivitätswerkzeug einsetzen
- Verschiedene Tools ausprobieren und vergleichen
- Ethische Fragen im Team diskutieren
- Weiterlernen und experimentieren

❌ **DON'T:**
- KI blind vertrauen ohne Verständnis
- Urheberrechtsfragen ignorieren
- Aufhören, selbst zu programmieren
- Sensible Daten an KI-Tools weitergeben

## 🔗 Weiterführende Links

- [Talent Factory: Claude Plugins](https://talent-factory.xyz/tools/claude-plugins/)
- [Claude Code Dokumentation](https://docs.anthropic.com/en/docs/claude-code)
- [Nachbearbeitung Modul 6](../03-nachbearbeitung/)
