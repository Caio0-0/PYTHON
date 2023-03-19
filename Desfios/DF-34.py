sala = float(input("Digite seu salario:"))
if sala>= 1250:
    a = sala*0.1
    b = "10%"
    sala = sala+a
else:
    a = sala*0.15
    b = "15%"
    sala = sala+a
print("seu salario teve um almento de {} e agora voce ira receber {}!".format(b,sala))