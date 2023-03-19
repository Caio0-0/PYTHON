d = float(input("Fale a distacia da sua viagem Km"))
if d <= 200:
    print("O valor da sua pasagem e de R${}".format(d*0.50))
else:
    print("o valor de sua pasagem e de R${}".format(d*0.45))