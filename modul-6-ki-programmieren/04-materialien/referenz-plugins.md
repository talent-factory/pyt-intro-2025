# Referenz: Claude Code Plugins

> **Hinweis:** Plugins sind ein fortgeschrittenes Thema — dieser Überblick dient als Ausblick für Interessierte.

## Was sind Claude Code Plugins?

Plugins erweitern Claude Code um zusätzliche Fähigkeiten. Sie ermöglichen es Claude Code, mit externen Diensten zu kommunizieren, spezielle Aufgaben auszuführen oder auf zusätzliche Datenquellen zuzugreifen.

Plugins basieren auf dem **Model Context Protocol (MCP)** — einem offenen Standard, der KI-Modellen den Zugriff auf externe Werkzeuge ermöglicht.

## Beispiel-Plugins

### 1. Context7

- **Funktion:** Aktuelle Dokumentation von Bibliotheken abrufen
- **Nutzen:** Claude Code erhält Zugriff auf die neueste Dokumentation, statt sich auf sein Trainingswissen zu verlassen
- **Beispiel:** "Zeige mir die aktuelle Dokumentation für Flask"

### 2. Playwright

- **Funktion:** Webseiten im Browser steuern und testen
- **Nutzen:** Automatisierte Browser-Tests, Screenshots erstellen, Formulare ausfüllen
- **Beispiel:** "Öffne die Webseite und mache einen Screenshot"

### 3. Sentry

- **Funktion:** Fehler-Monitoring und -Analyse
- **Nutzen:** Produktionsfehler direkt in Claude Code analysieren
- **Beispiel:** "Zeige mir die letzten Fehler in meiner Anwendung"

### 4. Linear / GitHub

- **Funktion:** Projekt-Management und Issue-Tracking
- **Nutzen:** Issues erstellen, Pull Requests verwalten, direkt aus Claude Code
- **Beispiel:** "Erstelle ein Issue für diesen Bug"

## Plugin-Installation

Plugins werden in den Claude Code Einstellungen konfiguriert. Die genaue Installation variiert je nach Plugin.

```bash
# Beispiel: Plugin-Konfiguration in den Einstellungen
claude settings
```

## Weiterführende Informationen

Eine ausführliche Übersicht über verfügbare Plugins und deren Installation finden Sie hier:

**[Claude Code Plugins — Talent Factory](https://talent-factory.xyz/tools/claude-plugins/)**

## Für wen sind Plugins?

Plugins sind besonders nützlich für:

- **Fortgeschrittene Entwickler**, die ihren Workflow automatisieren möchten
- **Teams**, die Claude Code in bestehende Werkzeuge integrieren wollen
- **Spezielle Anwendungsfälle**, die über Standard-Programmierung hinausgehen

Für den Einstieg in die KI-gestützte Programmierung sind Plugins **nicht erforderlich**. Konzentrieren Sie sich zunächst auf die Grundlagen von Claude Code und effektives Prompt-Schreiben.
