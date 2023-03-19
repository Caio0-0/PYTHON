lista = []
maxi = 0
minim = 0
for c in range(0,5):
    lista.append(int(input(f"Digite um valor na {c} possição:")))
    if c == 0:
        maxi = minim = lista[c]
    else:
        if lista[c] > maxi:
            maxi = lista[c]
        if lista[c] < minim:
            minim = lista[c]
print(f"Maior numero digitado foi {maxi} na posição")
for i,v in enumerate(lista):
    if v == maxi:
        print(f"{i}...",end="")
print()
print(f"Menor numero digitado foi {minim} na posição")
for i,v in enumerate(lista):
    if v == minim:
        print(f"{i}...",end="")
