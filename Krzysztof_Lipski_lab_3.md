---
author: Krzysztof Lipski
title: Laboratorium 3
date: 23.03.2023
keywords: 14C
geometry: margin=2cm
output: pdf_document
fontsize: 12pt
lang: pl
---

## TASK 1

1. Y-chromosomalna
2. Mitochondrialna
3. Autosomalna

## TASK 2

Nie

## TASK 3

N jest to nukleotyd o pełnej nazwie Adenina / Guanina / Cytosinea/ Tymina. Gdyby zawierał taki nukleotyd oznaczałoby, że istnieje zmienność przeciwciał V(D)J.

## TASK 4

Genom nie zawiera ozaczeń innych niż A, C, T lub G, oznacza to, że genom składa się tylko z Adeniny, Cytozyny, Guaniny i Tyniny. Świadczy to o tym, że jest to czyste DNA bez RNA.

## TASK 5

Oznaczenie Y świadczyłoby o obecności Pirymidyny $C_4H_4N_2$.

## TASK 6

Pełne regiony podanego mDNA to HVR2 oraz HVR1.

## TASK 7

Znalazł markery HVR2, CR, HVR1

## TASK 8

Marker genetyczny jest to cecha organizmu wykorzystywana do określenia jego genotypu. Może to być obecność lub brak jakiegoś genu lub białka, albo występowanie jakiejś szczególnej jego postaci. Markery genetyczne znajdują też zastosowanie do identyfikowania osób lub osobników zwierząt czy roślin.

## TASK 9

Algorytm wykazał haplogrupę J1c7.

## TASK 10

rCRS to skrót od Revised Camridge Reference Sequence.

## TASK 11

H2a2a1

## TASK 12

- Nr. EU151466.1
- Narodowość: Francja, uniwersytet Hiszpański.

## TASK 13

Występuje mutacja S: Tranzycja - zamiana guaniny na adeninę.

## TASK 14

![Haplogroup frequency heatmap](haplogroup_frequency_heatmap.jpeg)

## TASK 15

DYS456- to marker genetyczny w DNA, a dokładniej na chromosomie Y.

## TASK 16

Sekwencja, która się powtarza, to 12 nukleotydów.

## TASK 17

27

## TASK 18

Za pomocą tego narzędzia można *przewidzieć* haplogrupę i znaleźć najbardziej prawdopodobną.

## TASK 19

Jest to baza zawierająca informacje na teamt haplogrupy chromosomu Y.

## TASK 20

- Minimalny zestaw markerów dla inkluzji YHRD
- Y12 - zestaw markerów pochodnych od PowerPlex Y
- Y17 - zestaw markerów pochodnych od Yfiler
- Y23 - zesttaw markerów pochodnych od PowerPlex 23
- Y27 - zestaw makerów pochodnych od Yfiler Plus
- Ymax - maerkerów reprezentujący wszystkie dostępne markery YHRD

## TASK 21

Zaobserwowane allele dla markera DYS19 to:

- 6,
- 9,
- 10
- 11,
- 12,
- 13,
- 13.2,
- 13.3,
- 14,
- 14.1,
- 14.2,
- 14.3,
- 15,
- 15.2,
- 16,
- 16.2,
- 17,
- 18,
- 19,
- 19.1,
- 20

## TASK 22

Baza YHRD zawiera 106 025 haplotypów

## TASK 23

| Count | DYS391 | DYS389I | DYS439 | DYS389II | DYS438 | DYS437 | DYS19 | DYS392 | DYS393 | DYS390 | DYS385 |
|-------|--------|---------|--------|----------|--------|--------|-------|--------|--------|--------|--------|
| 295   | 10     | 13      | 10     | 30       | 11     | 14     | 17    | 11     | 13     | 25     | 10,14  |
| 261   | 10     | 13      | 11     | 29       | 11     | 14     | 16    | 11     | 13     | 25     | 11,14  |
| 138   | 10     | 13      | 10     | 30       | 11     | 14     | 16    | 11     | 13     | 25     | 11,14  |
| 116   | 11     | 13      | 10     | 30       | 11     | 14     | 16    | 11     | 13     | 25     | 11,14  |
| 88    | 11     | 13      | 10     | 30       | 11     | 14     | 15    | 11     | 13     | 25     | 11,14  |
| 82    | 11     | 13      | 13     | 31       | 10     | 15     | 16    | 11     | 13     | 24     | 14,15  |
| 78    | 10     | 13      | 11     | 30       | 11     | 14     | 16    | 11     | 13     | 25     | 11,14  |
| 75    | 10     | 13      | 10     | 30       | 11     | 14     | 16    | 11     | 13     | 25     | 10,14  |
| 73    | 10     | 13      | 11     | 29       | 11     | 14     | 15    | 11     | 13     | 25     | 11,14  |
| 70    | 10     | 13      | 10     | 30       | 11     | 14     | 15    | 11     | 13     | 25     | 11,14  |

[Poprawiona tabela z walidatora, za pomocą opcji Search](PBIO-Y12-TASK23_validated.xlsx)

## TASK 24


## TASK 25

## TASK 26

```python
def compare_dna_sequences(seq1, seq2):
    if len(seq1) != len(seq2):
        print("Sekwencje różnej długości")
        return
    result = []
    for i in range(len(seq1)):
        if seq1[i] != seq2[i]:
            result.append((i+1, seq1[i], seq2[i]))
    return result

seq1 = input("Podaj sekwencję DNA 1: ")
seq2 = input("Podaj sekwencję DNA 2: ")
print(compare_dna_sequences(seq1, seq2))
```

## TASK 27
