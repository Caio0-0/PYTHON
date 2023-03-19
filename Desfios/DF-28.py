import random
numero = random.randint(1, 5)
print("Já pensei em um numero tente acertar")
print("chute um numero entre 1 e 5:")
numJ = int(input("Chute um numero:"))
if numJ == numero:
    print("Parabens voce acertou :)!!")
else:
    print("voce erro :(!!")
print("---fim---")