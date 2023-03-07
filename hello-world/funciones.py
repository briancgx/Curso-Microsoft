# Funciones sin argumentos

# Para crear una función usamos la clave def, seguida de un nombre, 
# paréntesis y después, del cuerpo con el código de la función:
# ejemplo:
def rocket_parts():
    print("payload, propellant, structure")
 
    
# Para usar la función debemos llamarla por su nombre, usando paréntesis:
rocket_parts()
# Output: 'payload, propellant, structure'


output = rocket_parts()
output is None
# True


# --------------------------------------------------------------------------------------

# En python varias funciones integradas requieren argumentos.

# Un ejemplo de una función integrada que requiere un argumento es any(). 
# Esta función toma un objeto iterable (por ejemplo, una lista) y devuelve True
# si algún elemento del objeto iterable es True. De lo contrario, devuelve False.
# ejemplo:
any([True, False, False])
# True
any([False, False, False])
# False

# Si llama a any() sin ningún argumento, se genera un error y necesita usar argumentos.


# Algunas funciones permiten el uso de argumentos opcionales mediante otra funcion 
# integrada denominada str()
# ejemplo:
str()
# ''
str(15)
# '15'

# -----------------------------------------------------------------------------------------------------

# Exigencia de un argumento 

# Las entradas obligatorias se denominan argumentos para la función
# Para requerir un argumento ponemos paréntesis:
def distance_from_earth (destination) :
    if destination == "Moon":
        return "238,855"
    else:
        return "Unable to computer to that destination"
    
    
# Insertamos llamar a la función distance_from_earth() sin ningún argumento:
print(distance_from_earth("Moon"))
print(distance_from_earth("Saturn"))

# --------------------------------------------------------------------------------------------------

# Para usar varios argumentos, debemos separarlos con comas.

# ejemplo: Vamos a crear una función que pueda 
# calcular cuántos días se tardarán en llegar a un destino, dadas la distancia y una velocidad constante:
def days_to_complete(distance, speed):
    hours = distance / speed
    return hours / 24

print(days_to_complete(238855, 75))

# -------------------------------------------------------------------------------------------------------------------

# Funciones como argumentos

# Podemos usar el valor de la función days_to_complete() y asignarlo a una variable y,
# después pasarlo a round(), [funcion integrada que redondea] para obetener un numero entero.
total_days =days_to_complete(238855, 75)
print(round(total_days))

# ------------------------------------------------------------------------------------------------------------------------------

# Argumentos de palabra clave

#Los argumentos opcionales requieren un valor predeterminado asignado a ellos. 
# Estos argumentos con nombre se denominan argumentos de palabra clave. 
# Los valores del argumento de palabra clave deben definirse en las propias funciones.
# ejemplo: Vamos a crear una función que devuelva la hora estimada de llegada usando el mismo valor que la misión Apolo 11

from datetime import timedelta, datetime

#def arrival_time (hours = 51):
#    now = datetime.now()
#    arrival = now + timedelta(hours = hours)
#    return arrival.strftime("Arribal: %A %H:%M")

#print(arrival_time()) #Predeterminado
#print(arrival_time(hours=0)) #AsignadoPorNosotros

# -----------------------------------------------------------------------------------------------------------------------------

# Combinación de argumentos y argumentos de palabra clave

# A veces, una función necesita una combinación de argumentos de palabra clave y argumentos. 
# En Python, esta combinación sigue un orden específico. 
# Los argumentos siempre se declaran primero, seguidos de argumentos de palabra clave.

# ejemplo: Actualice la función arrival_time() para que tome un argumento necesario, que es el nombre del destino:

#from datetime import timedelta, datetime

def arrival_time (destination, hours = 51):
    now = datetime.now()
    arrival = now + timedelta(hours = hours)
    return arrival.strftime(f"{destination} Arrival: %A %H:%M")

# Ahora ya no podemos llamar a la funcion sin argumentos, ya que añadimos un argumento necesario
print(arrival_time("Moon")) #Un argumento
print(arrival_time("Orbit", hours = 0.13)) #Más de dos valores

# -------------------------------------------------------------------------------------------------------------------------------

# Argumentos de variable

# Los argumentos en las funciones son necesarios. 
# Pero cuando se usan argumentos de variable, la función permite pasar cualquier número de argumentos (incluido 0). 
# La sintaxis para usar argumentos de variable es agregar un asterisco único como prefijo (*) antes del nombre del argumento.

# ejemplo:
def variable_length(*args):
    print(args)
# Output:

# En este caso, *args indica a la función que acepte cualquier número de argumentos (incluido 0). 
# En la función, args ahora está disponible como la variable que contiene todos los argumentos como una tupla. 
# Pruebe la función pasando cualquier número o tipo de argumentos:
variable_length()
# Output: 
variable_length("one", "two")
# Output: ('one', 'two')
print(variable_length(None))
# Output: (None,)



# Un cohete realiza varios pasos antes de un lanzamiento. 
# En función de las tareas o retrasos, estos pasos pueden tardar más de lo previsto. 
# Vamos a crear una función de longitud variable que pueda calcular cuántos minutos quedan hasta el inicio, 
# dado el tiempo que va a tardar cada paso:
def sequence_time(*args):
    total_minutes = sum(args)
    if total_minutes < 60:
        return f"Total time to launch is {total_minutes} minutes"
    else:
        return f"Total time to launch is {total_minutes/60} hours"
    
# probamos:
print(sequence_time(4, 14, 18))
# Output: Total time to launch is 36 minutes
print(sequence_time(4,14,48))

# -------------------------------------------------------------------------------------------------------------------------------

# Argumentos de palabra clave variable

# Para que una función acepte cualquier número de argumentos de palabra clave, debe usar una sintaxis similar. 
# En este caso, se requiere un asterisco doble:
def variable_lengthx(**kwargs):
    print(kwargs)
    
# Pruebe la función de ejemplo, que imprime los nombres y valores pasados como kwargs:
variable_lengthx(tanks = 1, day = "wednesday", pilots = 3)



# ejemplo practico: vamos a usar argumentos de palabra clave variable para notificar los astronautas asignados a la misión. 
def crew_members(**kwargs):
    print(f"{len(kwargs)} astronauts assigned for this mission:")
    for title, name in kwargs.items():
        print(f"{title}: {name}")
# probamos:
crew_members(capitain="Neil Armstrong", pilot="Buzz Aldrin", comand_pilot="Michael Collins")

# Nota: si usamos palabras clave repetidas obtendremos un error 