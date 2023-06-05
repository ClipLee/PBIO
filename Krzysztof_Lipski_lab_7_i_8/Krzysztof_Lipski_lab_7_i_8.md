---
author: Krzysztof Lipski
title: Laboratorium 7 i 8
date: 25.05.2023
keywords: 14C
geometry: margin=2cm
output: pdf_document
fontsize: 12pt
lang: pl
---

## TASK 1

Ma rozmiar: 249280735 bp
Link: [Homo sapiens isolate NA12878 chromosome 1, whole genome shotgun sequen - Nucleotide - NCBI (nih.gov)](https://www.ncbi.nlm.nih.gov/nuccore/CM009447.1)

## TASK 2

Sekwencjonowanie "double-end" polega na sekwencjonowaniu obydwu końców DNA, a "single-end" na tylko jednym końcu.

"Single-end" jest prostsze i tańsze, ale mniej dokładne niż "double-end", które zaweira informacji o długości i orientacji fragmentów DNA względem siebie.

## TASK 3

HISEQ

## TASK 4

1. @HISEQ1:9:H8962ADXX:1:1101:1297:98785/1

2. CAAGAAATATGGGACTATGTGAAAAGACCAAATCTACTTCGGATTGGTGTACCTGAAAGTGATGGGGAGAATGGAAACAAGTTGGAAAACACTCTGCAGGATATTATCCAGGAGAACTTCCCCAATCTAGCACGGCAGGCCAACGTTC

3. +

4. @@@DDDDADHFHHIB@;FF3GHGEFEB>G9CF:FFFGD9BBFAGGGEA@)=@@FCC@EGEFBD@DDECCCC@@A@>@ACCCBB@CC(5@>8<::@CC>AACCCBBBB@CACCC?

 Dodatkowo w podglądzie był jeszcze ciąg znaków: C?C?34(:A@<5<.>0.

## TASK 5

Dane dobrej jakości (Good Illumina Data) mają wysoką jakość sekwencjonowania i niski poziom błędów.

Dane niskiej jakości (Bad Illumina Data) mają niską jakość sekwencjonowania i wysoki poziom błędów.

---

Większość sekwencerów generuje raport QC, jednak jest on zazwyczaj skupiony na identyfikowaniu problemów wygenerowanych przez sam sekwencer.

## TASK 6

Total Sequences: 230 282

## TASK 7

Nie

## TASK 8

Sequence length: 148

## TASK 9

Są to dane Illumna - graficzną reprezentację statystyk jakości na przestrzeni wszystkich baz.

## TASK 10

Bazując na dokumentacji - **tak**, dane są dobrej jakości.

## TASK 11

Error rate wynosi 0.2% w sytuacji, gdy obserwowana średnia jakość jest poniżej 27.

Error rate wynosi 1%, gdy błąd jest zgłaszany oraz jeśli najczęściej obserwowana średnia jakość jest poniżej 20.

W sekwencjonowaniu error rate oznacza procent baz wywołanych niepoprawnie w dowolnym cyklu. Można zaobserwować jego wzrost wraz z długością odczytu.

## TASK 12

Ilość AT oraz CG powinna się zgadzać, ponieważ DNA składa się z par zasad azotowych:

- adeniny (A) łączącej się z tyminą (T) 

- cytozyny © łączącej się z guaniną (G).

W każdej parze zasad azotowych ilość A powinna być równa ilości T, a ilość C równa ilości G. Dlatego też, jeśli ilość AT oraz CG nie zgadza się, może to wskazywać na obecność błędów w sekwencjonowaniu.

## TASK 13

N w sekwencji DNA pochodzącej z sekwencjonowania oznacza, że sekwencer nie był w stanie dokonać poprawnego wywołania "basee call" zasady azotowej w danym miejscu i zastąpił ją literą N. 

Wartość Per base N content pokazuje procentowy udział N w każdym cyklu sekwencjonowania

## TASK 14

To narzędzie służy do mapowania średnich i długich odczytów względem genomu referencyjnego.

## TASK 15

Odczyty o długości większej niż 100 bp

## TASK 16

230552 odczytów

## TASK 17

99.99%

## TASK 18

Mapowanie sekwencji DNA do genomu referencyjnego polega na przyrównywaniu odczytów sekwencjonowanych fragmentów DNA do sekwencji wzorcowej, czyli takiej która jest reprezentatywna dla danego gatunku. Mapowanie pozwala naokreślenie umiejscowienia w genomie, z którego pochodzi dany fragment DNA.

## TASK 19

chr10

## TASK 20

99871

## TASK 21

## TASK 22

## TASK 23

## TASK 24
