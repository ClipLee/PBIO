---
author: Krzysztof Lipski
title: Laboratorium 4
date: 25.04.2023
keywords: 14C
geometry: margin=2cm
output: pdf_document
fontsize: 12pt
lang: pl
---

## TASK 1

[link](https://www.rcsb.org/structure/5O9Z)

## TASK 2

![image-20230427014933458](C:\Users\klips\AppData\Roaming\Typora\typora-user-images\image-20230427014933458.png)

## TASK 3

![](C:\Users\klips\Documents\PJATK\6 - Letni\PBIO\PBIO\Krzysztof_Lipski_lab_4\sticks.png)

## TASK 4

Na ekranie widać model substancji chemicznej, przedstawiającej położenie atomów tej substancji, oraz wiązania między nimi.

Kulkami są <u>atomy</u>, a pomiędzy nimi łączenia to <u>wiązania</u>.

## TASK 5

![](C:\Users\klips\Documents\PJATK\6 - Letni\PBIO\PBIO\Krzysztof_Lipski_lab_4\cartoon_protein.png)

Jest ukazana uproszczona reprezentacja struktury protein, poprzez wstążki. Jest to trójwymiarowa reprezentacja, współcześnie najczęściej wykorzystywana

## TASK 6

![](C:\Users\klips\Documents\PJATK\6 - Letni\PBIO\PBIO\Krzysztof_Lipski_lab_4\protein_ribbon_view.png)

## TASK 7

Jest to sposób reprezenacji struktury przedstawiający generalny keirunek i organizację szkieletu protein, i służy do generalnego odzwierciedlenia szczegółów całej struktury atomowej.

## TASK 8

![image-20230427020637566](C:\Users\klips\AppData\Roaming\Typora\typora-user-images\image-20230427020637566.png)

Helisa alpha - wzrost wzdłuż osi x

Beta-loops - maleje wzdłuż osi x

Hot-spoty - większość pojawia się na początku osi x

## TASK 9

Oznaczają prawdopodobieństwo wartości pH, Pe i pC, dla przewidzianej (H) helisy, (E) $\beta$ nici i (C) coli.

## TASK 10

Oznacza numer przewidzianych helis transmembranowych.

## TASK 11

Exp number of AAs in TMHs: 159.47336 — oczekiwana liczba aminokwasów w helisach transmembranowych

## TASK 12

Największe prawdopodobieństwo transmembranowych helis jest w okolicach 75-100, 100-140, 150-170,. 190-220, 240-250, 325-350 i 360-380. Najpierw wartość 1 posiada wewnątrzkomórkowa strona błony, a następnie zewnętrzna, po czym po transmembranowych helisach następuje ich zamiana.

## TASK 13

Analiza z pierwszej strony wydaje się być bardziej dokładna, oraz przedstawiać więcej szczegółów. Druga strona dodatkowo przedstawia najbardziej prawdopodobną topologię dla typu alpha TM.

## TASK 14

![](C:\Users\klips\Documents\PJATK\6 - Letni\PBIO\PBIO\Krzysztof_Lipski_lab_4\task4_protein_MembraneFold.png)

## TASK 15

Membrane fold łączy dwa typy narzędzi przewidywania sekwencji protein:

- strukturę protein (AlphaFold, OmegaFold i transmembranową topologie protein)
- zestaw narzędzi Mol* w celu wizualizacji

## TASK 16

**PDB DOI:** [https://doi.org/10.2210/pdb4UUM/pdb](https://doi.org/10.2210/pdb4UUM/pdb)

## TASK 17

![](C:\Users\klips\Documents\PJATK\6 - Letni\PBIO\PBIO\Krzysztof_Lipski_lab_4\task 17.jpeg)

## TASK 18

Pierwszy aminokwas tego białka to META, jest to Metionina.

## TASK 19

Są to koordynaty (oś x, y i z) atomów, które są częścią proteiny. Są one podane w angstremach (Å).

## TASK 20

Opcja *Fast* korzysta z metod przypisania: sekwencja-sekwencja i sekwencja-profil

## TASK 21

- No. of sequences submitted: 1
- No. of hits detected : 79
- No. of models calculated : 56
- Model selection criteria : MPQS TSVMOD LONGEST_DOPE DOPE
- No. of models selected : 1

## TASK 22

Według dokumentacji strony *modbase.compbio.ucsf.edu*, dane można uznać za wiarygodne.

## TASK 23

Struktura białka 4UUL, pobrana ze strony www.rcs.org, z odnośnika z [wygenerowanego modelu](https://modbase.compbio.ucsf.edu/modbase-cgi/model_details.cgi?queryfile=1683623934_6314&searchmode=default&displaymode=moddetail&seq_id=aa1c038aaa2d48fbd72da4436c1ed4bcMSEAAQGG).

## TASK 24

```python
sekwencja_białkowa = input("Podaj sekwencję białkową: ")
char = "*"
output = ""
for i in sekwencja_białkowa:
    if i == "P":
        output += char + i
    else:
        output += i
print(output)
```
