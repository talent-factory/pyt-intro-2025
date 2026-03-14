# Lektion 3: Effektiv mit Claude Code arbeiten

**Dauer:** 50 Minuten
**Format:** 10 Min Theorie + 20 Min Live-Demo + 20 Min Übung

## 🎯 Lernziele

- Prompting-Strategien kennen und anwenden
- Code erklären, debuggen und generieren lassen
- Iterativ mit KI arbeiten

## 📖 Theorie (10 Min)

### Prompting-Strategien

Drei Prinzipien für gute Prompts:

**1. Spezifisch sein:**

```
❌ "Schreibe eine Funktion"
✅ "Schreibe eine Python-Funktion sortiere_namen(namen_liste),
   die eine Liste von Namen alphabetisch sortiert und zurückgibt"
```

**2. Kontext geben:**

```
❌ "Finde den Fehler"
✅ "In der Datei quiz.py bekomme ich einen TypeError in Zeile 15.
   Die Funktion soll zwei Zahlen addieren, aber erhält einen String"
```

**3. Iterativ arbeiten:**

```
Schritt 1: "Schreibe eine Funktion, die eine Einkaufsliste verwaltet"
Schritt 2: "Füge eine Sortierfunktion nach Preis hinzu"
Schritt 3: "Ergänze eine Gesamtsumme am Ende"
```

### Do's und Don'ts

| ✅ Do | ❌ Don't |
|-------|---------|
| Konkreten Funktionsnamen nennen | "Schreibe irgendwas" |
| Erwartetes Verhalten beschreiben | Nur das Problem nennen, nicht das Ziel |
| Auf Dateien im Projekt verweisen | Code per Copy-Paste einfügen |
| Schritt für Schritt verfeinern | Alles in einem Prompt verlangen |
| Deutsche Variablennamen fordern | Auf Sprachstil verzichten |

### Typische Anwendungsfälle

| Anwendung | Beispiel-Prompt |
|-----------|-----------------|
| **Erklären** | "Was macht die for-Schleife in Zeile 15-23?" |
| **Debuggen** | "Warum gibt diese Funktion immer None zurück?" |
| **Generieren** | "Schreibe eine Funktion, die Duplikate entfernt" |
| **Refactoring** | "Vereinfache diese verschachtelte if-Struktur" |

## 💻 Live-Demo (20 Min)

### Demo 1: Code erklären lassen

**Aufgabe an Claude Code:**

```
Was macht die for-Schleife in der Datei
modul-3-kontrollstrukturen/05-beispiele/zahlenraten.py?
Erkläre Zeile für Zeile.
```

**Was passiert:**
- Claude Code findet die Datei
- Liest den relevanten Codeabschnitt
- Erklärt jede Zeile verständlich

**Diskussion:** Ist die Erklärung für Anfänger verständlich?

### Demo 2: Fehler finden lassen

**Fehlerhaften Code zeigen:**

```python
def berechne_summe(zahlen):
    """Berechnet die Summe einer Liste."""
    summe = 0
    for i in range(len(zahlen)):
        summe += zahlen[i + 1]  # Bug: Index out of range!
    return summe

ergebnis = berechne_summe([10, 20, 30])
print(f"Summe: {ergebnis}")
```

**Aufgabe an Claude Code:**

```
Dieser Code hat einen Fehler. Finde den Bug und erkläre,
warum er auftritt und wie man ihn behebt.
```

**Erwartete Antwort der KI:**
- Der Bug ist `zahlen[i + 1]` statt `zahlen[i]`
- Bei `i = 2` (letzter Index) wird `zahlen[3]` aufgerufen → `IndexError`
- **Fix:** `summe += zahlen[i]`

**Diskussion:** Hat die KI den Fehler sofort gefunden? Wie hilfreich ist die Erklärung?

### Demo 3: Code generieren lassen

**Aufgabe an Claude Code:**

```
Schreibe eine Python-Funktion einkaufsliste_sortiert(artikel),
die eine Liste von Dictionaries mit 'name' und 'preis' nimmt
und nach Preis aufsteigend sortiert zurückgibt.
Verwende deutsche Variablennamen und Kommentare.
```

**Erwartetes Ergebnis:**

```python
def einkaufsliste_sortiert(artikel):
    """
    Sortiert eine Einkaufsliste nach Preis (aufsteigend).

    Args:
        artikel: Liste von Dictionaries mit 'name' und 'preis'

    Returns:
        list: Sortierte Liste
    """
    # Liste nach Preis sortieren
    sortierte_liste = sorted(artikel, key=lambda a: a['preis'])
    return sortierte_liste
```

**Diskussion:** Entspricht der Code unserem Kurs-Stil?

### Demo 4: Iterativ verfeinern

Aufbauend auf Demo 3:

```
Füge der Funktion noch eine Gesamtsumme hinzu.
Die Funktion soll die sortierte Liste ausgeben und
am Ende die Gesamtsumme aller Preise anzeigen.
```

**Erwartetes Ergebnis:**

```python
def einkaufsliste_anzeigen(artikel):
    """
    Zeigt eine Einkaufsliste sortiert nach Preis mit Gesamtsumme.

    Args:
        artikel: Liste von Dictionaries mit 'name' und 'preis'
    """
    # Nach Preis sortieren
    sortierte_liste = sorted(artikel, key=lambda a: a['preis'])

    # Sortierte Liste ausgeben
    print("=" * 35)
    print("Einkaufsliste (nach Preis)")
    print("=" * 35)

    gesamtsumme = 0
    for eintrag in sortierte_liste:
        print(f"  {eintrag['name']:.<20} {eintrag['preis']:.2f} CHF")
        gesamtsumme += eintrag['preis']

    print("-" * 35)
    print(f"  {'Gesamt':.<20} {gesamtsumme:.2f} CHF")
    print("=" * 35)
```

**Erkenntnis:** Durch **iteratives Verfeinern** wird das Ergebnis schrittweise besser, ohne alles auf einmal beschreiben zu müssen.

## ✏️ Übungen (20 Min)

### Übung 1: Mit KI eine Aufgabe lösen

Wählen Sie eine **Aufgabe aus Modul 3 oder 4**, die Sie bereits gelöst haben. Arbeiten Sie in 3 Schritten:

**Schritt 1 — Mit KI lösen:**
Formulieren Sie einen Prompt und lassen Sie Claude Code die Aufgabe lösen.

**Schritt 2 — Lösung verstehen:**
Lassen Sie sich die Lösung erklären:
```
Erkläre mir diese Lösung Zeile für Zeile.
Was macht jeder Abschnitt?
```

**Schritt 3 — Bewerten:**
Vergleichen Sie mit Ihrer eigenen Lösung:
- Welche Lösung ist verständlicher?
- Welche ist effizienter?
- Was würden Sie anders machen?

### Übung 2: Iteratives Prompting

Starten Sie mit einem **einfachen Prompt** und verfeinern Sie in **3 Folgefragen:**

**Start-Prompt:**
```
Schreibe ein Python-Programm für ein Quiz.
```

**Dann 3 Folgefragen stellen, zum Beispiel:**
1. "Füge 5 Fragen zu Python-Grundlagen hinzu"
2. "Zeige am Ende die Punktzahl als Prozentzahl"
3. "Gib bei falschen Antworten die richtige Antwort aus"

**Aufgabe:** Dokumentieren Sie Ihren Verlauf:
- Wie hat sich das Programm mit jedem Schritt verändert?
- Welche Folgefrage hatte den grössten Effekt?
- Was haben Sie über gutes Prompting gelernt?

## 📝 Zusammenfassung

| Strategie | Beschreibung |
|-----------|-------------|
| **Spezifisch** | Funktionsname, Parameter, Rückgabewert nennen |
| **Kontextreich** | Auf Dateien verweisen, Fehlermeldung zeigen |
| **Iterativ** | Schritt für Schritt verfeinern |

### Typischer Workflow

```
1. Aufgabe beschreiben (spezifischer Prompt)
2. Ergebnis prüfen (Code lesen und verstehen)
3. Verfeinern (Folgeprompt mit Anpassungen)
4. Testen (Code ausführen und prüfen)
```

### Wichtige Punkte

✅ **DO:**
- Spezifische Prompts mit klaren Anforderungen
- Iterativ arbeiten statt alles auf einmal
- KI-Code immer verstehen, bevor Sie ihn verwenden

❌ **DON'T:**
- Vage Prompts ohne Details
- Riesige Anforderungen in einem einzigen Prompt
- Code der KI ungeprüft übernehmen

## 🔗 Weiter

[Lektion 4: Showcase — Was noch möglich ist](./lektion-4-showcase.md)
