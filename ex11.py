#https://github.com/Andredev-dias/Base-de-Algoritmos-em-C/blob/master/testematriz12.c

import numpy as np

linhas = 3
colunas = 5

matriz = np.array([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]])

for i in range(linhas):
    for j in range(colunas):
        valor = int(input("Informe a posição " + str(i) + "," + str(j) + " da matriz: "))
        matriz[i][j] = valor
        
print(matriz)