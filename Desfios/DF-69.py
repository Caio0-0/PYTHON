m = maior = f = 0

while True:
    print("-"*35)
    print("CADASTRE UMA PESSOA")
    print("-"*35)
    idade = int(input("Idade: "))
    sexo = " "
    while sexo not in "MF":
        sexo = str(input("Qual seu sexo[M/F]:")).strip().upper()[0]
    if idade >= 18:
            maior = maior + 1
    if sexo == "M":
            m = m + 1  
    if idade < 20 and sexo == "F":
            f = f + 1
    print("-="*35)
    cont = " "
    while cont not in "SN":
        cont = str(input("Quer continuar [S/N]:")).strip().upper()[0]
        
    if cont == "N":
        break
print("-="*35)
print(f"Total de pessoas com mais de 18 anos:{maior}")
print(f"Ao todo temos {m} homens cadastrados")
print(f"E temos {f} mulher com menos de 20 anos")
print("-="*35)
        