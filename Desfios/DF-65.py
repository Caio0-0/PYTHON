
res = ""
soma = quat = menor = maior = 0
while res != "N":
    n = float(input("Digite um numero:"))
    soma = soma+n
    quat = quat + 1
    if quat == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    res = str(input("Quer continuar [S/N]:")).upper()
print("Voce digitou {} numero e a media foi {}".format(quat,soma/quat))
print("O maior valor foi {} e o menor foi {}".format(maior,menor))