#https://github.com/Andredev-dias/Base-de-Algoritmos-em-C/blob/master/iflista6.c

idAluno = int(input("Número da identificação do aluno: "))
n1 = int(input("Primeira nota: "))
n2 = int(input("Segunda nota: "))
n3 = int(input("Terceira nota: "))

media = (n1+n2+n3) / 3
conceito = "E"

if media >= 90:
    conceito = "A"
elif media >= 75:
    conceito = "B"
elif media >= 60:
    conceito = "C"
elif media >= 40:
    conceito = "D"
else:
    conceito = "E"

if media >= 60:
    print("\nAPROVADO\nID Aluno: " + str(idAluno) + "\nConceito: " + conceito + "\nNotas: " + str(n1) + " | " + str(n2) + " | " + str(n3) + "\nMédia: " + str(media))
else:
    print("\nREPROVADO\nID Aluno: " + str(idAluno) + "\nConceito: " + conceito + "\nNotas: " + str(n1) + " | " + str(n2) + " | " + str(n3) + "\nMédia: " + str(media))
    