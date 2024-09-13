#https://github.com/Andredev-dias/Base-de-algoritmos-em-C-v3/blob/master/recursividadeCaula.c

def conta(n):
    if n > 0:
        print(str(n))
        conta(n - 1)
        
num = int(input("\nDigite um número: "))
conta(num)
