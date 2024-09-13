#https://github.com/Andredev-dias/Base-de-Algoritmos-em-C/blob/master/whilepratica06.c

adulto = 0
ia = 0
ib = 0
ja = 0
jb = 0
total = 0

idade = int(input("Qual a idade do nadador? "))

while idade > 0:
    if idade >= 5 and idade <= 7:
        ia +=1
        total += 1
        print("Infantil A")
    elif idade >= 8 and idade <= 10:
        ib +=1
        total += 1
        print("Infantil B")
    elif idade >= 11 and idade <= 13:
        ja +=1
        total += 1
        print("Juvenil A")
    elif idade >= 14 and idade <= 17:
        jb +=1
        total += 1
        print("Juvenil B")
    elif idade >= 18:
        adulto += 1
        total += 1
        print("Adulto")
    else:
        print("Não está em nenhuma categoria.")

    idade = int(input("Qual a idade do nadador? "))


print("\n-----Quantidade de nadadores por categoria-----")
print("Infantil A: " + str(ia))
print("Infantil B: " + str(ib))
print("Juvenil A: " + str(ja))
print("Juvenil B: " + str(jb))
print("Adulto: " + str(adulto))

print("\nTotal de nadadores: " + str(total))