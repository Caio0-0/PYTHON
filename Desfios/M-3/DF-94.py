from operator import itemgetter
pessoas = {}
lisa = []
soma = media = 0
while True:
    pessoas.clear()
    pessoas["nome"] = str(input("Nome: "))
    while True:
        pessoas["sexo"] = str(input("Sexo: ")).upper()
        if pessoas["sexo"] in "MF":
            break
        else:
            print("Erro apenas[M/F]. ",end="")
    pessoas["idade"] = int(input("Idade: "))
    soma = soma + pessoas["idade"]
    r = str(input("Quer continuar [S/N]:"))
    lisa.append(pessoas.copy())
    if r in "Nn":
        break
media = soma/len(lisa)
print(f" A) Ao total temos {len(lisa)} pessoas cadastradas.")
print(f" B) A media de idade é de {media} anos.")
print(f" C) As muleres cadastradas foram ", end="")
for p in lisa:
    if p["sexo"] in "Ff":
        print(p["nome"],end=" ")
print()
print(" D) Lista de pessoas que estão acima da media: ")
for p in lisa:
    if p["idade"] >= media:
        print("      ")
        for k , v in p.items():
            print(f"{k} = {v};",end="")
        print()