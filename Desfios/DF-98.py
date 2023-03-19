def contador(i,f,p):
    print("-="*15)
    print(f"Contagem de {i} ate {f} de {p} em {p}")
    if p < 0 :
        p*= -1
    if p==0:
        p = 1
    if i<f:
        cont =i
        while cont <= f:
            print(f"{cont}",end=" ")
            cont += p
        print("FIM")
    if i>f:
        cont = i 
        while cont >= f:
            print(f"{cont}",end=" ")
            cont -= p
        print("FIM")
contador(1,10,1)
contador(10,0,2)
print("-="*15)
print("Agora é sua vez de personalizar a contagem:")
inicio = int(input("INICIO: "))
fim = int(input("FIM: "))
passo = int(input("PASSO: "))
contador(inicio,fim,passo)