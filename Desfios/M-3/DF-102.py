def fatorial(n,show=False):
    f = 1
    for c in range(n, 0,-1):
        f *= c
        if show==True:
            print(f,end=" ")

    print(f)
numero = int(input("Digite um numero:"))
fatorial(numero,show=True)
print("")