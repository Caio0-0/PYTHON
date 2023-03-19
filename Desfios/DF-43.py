peso = float(input("Seu peso (Kg): "))
altura = float(input("Sua altura em (m): "))
imc = peso/(2**altura)
if imc < 18.5:
    print("Classificação: Abaixo do peso")

elif imc >= 18.5 and imc < 25:
    print("Classificação: Peso ideal")
elif imc >= 25 and imc < 30:
    print("Classificação: Sobrepeso")

elif imc >= 30 and imc < 40:
    print("Classificação: Obesidade")
 
elif imc > 40:
    print("Classificação: Obesidade mórbida")