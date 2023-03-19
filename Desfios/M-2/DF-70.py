print("-"*35)
print("            LOJA DO CAIO")
print("-"*35)
cont = barato = soma = mais = 0
nomeB = " "
while True:
    nome = str(input("Digite o nome do Produto: "))
    pro = float(input("Proço: "))
    cont = cont+1
    soma = pro+soma
    if pro >= 1000:
        mais =mais+1
    if cont == 1:
        barato = pro
        nomeB = nome 
    elif cont != 1:
        if barato > pro:
            barato = pro
            nomeB = nome
    sair = " "
    while sair not in "SN":
        sair = str(input("Quer continuar [S/N]: ")).strip().upper()[0]
    if sair == "N":
        break
    print("-="*35)
print("---------------FIM DO PROGAMA-----------------")
print(f" O total da compra foi R${soma}")
print(f"Temo {mais} produtos custando mais de R$1000")
print(f"o produto mais barato foi {nomeB} que cusra {barato}")