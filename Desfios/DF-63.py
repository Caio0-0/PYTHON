print("-"*40)
print("Sequência de Fibonacci")
print("-"*40)
quan = int(input("Quantos termos quer mostrar: "))
cont = 0
a = 1
b = 0 
f = 0 
while cont != quan: 
    print(b,end=" -->")
    cont += 1
    b = a+b
    a = f
    f = b

print("FIM")
