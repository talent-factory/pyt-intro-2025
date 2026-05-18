# Lösungen zu `code_mit_bugs.py`

> ⚠️ **Spoiler!** Erst die Bugs selbst suchen, bevor du hier nachschaust.

## Bug 1: `summiere_bis(n)` — Off-by-one Fehler

**Symptom:** `summiere_bis(5)` liefert `10` statt `15`.

**Ursache:** `range(1, n)` zählt von 1 bis `n-1`, nicht bis `n` (Stopp ist exklusiv).

**Fix:**

```python
for i in range(1, n + 1):  # +1 damit n inklusive ist
    summe += i
```

## Bug 2: `ist_bestanden(punkte)` — Falscher Vergleichsoperator

**Symptom:** `ist_bestanden(60)` gibt `False` zurück, obwohl 60 Punkte bestehen sollen.

**Ursache:** `if punkte > 60` schliesst genau 60 aus. Die Aufgabe verlangt aber „ab 60 Punkten".

**Fix:**

```python
if punkte >= 60:  # >= statt >
    return True
```

Alternativ kann man die Funktion auch in eine Zeile schreiben:

```python
return punkte >= 60
```

## Bug 3: `finde_maximum(zahlen)` — Fehlende `return`-Anweisung

**Symptom:** `finde_maximum([3, 7, 2, 9, 4])` gibt `None` zurück (zeigt aber den korrekten Wert mit `print()`).

**Ursache:** Das Maximum wird berechnet und ausgegeben, aber nicht zurückgegeben.

**Fix:**

```python
print(f"Das Maximum ist: {maximum}")
return maximum  # Diese Zeile fehlte!
```

## Bug 4: `zaehle_runter(start)` — Falsches Inkrement (Endlosschleife)

**Symptom:** `zaehle_runter(5)` liefert `[5, 6, 7, 8, 9, ...]` statt `[5, 4, 3, 2, 1]`. Ohne den Sicherheitsabbruch wäre es eine echte Endlosschleife.

**Ursache:** `aktuell += 1` zählt hoch statt runter.

**Fix:**

```python
aktuell -= 1  # Minus statt Plus
```

## 💡 Lernhinweise

- **Off-by-one** ist einer der häufigsten Anfänger-Bugs (Bug 1) — `range()` ist exklusiv am Ende
- **`>` vs. `>=`** wirken klein, ändern aber die Logik komplett (Bug 2)
- **`return` vergessen** ergibt stillschweigend `None` (Bug 3) — pytest hätte das sofort gefunden
- **Endlosschleifen** kann man mit einer Sicherheits-Bedingung abfangen (Bug 4)
