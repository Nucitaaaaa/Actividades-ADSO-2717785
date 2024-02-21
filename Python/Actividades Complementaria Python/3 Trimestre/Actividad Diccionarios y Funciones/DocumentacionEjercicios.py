
#*1. Tecnicas de iteración

#Se crea un diccionario con dos claves (nombre, notafinal) y dos valores.
calificaciones = { 
    'nombre': 'Sandra', 
    'notafinal': 5.0
}

#Se reasignan los valores de este, ahora siendo la clave los nombres y los valores las notas
calificaciones = {
'Sandra': 5.0, 
'Adriana':5.0,
'Mauricio': 4.5,
'Jose':2.5
}

#Se crea un bucle donde se iterará en cada item del diccionario y se mostrarán las claves(i) y los valores(J). (metodo: .items())
for i, j in calificaciones.items():
    print(i,j)


#*2. Tecnicas de iterar los diccionarios

print("Técnicas por clave")
#Se crea un bucle donde se mostrarán solo las claves de el diccionario. (metodo: .key())
for i in calificaciones.keys():
    print(i)

print("Iterar por valor")
#Se crea un bucle donde se mostrarán solo los valores de el diccionario. (metodo: .values())
for j in calificaciones.values():
    print(j)

# Se crean dos listas con valores 
nombres = ['Maria', 'Sebastian', 'Ana']
edades = ['18', '25', '30']

#Se crea un bucle donde se iterará en las dos listas simultaneamente (metodo: .zip() y se mostrarán sus valores)
for n, e in zip(nombres, edades):
    print('Tú nombre es {0}  y tu edad {1}.'.format(n, e))


#*3. Definir una función

#se define una función la cual muestra una cadena de texto
def saludar():
    print("saludo")

#se define una función la cual retorna (funcion: return) un numero
def retornarnumero():
    return 1

#se llaman a las funciones
saludar() 
retornarnumero() 

#Se crea un condicional donde se valida si el numero que se retorna en la función es 1
if retornarnumero()==1:
    print("devolvió un uno")
else:
    print("No devolvió un uno")


#*4. Valores con parametros

#Se define una función la cual retorna la raiz del numero pasado como argumento para el parametro "value"
def raiz(value):
    return value ** (1/2)

print(f'La raiz cuadrada es: {raiz(4)}')


#Se define una función que valida si el argumento pasado al parametro "obj" es falso (0) o verdadero (1...) ya que se valida el parametro como un boolean
def validarsiexiste(obj):
    if obj:
        print(f"{obj} is True")
    else:
        
        print(f"{obj} is False")

validarsiexiste(1)


#?Ejercicio 
#Escriba una función en Python que reproduzca lo siguiente:
#𝑓(𝑥, 𝑦) = 𝑥2 + 𝑦2      Valor para X=3 y valor para Y=5


def ejercicio(x,y):
    return (x**2) + (y**2)

print(ejercicio(3,5))


#*5. Funciones con parametros posicionales 
#Se define una función la cual retorna un diccionario con los argumentos que se les asignan a los parametros en funcion del orden de los argumentos
def compra(marca,cantidad,valor):
    return dict(
        marca=marca,
        cantidad=cantidad,
        valor=valor*cantidad
    )

print(f' lo comprado fue:{compra("AMD",3,2500000)}')


#*6. Funciones con Parámetros Nominales
#Se define una función la cual retorna un diccionario con los argumentos que se les asignan a los parametros al llamar la funcion
def compra(marca,cantidad,valor):
    return dict(
        marca=marca,
        cantidad=cantidad,
        valor=valor*cantidad
    )

print(f' lo comprado fue:{compra(marca="AMD",cantidad=3,valor=2500000)}')


#*7. Parámetros por defecto
#Se define una función a la cual se le asigna un valor por defecto a uno de los parametros, y retorna un diccionario con los argumentos que se les asignan a los parametros al llamar la funcion
def compra(marca,cantidad,valor=2500000):
    return dict(
        marca=marca,
        cantidad=cantidad,
        valor=valor*cantidad
    )

print(f' lo comprado fue:{compra("AMD",3)}')


#*8. Modificando parametros mutables 

#se define una función la cual mostrará la lista del parametro 2, con el o los valores que se les asignó en el parametro 1
def lista(arg, result=[]):
    result.append(arg)
    print(result)
    
lista('domingo', [])

#se define una función la cual mostrará una lista con el argumento que se le asigne en el parametro 1, si el valor del parametro 2 es None
def listalimpia(arg, result=None):
    if result is None:
        result = []
        result.append(arg)
        print(result)
listalimpia("a")
listalimpia("b") 


#?Ejercicio 2
#Tomé el presente ejercicio,  y pasé a la función la lista con los días de la semana restantes
def lista(arg, result=[]):
    result.append(arg)
    print(result)
    
lista('domingo', ['lunes', 'martes', 'miercoles', 'jueves', 'viernes', 'sabado'])


#*9. Funciones anonimas <<lambda>>

#Se crea una función lambda la cual recibe un parametro(t) y retorna la cantidad de palabras en una frase que se le pase a este parametro (metodos: .strip(quita espacios al rededor) .split(convierte cada palabra de el argumento en una lista))
numero_palabras = lambda t: len(t.strip().split())

print(numero_palabras("hola, esto es una prueba con lambda"))


#*10 Función lambda 2

# Definir una función lambda que representa el operador AND (&)
operadorand = lambda x, y: x & y

# Iterar sobre todas las combinaciones posibles de valores de i y j 
for i in range(2):
    for j in range(2):
        # Imprimir la operación AND entre i y j utilizando la función 
        print(f"{i} & {j} = {operadorand(i, j)}")






