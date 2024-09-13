#https://github.com/Andredev-dias/Base-de-algoritmos-em-C-v3/blob/master/recursividade2lista.c

def somatorio(numero):
    acumulo = 0
    if numero > 0:
        print(str(numero) + " é um dos números.")
        acumulo = somatorio(numero - 1) + numero
    return acumulo   

num = int(input("\nInforme um número inteiro positivo: "))
resposta = somatorio(num)

print("\nO somatório dos números é " + str(resposta))
           