# Operadores matematicos:
# a == b   a es igual que b
# a != b   a es desigual que b
# a < b    a menor que b
# a <= b   a menor o igual que b
# a > b    a mayor que b
# a >= b   a mayor o igual que b

# ----------------------------------------------------------------------------------------

# Sintaxis de [if]:
# if test_expresion:   (Siempre usando los ":")
#   statement(s) to be run
     
# Prueba:
a = 97
b = 55
# test expression
if a < b:
    print (b)
# La expresion anterior no imprime porque b es menor que a

# La sangría se usa para una misma instruccion, si quieres que esta acabe, se quita
# ejemplo:
a = 24
b = 44
if a <= 0:
    print(a)
print(b)

# ----------------------------------------------------------------------------------------

# Sintaxis de [else]: 
# if test_expression:
#    statement(s) to be run
# else:
#    statement(s) to be run
     
#ejemplo:
a = 93
b = 27
if a >= b:
    print(a)
else:
    print(b)

# --------------------------------------------------------------------------------------------

# elif
# La palabra clave elif es la abreviatura de else if. 
# El uso de instrucciones elif permite agregar varias expresiones de prueba al programa. 
# Estas instrucciones se ejecutan en el orden en que se escriben, por lo que 
# el programa escribirá una instrucción elif solo si la primera instrucción if es False.

# Sintaxis de [elif]
# if test_expression:
#    statement(s) to be run
# elif test_expression:
#    statement(s) to be run

#ejemplo:
a = 93
b = 27
if a >= b:
    print('a is greater than or equal to b')
elif a == b:
    print('a is equal to b')

# -----------------------------------------------------------------------------------------------

# Combinacion instrucciones if, elif y else


# La Sintaxis para un codigo con tres tipos de instruccion es la siguiente:
# if test_expression:
#    statement(s) to be run
# elif test_expression:
#    statement(s) to be run
# elif test_expression:
#    statement(s) to be run
# else:
#    statement(s) to be run

# ejemplo:
a = 93
b = 27
if a > b:
    print("a is greater than b")
elif a < b:
    print("a is less than b")
else: 
    print ("a is equal to b")

#------------------------------------------------------------------------------------------------

# Uso de logica condicional anidada:

# Ejemplo de sintaxis: 
# if test_expression:
    # statement(s) to be run
    # if test_expression:
        # statement(s) to be run
    # else: 
        # statement(s) to be run
# elif test_expression:
    # statement(s) to be run
    # if test_expression:
        # statement(s) to be run
    # else: 
        # statement(s) to be run
# else:
    # statement(s) to be run
    
    
# ejemplo:
a = 16
b = 25
c = 27
if a > b:
    if b > c:
        print ("a is greater than b and b is greater than c")
    else: 
        print ("a is greater than b and less than c")
elif a == b:
    print ("a is equal to b")
else:
    print ("a is less than b")