casa = float(input("Valor da casa: R$"))
salario = float(input("Salário do comprador: R$"))
fina = float(input("Quantos anos de financiamento:"))

if salario*0.3 < casa/(12*fina):
    print("Para pagar uma casa de R${} em {} anos a prestação de {:.2f} ".format(casa,fina,casa/(12*fina)))
    print("Emprestimo NEGADO!!")
elif salario*0.3 > casa/(12*fina):
    print("Para pagar uma casa de R${} em {} anos a prestação de {:.2f} ".format(casa,fina,casa/(12*fina))) 
    print("Emprestimo CONCEDIDO")   