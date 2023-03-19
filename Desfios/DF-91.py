from random import randint
from operator import itemgetter
print("Valores soteados:")
joga = {"Jogador1":randint(1,6),"Jogador2":randint(1,6),"Jogador3":randint(1,6),"Jogador4":randint(1,6)}
for c in joga:
    print(f"{c} tiroe {joga[c]} no dado  ")
ran = []
print("=-"*34)
print("   == RANKING DOS JOGADORES ==")
ran = sorted(joga.items(), key = itemgetter(1), reverse=True)
for c,v in enumerate(ran):
    print(f"{c+1}º lugar: {v[0]} tirou {v[1]} no dado")








