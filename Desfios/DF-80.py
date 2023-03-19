numero = []
for c in range(0,5):
    n = int(input("Digite um valor:"))
    if c == 0 or n > numero(len(numero)-1):
        numero.insert(n)
    else:
        pos = 0
        while pos < len(numero):
            if n <= numero(pos):
                numero.insert(pos,n)
                break
        pos += 1
print(numero)


