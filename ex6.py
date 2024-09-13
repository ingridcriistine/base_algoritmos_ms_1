#https://github.com/Andredev-dias/Base-de-Algoritmos-em-C_v2/blob/master/listacondicional1.c

nome = input("Qual seu nome? ")
idade = int(input("\nQual sua idade? "))
sexo = input("\nM - masculino \nF - feminino\nInforme seu sexo: ")

print("\n\nO nome fornecido foi: " + nome)
print("A idade fornecida foi: " + str(idade))
print("O sexo informado foi: " + sexo)

if sexo == "M":
    if idade >= 18 and idade <= 65:
        print("\n" + nome + ", está compreendido(a) entre 18 e 65 anos de idade e é do sexo masculino.\n")
else:
    print("\n" + nome + ", ou não está entre 18 e 65 anos de idade e/ou não é masculino.\n")