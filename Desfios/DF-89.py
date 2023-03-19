lista = []
while True:
    nome = str(input("Nome: "))
    n1 = float(input("1º Nota: "))
    n2 = float(input("2º Nota: "))
    media = (n1+n2)/2
    lista.append([nome,[n1,n2],media])
    r = str(input("Quer continuar [S/N]: "))
    if r in "Nn":
        break
    print(lista)
print("-="*30)
print("No. NOME              MEDIA")
print("-"*34)
for c,p in enumerate(lista):
    print(c,f"{p[0]:^8}{p[2]:^24}")
print("-"*34)
while True :
    v = int(input("Mostrar a nota de qual aluno [999 interronpe]:"))
    for c, p in enumerate(lista):
        if v == c:
            print(f"Notas de {p[0]} são {p[1]}")
    if v == 999:
        break