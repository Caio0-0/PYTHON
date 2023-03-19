ano = int(input("Digite o ano que nasceu:"))
idade = 2017-ano 
print("O atleta te {} anos".format(idade))
if idade > 1 and idade <= 9:
    print("Classificação: MIRIM")
elif idade > 9 and idade <= 14:
    print("Classificação: INFANTIL")
elif idade > 14 and idade <=19:
    print("Classificação: JUNIOR")
elif idade > 19 and idade <=25:
    print("Classificação: SÊNIOR")
elif idade > 25:
    print("Classificação: MASTER")