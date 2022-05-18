def print_factorial(x):
    print("El factorial de: ",x,"en: ")
    for i in range(1,x + 1):
        if x % i ==0:
            print(i)
numero = 720

print_factorial(numero)
