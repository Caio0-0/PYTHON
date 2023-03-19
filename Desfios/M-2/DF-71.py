print("="*35)
print("              BANCO")
print("="*35)
volor = int(input("Digite um valor:"))
total = volor
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f"total de {totced} cedulas de R${ced}") 
        if ced == 50:
            ced = 20
        if ced == 20:
            ced = 10
        if ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break