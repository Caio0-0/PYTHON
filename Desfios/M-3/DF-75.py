n1 = int(input("Digite um numero:")), int(input("Digite otro numero:")),int(input("Digite mais um numero:")),int(input("Digite o ultimo numero:"))

print(f"Voce digitou {n1}")
print(f"O valor 9 apareceu {n1.count(9)} vezes")
if 3 in n1:
    print(f"O valor 3 apareceu na {n1.index(3)+1}º posição")
else:
    print(f"O valor 3 não foi encontrado")
print(f"Os valore pare igitado foram",end="")
for c in n1:
    if c %2==0:
        print(c,end=" ")