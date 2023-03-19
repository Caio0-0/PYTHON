time = []
jogador = {}
partida = []
while True:
    jogador.clear()
    jogador["nome"] = str(input("Qual e seu nome:"))
    tot = int(input(f"Quanto jogos {jogador['nome']} jogou: "))
    partida.clear()
    for c in range(0, tot):
        partida.append(int(input(f"     quantos gols na {c+1} partida:")))
    jogador["gols"] = partida[:]
    jogador["total"] = sum(partida)
    time.append(jogador.copy())
    r = str(input("Quer continuar[S/N]: "))
    if r in "Nn":
        break
print("-="*35)
print("cod nome               gols              total")
print("-"*70)
for k,v in enumerate(time):
    print(f"{k:>2} ",end="")
    for d in v.values():
        print(f"{str(d):<19}",end="")
    print()
while True:
    f =int(input("Mostrar dados de qual jogador [999 para parar]: "))
    if f == 999:
        break
    for k,v in enumerate(time):
        if f == k:
            print(f'---LEVANTAMENTO DO JOGADOR {v["nome"]}:')
            for i,g in enumerate(time[f]["gols"]):
                print(f"No jogo {i+1} fer {g} gols ")
print("------------------VOLTE SEMPRE-------------------")
 