import pandas as pd

break_line = "\n" + 50*"-" + "\n"

# Wczytanie danych z pliku Excel
dataframe = pd.read_excel('Krzysztof_Lipski_lab_9_i_10/dane_sekwencji.xlsx')

# Obliczenie statystyk dla każdej właściwości
srednia_w1 = dataframe['Własność1'].mean()
mediana_w1 = dataframe['Własność1'].median()
odchylenie_std_w1 = dataframe['Własność1'].std()

# Obliczenie statystyk dla każdej właściwości
srednia_w2 = dataframe['Własność2'].mean()
mediana_w2 = dataframe['Własność2'].median()
odchylenie_std_w2 = dataframe['Własność2'].std()

# Wyświetlenie wyników
print("Średnia własność 1:" , srednia_w1)
print("Mediana własność 1:", mediana_w1)
print("Odchylenie standardowe własność 1:", odchylenie_std_w1)

print(break_line)

print("Średnia własność 2:" , srednia_w2)
print("Mediana własność 2:", mediana_w2)
print("Odchylenie standardowe własność 2:", odchylenie_std_w2)