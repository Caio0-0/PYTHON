f = str(input("Digite uma faze:")).strip().upper()
r = f.split()
j = "".join(r)
invr = ""
for c in range(len(j)-1,-1,-1):
    invr += j[c]
if j == invr:
    print("É palindromo")
else:
    print("Não é palindromo")