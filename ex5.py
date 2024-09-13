#https://github.com/Andredev-dias/Base-de-Algoritmos-em-C_v2/blob/master/listavetoresmatrizesestrings1.c

nomes = []
valores = []

for i in range(5):
    nome = input("Informe o " + str((i+1)) + " nome: ")
    nomes.append(nome)
    
    valor = int(input("Informe o " + str((i+1)) + " valor a ser calculado: "))
    valores.append(valor)

print("______________________________")

for j in range(5):
    print(nomes[j] + " com o valor x2 = " + str((valores[j]) * 2))