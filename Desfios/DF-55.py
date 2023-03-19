
maior = 0
menor = 0

for c in range(1,6):
    d = float(input("Digite o {}º pesso: ".format(c)))
    if d == 1:
        maior = d
        menor = d
    else:
        if d > maior:
            maior = d
        if d < menor:
            menor = d
print("O maior peso foi {}Kg".format(maior))
print("O menor peso foi {}Kg".format(menor))