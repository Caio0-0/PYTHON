

numero = list()
while True:
    n = int(input("Digte um valor:"))
    if n not in numero:
        numero.append(n)
    else:
        print("Valor duplicado não vou adicionar!!!")
    esco = str(input("Quer continuar [S/N]:")).strip().upper()
    if esco == "N":
        break

print(numero)