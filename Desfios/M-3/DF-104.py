def leiaInt(msg):
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            break
        else:
             print("erro")
    return valor
n = leiaInt("Digite um numero: ")
print(f"O numero que você digitou foi {n}")
print("")