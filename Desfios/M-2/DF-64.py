n = 0
quan = 0
soma = 0
while n != 999:
    n = int(input("Digite um numero[999 para parar]:"))
    if n != 999:
        quan = quan + 1
        soma = soma + n
print("Você digitou {} números e a soma entre eles foi {}.".format(quan,soma))