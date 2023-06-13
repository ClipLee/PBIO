import pandas as pd
import matplotlib.pyplot as plt

# Wczytanie danych z pliku CSV
dane = pd.read_csv('Krzysztof_Lipski_lab_9_i_10/dane_szczepienia.csv')

# Stworzenie wykresu słupkowego
plt.bar(dane['Grupa wiekowa'], dane['Liczba zaszczepionych'])

# Dodanie tytułu wykresu i opisu osi x i y
plt.title('Liczba osób, które otrzymay szczepienie przeciwko COVID-19 w różnych grupach wiekowych')
plt.xlabel('Grupa wiekowa')
plt.ylabel('Liczba zaszczepionych')

plt.show()
