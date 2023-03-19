somaI = 0
idadeM = 0
garNome = ""
menos20 = 0
for c in range(1,5):
    print("----- {}º PESSOA -----".format(c))
    nome = str(input("NOME: "))
    idade = float(input("IDADE: "))
    sexo =  str(input("SEXO[M/F]: ")).strip().upper()
    somaI += idade
    if c == 1 and sexo == "M":
        idadeM = idade 
        garNome = nome
    else:
        if idade > idadeM and sexo == "M":
            idadeM = idade
            garNome = nome
    if sexo == "F" and idade < 20:
        menos20 += 1
print("A media de idade do grupo:{}".format(somaI/4))
print("O {} tem {} anos e é o mais velho.".format(garNome,idadeM))
print("E possue {} mulheres com menos de 20 anos".format(menos20 ))



