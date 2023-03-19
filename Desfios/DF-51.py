print("============================")
print("    10 TERMAOS DE UMA PA    ")
print("============================")
p = int(input("Primeiro termo: "))
razao = int(input("Razão: "))
dez = p + (10 - 1)*razao
for c in range(p,dez,razao):
    print(c,end="-> ")
print("ACABOU")