# Design: Modul 7 — Objektorientierte Programmierung

**Datum:** 2026-03-06
**Status:** Genehmigt
**Hinweis:** Dieses Modul war ursprünglich als Modul 6 geplant und wurde am 2026-03-14
auf Modul 7 verschoben, da Modul 6 nun "KI-gestütztes Programmieren" behandelt.
Siehe: `docs/plans/2026-03-14-modul6-ki-programmieren-design.md`
**Autor:** Daniel Senften / Claude

## Zusammenfassung

Modul 7 fuehrt die objektorientierte Programmierung (OOP) als fokussiertes Abschlussmodul
in den Python-Basiskurs ein. Es ersetzt Modul 5 als Kursabschluss. Der Fokus liegt auf
Klassen, `__init__`, `__str__`, Attributen und Methoden — ohne Vererbung. Das durchgaengige
Praxisthema ist die Kontaktverwaltung, die von der prozeduralen Loesung (M4/M5) zur
OOP-Loesung refactored wird.

## Lernziele

1. Verstehen, was Klassen und Objekte sind (Bauplan vs. konkretes Ding)
2. Eigene Klassen mit `__init__` und Attributen definieren
3. Methoden schreiben, die auf Objektdaten arbeiten
4. `__str__` fuer lesbare Darstellung implementieren
5. Mehrere Objekte in Listen/Dicts verwalten
6. Klassen mit pytest testen
7. Dateipersistenz (JSON) mit Klassen verbinden (M5-Rueckbezug)

## Modulstruktur

**Name:** Modul 7: Objektorientierte Programmierung
**Dauer:** 1 Tag (4 Lektionen a 50 Minuten)
**Voraussetzung:** Module 1-6 abgeschlossen
**Besonderheit:** Abschlussmodul mit Mini-Projekt
**Durchgaengiges Thema:** Kontaktverwaltung — Refactoring von prozedural zu OOP

### Lektionen

| # | Thema | Inhalt | Rueckbezug |
|---|-------|--------|-----------|
| 1 | Klassen & Objekte verstehen | `class`, `__init__`, Attribute, erste `Kontakt`-Klasse. Vergleich Dict vs. Klasse. | M1 (Variablen), M4 (Dicts) |
| 2 | Methoden & `__str__` | Methoden, `self`, `__str__`, `aendern()`, `als_dict()` | M4 (Funktionen), M2 (f-Strings) |
| 3 | Klassen testen mit pytest | Tests fuer `Kontakt`-Klasse, Edge Cases | M4 (pytest) |
| 4 | Mini-Projekt: Kontaktverwaltung | `Kontaktverwaltung`-Klasse mit `hinzufuegen()`, `suchen()`, `loeschen()`, `speichern()`, `laden()`. JSON-Persistenz | M3 (Schleifen/Menue), M5 (JSON) |

### Lektionsformat

Jede Lektion: Theorie (15 Min) → Live-Coding (20 Min) → Uebung (15 Min)

### Uebungen (8 Stueck)

| # | Titel | Beschreibung |
|---|-------|-------------|
| 1 | Erste Klasse | `Kontakt`-Klasse mit name und email erstellen |
| 2 | Objekte erzeugen | Mehrere Kontakt-Objekte erstellen und ausgeben |
| 3 | Methoden hinzufuegen | `info()` und `aendern()` Methoden |
| 4 | `__str__` Magic | Lesbare Darstellung implementieren |
| 5 | Test schreiben | Ersten pytest-Test fuer `Kontakt` schreiben |
| 6 | Edge Cases testen | Leere Strings, Spezialzeichen testen |
| 7 | Kontaktverwaltung bauen | Klasse mit Liste von Kontakten |
| 8 | Speichern & Laden | JSON-Persistenz integrieren |

### Nachbearbeitungsaufgaben (3 Stueck)

1. Kontaktverwaltung erweitern (Suchfunktion, Sortierung, Telefonnummer)
2. Bibliothek-Klasse (neues Thema: `Buch` und `Bibliothek` eigenstaendig)
3. Freies Mini-Projekt (eigene Klasse nach Wahl)
4. Abschlussreflexion ueber den gesamten Kurs (Module 1-7)

### Beispielprogramme (10 Stueck)

- `klasse_grundlagen.py` — Erste Klasse definieren
- `kontakt.py` — Kontakt-Klasse vollstaendig
- `methoden.py` — Methoden und self
- `str_repr.py` — Magic Methods
- `objekte_in_listen.py` — Mehrere Objekte verwalten
- `kontaktverwaltung.py` — Vollstaendige Verwaltungsklasse
- `test_kontakt.py` — pytest fuer Klassen
- `vergleich_dict_klasse.py` — Vorher/Nachher Vergleich
- `json_persistenz.py` — Objekte speichern/laden
- `bibliothek.py` — Zweites Klassenbeispiel

### Materialien

- Cheatsheet: Klassen & Objekte
- Handout: OOP Grundlagen
- Cheatsheet: Magic Methods (`__init__`, `__str__`)
- Haeufige Fehler bei Klassen (self vergessen, etc.)

## Aenderungen an bestehenden Modulen

### Modul 5

- Abschlussreflexion und "Naechste Schritte" wandern nach Modul 7
- Modul 5 verweist auf Modul 7 als naechstes Modul
- Modul 5 verliert die Besonderheit "Abschlussmodul"

### Kurs-README

- Aktualisierung auf 7 Module
- Neuer Eintrag fuer Modul 7

### CLAUDE.md

- Projektstruktur um Modul 7 erweitern
- Moduluebersicht aktualisieren

## Paedagogischer roter Faden

```
M4: erstelle_kontakt() → gibt Dict zurueck
M5: Kontakte in JSON speichern/laden
M6: Kontakt als Klasse → alles zusammen in einem Objekt
```

Die Teilnehmenden erleben die Evolution ihres eigenen Codes: von Funktionen mit
Dicts zu Klassen mit Methoden und Persistenz.

## Design-Entscheidungen

1. **Kein Vererbung:** Fokus auf solide Grundlagen statt Ueberfrachtung. Vererbung
   ist fuer absolute Anfaenger in einem Tag zu viel.
2. **Testing integriert:** pytest-Wissen aus M4 wird gefestigt. Zeigt, dass Klassen
   gut testbar sind.
3. **Kontaktverwaltung als Thema:** Direkter Rueckbezug zu M4/M5, Vorher/Nachher-Vergleich
   macht OOP-Mehrwert greifbar.
4. **Mini-Projekt in Lektion 4:** Verbindet OOP mit Dateipersistenz (M5) und
   Menuefuehrung (M3) — alles fliesst zusammen.
5. **Neues Abschlussmodul:** Modul 7 wird das Abschlussmodul, Modul 5 wird zum
   normalen Zwischenmodul.
