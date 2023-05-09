sekwencja_białkowa = input("Podaj sekwencję białkową: ")
char = "*"
output = ""
for i in sekwencja_białkowa:
    if i == "P":
        output += char + i
    else:
        output += i
print(output)