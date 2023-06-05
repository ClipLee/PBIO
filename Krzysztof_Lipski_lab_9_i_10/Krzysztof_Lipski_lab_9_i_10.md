---
author: Krzysztof Lipski
title: Laboratorium 9 i 10
date: 25.05.2023
keywords: 14C
geometry: margin=2cm
output: pdf_document
fontsize: 12pt
lang: pl
---

## TASK 1-2

```python
dna_seq = input("Podaj sekwencję DNA: ")

# Zainicjowanie liczników nukleotydów
licznik_adeniny = 0
licznik_cytozyny = 0
licznik_guaniny = 0
licznik_tyminy = 0

# Przejście przez każdy nukleotyd w sekwencji DNA
for nukleotyd in dna_seq:
    if nukleotyd == "A":
        licznik_adeniny += 1
    elif nukleotyd == "C":
        licznik_cytozyny += 1
    elif nukleotyd == "G":
        licznik_guaniny += 1
    elif nukleotyd == "T":
        licznik_tyminy += 1

print("Liczba adenin: ", licznik_adeniny)
print("Liczba cytozyn: ", licznik_cytozyny)
print("Liczba guanin: ", licznik_guaniny)
print("Liczba tymin: ", licznik_tyminy)

```

## TASK 3-5

```python
sekwencja_dna = input("Podaj sekwencję DNA: ")

# Podmiana wystąpień tyminy i uracylu
sekwencja_rna = sekwencja_dna.replace("T", "U")

print("Sekwencja RNA: ", sekwencja_rna)
print("Długość sekwencji RNA: ", len(sekwencja_rna))

```

## TASK 6-8

```python
# Słownik zawierający masy aminokwasów
amino_acid_masses = {
    "A": 89.094,
    "C": 121.154,
    "D": 133.104,
    "E": 147.131,
    "F": 165.192,
    "G": 75.067,
    "H": 155.156,
    "I": 131.175,
    "K": 146.189,
    "L": 131.175,
    "M": 149.208,
    "N": 132.119,
    "P": 115.132,
    "Q": 146.146,
    "R": 174.203,
    "S": 105.093,
    "T": 119.120,
    "V": 117.148,
    "W": 204.228,
    "Y": 181.191,
}

peptyd = input("Podaj sekwencję peptydu: ")

# Masa cząsteczkowa peptydu
masa = sum([amino_acid_masses[a] for a in peptyd])

# Wynik
print("Masa cząsteczkowa peptydu: ", round(masa, 2))


```

## TASK 9-10

```python
sekwencja_dna = "ATGCTACGATCGTACGGCGCAAATAGCTAGCTAGCTAGC"

# Liczba par zasad GC w sekwencji
liczba_gc = sekwencja_dna.count("G") + sekwencja_dna.count("C")

# Procentowej zawartość par zasad GC
procent_gc = liczba_gc / len(sekwencja_dna) * 100

# Wyświetlenie wyniku
print("Procentowa zawartość par zasad GC: {:.2f}%".format(procent_gc))

```

## TASK 11-12

```pytho

```

## TASK 13

## TASK 14

## TASK 15

## TASK 16

## TASK 17

## TASK 18

## TASK 19

## TASK 20

## TASK 21

## TASK 22

## TASK 23

## TASK 24
