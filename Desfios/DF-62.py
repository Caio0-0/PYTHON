p1 = int(input("Primeiro termo: "))
pa = int(input("Razão da PA: "))
cont = 1
a = p1
mais = 1
quant = 0
while cont <= 10:
    print(a,end=" -=-> ")
    cont += 1 
    a = a+pa
    quant = quant + 1
print("PAUSA")
while mais != 0 : 
    cont = 1
    mais = int(input("Quantos termos voce quer mostrar a mais:"))
    if mais != 0:
        quant = quant + mais
    while cont <= mais:
        print(a,end=" -=-> ")
        cont += 1
        a = a+pa
    print("PAUSA")
print("{} termos mostrados.".format(quant))