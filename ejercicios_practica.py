#!/usr/bin/env python
'''
Bucles [Python]
Ejercicios de práctica
---------------------------
Autor: Inove Coding School
Version: 1.2

Descripcion:
Programa creado para poner a prueba los conocimientos
adquiridos durante la clase
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.2"

condicion = False


def ej1():
    # Ejercicios con bucles "while"

    print("Ejercicio 1:\n")

    x = 0
    # Dado el siguiente "while", complete la condicion
    # para que el "while" itere siempre que <x sea menor a 6>
    # Además, complete la línea de código necesaria para que
    # el valor de "x" incremente "1" en cada iteración

    while x < 6:  # reemplace "condicion" por lo que crea necesario
        print("Valor de x =", x)
        x = x + 1

        # Coloque la línea de código para que "X" incremente "1"
    print("\n _________________________________________\n")

    x = 5
    # Dado el siguiente "while", complete la condicion
    # para que el "while" itere siempre que <x sea mayor o igual a 0>
    # Además, complete la línea de código necesaria para que
    # el valor de "x" decremente "1" en cada iteración

    while x >= 0:    # reemplace "condicion" por lo que crea necesario
        print("Valor de x =", x)
        x = x-1

    print("\n _________________________________________\n")
        
        # Coloque la línea de código para que "X" decremente "1"


def ej2():
    # Ejemplos con bucles "for"

    # Dado la siguiente lista de colores, utilizar "for"
    # para imprimir en pantalla todos los colores
    print ("Ejercicio 2:\n")

    colores = ['rojo', 'naranja', 'verde', 'azul']

    for color in colores:
        print("Elementos de la lista:", color)

    # Itere el "for" utilizando la lista como parámero
    # y utilizar como elemento del "for" cada color
    # for color ...

    # Itere el "for" utilizando el tamaño de la lista
    # como parámetro y utilizar el índice para acceder a
    # los elementos de la lista
    # for i ...
    print("\n _________________________________________\n")

def ej3():
    # Ejemplos con bucles "for"
    print("Ejercicio 3:\n")

    # Dado la siguiente lista de números, utilizar "for"
    # para recorrer toda la lista y realizar la sumatoria de todos los números
    # La sumatoria se deberá ir guardando en la variable "suma"
    numeros = [1, 5, -1, 6, 10, 2, -5]
    suma = 0   # Variable ya inicializada, la suma arranca en cero

    for numero in numeros:
        suma = suma + numero
        print(suma)        
        
    print("\n _________________________________________\n")

    



def ej4():
    # Ejercicios con bucles "while"
    print("Ejercicio 4:\n")
    # Realizar un bucle "while" cuya condición de continuidad
    # sea que <x sea menor a 10> y que <x sea distinto de 6>
    # Colocar ambas condiciones como condicion del "while" realizando
    # una condición compuesta (utilice el operador "and" o "or" según corresponda)
    # En cada iteracion del bucle debe incrementar el valor de "x" en "2"
    # e imprimir en pantalla el resultado de X (antes de incrementar) con print
    
    x = 0
    while x < 10 and x != 6:
        print("Cuando x es:", x,":")
        x += 2
        print("El resultado es", x, "\n")

    print("\n _________________________________________\n") 

    # Realice el mismo bucle "while" pero en vez de estar formado por una condición
    # compuesta, que el "while" siga iterando mientras <x sea menos a 10>, y dentro del
    # "while" consultar si <x es igual a 6>, y en ese caso realizar una interrupción del bucle
    # En cada iteracion del bucle debe incrementar el valor de "x" en "2"
    # e imprimir en pantalla el resultado de X (antes de incrementar) con print
    
    x = 0

    while x < 10:
        print("Cuando x es:", x,":")
        if x == 6:
            print("El resultado no se muestra porque no cumple con la condicion")
            break
        x += 2
        print("El resultado es", x, "\n")

    print("\n _________________________________________\n")
    

def ej5():
    print("Ejercicio 5:\n")
    # Ejercicio de secuencias numéricas
    # Pedir por consola dos números que representen el principio y fin de una
    # secuencia numérica.
    # Realizar un bucle "for" que recorra esa secuencia armada con "range"
    # y calcule a sumatoria total de todos los números dentro de esa secuencia
    # Tener en cuenta que "range" no incluye el número de "fin" en su secuencia,
    # sino que va hasta el anterior

    inicio = int(input('Ingrese el primero número de la secuencia\n'))
    numero_dos = int(input('Ingrese numero final  de la secuencia\n'))

    print ("El rango es entre los numeros", inicio, "y", numero_dos, "\n")
    suma = 0
   
    for i in range (inicio, numero_dos):
        suma = i + suma
        print("Elemento de rango numero:",i,"\nla suma es:", suma)


    # fin....

    # for ... in range(....)

    # Imprimir el valor de la sumatoria
    print("\n _________________________________________\n")


def ej6():
    print("Ejercicio 6:\n")
    # Ejercicio de secuencias numéricas
    # Pedir por consola dos números que representen el principio y fin de una
    # secuencia numérica.
    # Realizar un bucle "for" que recorra esa secuencia armada con "range"
    # y cuante cuantes números son negativos y cuantos números son mayor o igual a cero
    # Tener en cuenta que "range" no incluye el número de "fin" en su secuencia,
    # sino que va hasta el anterior

    inicio = int(input('Ingrese el primero número de la secuencia\n'))
    numero_dos = int(input('Ingrese numero final  de la secuencia\n'))
    
    rango = range(inicio, numero_dos)
    print ("La lista de rango es:", list(rango))
    print ("La lista esta compuesta por", len(rango),"numeros")

    for numero in rango:
        if numero > 0:
            print ("El numero", numero,"es positivo")
        elif numero == 0:
            print("El numero", numero, "es neutro")
        else:
            print("El numero", numero, "es negativo")
            
        

if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python \n")
    ej1()
    ej2()
    ej3()
    ej4()
    ej5()
    ej6()

