# Prompt-Guide: Effektive Prompts für KI-Programmierung

## Grundregeln

### Do's — So schreiben Sie gute Prompts

1. **Spezifisch sein** — Genau beschreiben, was Sie wollen
2. **Kontext mitgeben** — Relevanten Code oder Fehlermeldungen einfügen
3. **Beispiele zeigen** — Gewünschte Ein-/Ausgabe beschreiben
4. **Iterativ arbeiten** — Schritt für Schritt verfeinern
5. **Rolle definieren** — Sagen, für wen der Code ist (z.B. "für Anfänger")

### Don'ts — Das sollten Sie vermeiden

1. **Vage bleiben** — "Mach was mit Listen" hilft nicht
2. **Zu breit fragen** — "Erkläre mir Python" ist zu viel auf einmal
3. **Ohne Kontext** — Fehler melden ohne den Code zu zeigen
4. **Blind übernehmen** — KI-Code immer erst verstehen und testen
5. **Aufgeben** — Wenn die Antwort nicht passt, umformulieren

## 10 Beispiel-Prompts mit Bewertung

### Kategorie: Erklären

| Nr | Schlecht | Gut | Warum besser? |
|----|----------|-----|---------------|
| 1 | "Was ist Python?" | "Erkläre mir den Unterschied zwischen einer for-Schleife und einer while-Schleife in Python, mit je einem einfachen Beispiel." | Spezifisches Thema, klare Erwartung |
| 2 | "Erkläre den Code" | "Erkläre mir Zeile für Zeile, was dieser Code macht: [Code einfügen]. Ich bin Python-Anfänger." | Kontext gegeben, Niveau definiert |

### Kategorie: Debuggen

| Nr | Schlecht | Gut | Warum besser? |
|----|----------|-----|---------------|
| 3 | "Mein Code geht nicht" | "Mein Code gibt folgenden Fehler: 'TypeError: unsupported operand type(s)'. Hier ist der Code: [Code]. Was muss ich ändern?" | Fehlermeldung + Code mitgegeben |
| 4 | "Hilf mir" | "Diese Funktion sollte die Summe einer Liste berechnen, gibt aber immer 0 zurück. Wo liegt der Fehler? [Code]" | Erwartetes vs. tatsächliches Verhalten beschrieben |

### Kategorie: Generieren

| Nr | Schlecht | Gut | Warum besser? |
|----|----------|-----|---------------|
| 5 | "Mach eine Funktion" | "Erstelle eine Python-Funktion 'berechne_durchschnitt(zahlen)', die den Durchschnitt einer Liste berechnet. Mit Docstring und Fehlerbehandlung für leere Listen." | Funktionsname, Parameter, Extras angegeben |
| 6 | "Schreibe ein Programm" | "Erstelle ein Python-Programm für einen einfachen Taschenrechner. Er soll +, -, *, / können. Eingabe über input(), Ausgabe mit print(). Deutsche Variablennamen." | Konkrete Anforderungen aufgelistet |

### Kategorie: Refactoring

| Nr | Schlecht | Gut | Warum besser? |
|----|----------|-----|---------------|
| 7 | "Mach den Code besser" | "Verbessere die Lesbarkeit dieses Codes: Füge Docstrings hinzu, benenne Variablen aussagekräftiger und extrahiere die Berechnung in eine eigene Funktion. [Code]" | Drei konkrete Verbesserungen benannt |
| 8 | "Optimiere das" | "Dieser Code hat verschachtelte if-Anweisungen. Kannst du ihn mit elif vereinfachen? [Code]" | Konkretes Problem und gewünschte Lösung |

### Kategorie: Testen

| Nr | Schlecht | Gut | Warum besser? |
|----|----------|-----|---------------|
| 9 | "Teste das" | "Welche Testfälle sollte ich für diese Funktion prüfen? Denke an Normalfälle, Grenzfälle und Fehlerfälle. [Code]" | Drei Testarten spezifiziert |
| 10 | "Ist der Code richtig?" | "Prüfe, ob diese Funktion korrekt funktioniert, wenn die Liste leer ist, nur ein Element hat oder negative Zahlen enthält. [Code]" | Konkrete Szenarien genannt |

## Kategorie-spezifische Tipps

### Erklären lassen

```
Gute Formulierungen:
- "Erkläre mir ... als wäre ich Anfänger"
- "Was bedeutet der Fehler ...?"
- "Zeige mir den Unterschied zwischen ... und ..."
- "Erkläre Schritt für Schritt, was passiert wenn ..."

Tipp: Geben Sie Ihr Niveau an ("Ich bin Anfänger",
"Ich kenne schon if-Anweisungen").
```

### Debuggen

```
Gute Formulierungen:
- "Mein Code gibt folgenden Fehler: [Fehler]. Hier ist der Code: [Code]"
- "Der Code läuft, aber das Ergebnis ist falsch. Erwartet: X, Erhalten: Y"
- "An welcher Stelle könnte der Fehler in diesem Code liegen?"

Tipp: Immer die vollständige Fehlermeldung UND den Code mitschicken.
```

### Generieren

```
Gute Formulierungen:
- "Erstelle eine Funktion die ... mit folgenden Anforderungen: ..."
- "Schreibe ein Programm das ... Verwende deutsche Variablennamen"
- "Generiere Code für ... mit Kommentaren auf Deutsch"

Tipp: Anforderungen als nummerierte Liste aufschreiben.
```

## Iteratives Arbeiten — Beispiel

```
Schritt 1: "Erstelle eine einfache Todo-Liste in Python."
         → KI liefert Grundgerüst

Schritt 2: "Füge bitte eine Funktion zum Löschen von Aufgaben hinzu."
         → KI erweitert den Code

Schritt 3: "Kannst du Fehlerbehandlung für ungültige Eingaben ergänzen?"
         → KI macht den Code robuster

Schritt 4: "Füge deutsche Kommentare und einen Docstring hinzu."
         → KI verbessert die Dokumentation
```

> **Merke:** Komplexe Programme baut man Schritt für Schritt auf — genau wie beim Programmieren selbst.

## Checkliste für jeden Prompt

Bevor Sie einen Prompt abschicken, prüfen Sie:

- [ ] Ist klar, **was** ich will?
- [ ] Habe ich relevanten **Kontext** mitgegeben?
- [ ] Ist mein **Niveau** erkennbar?
- [ ] Habe ich ein **Beispiel** für die gewünschte Ausgabe?
- [ ] Ist der Prompt **spezifisch** genug?
