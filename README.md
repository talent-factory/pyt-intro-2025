# Python Programmierung Basis

Ein praxisorientierter Einführungskurs in Python für absolute Anfänger ohne Programmierkenntnisse.

## 🎯 Kursziele

Nach Abschluss des Kurses können Sie:

- Die wichtigsten Programmiergrundlagen verstehen und anwenden
- Kleinere Programme in Python selbstständig schreiben
- Mit der Entwicklungsumgebung VS Code professionell arbeiten
- Variablen, Datentypen und Operatoren sicher einsetzen
- Kontrollstrukturen (if/else, Schleifen) implementieren
- Funktionen definieren und nutzen
- Dateien lesen und schreiben
- Code modular strukturieren

## 📚 Kursstruktur

Der Kurs umfasst **7 Module** mit je **4 Lektionen à 50 Minuten**:

### [Modul 1: Einstieg in die Programmierung](./modul-1-einstieg/)

**Was ist Programmieren? Erste Schritte mit Python**

- Programmieren verstehen - was heisst das?
- Python Shell & erste Schritte (REPL, Jupyter)
- VS Code als Entwicklungsumgebung
- Variablen, Zahlen und einfache Operationen

### [Modul 2: Grundlegende Datentypen und Operatoren](./modul-2-datentypen/)

**Mit Daten arbeiten**

- Strings - Texte verarbeiten
- Boolsche Werte und Vergleiche
- Typkonvertierung und Input/Output
- Interaktive Programme erstellen

### [Modul 3: Kontrollstrukturen und Prozedurale Programmierung](./modul-3-kontrollstrukturen/)

**Programmfluss steuern**

- Bedingte Anweisungen (if/elif/else)
- For-Schleifen und Iteration
- While-Schleifen und Schleifenkontrolle
- Verschachtelte Strukturen und Algorithmen

### [Modul 4: Datenstrukturen und Funktionen](./modul-4-funktionen-datenstrukturen/)

**Code organisieren und wiederverwenden**

- Listen - Sammlungen von Daten
- Dictionaries - Schlüssel-Wert-Paare
- Funktionen definieren und aufrufen
- Code modular strukturieren

### [Modul 5: Dateien, Module und Mini-Projekte](./modul-5-dateien-module/)

**Reale Anwendungen entwickeln**

- Dateien lesen und schreiben
- CSV-Dateien verarbeiten
- Module und Modularisierung
- Mini-Projekt-Workshop

### [Modul 6: KI-gestütztes Programmieren](./modul-6-ki-programmieren/)

**KI als Programmierpartner**

- KI-Landschaft: Chat, IDE, CLI
- Claude Code: Installation und erste Schritte
- Effektives Prompting und iteratives Arbeiten
- Showcase: Plugins, Skills und Agenten

### [Modul 7: Objektorientierte Programmierung](./modul-7-oop/)

**Klassen und Objekte**

- Klassen und Objekte verstehen
- Methoden und \_\_str\_\_ implementieren
- Klassen mit pytest testen
- Mini-Projekt: Kontaktverwaltung

## 🎓 Zielgruppe

- **Anfänger ohne Programmierkenntnisse**
- Lernfreudige Personen, die Python lernen möchten
- Keine Vorkenntnisse erforderlich
- Eigenes Notebook erforderlich

## 💻 Technische Voraussetzungen

### Option 1: GitHub Codespaces (empfohlen für Anfänger)

- Nur Browser und GitHub-Account erforderlich
- Keine lokale Installation notwendig
- Sofort einsatzbereit

### Option 2: Lokale Installation

- **Python** 3.11 oder höher
- **VS Code** (neueste Version)
- **Git** (neueste Version)
- **uv** - Package Manager

Detaillierte Installationsanleitungen finden Sie in [Modul 1 - Vorbereitung](./modul-1-einstieg/00-vorbereitung/).

## 📖 Modulaufbau

Jedes Modul folgt einer konsistenten Struktur:

### 00-vorbereitung (2-3 Stunden vor dem Präsenztag)

- Leseaufträge und Videos
- Vorbereitende Übungen
- Setup und Installation

### 01-praxis (4 Lektionen à 50 Minuten)

- **Theorie:** Konzepte verstehen (15 Min.)
- **Live-Demo:** Best Practices zeigen (20 Min.)
- **Übungen:** Praktische Anwendung (15 Min.)

### 02-uebungen

- Praktische Übungen während der Präsenzzeit
- Verschiedene Schwierigkeitsgrade
- Pair-Programming möglich

### 03-nachbearbeitung (4-6 Stunden nach dem Präsenztag)

- 3-4 vertiefende Aufgaben
- Persönliche Reflexion
- Abgabe vor dem nächsten Modul

### 04-materialien

- Handouts und Cheatsheets
- Referenzmaterial
- Zusätzliche Ressourcen

### 05-beispiele

- Code-Beispiele vom Dozenten
- Musterlösungen
- Best-Practice-Implementierungen

## 🚀 Schnellstart

### Mit GitHub Codespaces

1. Repository auf GitHub öffnen
2. Auf "Code" → "Codespaces" → "Create codespace" klicken
3. Warten bis Umgebung bereit ist
4. Loslegen!

### Lokal

```bash
# Repository klonen
git clone https://github.com/talent-factory/pyt-intro-2025.git
cd pyt-intro-2025

# Dependencies installieren
pip install uv
uv sync

# Jupyter starten (optional)
uv run jupyter notebook
```

### Repository aktualisieren

Falls Änderungen am Kursmaterial vorgenommen wurden, können Sie diese wie folgt abrufen:

```bash
# Ins Repository-Verzeichnis wechseln
cd pyt-intro-2025

# Änderungen vom Server abrufen
git pull
```

**Falls Sie auf einem eigenen Branch arbeiten:**

Wenn Sie Ihre Übungen auf einem eigenen Branch bearbeiten, gehen Sie wie folgt vor:

```bash
# 1. Aktuellen Stand committen (falls nötig)
git add .
git commit -m "Meine Änderungen"

# 2. Zum develop-Branch wechseln und aktualisieren
git checkout develop
git pull

# 3. Zurück zu Ihrem Branch wechseln
git checkout mein-branch

# 4. Änderungen von develop in Ihren Branch übernehmen
git merge develop
```

> 💡 **Tipp:** Falls beim Merge Konflikte auftreten, fragen Sie Ihren Kursleiter um Hilfe.

## 📊 Zeitaufwand

- **Vorbereitung:** 2-3 Stunden pro Modul
- **Präsenz:** 4 Stunden pro Tag (inkl. Pausen)
- **Nachbearbeitung:** 4-6 Stunden pro Modul
- **Gesamt:** ca. 70-85 Stunden über 7 Wochen

## 📞 Support & Kontakt

Bei Fragen oder Problemen:

- **E-Mail:** [daniel.senften@talent-factory.ch](mailto:daniel.senften@talent-factory.ch)
- **Website:** [Talent Factory](https://talent-factory.xyz)

## 📄 Lizenz

© 2025 Talent Factory. Alle Rechte vorbehalten.

Die Kursmaterialien sind für Kursteilnehmer lizenziert.

---

**Bereit für Ihre Python-Reise? Starten Sie mit [Modul 1](./modul-1-einstieg/)!**
