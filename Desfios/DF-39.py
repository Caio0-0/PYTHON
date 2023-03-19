print("=================================================")
na = int(input("|Digite o ano que voce nascel:"))
idade = 2023 - na
if idade == 18:
    print("você ja tem {} já chegol a hora de se alistar".format(idade))
elif idade > 18:
    print("já se passaram {} anos e voce tinha que se alisar em {}".format(idade-18,na+18))
elif idade < 18:
    print("voce vai ter se alistar em {}".format(na+18)) 