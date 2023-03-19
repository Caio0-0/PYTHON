dado = {}
partida = []
dado['Nome'] = str(input("Nome do jogador: "))
p = int(input(f"Quantas pardidas {dado['Nome']} jogou: "))
dado["total"] = 0
for c in range(0,p):
    partida.append(int(input(f"Quantos gols na partida {c}: ")))
dado["gols"] = partida[:]
dado["total"] = sum(partida)
print('-='*35)
print(dado)
print('-='*35)
for k, v in dado.items():
    print(f"O campo {k} tem valor {v}")
print('-='*35)
print(f"O jogador {dado['Nome']} jogou {len(dado['gols'])}")
for c,v in enumerate(dado["gols"]):
    if v == 1:
        print(f"    =>Na partida {c}, fez {v} gol")
    else:
        print(f"    =>Na partida {c}, fez {v} gols")