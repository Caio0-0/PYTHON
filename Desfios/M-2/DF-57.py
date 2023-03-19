s = str(input("Digite seu sexo [M/F]:")).strip().upper()[0]
while s not in "MmFf":
        s = str(input("Sexo invalido!! Digite seu sexo[M/F]:")).strip().upper()[0]
print("Seu sexo é {}".format(s))