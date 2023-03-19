soma = 0
quant = 0
for c in range(1,501):
    if c%2==1 and c%3==0:
        soma = soma + c
        quant = quant+1
print("a soma dos {} numros é:{}".format(quant,soma))  