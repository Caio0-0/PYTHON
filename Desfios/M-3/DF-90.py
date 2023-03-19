caracte = {}
caracte["Nome"] = str(input("Nome: "))
caracte["media"] = float(input(f"Media de {caracte['Nome']}:"))
caracte["Situaçao"] = "Aprovado"
for k,v in caracte.items():
    print(f"{k} é igual a {v}")
    if caracte["media"] <7:
        caracte ["Situaçao"] = "Reprovado"
