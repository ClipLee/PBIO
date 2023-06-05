import pandas as pd

# Wczytanie danych z pliku Excel
df = pd.read_excel('dane_sekwencji.xlsx')

# Obliczenie statystyk dla każdej właściwości
srednia = df.mean()
mediana = df.median()
odchylenie_std = df.std()

# Wyświetlenie wyników
print("Średnia:")
print(srednia)
print("\nMediana:")
print(mediana)
print("\nOdchylenie standardowe:")
print(odchylenie_std)
