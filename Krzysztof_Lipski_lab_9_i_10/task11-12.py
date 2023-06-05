# Dane wejściowe
homozygoty_dominujace = 100
heterozygoty = 200
homozygoty_recesywne = 100
# dalej już Twój kod

# Liczba alleli
liczba_alleli = homozygoty_dominujace + heterozygoty + homozygoty_recesywne

# Występowanie allelu dominującego (A)
czestotliwosc_a = (2 * homozygoty_dominujace +
                   heterozygoty) / (2 * liczba_alleli)

# Występowanie allelu recesywnego (a)
czestotliwosc_A = 1 - czestotliwosc_a

# Wyświetlenie wyniku
print("Częstotliwość dla allelu A:", "{:.2f}".format(czestotliwosc_a))
print("Częstotliwość dla allelu a:", "{:.2f}".format(czestotliwosc_A))

print("test dla A:", czestotliwosc_a)
print("test dla A:", czestotliwosc_A)
