#https://github.com/Andredev-dias/Base-de-algoritmos-em-C-v3/blob/master/tabuadaqualquernum.c

num = int(input("Informe um número: "))

print("\nT A B U A D A")
print("===============")

for i in range(11):
    r = i * num
    print(str(i) + " x " + str(num) + " = " + str(r))
    
print("===============")