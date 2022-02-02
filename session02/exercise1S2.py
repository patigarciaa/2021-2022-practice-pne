#sacar la serie de fibonacci

N = 11
#constant is a variable which value wont change
n1 = 0
n2 = 1
print(n1, end=" ")
print(n2, end=" ")
for i in range(2, 11):#empiezas desde el 2 porque descuentas el n1 y el n2, si pongo 0 me va adar 13 numeros en vez de los 11 que queremos
    num = n1 + n2
    print(num, end=" ")
    n1 = n2
    n2 = num
print()