tex = str(input("digite uma frase:")).upper().strip()
print("A letra A aparrece {} vezes".format(tex.count("A")))
print("Ela aparece na {} posição".format(tex.find("A")+1))
print("Ela aparece por utimo na posiçao {}".format(tex.rfind("A")+1))