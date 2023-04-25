def compare_dna_sequences(seq1, seq2):
    if len(seq1) != len(seq2):
        print("Sekwencje są różnej długości")
        return
    result = []
    for i in range(len(seq1)):
        if seq1[i] != seq2[i]:
            result.append((i+1, seq1[i], seq2[i]))
    return result


seq1 = input("Podaj 1 sekwencję DNA: ")
seq2 = input("Podaj 2 sekwencję DNA: ")
print(compare_dna_sequences(seq1, seq2))
