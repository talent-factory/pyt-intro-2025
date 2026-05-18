# Leseauftrag: KI-gestütztes Programmieren

**Zeitaufwand:** 60-90 Minuten

## 1. Was ist KI-gestütztes Programmieren?

KI-gestütztes Programmieren bedeutet, dass Sie eine Künstliche Intelligenz als Werkzeug beim Programmieren einsetzen. Die KI kann Ihnen helfen, Code zu schreiben, Fehler zu finden, Code zu erklären und vieles mehr.

**Wichtig:** Die KI ist ein Werkzeug — genau wie ein Taschenrechner in der Mathematik. Sie müssen verstehen, was Sie tun, und die Ergebnisse kritisch prüfen.

### Was kann KI beim Programmieren?

- **Code erklären:** "Was macht diese Funktion?"
- **Code schreiben:** "Schreibe eine Funktion, die Primzahlen findet"
- **Fehler finden:** "Warum funktioniert mein Code nicht?"
- **Code verbessern:** "Wie kann ich diesen Code besser machen?"
- **Konzepte erklären:** "Was ist eine Schleife?"

### Was kann KI NICHT?

- Immer korrekten Code liefern
- Ihre Absichten erraten, wenn der Prompt unklar ist
- Komplexe Geschäftslogik ohne Kontext verstehen
- Verantwortung für den Code übernehmen

## 2. Drei Wege: Chat, IDE, CLI

Es gibt drei Hauptkategorien von KI-Tools für Programmierer:

### Chat-basierte Tools

**Beispiele:** Claude.ai, ChatGPT, Gemini

**So funktioniert es:** Sie öffnen eine Website, tippen Ihre Frage ein und erhalten eine Antwort. Den generierten Code müssen Sie dann manuell kopieren und in Ihr Programm einfügen.

**Beispiel-Prompt:**
> "Erkläre mir den Unterschied zwischen einer while-Schleife und einer for-Schleife in Python. Gib mir je ein Beispiel."

**Vorteile:**
- Kostenlos verfügbar
- Kein Setup nötig
- Gut für Erklärungen und Lernfragen

**Nachteile:**
- Kein Zugriff auf Ihren Code
- Manuelles Copy-Paste nötig
- Kennt Ihr Projekt nicht

### IDE-Integrationen

**Beispiele:** GitHub Copilot, Cursor, Cody

**So funktioniert es:** Die KI ist direkt in Ihren Code-Editor eingebaut. Während Sie tippen, schlägt sie automatisch Code-Vervollständigungen vor.

**Vorteile:**
- Nahtlose Integration
- Sieht Ihren aktuellen Code
- Automatische Vorschläge

**Nachteile:**
- Oft kostenpflichtig
- Kann ablenkend sein
- Vorschläge nicht immer passend

### CLI-Tools (Command-Line Interface)

**Beispiele:** Claude Code, GitHub Copilot CLI, Aider

**So funktioniert es:** Sie arbeiten im Terminal (Kommandozeile) und geben der KI Aufgaben. Die KI kann direkt auf Ihre Projektdateien zugreifen, Code lesen, ändern und sogar Befehle ausführen.

**Beispiel-Prompt:**
> "Lies die Datei main.py und erkläre mir, was sie macht."

**Vorteile:**
- Direkter Zugriff auf Ihr Projekt
- Kann Dateien lesen und ändern
- Arbeitet im Projektkontext

**Nachteile:**
- Terminal-Kenntnisse nötig
- Erfordert Installation
- Oft kostenpflichtig

## 3. Was ist ein Prompt?

Ein **Prompt** ist die Anweisung, die Sie der KI geben. Je besser Ihr Prompt, desto besser die Antwort.

### Schlechter Prompt

> "Hilf mir mit Python"

**Problem:** Zu vage. Die KI weiss nicht, was Sie brauchen.

### Guter Prompt

> "Schreibe eine Python-Funktion namens `berechne_durchschnitt`, die eine Liste von Zahlen als Parameter nimmt und den Durchschnitt zurückgibt. Verwende deutsche Variablennamen und füge einen Docstring hinzu."

**Warum besser?**
- Spezifische Aufgabe
- Klare Anforderungen (Funktionsname, Parameter)
- Stil-Vorgaben (deutsche Namen, Docstring)

### Tipps für gute Prompts

1. **Sei spezifisch:** Beschreiben Sie genau, was Sie brauchen
2. **Gib Kontext:** Erklären Sie, wofür der Code ist
3. **Nenne Einschränkungen:** z.B. "für Anfänger verständlich"
4. **Iteriere:** Wenn das Ergebnis nicht passt, verfeinern Sie den Prompt
5. **Gib Beispiele:** Zeigen Sie, wie das Ergebnis aussehen soll

### Iteratives Prompting

Oft liefert der erste Prompt nicht das perfekte Ergebnis. Das ist normal! Verfeinern Sie schrittweise:

1. **Erster Prompt:** "Schreibe eine Funktion für Primzahlen"
2. **Verfeinerung:** "Füge Fehlerbehandlung für negative Zahlen hinzu"
3. **Verfeinerung:** "Optimiere die Funktion für grosse Zahlen"

## 4. Ethik und Verantwortung

### Sie sind verantwortlich

Wenn Sie KI-generierten Code verwenden, sind **Sie** dafür verantwortlich:
- Dass der Code korrekt funktioniert
- Dass der Code sicher ist
- Dass der Code die Aufgabe erfüllt

### Häufige Probleme mit KI-Code

- **Halluzinationen:** Die KI erfindet manchmal Funktionen oder Bibliotheken, die nicht existieren
- **Veralteter Code:** Die KI kennt möglicherweise nicht die neuesten Versionen
- **Fehlende Randfälle:** Die KI vergisst oft Sonderfälle (z.B. leere Listen, negative Zahlen)
- **Sicherheitslücken:** KI-Code kann Sicherheitsprobleme enthalten

### Goldene Regeln

1. **Verstehen Sie den Code:** Verwenden Sie keinen Code, den Sie nicht verstehen
2. **Testen Sie immer:** Prüfen Sie KI-generierten Code gründlich
3. **Lernen Sie weiter:** KI ersetzt nicht das Lernen von Programmierung
4. **Seien Sie ehrlich:** Kennzeichnen Sie KI-Unterstützung, wenn verlangt
5. **Bleiben Sie kritisch:** Hinterfragen Sie jede KI-Antwort

---

Weiter zu den [Ersten Experimenten](./erste-experimente.md)
