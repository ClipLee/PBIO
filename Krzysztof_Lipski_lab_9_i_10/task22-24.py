from Bio.Seq import Seq

# Wczytaj sekwencję DNA za pomocą funkcji input()
seq_dna = input('Wprowadź sekwencję DNA: ')

# Przeprowadź transkrypcję sekwencji DNA na sekwencję RNA
seq_rna = Seq(seq_dna).transcribe()

# Przeprowadź translację sekwencji RNA na łańcuch białkowy
seq_protein = seq_rna.translate()

print('Sekwencja DNA:', seq_dna)
print('Sekwencja RNA:', seq_rna)
print('Łańcuch białkowy:', seq_protein)
