#https://github.com/Andredev-dias/Base-de-Algoritmos-em-C_v2/blob/master/listalaco2.c

total = 0

for i in range(5):
    sal = int(input("Qual seu salario? "))
    total = total + sal

media = total / 5

print("Total dos salarios: " + str(total))
print("Media dos salarios: " + str(media))