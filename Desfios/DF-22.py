nome = str(input("Digite seu nome:"))
nomeP = nome.split()
numeroP = len(nomeP[0])
numeroJ = "".join(nomeP)
tamanhoN = len(numeroJ)

print("===========================================================================================")
print("|Seu nome em MAIÚSCULO:{}".format(nome.upper()))
print("|Seu nome em minúsculo:{}".format(nome.lower()))
print("|O seu primeiro nome possui {} letras".format(numeroP))
print("|E seu nome total possui {} letras".format(tamanhoN))
print("=============================================================================================")
