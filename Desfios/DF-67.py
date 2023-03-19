cont = 1
while True:
    cont = 1
    print("-"*40)
    va = int(input("Quer ver a tabuada de qual valor: "))
    print("-"*40)
    if va < 0:
        break
    while cont <= 10:
        print(f"{va} x {cont} = {va*cont}")
        cont = cont+1
print("PROGMA TABUADA ENCERRADO.volte sempre!")
    
    