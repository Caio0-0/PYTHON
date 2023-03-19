nomeP = list()
dado = list()
maior = menor =0
while True:
    dado.append(str(input("Nome: ")))
    dado.append(float(input("Idade: ")))
    r = str(input("Quer continuar[S/N]: "))
    if r in "Nn":
        break 
for n,p in enumerate(nomeP):
    if n == 0:
        maior = menor = p[1]
    else:
        if  p[1]>=maior:
            maior = p[1]
        if p[1]<=menor:
            menor = p[1]
print("=-"*40)
print(f"Voce cadastrou {len(nomeP)} pessoas")
print(f"O peso mairo foi de {maior}kg. Peso de",end="")
for p in nomeP:
    if p[1] == maior:
        print(f"[{p[0]}]",end="")
print()
print(f"O menor peso foi de {menor}Kg. Peso de ",end="")
for p in nomeP:
    if p[1] == menor:
        print(f"[{p[0]}]",end="")
print()