def mair(*num):
    print("-="*25)
    print("Analizndo os valore")
    maiorV = 0
    for c,v in enumerate(num):
        print(v, end=" ")
        if c == 0:
            maiorV = v
        else:
            if maiorV<v:
                maiorV =v
    print(f" Form informado {len(num)} numeros")
    print(f"O maior é o {maiorV}")
mair(2,9,4,5,7,1)
mair(4,7,0)
mair(1,2)
mair(6)
mair(0)