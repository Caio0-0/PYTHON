lista = []
while True:
    n = int(input("Digite um valor: "))
    lista.append(n)
    r = str(input("Quer continuar [S/N]: ")) 
    if r in "Nn":
        break
print(f"Voce digitou {len(lista)} elementos")
lista.sort(reverse=True)
print(f"Os valores em ordem decrecente são {lista}")
if 5 in lista:
    print("E o valoer 5 faz parte da lista")
else:
    print("o Valor 5 não faz parte da lista")