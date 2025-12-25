# Einführung in Python

## Was ist Python?

Python ist eine vielseitige, hochrangige Programmiersprache, die für ihre Lesbarkeit und einfache Syntax bekannt ist. Sie wurde Ende der 1980er Jahre von Guido van Rossum entwickelt und ist heute eine der beliebtesten Programmiersprachen weltweit.

## Warum Python lernen?

- **Einfach zu lernen**: Python hat eine klare und intuitive Syntax
- **Vielseitig einsetzbar**: Webentwicklung, Datenanalyse, KI, Automatisierung und mehr
- **Große Community**: Umfangreiche Dokumentation und viele Bibliotheken verfügbar
- **Plattformunabhängig**: Läuft auf Windows, macOS, Linux und anderen Betriebssystemen

## Installation

Python kann von der offiziellen Website heruntergeladen werden: [python.org](https://www.python.org)

Nach der Installation können Sie Python über die Kommandozeile starten:

```bash
python --version
```

## Grundlegende Konzepte

### 1. Variablen und Datentypen

Variablen in Python müssen nicht deklariert werden und können verschiedene Datentypen speichern:

```python
# Ganzzahlen (Integer)
alter = 25

# Gleitkommazahlen (Float)
groesse = 1.75

# Zeichenketten (String)
name = "Anna"

# Boolesche Werte
ist_student = True
```

#### Wichtige Datentypen:
- `int` - Ganze Zahlen
- `float` - Dezimalzahlen
- `str` - Zeichenketten
- `bool` - Wahrheitswerte (True/False)
- `list` - Listen
- `dict` - Wörterbücher
- `tuple` - Tupel

### 2. Ausgabe auf dem Bildschirm

```python
print("Hallo, Welt!")
print("Mein Name ist", name)
print(f"Ich bin {alter} Jahre alt")
```

### 3. Benutzereingabe

```python
name = input("Wie heißt du? ")
print(f"Hallo, {name}!")
```

### 4. Operatoren

#### Arithmetische Operatoren:
```python
addition = 10 + 5        # 15
subtraktion = 10 - 5     # 5
multiplikation = 10 * 5  # 50
division = 10 / 5        # 2.0
ganzzahldivision = 10 // 3  # 3
modulo = 10 % 3          # 1
potenz = 2 ** 3          # 8
```

#### Vergleichsoperatoren:
```python
gleich = (5 == 5)           # True
ungleich = (5 != 3)         # True
groesser = (10 > 5)         # True
kleiner = (5 < 10)          # True
groesser_gleich = (10 >= 10)  # True
kleiner_gleich = (5 <= 10)    # True
```

### 5. Kontrollstrukturen

#### if-Anweisungen:
```python
alter = 18

if alter >= 18:
    print("Du bist volljährig")
elif alter >= 13:
    print("Du bist ein Teenager")
else:
    print("Du bist ein Kind")
```

#### for-Schleifen:
```python
# Schleife über eine Liste
fruechte = ["Apfel", "Banane", "Orange"]
for frucht in fruechte:
    print(frucht)

# Schleife mit range()
for i in range(5):
    print(i)  # Gibt 0, 1, 2, 3, 4 aus
```

#### while-Schleifen:
```python
zaehler = 0
while zaehler < 5:
    print(zaehler)
    zaehler += 1
```

### 6. Listen

Listen sind veränderbare Sequenzen von Elementen:

```python
# Liste erstellen
zahlen = [1, 2, 3, 4, 5]
gemischt = [1, "Hallo", True, 3.14]

# Auf Elemente zugreifen
erstes_element = zahlen[0]  # 1
letztes_element = zahlen[-1]  # 5

# Elemente hinzufügen
zahlen.append(6)

# Elemente entfernen
zahlen.remove(3)

# Länge der Liste
laenge = len(zahlen)
```

### 7. Wörterbücher (Dictionaries)

Wörterbücher speichern Schlüssel-Wert-Paare:

```python
# Wörterbuch erstellen
person = {
    "name": "Max",
    "alter": 30,
    "stadt": "Berlin"
}

# Auf Werte zugreifen
name = person["name"]

# Wert hinzufügen oder ändern
person["beruf"] = "Programmierer"

# Über Schlüssel und Werte iterieren
for schluessel, wert in person.items():
    print(f"{schluessel}: {wert}")
```

### 8. Funktionen

Funktionen ermöglichen es, Code wiederzuverwenden:

```python
# Einfache Funktion
def begruessung():
    print("Hallo!")

# Funktion mit Parametern
def begruessung_mit_namen(name):
    print(f"Hallo, {name}!")

# Funktion mit Rückgabewert
def addiere(a, b):
    return a + b

# Funktionen aufrufen
begruessung()
begruessung_mit_namen("Anna")
ergebnis = addiere(5, 3)
```

### 9. Kommentare

```python
# Dies ist ein einzeiliger Kommentar

"""
Dies ist ein
mehrzeiliger
Kommentar
"""

def funktion():
    """
    Dies ist ein Docstring,
    der die Funktion dokumentiert.
    """
    pass
```

## Nützliche eingebaute Funktionen

- `len()` - Länge einer Sequenz
- `type()` - Typ eines Objekts
- `str()`, `int()`, `float()` - Typkonvertierung
- `range()` - Zahlensequenz erzeugen
- `sorted()` - Sortierte Liste zurückgeben
- `sum()` - Summe von Zahlen
- `max()`, `min()` - Maximum und Minimum

## Beispielprogramm

Hier ist ein einfaches Programm, das verschiedene Konzepte kombiniert:

```python
# Einfacher Taschenrechner

def taschenrechner():
    print("=== Einfacher Taschenrechner ===")
    
    zahl1 = float(input("Erste Zahl: "))
    operation = input("Operation (+, -, *, /): ")
    zahl2 = float(input("Zweite Zahl: "))
    
    if operation == "+":
        ergebnis = zahl1 + zahl2
    elif operation == "-":
        ergebnis = zahl1 - zahl2
    elif operation == "*":
        ergebnis = zahl1 * zahl2
    elif operation == "/":
        if zahl2 != 0:
            ergebnis = zahl1 / zahl2
        else:
            print("Fehler: Division durch Null!")
            return
    else:
        print("Ungültige Operation!")
        return
    
    print(f"Ergebnis: {ergebnis}")

# Programm ausführen
taschenrechner()
```

## Nächste Schritte

Nach dieser Einführung können Sie folgende Themen erkunden:

1. **Objektorientierte Programmierung** - Klassen und Objekte
2. **Module und Pakete** - Code organisieren und wiederverwenden
3. **Fehlerbehandlung** - try/except Blöcke
4. **Dateioperationen** - Lesen und Schreiben von Dateien
5. **Externe Bibliotheken** - NumPy, Pandas, Matplotlib, etc.

## Ressourcen zum Weiterlernen

- [Offizielle Python-Dokumentation](https://docs.python.org/de/)
- [Python Tutorial für Anfänger](https://www.python-lernen.de/)
- [Real Python](https://realpython.com/) (Englisch)
- [Codecademy Python-Kurs](https://www.codecademy.com/learn/learn-python-3)

## Viel Erfolg beim Programmieren!

Python ist eine großartige Sprache für Anfänger und Experten gleichermaßen. Mit Übung und Geduld werden Sie schnell Fortschritte machen. Viel Spaß beim Coden!
