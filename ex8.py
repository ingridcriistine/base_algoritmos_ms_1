#https://github.com/Andredev-dias/Base-de-Algoritmos-em-C/blob/master/if04.c

tempo = int(input("Informe o tempo de fidelidade: "))
valor = int(input("Informe o valor gasto na compra: "))

if tempo >= 5:
    if valor > 5000:
        print("20% de desconto!")
    else:
        if valor > 1000:
            print("10% de desconto!")
        else:
            print("Sem desconto.")
else:
    print("Sem desconto.")