matr = [0,0,0],[0,0,0],[0,0,0]
somaP = somaT = somaL = maior = 0
for c in range(0,3):
    for l in range(0,3):
        matr[c][l] = int(input(f"Digite um valor para [{c}, {l}]: "))
print("=-"*30)
for c in range(0,3):
    for l in range(0,3):
        print(f"[{matr[c][l]:^5}]",end="")
    print()
print("=-"*30)
for c in range(0,3):
    for l in range(0,3):
        if matr[c][l]%2==0:
            somaP = somaP + matr[c][l]     
        if l == 2:
            somaT = somaT + matr[c][l]
        if c == 1:
            if l == 0:
                maior = [c][l]
            else:
                if matr[c][l]>maior:
                    maior = matr[c][l] 
print(f"A soma dos numeros pares é {somaP}")
print(f"A soma dos valore da terceira coluna é {somaT}")
print(f"O maior valor da segunda coluna é {maior}")