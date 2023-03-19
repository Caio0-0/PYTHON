import random
vi = 0
while True:
    c = random.randint(0,10)
    n = int(input("Diga um valor: "))
    pi = str(input("Par ou Impar [P/I]:")).upper()
    if (n+c)%2==0: 
        if pi == "P":
            print("-"*40)
            print(f"voce jogou {n} e o computador {c}.Total {n+c} PAR")
            print("Voce VENCEU!!")
            print("-="*40)
            vi = vi+1
        if pi =="I":
           break
    elif (n+c)%2==1:
        if pi == "I":
            print("-="*40)
            print(f"voce jogou {n} e o computador {c}.Total {n+c} IMPAR")
            print("Voce VENCEU!!")
            print("-"*40)
            vi = vi+1
        if pi == "P":
            break
if (n+c)%2==0:
    print("-"*40)
    print(f"voce jogou {n} e o computador {c}.Total {n+c} PAR")
    print("Voce PERDEU!!")
    print("-"*40)
elif (n+c)%2==1:
    print("-="*40)
    print(f"voce jogou {n} e o computador {c}.Total {n+c} IMPAR")
    print("Voce PERDEU!!")
    print("-="*40)
print(f"GAME OVER! Voce venceu {vi} vezes")
