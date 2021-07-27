from math import sqrt

def fibonacci(num):
    if num <= 1: return num
    else: return(fibonacci(num-1)+fibonacci(num-2))

def mul_tables(num):
    table = ''
    for i in range(1,11):
        table = table + f'{num} X {i} = {num*i}\n'
    return table

def quadratic_form(A,B,C):
    root = pow(B,2)-(4*A*C)
    if root <0:
        return 'La solución requiere números complejos'
    x1 = (-B+sqrt(root))/(2*A)  
    x2 = (-B-sqrt(root))/(2*A)
    return (x1,x2)

def run():
    option = None
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
                    print(mul_tables(i))
        elif option==3:
            while True:
                try:
                    A = int(input('Ingrese el valor de A: '))
                    B = int(input('Ingrese el valor de B: '))
                    C = int(input('Ingrese el valor de C: '))
                    x = quadratic_form(A,B,C)
                    if type(x) == tuple:
                        print(f'Resultado de x+: {x[0]}')
                        print(f'Resultado de x-: {x[1]}')
                    else:
                        print(x)
                    break
                except ValueError:
                    print('Ingrese un número válido')
        elif option==4:
            break

if __name__ == "__main__":
    run()
    
    