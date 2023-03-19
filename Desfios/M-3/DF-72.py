
nome = ("zero","um","dois1","tres","quatro","cinco","seis","sete","oito","nove","dez","onze","doze","trese","catosr","quinse","deseseis","desesete","desoito","desenove","vinte")
while True:
    nu = int(input("Digite um valor entre 0 e 20:"))
    if 0 <= nu <=20:
        break
    print("Tente novamente. ",end="")
for cont in range(0,len(nome)):
    if nu == cont:
        print (f"Voce digitou o numero {nome[cont]}")
