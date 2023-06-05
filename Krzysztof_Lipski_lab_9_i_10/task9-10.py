sekwencja_dna = "ATGCTACGATCGTACGGCGCAAATAGCTAGCTAGCTAGC"

# Liczba par zasad GC w sekwencji
liczba_gc = sekwencja_dna.count("G") + sekwencja_dna.count("C")

# Procentowej zawartość par zasad GC
procent_gc = liczba_gc / len(sekwencja_dna) * 100

# Wyświetlenie wyniku
print("Procentowa zawartość par zasad GC: {:.2f}%".format(procent_gc))
