def hairpin(sequence):
    max_pairs = 0
    for i in range(1, len(sequence) // 2 + 1):
        pairs = 0
        for j in range(i):
            if sequence[j] == complement(sequence[-i+j]):
                pairs += 1
        max_pairs = max(max_pairs, pairs)
    return max_pairs

def complement(nucleotide):
    if nucleotide == 'A':
        return 'T'
    elif nucleotide == 'T':
        return 'A'
    elif nucleotide == 'C':
        return 'G'
    elif nucleotide == 'G':
        return 'C'

seq = input("Podaj sekwencję DNA: ")
print(hairpin(seq))