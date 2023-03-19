def voto(n):
    v = 2018 - n
    print(f"Com {v} anos: ",end="")
    if 65 > v >= 18:
        print("VOTO OBRIGTORIO.")
    if 16 < v < 18 or v >=65:
        print("VOTO OPICIONAL.")
    if v < 16:
        print("NÃO VOTO.")
na = int(input("Ano de nascimento: "))
voto(na)