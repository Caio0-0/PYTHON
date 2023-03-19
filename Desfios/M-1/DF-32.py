ano = float(input("Digite o ano:"))
if ano%4==1:
    print("O ano de {} não é bissexto".format(ano))
else:
    print("O ano {} é bissexto".format(ano))