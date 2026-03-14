# CLAUDE.md - KI-Assistenten Projektdokumentation

> Dieses Dokument dient als Schnellreferenz für KI-Assistenten zur Navigation und zum Verständnis des Projekts.

## Projektübersicht

**Name:** Python Programmierung Basis - Einführungskurs 2025
**Repository:** pyt-intro-2025
**Zielgruppe:** Absolute Anfänger ohne Programmierkenntnisse
**Umfang:** 5 Module + 1 Zusatzmodul, je 1 Präsenztag, ~60-73 Stunden gesamt

## Projektstruktur

```
pyt-intro-2025/
├── modul-1-einstieg/                   ✅ Vollständig
├── modul-2-datentypen/                 ✅ Vollständig
├── modul-3-kontrollstrukturen/         ✅ Vollständig
├── modul-4-funktionen-datenstrukturen/ ⚠️ In Entwicklung
├── modul-5-dateien-module/             ⚠️ In Entwicklung
├── modul-6-ki-programmieren/           ⚠️ Zusatzmodul, in Entwicklung
├── refs/                               (Referenzmaterialien)
├── .devcontainer/                      (GitHub Codespaces Config)
├── README.md                           (Haupt-Dokumentation)
├── CLAUDE.md                           (Dieses Dokument)
├── pyproject.toml                      (Python Projekt-Config)
└── main.py                             (Entry Point)
```

## Standard-Modulstruktur

Jedes Modul folgt dieser **identischen** 6-Ordner-Struktur:

```
modul-X-thema/
├── 00-vorbereitung/     # Leseauftrag, Experimente, Quiz
│   ├── README.md
│   ├── leseauftrag.md
│   ├── erste-experimente.md
│   └── quiz.md
├── 01-praxis/           # 4 Lektionen à 50 Min
│   ├── README.md
│   └── lektion-X-titel.md
├── 02-uebungen/         # 4-8 Übungen
│   ├── README.md
│   └── uebung-X-titel.md
├── 03-nachbearbeitung/  # 3 Aufgaben + Reflexion
│   ├── README.md
│   ├── aufgabe-X-titel.md
│   └── reflexion.md
├── 04-materialien/      # Handouts, Cheatsheets
│   └── README.md
├── 05-beispiele/        # Python-Beispielcode
│   ├── README.md
│   └── *.py
└── README.md            # Modul-Übersicht
```

## Entwicklungsstand (Stand: 2025-11-27)

### ✅ Vollständig produktionsreif

| Modul | Status | Python-Dateien | Lektionen | Übungen |
|-------|--------|----------------|-----------|---------|
| **Modul 1** | ✅ | 10 vollständig | 4 | 4 |
| **Modul 2** | ✅ | 9 vollständig | 4 | 8 |
| **Modul 3** | ✅ | 10 vollständig | 4 | 8 |
| **Modul 4** | ✅ | 10 vollständig | 4 | 8 |
| **Modul 5** | ✅ | 10 vollständig | 4 | 8 |
| **Modul 6** *(Zusatz)* | ⚠️ | 10 in Entwicklung | 4 | 8 |

**Gesamt:** 59 Python-Programme (49 vollständig, 10 in Entwicklung), alle Module mit 4 Lektionen

## Naming Conventions

### Dateien
- Module: `modul-X-thema/`
- Lektionen: `lektion-X-titel.md` (X = 1, 2, 3, ...)
- Übungen: `uebung-X-titel.md`
- Aufgaben: `aufgabe-X-titel.md`
- Beispiele: `beschreibender-name.py` (Modul 1-3) oder `beispiel-X.py` (Modul 4-5, leer)

### Python-Code
- **Variablennamen:** Deutsche Namen, snake_case (`alter`, `vorname`, `ist_gueltig`)
- **Funktionen:** Deutsche Namen, snake_case (`berechne_summe()`, `ist_gerade()`)
- **Kommentare:** Deutsch, ausführlich für Lernzwecke
- **Docstrings:** In allen Funktionen/Modulen

## Code-Stil Richtlinien

### Didaktischer Code

```python
# ✅ Gut: Klar und verständlich für Anfänger
def berechne_durchschnitt(zahlen):
    """
    Berechnet den Durchschnitt einer Liste von Zahlen.

    Args:
        zahlen: Liste von Zahlen

    Returns:
        float: Durchschnittswert
    """
    summe = 0
    for zahl in zahlen:
        summe += zahl
    durchschnitt = summe / len(zahlen)
    return durchschnitt

# ❌ Vermeiden: Zu kompakt für Anfänger
def berechne_durchschnitt(zahlen):
    return sum(zahlen) / len(zahlen) if zahlen else 0
```

### Ausgabe-Stil

```python
# Trennlinien für bessere Lesbarkeit
print("=" * 40)
print("Programmtitel")
print("=" * 40)
```

## Git Workflow

- **Main Branch:** `develop` (nicht `main`!)
- **Commit-Format:** Emoji Conventional Commits (Deutsch)
  - 🎉 `feat:` Neue Funktionalität
  - 🔧 `chore:` Wartung, Konfiguration
  - 📚 `docs:` Dokumentation
  - 🐛 `fix:` Fehlerbehebung
  - ♻️ `refactor:` Code-Umstrukturierung

### Beispiel-Commit

```
📚 docs: Erweitere Modul 3 README und füge Cheatsheets hinzu

- README von 40 auf 150 Zeilen erweitert
- Cheatsheet Schleifen hinzugefügt
- Handout Kontrollstrukturen ergänzt
```

## Python-Umgebung

- **Python-Version:** 3.11+
- **Package Manager:** `uv`
- **IDE:** VS Code
- **Deployment:** GitHub Codespaces Support
- **Testing:** Aktuell keine Tests (siehe Nächste Schritte)

## README-Standards

Jedes README sollte enthalten:

1. **Titel & Metadaten** (Dauer, Voraussetzungen)
2. **🎯 Lernziele** (nummeriert, mit Checkboxen)
3. **📖 Themen im Detail** (Inhaltsbeschreibung)
4. **📚 Modulstruktur** (Alle 6 Ordner verlinkt)
5. **⏱️ Zeitplan** (Tabelle mit Phasen)
6. **✅ Erfolgskriterien** (Checkliste)
7. **💡 Tipps für den Erfolg**
8. **🔗 Weiterführende Links**

## Häufige Aufgaben

### Neues Modul erstellen

1. Ordnerstruktur gemäss Standard anlegen (6 Ordner)
2. README.md in jedem Ordner erstellen
3. Modul-README nach Standard-Template schreiben
4. Leseauftrag, Experimente, Quiz vorbereiten
5. 4 Lektionen ausarbeiten
6. 4-8 Übungen mit Lösungen erstellen
7. 3 Nachbearbeitungsaufgaben entwickeln
8. Materialien (Handouts, Cheatsheets) erstellen
9. 10 Python-Beispiele programmieren

### Neue Lektion hinzufügen

1. Datei `01-praxis/lektion-X-titel.md` erstellen
2. Format: Theorie (15 Min) + Live-Coding (20 Min) + Übung (15 Min)
3. Code-Beispiele einfügen
4. Häufige Fehler dokumentieren
5. In `01-praxis/README.md` verlinken

### Python-Beispiel schreiben

1. Datei in `05-beispiele/` erstellen
2. Docstring am Anfang
3. Deutsche Kommentare
4. Mehrere Funktionen zeigen
5. `if __name__ == "__main__":` Block
6. Trennlinien in print()-Ausgaben
7. In `05-beispiele/README.md` beschreiben

## Nächste Schritte (Priorität)

1. **Testing erweitern:**
   - Tests für alle 49 Python-Programme
   - pytest-Framework bereits eingerichtet
   - CI/CD Pipeline (GitHub Actions)

2. **Qualitätssicherung:**
   - Alle Links in Dokumenten prüfen
   - Übungen auf Vollständigkeit prüfen
   - Beispielprogramme testen

## Wichtige Hinweise

- **Keine Redundanzen:** Verwende Verlinkungen statt Wiederholungen
- **Konsistenz:** Alle Module folgen identischer Struktur
- **Didaktik:** Code-Klarheit > Kompaktheit
- **Sprache:** Deutsch für Variablen, Kommentare, Dokumentation
- **Zielgruppe:** Absolute Anfänger ohne Vorkenntnisse

## Kontakt

**Autor:** Daniel Senften
**Email:** daniel.senften@talent-factory.ch
**Organisation:** Talent Factory
**Jahr:** 2025

---

**Letzte Aktualisierung:** 2025-11-19
