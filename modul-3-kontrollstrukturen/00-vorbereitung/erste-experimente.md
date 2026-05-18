# Erste Experimente: Kontrollstrukturen

**Zeitaufwand:** 45-60 Minuten
**Ziel:** Erstes Erfahren mit Bedingungen, Schleifen und Listen in der Python Shell

## 🎯 Ziele

Nach diesen Experimenten können Sie:

- `if`-Anweisungen schreiben und testen
- `while`- und `for`-Schleifen anwenden
- Mit Listen arbeiten und über sie iterieren
- Einfache Programme mit Kontrollstrukturen kombinieren

---

## Experiment 1: If-Anweisungen

Tippen Sie folgenden Code in die Python Shell oder in eine `.py`-Datei:

```python
alter = 20
if alter >= 18:
    print("Volljährig")
else:
    print("Minderjährig")
```

**Ändern Sie `alter`** auf verschiedene Werte (z.B. 15, 18, 21) und beobachten Sie die Ausgabe.

### Variation: elif

```python
note = 4.5
if note >= 5.5:
    print("Sehr gut")
elif note >= 4.5:
    print("Gut")
elif note >= 4.0:
    print("Genügend")
else:
    print("Ungenügend")
```

**Probieren Sie:** Welche Note ergibt welche Ausgabe?

---

## Experiment 2: Vergleichsoperatoren

```python
print(5 > 3)    # True
print(5 == 5)   # True
print(5 != 3)   # True
print(5 < 3)    # False
print(5 >= 5)   # True
```

**Aufgabe:** Probieren Sie auch `and`, `or` und `not`:

```python
print(True and False)
print(True or False)
print(not True)
```

---

## Experiment 3: While-Schleifen

```python
zaehler = 1
while zaehler <= 5:
    print(zaehler)
    zaehler += 1
```

**Aufgabe:** Ändern Sie die Schleife so, dass sie **rückwärts** von 10 bis 1 zählt.

### Achtung: Endlosschleife

```python
# NICHT ausführen! Beispiel für eine Endlosschleife:
# zaehler = 1
# while zaehler <= 5:
#     print(zaehler)
#     # zaehler wird nicht erhöht -> Endlosschleife!
```

Falls Sie versehentlich eine Endlosschleife starten: `Ctrl+C` beendet das Programm.

---

## Experiment 4: For-Schleifen mit range()

```python
for i in range(5):
    print(i)
```

```python
for i in range(2, 8):
    print(i)
```

```python
for i in range(0, 20, 2):
    print(i)
```

**Aufgabe:** Geben Sie alle Zahlen von 1 bis 10 aus, die durch 3 teilbar sind.

---

## Experiment 5: Listen

```python
fruechte = ["Apfel", "Banane"]
print(fruechte)
fruechte.append("Orange")
print(fruechte)
print(fruechte[0])      # erstes Element
print(len(fruechte))    # Anzahl
```

### Über eine Liste iterieren

```python
fruechte = ["Apfel", "Banane", "Orange"]
for frucht in fruechte:
    print(f"Ich esse gerne {frucht}.")
```

**Aufgabe:** Erstellen Sie eine Liste mit 5 Hobbys und geben Sie jedes Hobby mit Nummer aus:

```text
1. Lesen
2. Schwimmen
...
```

Tipp: `enumerate()` hilft Ihnen dabei:

```python
hobbys = ["Lesen", "Schwimmen", "Velofahren", "Kochen", "Reisen"]
for nummer, hobby in enumerate(hobbys, start=1):
    print(f"{nummer}. {hobby}")
```

---

## Experiment 6: break und continue

```python
for i in range(10):
    if i == 5:
        break
    print(i)
```

```python
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)
```

**Beobachtung:** Was ist der Unterschied zwischen `break` und `continue`?

---

## Experiment 7: Kombination — Zahlenraten (Mini-Spiel)

```python
geheim = 7
versuche = 0
geraten = -1

while geraten != geheim:
    geraten = int(input("Rate die Zahl (1-10): "))
    versuche += 1
    if geraten < geheim:
        print("Zu klein")
    elif geraten > geheim:
        print("Zu gross")

print(f"Richtig! Du hast {versuche} Versuche gebraucht.")
```

**Aufgabe:** Erweitern Sie das Spiel so, dass nach maximal 3 Versuchen abgebrochen wird.

---

## ✅ Checkliste

Nach diesen Experimenten sollten Sie:

- [ ] `if`/`elif`/`else` selbstständig anwenden können
- [ ] Den Unterschied zwischen `=` und `==` kennen
- [ ] `while`- und `for`-Schleifen schreiben können
- [ ] `range()` mit 1, 2 und 3 Argumenten verstehen
- [ ] Über eine Liste iterieren können
- [ ] `break` und `continue` einsetzen können
- [ ] Eine Endlosschleife mit `Ctrl+C` beenden können

---

**Nächster Schritt:** [Quiz](./quiz.md)
