

def fib(n):
    n1 = 0
    n2 = 1
    if n == 1:
        return n1
    elif n == 2:
        return n2
    else:
        for i in range(2, n + 1):#empiezas desde el 2 porque descuentas el n1 y el n2, si pongo 0 me va adar 13 numeros en vez de los 11 que queremos
            num = n1 + n2
            n1 = n2
            n2 = num
        return num


print("5th Fibonacci's term:", fib(5))
print("11th Fibonacci's term:", fib(11))
print("55th Fibonacci's term:", fib(55))

