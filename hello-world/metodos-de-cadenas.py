# Los métodos de cadena forman parte del tipo str. 
# Esto significa que los métodos existen como variables de cadena o directamente como parte de la cadena. 
# Por ejemplo, el método [.title()] se puede usar directamente con una cadena:

example_title =  "temperatures and facts about the moon".title()
print(example_title)
# Esto nos imprimiría:
#   Temperatures And Facts About The Moon

# tambien podemos usarlo en la variable:
example_title_2 = "temperatures and facts about the moon"
print(example_title_2.title())
# Esto nos imprimiría:
#   Temperatures And Facts About The Moon

# --------------------------------------------------------------------------------------------------------

# Division de una cadena

# Un metodo comun es [.split()] Sin argumentos, el metodo separará la cadena en cada espacio.

# ejemplo:
temperatures = """Daylight: 260 F
Nighttime: -280 F"""
print(str(temperatures.split()))
# Esto nos imprimiría:
#   ['Daylight:', '260', 'F', 'Nighttime:', '-280', 'F']


# Si a esto le añadimos el caracter de nueva linea implícito se puede usar para divir
# la cadena al final de cada linea y crear lineas unicas:  [.split(\n)
# ejemplo:
temperatures = """Daylight: 260 F
Nighttime: -280 F"""
print(str(temperatures.split('\n')))
# Esto nos imprimiría: 
#    ['Daylight: 260 F', 'Nighttime: -280 F']

# --------------------------------------------------------------------------------------------------------

# Busqueda de cadena

# El operador [in] lo utilizamos para encontrar palabras clave o caractéres:
# ejemplo:

"Moon" in "This text will describe facts and challenges with space travel"
#False
"Moon" in "This text will describe facts about the Moon"
#True


# Un enfoque para buscar la posicion de una palabra especifica en una cadena
# consiste en usar el metodo [.find()]
# ejemplo:

temperatures = """Saturn has daytime temperature of -170 degrees Celsius,
while Mars has -28 Celsius."""
print(str(temperatures.find("Moon")))
# Esto imprimirá -1 y significa que no se encuentra la palabra "Moon"
print(str(temperatures.find("Mars")))
# Esto imprimirá el lugar donde "Mars" se encuentra, en este caso "62"

# --------------------------------------------------------------------------------------------------------

# Si unicamente queremos saber si el contenido existe es usar el metodo [.count()]
# esto nos devolverá las veces que se repita esta palabra o caractér

# ejemplo:
print(str(temperatures.count("Mars")))
# Imprime 1
print(str(temperatures.count("Moon")))
# Imprime 0


# Debemos tomar en cuenta que buscará la palabra tal y como la escribimos (Mayusculas o minusculas)
# por tanto podemos convertir todo a una cadena de letras minusculas con [.lower()]
# ejemplo:
example_lower = "The Moon And The Earth".lower()
print(example_lower)
# Esto nos imprime "the moon and the earth"


# Para comprobar una palabra en un texto con [.lower()] podemos hacerlo así:
example_text_lower = "Temperatures on the Moon can vary wildly."
"temperatures" in example_text_lower
# Si usamos unicamente la variable será False, por los caractéres
"temperatures" in example_text_lower.lower()
# En este caso es True, por la busqueda en minuscula y los caractéres también


# De la misma manera podemos pasar todo a mayusculas con [.upper()]
# ejemplo:
example_upper = "The Moon And The Earth"
print(example_upper.upper())
# Esto nos imprime "THE MOON AND THE EARTH"

# ---------------------------------------------------------------------------------------------------------

# A veces tendremos problemas un poco complejos, ejemplo:
temperatures = "Mars Average Temperature: -60 C"
# Extraer la temperatura en Marte, entonces:
# dividimos en partes con ":" como referencia
parts = temperatures.split(':')
# Usamos [-1] para obtener el ultimo elemento que esté en las divisiones
print(parts[-1])

# ---------------------------------------------------------------------------------------------------------

# De igual manera podemos encontrar más irregulares y debemos usar distintas tecnicas:
mars_temperature = "The highest temperature on Mars is about 30 C"
for item in mars_temperature.split():
    if item.isnumeric():
    # El metodo [.isnumeric()] se utiliza para encontrar enteros
        print(item)

# Además el método [.isdecimal()] se utiliza para encontrar decimales
# IMPORTANTE [.isnumeric()] FUNCIONA UNICAMENTE CON POSITIVOS

# Para el caso de los negativos podemos uar métodos como [.startswith('-')]
# ejemplo:
"-60".startswith('-')
#True

# Similar el método [.endswith()] comprueba el ultimo caracter de la cadena
#ejemplo:
if "30 C".endswith("C"):
    print("This temperature is in Celsius")
    #Imprmirá dicha frase ya que se cumple la condicion         

# ---------------------------------------------------------------------------------------------------------

# Ademas de los métodos anteriores podemos usar [.replace()] para buscar y reemplazar repeticiones
# ejemplo:
example_replace = "Saturn has a daytime temperature of -170 degrees Celsius, while Mars has -28 Celsius.".replace("Celsius", "C")
print(example_replace)
# Esto imprimirá "Saturn has a daytime temperature of -170 degrees C, while Mars has -28 C."

# ----------------------------------------------------------------------------------------------------------

# Casi como el método [.split()], existe [.join()] con la diferencia que este los agrupa (lo contrario a split)
# este metodo necesita un elemento iterable (como una lista de python) como argumento, por lo que se usa distinto
# a los demás métodos de cadena
# ejemplo:
example_join = ["The Moon is drifting away from the Earth.", "On average, the Moon is moving about 4cm every year"]
print(' '.join(example_join))
# Esto imprimirá 'The Moon is drifting away from the Earth. On average, the Moon is moving about 4cm every year'
