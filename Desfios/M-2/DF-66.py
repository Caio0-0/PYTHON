soma = quat = 0
while True:
    n = int(input("Digite um valor (999 para parar):"))
    if n == 999:
        break
    soma = soma + n
    quat = quat + 1
print(f"A somo dos {quat} valores foi de {soma}") 