n=str(input("Digite sua espreção: "))
a = n.count("(")
f = n.count(")")
if (f+a)%2==0:
    print("Espreção validade")
else:
    print("Espreção invalida")
