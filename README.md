

---

## 2. Operatoren

```python
# Arithmetische Operatoren
x = 10
y = 3

print(x + y)    # Addition: 13
print(x - y)    # Subtraktion: 7
print(x * y)    # Multiplikation: 30
print(x / y)    # Division: 3.333...
print(x // y)   # Ganzzahlige Division: 3
print(x % y)    # Modulo (Rest): 1
print(x ** y)   # Potenz: 1000

# Vergleichsoperatoren
print(x > y)    # True
print(x == y)   # False
print(x != y)   # True

# Logische Operatoren
a = True
b = False
print(a and b)  # False
print(a or b)   # True
print(not a)    # False
```

---

## 3. Listen

Listen sind veränderbare, geordnete Sammlungen von Elementen.

```python
# Liste erstellen
fruechte = ["Apfel", "Banane", "Orange"]
zahlen = [1, 2, 3, 4, 5]
gemischt = [1, "Text", True, 3.14]

# Auf Elemente zugreifen
print(fruechte[0])          # Apfel (erstes Element)
print(fruechte[-1])         # Orange (letztes Element)

# Liste verändern
fruechte.append("Traube")   # Am Ende hinzufügen
fruechte.insert(1, "Kiwi")  # An Position einfügen
fruechte.remove("Banane")   # Element entfernen
letztes = fruechte.pop()    # Letztes Element entfernen und zurückgeben

# Slicing (Teilbereiche)
zahlen = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(zahlen[2:5])          # [2, 3, 4]
print(zahlen[:3])           # [0, 1, 2]
print(zahlen[7:])           # [7, 8, 9]
print(zahlen[::2])          # [0, 2, 4, 6, 8] (jedes zweite)

# Nützliche Methoden
print(len(zahlen))          # Länge: 10
print(sum(zahlen))          # Summe: 45
print(max(zahlen))          # Maximum: 9
```

---

## 4. Dictionaries (Wörterbücher)

Dictionaries speichern Schlüssel-Wert-Paare.

```python
# Dictionary erstellen
person = {
    "name": "Anna",
    "alter": 28,
    "stadt": "Berlin"
}

# Auf Werte zugreifen
print(person["name"])           # Anna
print(person.get("alter"))      # 28

# Werte ändern und hinzufügen
person["alter"] = 29
person["beruf"] = "Entwicklerin"

# Schlüssel und Werte durchlaufen
for key, value in person.items():
    print(f"{key}: {value}")

# Nützliche Methoden
print(person.keys())            # Alle Schlüssel
print(person.values())          # Alle Werte
print("name" in person)         # Prüfen ob Schlüssel existiert
```

---

## 5. Tupel und Sets

```python
# Tupel (unveränderbar)
koordinaten = (10, 20)
farben = ("rot", "grün", "blau")
# koordinaten[0] = 15  # Fehler! Tupel sind unveränderbar

# Set (Menge ohne Duplikate)
zahlen = {1, 2, 3, 3, 4, 5}
print(zahlen)                   # {1, 2, 3, 4, 5}

# Set-Operationen
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a | b)                    # Vereinigung: {1, 2, 3, 4, 5, 6}
print(a & b)                    # Schnittmenge: {3, 4}
print(a - b)                    # Differenz: {1, 2}
```

---

## 6. Kontrollstrukturen

### If-Else Bedingungen

```python
alter = 18

if alter >= 18:
    print("Volljährig")
elif alter >= 13:
    print("Teenager")
else:
    print("Kind")

# Kurzform (Ternary Operator)
status = "Erwachsen" if alter >= 18 else "Minderjährig"
```

### Schleifen

```python
# For-Schleife
fruechte = ["Apfel", "Banane", "Orange"]
for frucht in fruechte:
    print(frucht)

# Mit Index
for i, frucht in enumerate(fruechte):
    print(f"{i}: {frucht}")

# Range
for i in range(5):              # 0, 1, 2, 3, 4
    print(i)

for i in range(2, 10, 2):       # 2, 4, 6, 8 (Start, Stop, Schritt)
    print(i)

# While-Schleife
count = 0
while count < 5:
    print(count)
    count += 1

# Break und Continue
for i in range(10):
    if i == 3:
        continue                # Überspringt 3
    if i == 7:
        break                   # Beendet Schleife bei 7
    print(i)
```

---

## 7. Funktionen

```python
# Einfache Funktion
def begruessung():
    print("Hallo!")

begruessung()

# Funktion mit Parametern
def addiere(a, b):
    return a + b

ergebnis = addiere(5, 3)        # 8

# Standardwerte
def gruss(name="Gast"):
    return f"Hallo, {name}!"

print(gruss())                  # Hallo, Gast!
print(gruss("Anna"))            # Hallo, Anna!

# Mehrere Rückgabewerte
def berechne(x, y):
    summe = x + y
    differenz = x - y
    return summe, differenz

s, d = berechne(10, 3)

# *args und **kwargs
def summe(*zahlen):
    return sum(zahlen)

print(summe(1, 2, 3, 4, 5))     # 15

def info(**daten):
    for key, value in daten.items():
        print(f"{key}: {value}")

info(name="Max", alter=25, stadt="München")

# Lambda-Funktionen (anonyme Funktionen)
quadrat = lambda x: x ** 2
print(quadrat(5))               # 25

zahlen = [1, 2, 3, 4, 5]
quadriert = list(map(lambda x: x ** 2, zahlen))
print(quadriert)                # [1, 4, 9, 16, 25]
```

---

## 8. List Comprehensions

Elegante Möglichkeit, Listen zu erstellen.

```python
# Normale Schleife
quadrate = []
for x in range(10):
    quadrate.append(x ** 2)

# List Comprehension (kürzer und schneller)
quadrate = [x ** 2 for x in range(10)]

# Mit Bedingung
gerade = [x for x in range(20) if x % 2 == 0]

# Verschachtelt
matrix = [[i + j for j in range(3)] for i in range(3)]
# [[0, 1, 2], [1, 2, 3], [2, 3, 4]]

# Dictionary Comprehension
quadrat_dict = {x: x ** 2 for x in range(5)}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
```

---

## 9. Klassen und Objektorientierung

```python
# Klasse definieren
class Hund:
    # Konstruktor
    def __init__(self, name, alter):
        self.name = name
        self.alter = alter
    
    # Methode
    def bellen(self):
        return f"{self.name} sagt: Wuff!"
    
    def geburtstag(self):
        self.alter += 1

# Objekt erstellen
mein_hund = Hund("Bello", 3)
print(mein_hund.name)           # Bello
print(mein_hund.bellen())       # Bello sagt: Wuff!
mein_hund.geburtstag()
print(mein_hund.alter)          # 4

# Vererbung
class Labrador(Hund):
    def __init__(self, name, alter, farbe):
        super().__init__(name, alter)
        self.farbe = farbe
    
    def apportieren(self):
        return f"{self.name} apportiert den Ball!"

lab = Labrador("Max", 2, "golden")
print(lab.bellen())             # Max sagt: Wuff!
print(lab.apportieren())        # Max apportiert den Ball!
```

---

## 10. Fehlerbehandlung

```python
# Try-Except
try:
    zahl = int(input("Gib eine Zahl ein: "))
    ergebnis = 10 / zahl
    print(f"Ergebnis: {ergebnis}")
except ValueError:
    print("Das war keine gültige Zahl!")
except ZeroDivisionError:
    print("Division durch Null ist nicht möglich!")
except Exception as e:
    print(f"Ein Fehler ist aufgetreten: {e}")
else:
    print("Alles hat geklappt!")
finally:
    print("Dieser Block wird immer ausgeführt")

# Eigene Exceptions
class NegativeZahlError(Exception):
    pass

def wurzel(x):
    if x < 0:
        raise NegativeZahlError("Zahl darf nicht negativ sein!")
    return x ** 0.5
```

---

## 11. Datei-Operationen

```python
# Datei schreiben
with open("beispiel.txt", "w") as datei:
    datei.write("Hallo Welt!\n")
    datei.write("Python ist toll!")

# Datei lesen
with open("beispiel.txt", "r") as datei:
    inhalt = datei.read()
    print(inhalt)

# Zeile für Zeile lesen
with open("beispiel.txt", "r") as datei:
    for zeile in datei:
        print(zeile.strip())

# An Datei anhängen
with open("beispiel.txt", "a") as datei:
    datei.write("\nNeue Zeile")

# JSON verarbeiten
import json

daten = {"name": "Anna", "alter": 28}

# JSON schreiben
with open("daten.json", "w") as f:
    json.dump(daten, f, indent=2)

# JSON lesen
with open("daten.json", "r") as f:
    geladen = json.load(f)
    print(geladen)
```

---

## 12. Module und Imports

```python
# Standardbibliothek importieren
import math
print(math.pi)                  # 3.14159...
print(math.sqrt(16))            # 4.0

# Spezifische Funktionen importieren
from math import sqrt, ceil
print(sqrt(25))                 # 5.0
print(ceil(4.3))                # 5

# Mit Alias
import datetime as dt
heute = dt.date.today()
print(heute)

# Nützliche Module
import random
print(random.randint(1, 10))    # Zufallszahl zwischen 1 und 10
print(random.choice(['a', 'b', 'c']))

from collections import Counter
wörter = ['apfel', 'banane', 'apfel', 'orange', 'apfel']
zählung = Counter(wörter)
print(zählung)                  # Counter({'apfel': 3, 'banane': 1, 'orange': 1})
```

---

## 13. NumPy - Numerisches Rechnen

NumPy ist die fundamentale Bibliothek für wissenschaftliches Rechnen in Python.

### Installation

```bash
pip install numpy
```

### Grundlagen

```python
import numpy as np

# Arrays erstellen
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([[1, 2, 3], [4, 5, 6]])

# Spezielle Arrays
nullen = np.zeros((3, 3))           # 3x3 Matrix mit Nullen
einsen = np.ones((2, 4))            # 2x4 Matrix mit Einsen
bereich = np.arange(0, 10, 2)       # [0, 2, 4, 6, 8]
linspace = np.linspace(0, 1, 5)     # 5 gleichmäßige Werte von 0 bis 1

# Array-Eigenschaften
print(arr2.shape)                   # (2, 3) - Dimensionen
print(arr2.dtype)                   # dtype('int64') - Datentyp
print(arr2.size)                    # 6 - Anzahl Elemente

# Mathematische Operationen (elementweise)
a = np.array([1, 2, 3, 4])
b = np.array([10, 20, 30, 40])

print(a + b)                        # [11, 22, 33, 44]
print(a * b)                        # [10, 40, 90, 160]
print(a ** 2)                       # [1, 4, 9, 16]
print(np.sqrt(a))                   # [1., 1.41, 1.73, 2.]

# Statistische Funktionen
zahlen = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(np.mean(zahlen))              # Mittelwert: 5.5
print(np.median(zahlen))            # Median: 5.5
print(np.std(zahlen))               # Standardabweichung: 2.87
print(np.sum(zahlen))               # Summe: 55
print(np.min(zahlen))               # Minimum: 1
print(np.max(zahlen))               # Maximum: 10

# Indexierung und Slicing
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

print(matrix[0, 1])                 # 2 (Zeile 0, Spalte 1)
print(matrix[:, 1])                 # [2, 5, 8] (gesamte Spalte 1)
print(matrix[1, :])                 # [4, 5, 6] (gesamte Zeile 1)
print(matrix[0:2, 1:3])             # [[2, 3], [5, 6]] (Submatrix)

# Boolean Indexing
zahlen = np.array([1, 2, 3, 4, 5, 6])
gerade = zahlen[zahlen % 2 == 0]
print(gerade)                       # [2, 4, 6]

# Array umformen
arr = np.arange(12)
reshaped = arr.reshape(3, 4)        # In 3x4 Matrix umformen
flattened = reshaped.flatten()      # Zurück in 1D

# Lineare Algebra
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

print(np.dot(A, B))                 # Matrix-Multiplikation
print(A.T)                          # Transponierte Matrix
print(np.linalg.inv(A))             # Inverse Matrix
print(np.linalg.det(A))             # Determinante: -2.0

# Zufallszahlen
np.random.seed(42)                  # Für Reproduzierbarkeit
random_arr = np.random.rand(3, 3)   # Zufallszahlen 0-1
random_int = np.random.randint(0, 10, size=5)  # Zufällige Integers
normal = np.random.randn(1000)      # Normalverteilung
```

---

## 14. PyTorch - Deep Learning Framework

PyTorch ist eine führende Bibliothek für maschinelles Lernen und neuronale Netze.

### Installation

```bash
pip install torch torchvision
```

### Grundlagen - Tensoren

```python
import torch

# Tensoren erstellen (ähnlich wie NumPy Arrays)
x = torch.tensor([1, 2, 3, 4, 5])
y = torch.tensor([[1, 2], [3, 4], [5, 6]])

# Spezielle Tensoren
zeros = torch.zeros(3, 3)           # 3x3 Tensor mit Nullen
ones = torch.ones(2, 4)             # 2x4 Tensor mit Einsen
rand = torch.rand(3, 3)             # Zufallswerte 0-1
randn = torch.randn(3, 3)           # Normalverteilte Zufallswerte

# Tensor-Eigenschaften
print(y.shape)                      # torch.Size([3, 2])
print(y.dtype)                      # torch.int64
print(y.device)                     # cpu (oder cuda bei GPU)

# Tensor-Operationen
a = torch.tensor([1.0, 2.0, 3.0])
b = torch.tensor([4.0, 5.0, 6.0])

print(a + b)                        # tensor([5., 7., 9.])
print(a * b)                        # tensor([4., 10., 18.])
print(torch.dot(a, b))              # Skalarprodukt: 32.0

# Matrix-Operationen
A = torch.randn(3, 4)
B = torch.randn(4, 2)
C = torch.mm(A, B)                  # Matrix-Multiplikation (3x2)

# Umwandlung NumPy <-> PyTorch
import numpy as np
np_array = np.array([1, 2, 3])
torch_tensor = torch.from_numpy(np_array)
back_to_numpy = torch_tensor.numpy()
```

### Automatische Differentiation (Autograd)

```python
# Gradientenberechnung für Training
x = torch.tensor(2.0, requires_grad=True)
y = x ** 2 + 3 * x + 1

# Rückwärtspropagation
y.backward()
print(x.grad)                       # dy/dx = 2*2 + 3 = 7.0

# Beispiel mit mehreren Variablen
a = torch.tensor(3.0, requires_grad=True)
b = torch.tensor(4.0, requires_grad=True)
c = a ** 2 + b ** 2
c.backward()
print(a.grad)                       # dc/da = 6.0
print(b.grad)                       # dc/db = 8.0
```

### Einfaches neuronales Netz

```python
import torch
import torch.nn as nn
import torch.optim as optim

# Einfaches Feed-Forward Netz definieren
class NeuralNetwork(nn.Module):
    def __init__(self):
        super(NeuralNetwork, self).__init__()
        self.layer1 = nn.Linear(10, 64)     # Input: 10, Hidden: 64
        self.layer2 = nn.Linear(64, 32)     # Hidden: 64 -> 32
        self.layer3 = nn.Linear(32, 1)      # Output: 1
        self.relu = nn.ReLU()
    
    def forward(self, x):
        x = self.relu(self.layer1(x))
        x = self.relu(self.layer2(x))
        x = self.layer3(x)
        return x

# Modell erstellen
model = NeuralNetwork()
print(model)

# Loss-Funktion und Optimizer
criterion = nn.MSELoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

# Training (vereinfachtes Beispiel)
for epoch in range(100):
    # Dummy-Daten
    inputs = torch.randn(32, 10)        # Batch von 32, Feature: 10
    targets = torch.randn(32, 1)        # Zielwerte
    
    # Forward Pass
    outputs = model(inputs)
    loss = criterion(outputs, targets)
    
    # Backward Pass und Optimierung
    optimizer.zero_grad()               # Gradienten zurücksetzen
    loss.backward()                     # Gradienten berechnen
    optimizer.step()                    # Gewichte aktualisieren
    
    if (epoch + 1) % 20 == 0:
        print(f'Epoch [{epoch+1}/100], Loss: {loss.item():.4f}')

# Modell speichern und laden
torch.save(model.state_dict(), 'model.pth')
model.load_state_dict(torch.load('model.pth'))
```

### GPU-Beschleunigung

```python
# Prüfen ob GPU verfügbar ist
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
print(f'Using device: {device}')

# Modell und Daten auf GPU verschieben
model = NeuralNetwork().to(device)
inputs = torch.randn(32, 10).to(device)
outputs = model(inputs)

# Zurück zur CPU
outputs_cpu = outputs.cpu()
```

### Nützliche PyTorch Features

```python
# Dataset und DataLoader für Batch-Processing
from torch.utils.data import Dataset, DataLoader

class CustomDataset(Dataset):
    def __init__(self, data, labels):
        self.data = data
        self.labels = labels
    
    def __len__(self):
        return len(self.data)
    
    def __getitem__(self, idx):
        return self.data[idx], self.labels[idx]

# DataLoader verwenden
dataset = CustomDataset(torch.randn(100, 10), torch.randn(100, 1))
dataloader = DataLoader(dataset, batch_size=16, shuffle=True)

for batch_data, batch_labels in dataloader:
    # Training mit Batches
    pass
```

---

## Übungen und Praxis

📚 **Möchtest du dein Wissen testen?**

Dieses Repository enthält ein interaktives Jupyter Notebook mit Übungsaufgaben zu allen behandelten Themen:

👉 **[uebungen.ipynb](uebungen.ipynb)** - Praktische Aufgaben zum Selbststudium

Das Notebook enthält:
- Aufgaben zu jedem Kapitel (Variablen, Listen, Funktionen, Klassen, etc.)
- Herausforderungen für NumPy und PyTorch
- Code-Zellen zum direkten Ausprobieren
- Hinweise auf die entsprechenden Abschnitte in dieser README

**Viel Erfolg beim Lernen und Programmieren!** 🐍

---
