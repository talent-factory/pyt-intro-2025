# Lektion 1: Was ist Programmieren?

**Dauer:** 50 Minuten  
**Format:** Theorie (15 Min.) + Live-Coding (20 Min.) + Übung (15 Min.)

## 🎯 Lernziele

Nach dieser Lektion können Sie:

- Erklären, was Programmieren bedeutet
- Verstehen, warum Python eine gute erste Sprache ist
- Den Unterschied zwischen Mensch und Computer-Denken erkennen
- Erste einfache Python-Beispiele nachvollziehen

---

## 📖 Theorie (15 Min.)

### 1. Was ist Programmieren?

**Definition:**  
Programmieren = Einem Computer **präzise Anweisungen** geben, um ein Problem zu lösen.

### Analogie: Kochrezept

Mensch (unpräzise):

> "Mach mal Pfannkuchen"

Computer (braucht Präzision):

> 1. Nimm 200g Mehl
> 2. Füge 300ml Milch hinzu
> 3. Rühre 2 Minuten
> 4. Erhitze Pfanne auf 180°C
> 5. ...

**Wichtig:** Computer sind **dumm** aber **schnell**. Sie tun **exakt**, was Sie sagen.

### 2. Warum Python?

**Vergleich:**

Python:

```python
print("Hello, World!")
```

Java:

```java
public class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Hello, World!");
    }
}
```

**Vorteile:**

- ✅ Einfache, lesbare Syntax
- ✅ Vielseitig (Web, Daten, KI, Automatisierung)
- ✅ Grosse Community
- ✅ Schnelle Ergebnisse

### 3. Wie denkt ein Computer?

**Sequenziell:** Schritt für Schritt

```python
x = 5          # Schritt 1: Speichere 5 in x
y = 10         # Schritt 2: Speichere 10 in y
summe = x + y  # Schritt 3: Addiere x und y
print(summe)   # Schritt 4: Zeige Ergebnis
```

**Literal:** Genau wie geschrieben

```python
# Falsch (für Computer):
"Addiere ein paar Zahlen"

# Richtig:
summe = 5 + 10
```

---

## 💻 Live-Coding (20 Min.)

### Demo 1: Hello World (5 Min.)

**Zeigen Sie:**

1. Terminal öffnen
2. Python starten: `python` oder `python3`
3. Eingeben:

```python
>>> print("Hello, World!")
Hello, World!
```

4. Erklären:
   - `print()` ist eine **Funktion**
   - `"Hello, World!"` ist ein **String** (Text)
   - Python führt aus und zeigt Ergebnis

### Demo 2: Einfache Berechnungen (5 Min.)

```python
>>> 2 + 2
4

>>> 10 * 5
50

>>> 100 / 4
25.0
```

**Erklären:**

- Python kann als Taschenrechner genutzt werden
- Ergebnis wird sofort angezeigt
- `/` gibt immer Dezimalzahl zurück (25.0)

### Demo 3: Variablen (5 Min.)

```python
>>> alter = 25
>>> alter
25

>>> name = "Anna"
>>> name
'Anna'

>>> print(f"{name} ist {alter} Jahre alt")
Anna ist 25 Jahre alt
```

**Erklären:**

- Variablen = Speicherplätze mit Namen
- `=` bedeutet "speichere in"
- F-Strings (`f"..."`) für formatierte Ausgabe

### Demo 4: Fehler sind okay! (5 Min.)

**Absichtlich Fehler machen:**

```python
>>> print("Hallo"
  File "<stdin>", line 1
    print("Hallo"
                 ^
SyntaxError: '(' was never closed
```

**Erklären:**

- Fehler sind **normal** und **hilfreich**
- Python sagt uns, **wo** der Fehler ist
- Fehler = Lernchance

**Korrigieren:**

```python
>>> print("Hallo")
Hallo
```

---

## ✏️ Übung (15 Min.)

### [Übung 1: Hello World](../02-uebungen/uebung-1-hello-world.md)

**Aufgabe:**

Studierende sollen:

1. Python Shell öffnen
2. Verschiedene Texte ausgeben
3. Einfache Berechnungen durchführen
4. Erste Variablen erstellen

**Dozent:**

- Zirkulieren und helfen
- Fragen beantworten
- Ermutigend sein

---

## 📝 Zusammenfassung (am Ende)

**Wichtigste Punkte:**

1. Programmieren = Präzise Anweisungen für Computer
2. Python = Einfach und vielseitig
3. Computer denken sequenziell und literal
4. Fehler sind normal und hilfreich

**Ausblick auf Lektion 2:**

- Mehr Python Shell
- Variablen vertiefen
- Datentypen kennenlernen

---

## 🎓 Für Dozenten

### Vorbereitung

- [ ] Python Shell funktioniert
- [ ] Beispiele vorbereitet
- [ ] Beamer/Projektor getestet

### Tipps

- **Langsam sprechen** - Anfänger brauchen Zeit
- **Interaktiv** - Fragen stellen
- **Fehler zeigen** - Nimmt Angst
- **Positiv bleiben** - Ermutigen

### Häufige Fragen

**Q: "Muss ich das alles auswendig lernen?"**  
A: Nein! Verstehen ist wichtiger. Syntax kommt mit Übung.

**Q: "Was, wenn ich einen Fehler mache?"**  
A: Perfekt! Fehler sind der beste Lernweg.

**Q: "Ist Programmieren schwer?"**  
A: Am Anfang ungewohnt, aber mit Übung wird es einfacher.

---

**Nächste Lektion:** [Lektion 2: Python Shell](./lektion-2-python-shell.md)
