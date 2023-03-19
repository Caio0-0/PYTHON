Preço = float(input("Preço das compras: R$"))
print("FORMAS DE PAFAMENTO")
print("[1] à vista dinheiro/cheque")
print("[2] à vista cartão")
print("[3] 2x no cartão")
print("[4] 3x ou mais no cartão")
op = int(input("Qual é a opção: "))
if op == 1:
    des = Preço*0.1
    print("voce teve um desconto de 10% ")
    print("NOVO VALOR: {}".format(Preço-des))
elif op == 2:
    des = Preço*0.05
    print("voce teve um desconto de 5%")
    print("NOVO VALOR: {}".format(Preço-des))
elif op == 3:
    des = Preço/2
    print("valor mensal:{}".format(des))
elif op == 4:
    par = int(input("Parcelar em quantos vezes:"))
    Preço = (Preço/par)*1.2
    print("voce tera que pagar por mês {}".format(Preço))