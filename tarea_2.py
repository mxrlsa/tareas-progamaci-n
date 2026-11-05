tarea 2 programacion

1. Crear una lista vacía y llenarla con los números  del 1 al 50 (1,2,3,...,48,49,50). Sugerencia: usar un ciclo, no generarla directamente con [1,2,3,...,48,49,50] ni list(range(0,50)) (1 punto)

 Primero hacemos una lista sin elementos:
lista = []

 Después utilizamos el ciclo for para ir agregando los números desde 1 hasta 50:
for i in range(1,51):
     lista.append(i)

 Finalmente, mostramos la lista:
print(lista)

 Resultado:
 [1,2,3,4,5,6,7,8,9,10...48,49,50]

 Como código adicional, se puede crear una lista con las bases nitrogenadas:
 bases = []
 for base in ["adenina", "timina", "citosina", "guanina"]
     bases.append(bases)
 print(bases)
 
 También podemos saber cuantos elementos contiene la lista:
 prind(len(bases))

 Resultado:
4


2. Crear una lista vacía y llenarla con los números múltiplos de 5 del 2 al 50 (5,10,15,...,40,45,50). Nota: hay que usar un ciclo, no se vale generarla directamente con [5,10,15,...,40,45,50] ni list(range(0,50,5)) (3 puntos)

 Primero se crea un lista vacía:
multiplos_de_5 = []

 Luego utilizamos un ciclo for para ir agregando múltiplos de 5:
for i in range(5,51,5) 
     multiplos_de_5.append(i)
      
     print(multiplos_de_5)
 Resultado:
[5,10,15,20,25,30,35,40,45,50]

3. Hacer un programa que imprima (4 puntos)

 Se utiliza un ciclo for que aumenta la cantidad de asteriscos en cada línea:
for i in range(1,11):
    print("*" *)

 Resultado:

*
**
***
****
*****
******
*******
********
*********
**********


4. Investigar cómo se usa un ciclo while y hacer un programa que imprima los números del 1 al 10. (2 puntos)

El ciclo while permite repetir instrucciones mientas una condición sea verdadera. Para este ejercicio se utiliza una variable que funciona como contador y aumenta en cada repetición.

 contador = 1

 while contador <=10:
      print (contador) 
      contador = contador + 1
 Resultado: 
1
2
3
4
5
6
7
8
9
10