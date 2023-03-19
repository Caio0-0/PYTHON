n1 = int(input("1º numero:"))
n2 = int(input("2º numero:"))
n3 = int(input("3º numero:"))
menor = n1
if n2<n1 and n2<n3:
    menor = n2
if n3 <n1 and n3 < n2:
    menor = n3
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print("O maior numero é {}".format(maior))
print("O menor numero é {}".format(menor))
