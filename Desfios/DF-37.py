n = int(input("Digite um numero:"))
print("[1]BINARIO")
print("[2]OCTAL")
print("[3]HEXADECIMAL")
op= int(input("Escreva sua opição:"))
if op == 1:
    print("O numero {} em binario é:{}".format(n,bin(n)))
elif op == 2:
    print("O numero {} em octal é:{}",format(n,oct(n)))
elif op == 3:
    print("o numero {} em hexadecimal é:{}",format(n,hex(n)))