#https://github.com/Andredev-dias/Base-de-algoritmos-em-C-v3/blob/master/listamold4.c

def area(altura, base):
    r = altura * base
    return r

alturaTerreno = int(input("Informe a medida lateral do terreno: "))
baseTerreno = int(input("Informe a base do terreno: "))

medidaArea = area(alturaTerreno, baseTerreno)
print("\nA área do terreno é de " + str(medidaArea) + "m, referente as medidas: " + str(alturaTerreno) + " e " + str(baseTerreno))