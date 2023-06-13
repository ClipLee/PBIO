import pandas as pd
from scipy.stats import ttest_ind

# Wczytanie danych
dane1 = pd.read_csv('Krzysztof_Lipski_lab_9_i_10/dane_biologiczne1.csv')
dane2 = pd.read_csv('Krzysztof_Lipski_lab_9_i_10/dane_biologiczne2.csv')

# Obliczenie średniej i odchylenia standardowego dla każdego zbioru danych
srednia1 = dane1['wartosc'].mean()
odchylenie1 = dane1['wartosc'].std()

srednia2 = dane2['wartosc'].mean()
odchylenie2 = dane2['wartosc'].std()

# Przeprowadzenie t-test dla dwóch niezależnych prób
statystyka_t, p_value = ttest_ind(dane1['wartosc'], dane2['wartosc'])

print('Średnia wartość dla pierwszego zbioru danych:', srednia1)
print('Odchylenie standardowe dla pierwszego zbioru danych:', odchylenie1)

print('Średnia wartość dla drugiego zbioru danych:', srednia2)
print('Odchylenie standardowe dla drugiego zbioru danych:', odchylenie2)

print('Statystyka t:', statystyka_t)
print('P-wartość:', p_value)
