from random import randint
maior = 0
menor = 0
nu = (randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10),)
for c in range(1,5):
    if c == 1:
        maior = menor = nu[c]
    if nu[c] > maior:
        maior = nu[c]
    if nu[c] < menor:
        menor = nu[c]
print(f"Os valores sorteado foram: {nu}")
print(f"O maior valor sortedo foi {maior}")
print(f"O menor valor sorteado foi {menor}") 