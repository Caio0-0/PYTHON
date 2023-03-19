from random import randint
def sorteio(lista):
    print("Sorteando 5 valores da lista: ",end="")
    for c in range(0,5):
        lista.append(randint(1,10))
        print(lista[c],end=" ")
    print("PRONTO!!")
def somaP(lista):
    soma = 0
    for c,v in enumerate(lista):
        if lista[c]%2==0:
            soma += v 
    print(f"Somando os valores pares de h{lista}, temos {soma}")
        
numero = []
sorteio(numero)
somaP(numero)
print("")