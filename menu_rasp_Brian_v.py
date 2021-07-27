from math import sqrt

def fibonacci(n):
    if n <= 1: 
        return n
    else: 
        return(fibonacci(n-1)+fibonacci(n-2))

def formula_general(A,B,C):
    if pow(B,2)-(4*A*C) <0:
        return 'La solución requiere números complejos'
    x1 = (-B+sqrt(pow(B,2)-(4*A*C)))/(2*A)  
    x2 = (-B-sqrt(pow(B,2)-(4*A*C)))/(2*A)
    return f'El resultado para x positiva es {x1} y para x negativa es {x2} '

option = 0
while option != 4:
    print('Bienvenido al menú:')
    print('1.- Calcular serie fibonacci')
    print('2.- Tablas de multiplicar del 1 al 7')
    print('3.- Fórmula general')
    print('4.- Salir')
    try:
        option = int(input("Escoja una opción: \n"))
    except ValueError:
        print('Ingrese un número válido')
        print('Intentelo de nuevo')
    if option ==1 :
        try:
            num = int(input('Ingrese un número: '))
            for i in range(num):
                print(fibonacci(i+1))
        except ValueError:
            print('Ingrese un número válido')
           
    elif option==2:
        for i in range(1,8):
            tabla_multi = ''
            for j in range(10):
                tabla_multi = tabla_multi + f'{i} X {j+1} = {i*(j+1)}\n'
            print(tabla_multi)

    elif option==3:
        while True:
            try:
                A = int(input('Ingrese el valor de A: '))
                B = int(input('Ingrese el valor de B: '))
                C = int(input('Ingrese el valor de C: '))
                x = formula_general(A,B,C)
                print(x)
                break
            except ValueError:
                print('Ingrese un número válido')
                
    elif option==4:
        break

    
    