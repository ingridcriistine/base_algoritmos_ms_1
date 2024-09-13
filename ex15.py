#https://github.com/Andredev-dias/Base-de-Algoritmos-em-C_v2/blob/master/listavetoresmatrizesestrings7.c

valores = []
par = []
impar = []

for a in range(10):
    valor = int(input("Informe o " + str(a+1) + " valor: "))
    valores.append(valor)
    
    if valor % 2 == 0:
        par.append(valor)
    else:
        impar.append(valor)
        
print("\nTodos os valores: " + str(valores))
print("Números pares: " + str(par))
print("Números ímpares: " + str(impar))