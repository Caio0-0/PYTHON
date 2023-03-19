n = int(input("Digite um numero:"))
v = 0
for c in range(1,n+1):
    if n%c == 0:
        v = v+1
if v==2:
    print("E primo")
else:
    print("Nao é primo")