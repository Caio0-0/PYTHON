import random
print("Suas opçoes:")
print("[1] PEDRA")
print("[2] PAPEL")
print("[3] TESOURA")

maq = random.randint(1,3)
jog = int(input("O que vai jogar: "))
if jog == 1 and maq == 3:
    print("VITORIA!!!")
    print("Maquina  jogou TESOURA")
elif jog == 3 and maq == 1:
    print("PERDEU!!!!")
    print("Maquina GANHOU ela jogou PEDRA")
elif jog == 2 and maq == 1:
    print("VITORIA!!!")
    print("Maquina jogou PEDRA")
elif jog == 1 and maq == 2:
    print("PERDEU!!!")
    print("Maquina GANHOU ela jogou PAPEL")
elif jog == 3 and maq == 2:
    print("VITORIA!!")
    print("Maquina jogou PAPEL")
elif jog == 2 and maq == 3:
    print("PERDEU!!")
    print("Maquina GANHOU ela jogou TESOURA")
elif jog == maq:
    print("jogo deu EMPATE")

