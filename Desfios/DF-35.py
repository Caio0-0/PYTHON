l1 = float(input("Fale o 1º lado:"))
l2 = float(input("Fale o 2º lado:"))
l3 = float(input("Fale o 3º lado:"))
if l1+l2>l3 and l2+l3>l1 and l3+l1>l2:
    print("forma uma priramede")
else:
    print("Não forma uma piramede")
