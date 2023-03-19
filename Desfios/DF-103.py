def jogador(jogdor="<Desconhecido>",gols="0"):
    if jogdor=='':
        jogdor = "<Desconhecido>"
    if gols =='':
        gols = "0"
    print(f"o jogador {jogdor} fez {gols} gol(s) no campeonato.")
joga = str(input("Nome do jogador: "))
gols = str(input("Numeros de gols: "))
jogador(jogdor=joga,gols=gols)
print("")