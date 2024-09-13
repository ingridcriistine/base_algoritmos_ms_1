#https://github.com/Andredev-dias/Base-de-Algoritmos-em-C/blob/master/vetmatricula.c

matriculas = []

for i in range(5):
    matricula = int(input("\nDigite o número de cadastro da " + str(i+1) + " matrícula: "))
    matriculas.append(matricula)
    print("Matricula " + str(matricula) + " cadastrada!")
    
print("\n-----------CONSULTA------------")
consulta = int(input("Informe a matrícula para consulta: "))

index = False
for j in range(5):
    if consulta == matriculas[j]:
        index = True
        break
    
if index == False:
    print("\nMatricula não encontrada!")
else:
    print("\nMatricula encontrada no index " + str(j) + " da lista!")
    
    