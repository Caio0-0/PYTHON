import random
n1 = str(input("nome 1º aluno:"))
n2 = str(input("nome 2º aluno:"))
n3 = str(input("nome 3º aluno:"))
lista = [n1,n2,n3]
escolhido = random.choice(lista)
print("o aluno escolhido foi {}".format(escolhido))