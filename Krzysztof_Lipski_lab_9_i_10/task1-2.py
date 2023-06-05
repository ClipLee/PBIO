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
