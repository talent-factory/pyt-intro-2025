# Übung 2: Code erklären lassen

**Dauer:** 15 Minuten
**Schwierigkeit:** ⭐ Einfach

## 📝 Aufgabe

Nehmen Sie eine eigene Lösung aus Modul 4 (Funktionen & Datenstrukturen) und lassen Sie Claude Code den Code erklären. Schreiben Sie anschliessend eine Zusammenfassung in eigenen Worten.

### Schritt 1: Code auswählen

Wählen Sie eine Ihrer Lösungen aus Modul 4, z.B.:

- Eine Funktion mit Parametern und Rückgabewert
- Ein Programm mit Listen oder Dictionaries
- Eine Lösung mit mehreren Funktionen

### Schritt 2: Claude Code fragen

Geben Sie Ihren Code ein und stellen Sie folgende Fragen:

```
Erkläre mir diesen Code Zeile für Zeile.
Was macht jede Funktion?
Welche Konzepte werden verwendet?
```

### Schritt 3: Zusammenfassung schreiben

Schreiben Sie in **eigenen Worten** auf, was Ihr Code macht. Verwenden Sie dabei die Fachbegriffe, die Sie gelernt haben.

## 💡 Beispiel

```python
def berechne_durchschnitt(noten):
    """Berechnet den Notendurchschnitt."""
    summe = 0
    for note in noten:
        summe += note
    return summe / len(noten)
```

**KI-Erklärung:** "Die Funktion nimmt eine Liste von Noten, summiert sie in einer Schleife und teilt durch die Anzahl..."

**Eigene Zusammenfassung:** "Meine Funktion berechnet den Durchschnitt. Sie geht alle Noten durch, zählt sie zusammen und teilt am Ende durch die Anzahl der Noten."

## 📋 Reflexions-Checkliste

- [ ] **Vollständigkeit:** Hat die KI alles erkannt, was der Code macht?
- [ ] **Fehlendes:** Gibt es etwas, das die KI nicht erwähnt hat?
- [ ] **Überraschungen:** Gab es etwas in der Erklärung, das Sie überrascht hat?
- [ ] **Neue Begriffe:** Haben Sie neue Fachbegriffe gelernt?

## ✅ Checkliste

- [ ] Eigenen Code aus Modul 4 ausgewählt
- [ ] Claude Code um Erklärung gebeten
- [ ] Zusammenfassung in eigenen Worten geschrieben
- [ ] Reflexions-Checkliste ausgefüllt
