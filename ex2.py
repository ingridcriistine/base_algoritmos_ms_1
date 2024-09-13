#https://github.com/Andredev-dias/Base-de-algoritmos-em-C-v3/blob/master/listamold6.c

print("LOJA DE CAMISETAS")

def calculo(p, m, g, nome):
    respP = p * 10
    respM = m * 12
    respG = g * 15
    valor = respP + respM + respG
    print("O valor arrecadado é de: R$ " + str(valor) + ",00, " + nome)

pequenas = int(input("Digite a quantidade de camisetas pequenas: "))
medias = int(input("Digite a quantidade de camisetas medias: "))
grandes = int(input("Digite a quantidade de camisetas grandes: "))
nome = input("Digite o seu nome: ")

calculo(pequenas, medias, grandes, nome)