#https://github.com/Andredev-dias/Base-de-Algoritmos-em-C_v2/blob/master/EX4.c

import numpy as np

linhas = 4
colunas = 4
valor = 1
soma = 0

matriz = np.array([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])

for i in range(linhas):
    for j in range(colunas):
        matriz[i][j] = valor
        valor *= 2
        soma += matriz[i][j]
        
print(matriz)
print("\nA soma da matriz é igual a " + str(soma))