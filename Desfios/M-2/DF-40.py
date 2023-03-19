n1 = float(input("Sua 1º nota:"))
n2 = float(input("Sua 2º nota:"))
media = (n1+n2)/2
if media < 5:
    print("Sua media foi {} e voce esta REPROVADO!".format(media))
elif media >= 5 and media < 6.9:
    print("Sua media foi {} e voce esta de RECUPERAÇÃO".format(media))
elif media >= 7:
    print("Sua media foi {} e parabéns voce esta APROVADO!!".format(media))