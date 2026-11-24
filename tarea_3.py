tarea 3

1. Investigar cómo se usa el operador módulo (modulus) en python, explicarlo con sus palabras y poner un ejemplo. (1 punto)
El operador módulo se utiliza para obtener el resto de una división entre dos números y se representa con el símbolo %.
# División con residuo
manzanas_sobrantes = 10 % 3
print(manzanas_sobrantes)  # Salida: 1

2. Crear una lista vacía y llenarla con los números pares del 2 al 50 (2,4,6,8,...,48,50) utilizando un for y un condicional para controlar que sólo los pares se agreguen.  (2 puntos)

    numeros_pares = []

for i in range(2,51):
if i % 2 ==0:
    numeros_pares.append(i)

prind(numeros_pares)

[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50]


3. Investigar para qué sirve el comando "break" en un for, explicarlo con sus palabras y hacer un ejemplo. (1 punto)
nos sirve para para detener y salir de un bucle for de manera prematura antes de que este haya terminado todas sus iteraciones progrmadas.

   
 for numero in range(1, 10):
     print(numero)
     if numero == 6:
         break

1
2
3
4
5
6
    

4. Programar el método find de los strings a mano. (2 puntos) Sugerencia: utilizar break cuando encuentren lo que buscan
palabra = 'banana'
# regresar la posición de la primera 'a'

palabra = "banana"
buscar = "a"
posicion =-1

 for i in range(len(palabra)):
        if palabra[i] == buscar:
            posicion =i
            break

  print(posicion)

1


5. Imprimir todos los números de la siguiente lista utilizando ciclos: (4 puntos)

lista = [[1], [1,2], [1,2,3], [1,2,3,4], [1,2,3,4,5]]

for sublista in lista:
    for numero in sublista:
        print(numero)

1
1
2
1
2
3
1
2
3
4
1
2
3
4
5
 