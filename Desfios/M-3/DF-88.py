from random import randint
lista = []
numero = cont = 0
veze = int(input("Quantos jogos voce quer que eu sorteir: "))
for c in range(0,veze):
    lista.clear
    cont = 0
    while True:
        numero = randint(1,60)
        if numero not in lista:
            lista.append(numero)
            cont += 1
        if cont == 6:
            break
    print(lista)
    lista.clear()