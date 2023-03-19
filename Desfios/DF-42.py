l1 = float(input("1º lado:"))
l2 = float(input("2º lado:"))
l3 = float(input("3º lado:"))
if l1+l2>l3 and l1+l3>l2 and l2+l3>l1:
    print("Forma um triangulo")
    if l1==l2 or l2==l3 or l3==l1:
        print("Triangulo ISOSCELES")
    elif l1==l2 and l2==l3 and l3==l1:
        print("Triangulo EQUILÁTERO")
    elif l1!=l2 and l2!=l3 and l3!=l1:
        print("Triangulo ESCALENO")
else:
    print("nao forma um triangulo")
