l = []
pares = []
impares = []
while True:
    n = int(input("Digite um valor:"))
    l.append(n)
    if n%2==0:
        pares.append(n)
    else:
        impares.append(n)
    r = str(input("Quer continuar[S/N]:"))
    if r in "Nn":
        break
print("=-"*30)
print(f"A lista completa é {l}")
print(f"A lista de pares é {pares}")
print(f"A lista de impares é {impares}")