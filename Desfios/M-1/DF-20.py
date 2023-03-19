import random
n1 = str(input("1 aluno:"))
n2 = str(input("2 aluno:"))
n3 = str(input("3 aluno:"))
lista = [n1,n2,n3]
random.shuffle(lista)
print ("a ordem de apresentação é")
print(lista)


