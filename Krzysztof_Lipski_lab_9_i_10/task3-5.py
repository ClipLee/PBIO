sekwencja_dna = input("Podaj sekwencję DNA: ")

# Podmiana wystąpień tyminy i uracylu
sekwencja_rna = sekwencja_dna.replace("T", "U")

print("Sekwencja RNA: ", sekwencja_rna)
print("Długość sekwencji RNA: ", len(sekwencja_rna))
