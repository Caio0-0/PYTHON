def notas(*n,sit=False):
    nota = {}
    nota["Total"] = len(n) 
    nota["maior"] = max(n)
    nota["menor"] = min(n)
    nota["Media"] = sum(n)/len(n)
    if sit:
        if nota["Media"]>=7:
            nota["situação"] = "BOA"
        if nota["Media"]>=5:
            nota["situação"] = "RAZOAVEL"
        else:
            nota["situação"] = "RUIM"
    print(nota)
resp = notas(2,2,2,10,sit=True)