#https://github.com/Andredev-dias/Base-de-algoritmos-em-C-v3/blob/master/recursividade2aula.c

def fatorial(num):
    if num == 0 or num == 1:
        return 1
    return num * fatorial(num - 1)

numero = int(input("Digite um número: "))
resultado = fatorial(numero)

print("\nO fatorial de " + str(numero) + " é: " + str(resultado))
        