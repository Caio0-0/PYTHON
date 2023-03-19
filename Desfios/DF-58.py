import random
c = random.randint(0,10)
print("Ola eu sou seu computadore e penssei em um numero de 0 a 10")
print(c)
j = int(input("Qual é seu palpite:"))
ten = 0
while j != c :
    j = int(input("ERROU!!TENTE NOVAMENTE:"))
    ten += 1 
    if j > c :
        print("Menos")
    elif j < c :
        print("Mais")
print("ACERTOU!!!")
if ten > 1:
    print("Voce pressisol de {} tentantivas".format(ten+1)) 