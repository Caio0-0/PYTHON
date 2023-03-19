som = 0
for c in range(1,7):
    va = int(input("digite o {}º numero:".format(c)))
    if va % 2 == 0 :
        som = som + va
print("A soma dos numeros pares foi:{}".format(som))