# Leseauftrag: Kontrollstrukturen

**Zeitaufwand:** 60-90 Minuten
**Ziel:** Verstehen, wie Programme Entscheidungen treffen und Code wiederholen

## 🎯 Lernziele

Nach diesem Leseauftrag verstehen Sie:

- Wie Programme mit `if`, `elif` und `else` Entscheidungen treffen
- Wie `while`-Schleifen wiederholten Code ausführen
- Wie `for`-Schleifen über Sequenzen iterieren
- Was die Einrückung (Indentation) in Python bedeutet
- Wie Listen funktionieren und mit Schleifen kombiniert werden

---

## 1. Bedingte Anweisungen (if/elif/else)

Programme treffen Entscheidungen mit `if`-Anweisungen.

### Einfaches `if`

```python
alter = 18
if alter >= 18:
    print("Volljährig")
```

Die Anweisung nach dem `if` wird **nur dann** ausgeführt, wenn die Bedingung wahr (`True`) ist.

### `if` / `else`

```python
alter = 16
if alter >= 18:
    print("Volljährig")
else:
    print("Minderjährig")
```

Mit `else` definieren Sie, was passiert, wenn die Bedingung **falsch** ist.

### `if` / `elif` / `else`

```python
note = 5
if note >= 5.5:
    print("Sehr gut")
elif note >= 4.5:
    print("Gut")
elif note >= 4.0:
    print("Genügend")
else:
    print("Ungenügend")
```

Mit `elif` ("else if") prüfen Sie mehrere Bedingungen nacheinander.

### Vergleichsoperatoren

| Operator | Bedeutung |
|----------|-----------|
| `==` | gleich |
| `!=` | ungleich |
| `<` | kleiner als |
| `>` | grösser als |
| `<=` | kleiner oder gleich |
| `>=` | grösser oder gleich |

**Achtung:** `=` ist eine Zuweisung, `==` ist ein Vergleich!

### Logische Operatoren

```python
alter = 20
hat_fuehrerschein = True

if alter >= 18 and hat_fuehrerschein:
    print("Darf Auto fahren")
```

- `and` — beide Bedingungen müssen wahr sein
- `or` — mindestens eine Bedingung muss wahr sein
- `not` — kehrt den Wahrheitswert um

---

## 2. While-Schleifen

Wiederholen Code **solange** eine Bedingung erfüllt ist.

```python
zaehler = 1
while zaehler <= 5:
    print(zaehler)
    zaehler += 1
```

**Wichtig:** Die Variable muss sich verändern, sonst gibt es eine **Endlosschleife**!

### Typische Anwendung: Eingabe wiederholen

```python
eingabe = ""
while eingabe != "quit":
    eingabe = input("Befehl eingeben (oder 'quit'): ")
```

---

## 3. For-Schleifen

Durchlaufen Sequenzen (z.B. Zahlenbereiche oder Listen).

### `range()` für Zahlen

```python
for i in range(5):
    print(i)
```

Ausgabe: `0, 1, 2, 3, 4` — `range(5)` zählt **von 0 bis (5-1)**.

```python
for i in range(2, 7):
    print(i)
```

Ausgabe: `2, 3, 4, 5, 6` — `range(start, stop)`.

```python
for i in range(0, 10, 2):
    print(i)
```

Ausgabe: `0, 2, 4, 6, 8` — `range(start, stop, schrittweite)`.

---

## 4. Listen

Listen speichern **mehrere Werte** in einer Variable.

```python
namen = ["Anna", "Max", "Lisa"]
print(namen[0])   # Anna (erstes Element)
print(len(namen)) # 3 (Anzahl)
```

### Über Listen iterieren

```python
namen = ["Anna", "Max", "Lisa"]
for name in namen:
    print(f"Hallo, {name}!")
```

### Listen verändern

```python
namen.append("Tom")   # Element hinzufügen
namen.remove("Max")   # Element entfernen
```

---

## 5. Einrückung (Indentation)

Python verwendet **Einrückung** statt geschweiften Klammern `{}`, um zusammengehörenden Code zu erkennen.

```python
if alter >= 18:
    print("Volljährig")     # gehört zum if
    print("Darf wählen")    # gehört zum if
print("Programm-Ende")      # gehört NICHT zum if
```

**Konvention:** 4 Leerzeichen pro Einrückungsebene (VS Code macht das automatisch).

---

## 6. `break` und `continue`

Steuern den Ablauf einer Schleife.

```python
for i in range(10):
    if i == 5:
        break     # beendet die Schleife komplett
    print(i)
```

```python
for i in range(10):
    if i % 2 == 0:
        continue  # springt zur nächsten Iteration
    print(i)      # gibt nur ungerade Zahlen aus
```

---

## ✅ Checkliste

Nach diesem Leseauftrag sollten Sie:

- [ ] `if`, `elif` und `else` einsetzen können
- [ ] Vergleichsoperatoren kennen
- [ ] `while`- und `for`-Schleifen unterscheiden
- [ ] `range()` mit verschiedenen Argumenten verstehen
- [ ] Über Listen iterieren können
- [ ] Wissen, wofür `break` und `continue` da sind
- [ ] Die Bedeutung der Einrückung in Python kennen

---

**Nächster Schritt:** [Erste Experimente](./erste-experimente.md)
