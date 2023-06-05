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
