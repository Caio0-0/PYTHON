b = 0
p = 0
for c in range(1,8):
    a = int(input("Em que ano a {}º pessoa nasceu: ".format(c)))
    if 2017-a>=21:
        b += 1 
    else:
        p += 1
print("tem {} pessoas maiores".format(b))
print("tem {} pessoas menores".format(p))


