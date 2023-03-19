velo = int(input("Digite sua velocidade em Km/h:"))
if velo > 80:
    print("Você tera que pagar uma multda de R${}".format((velo-80)*7))
else:
    print("Você esta na velocidade OK")