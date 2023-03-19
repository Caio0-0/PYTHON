dado = {}
dado["nome"] = str(input("Nome: "))
dado["nasci"] = int(input("Ano de nascimento: "))
dado["carte"] = int(input("Carteira de Trabalho (0 não tem):"))
dado["nasci"] = 2018 - dado["nasci"]

if dado["carte"] != 0:
    dado["contra"] = int(input("Ano de contratação: "))
    dado["Salario"] = float(input("Salario: R$ "))
    dado["Aposentadoria"] = ((dado["contra"]+35)-2018)+dado["nasci"]
print("-="*40)
print(dado)
for k, v in dado.items():
    print(f"{k} tem o valor {v}" )