maior = 0
p1 = int(input("1º valor: "))
p2 = int(input("2º Valor: "))
op = 0
while op != 5 :
    print("   [ 1 ] somar")
    print("   [ 2 ] multiplicar")
    print("   [ 3 ] maior")
    print("   [ 4 ] novos numeros")
    print("   [ 5 ] sair do programa")
    op = int(input(">>>>>> Qual é sua opção:"))
    print("=-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==-==")
    if op == 1:
        print("A soma de {} + {} = {}".format(p1,p2,p1+p2))
    if op == 2 :
        print("{} x {} = {}".format(p1,p2,p1*p2))
    if op == 3 :
        if p1 > p2 :
            maior = p1
            print("entre {} e {} omaior é {}".format(p1,p2,maior))
        elif p2 > p1 :
            maior = p2
            print("Entre {} e {} o mairo é {}".format(p1,p2,maior))
        elif p1 == p2 :
            print("os dois valores são iguais")
    if op == 4 :
        p1 = int(input("1º novo valor: "))
        p2 = int(input("2º novo Valor: "))
    if op > 5:
        print("opção invalida!!!")
print("Fim do progama")

