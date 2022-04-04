# 1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla

a = 8
print(f"a = {a}")

# 2) Imprimir el tipo de dato de la constante 8.5

print("Tipo de dato de la constante 8.5 es: ", type(8.5))

# 3) Imprimir el tipo de dato de la variable creada en el punto 1

print("Tipo de dato de la variable 'a' es: ", type(a))

# 4) Crear una variable que contenga tu nombre

nombre = "Esteban Ojea Quintana"

# 5) Crear una variable que contenga un número complejo

b = 8 + 5j

# 6) Mostrar el tipo de dato de la variable crada en el punto 5

print("Tipo de dato de la variable 'b' es: ", type(b))

# 7) Crear una variable que contenga el valor del número Pi redondeado a 4 decimales

pi = 3.1416

# 8) Crear una variable que contenga el valor 'True' y otra que contenga el valor True. ¿Se trata de lo mismo?

var_1 = 'True'
var_2 = True

# 9) Imprimir el tipo de dato correspondientes a las variables creadas en el punto 9

print("var_1: ", type(var_1), "\nvar_2: ", type(var_2))

# 10) Asignar a una variable, la suma de un número entero y otro decimal

c = 2 + 3.5
print(f"c = {c}")

# 11) Realizar una operación de suma de números complejos

d = 2 + 3j + 4 + 5j
print(f"d = {d}")

# 12) Realizar una operación de suma de un número real y otro complejo

e = 8.8 + d
print(f"e = {e}")

# 13) Realizar una operación de multiplicación

print(2*3)

# 14) Mostrar el resultado de elevar 2 a la octava potencia

print(2**8)

# 15) Obtener el cociente de la división de 27 entre 4 en una variable y luego mostrarla

f = 27 / 4
print(f"f = {f}")

# 16) De la división anterior solamente mostrar la parte entera

print(27//4)

# 17) De la división de 27 entre 4 mostrar solamente el resto

print(27%4)

# 18) Utilizando como operandos el número 4 y los resultados obtenidos en los puntos 16 y 17. Obtener 27 como resultado

a = 27 // 4
b = 27 % 4
print(a*4 + b)

# 19) Utilizar el operador "+" en una operación donde intervengan solo variables alfanuméricas

print("a" + "4")

# 20) Evaluar si "2" es igual a 2. ¿Por qué ocurre eso?

print("2" == 2)

# 21) Utilizar las funciones de cambio de tipo de dato, para que la validación del punto 20 resulte verdadera

print(int("2") == 2)

# 22) ¿Por qué arroja error el siguiente cambio de tipo de datos? a = float('3,8')

a = float('3.8')

# 23) Crear una variable con el valor 3, y utilizar el operador '-=' para modificar su contenido

h = 3
h-=1
print(h)

# 24) Realizar la operacion 1 << 2 ¿Por qué da ese resultado? ¿Qué es el sistema de numeración binario?

a = 3 << 1
print(a)

# 25) Realizar la operación 2 + '2' ¿Por qué no está permitido? ¿Si los dos operandos serían del mismo tipo, siempre arrojaría el mismo resultado?

#2 + "2"

# 26) Realizar una operación válida entre valores de tipo entero y string

a = "este es un string "
b = 2
print(a * b + a + "hola")