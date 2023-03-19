matr = [0,0,0],[0,0,0],[0,0,0]
d = 0
for c in range(0,3):
    for g in range(0,3):
        matr[c][g] = int(input(f"Digite um valor para [{c}, {g}]: "))
print("=-"*30)
for c in range(0,3):
    for g in range(0,3):
        print(f"[{matr[c][g]:^5}]",end="")
    print()