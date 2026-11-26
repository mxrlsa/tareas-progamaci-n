tarea 6

(3 puntos)
1. Construye una lista que funcione como un conjunto (set). Esto es, construye una función a la que le pasas una lista y un elemento que agregar pero sólo lo agregue si no existe dentro de la lista, también hay que hacer una función que agregue valores (si la llave no existe hay que agregarla y si ya existe hay que sobre-escribir su valor).

def agregar_unico(lista, elemento):
       if elemento not in lista:
        lista.append(elemento)
    return lista


assert agregar_unico([1, 2, 3], 4) == [1, 2, 3, 4]
assert agregar_unico([1, 2, 3], 2) == [1, 2, 3]
assert agregar_unico([], "A") == ["A"]

numeros = [1, 2, 3]
agregar_unico(numeros, 3)
agregar_unico(numeros, 7)
print(numeros)

resultado: [1, 2, 3, 7]


(4 puntos)
2. Construye dos listas que funcionen juntas como un diccionario. Por ejemplo, simular el diccionario 
d = {'uno':1, 'dos':2, 'tercero':3}
Utilizando las listas debe poder responder
"la llave uno, tiene valor 1"
Sugerencia, usar el método index de las listas para buscar la llave y luego el índice para buscar el valor correspondiente.

llaves = ["uno", "dos", "tercero"]
valores = [1, 2, 3]


def agregar_par(llaves, valores, llave, valor):
   
    if llave in llaves:
        posicion = llaves.index(llave)
        valores[posicion] = valor
    
    else:
        llaves.append(llave)
        valores.append(valor)


def consultar(llaves, valores, llave):
    if llave in llaves:
        posicion = llaves.index(llave)
        return "la llave " + llave + ", tiene valor " + str(valores[posicion])
    else:
        return "la llave " + llave + " no existe"



print(consultar(llaves, valores, "uno"))

agregar_par(llaves, valores, "cuatro", 4)   
print(consultar(llaves, valores, "cuatro"))

agregar_par(llaves, valores, "uno", 100)    
print(consultar(llaves, valores, "uno"))

print(consultar(llaves, valores, "cinco"))  

resultado:
la llave uno, tiene valor 1
la llave cuatro, tiene valor 4
la llave uno, tiene valor 100
la llave cinco no existe


(3 puntos)
3. Hacer una función que convierta un string con nucleótidos en la proteína correspondiente. Sugerencia, crea un diccionario del código genético. Nota: los codones de paro comunmente se sustituyen por un asterisco (*). Tener cuidado con qué pasa si la secuencia no tiene una longitud múltiplo de 3.

codigo_genetico = {
    "TTT": "F", "TTC": "F", "TTA": "L", "TTG": "L",
    "CTT": "L", "CTC": "L", "CTA": "L", "CTG": "L",
    "ATT": "I", "ATC": "I", "ATA": "I", "ATG": "M",
    "GTT": "V", "GTC": "V", "GTA": "V", "GTG": "V",
    "TCT": "S", "TCC": "S", "TCA": "S", "TCG": "S",
    "CCT": "P", "CCC": "P", "CCA": "P", "CCG": "P",
    "ACT": "T", "ACC": "T", "ACA": "T", "ACG": "T",
    "GCT": "A", "GCC": "A", "GCA": "A", "GCG": "A",
    "TAT": "Y", "TAC": "Y", "TAA": "*", "TAG": "*",
    "CAT": "H", "CAC": "H", "CAA": "Q", "CAG": "Q",
    "AAT": "N", "AAC": "N", "AAA": "K", "AAG": "K",
    "GAT": "D", "GAC": "D", "GAA": "E", "GAG": "E",
    "TGT": "C", "TGC": "C", "TGA": "*", "TGG": "W",
    "CGT": "R", "CGC": "R", "CGA": "R", "CGG": "R",
    "AGT": "S", "AGC": "S", "AGA": "R", "AGG": "R",
    "GGT": "G", "GGC": "G", "GGA": "G", "GGG": "G"
}


def traducir(secuencia):
    proteina = ""
    codon = ""
    contador = 0

    for letra in secuencia.upper():
        codon = codon + letra
        contador = contador + 1

        
        if contador == 3:
            if codon in codigo_genetico:
                proteina = proteina + codigo_genetico[codon]
            else:
                proteina = proteina + "?"   
            codon = ""
            contador = 0

    
    return proteina


# Pruebas
assert traducir("ATGGCCTAA") == "MA*"
assert traducir("atggcctaa") == "MA*"   
assert traducir("ATGGC") == "M"        
assert traducir("ATGG") == "M"          
assert traducir("") == ""

print(traducir("ATGGCCTAA"))

resultado: MA*