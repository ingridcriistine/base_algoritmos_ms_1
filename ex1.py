#https://github.com/Andredev-dias/Base-de-algoritmos-em-C-v3/blob/master/exer9funcoescorrigido.c

def soma(n1, n2):
    valor = n1 + n2
    return valor

print("SOMA\n")

num1 = int(input("Informe o primeiro numero: \n"))
num2 = int(input("Informe o segundo numero: \n"))

res = soma(num1, num2)

print("O resultado entre " + str(num1) + " + " + str(num2) + " = " + str(res))