# Creación de diccionarios

# Para indicar un diccionario python usa llaves {} y dos pubntos ":".
# Podemos crear un diccionario vacio y añadir valores después o rellenarlo al momento.
# Las claves o valores se separan por : y el nombre de cada clave esta entre " ", como un literal de cadena

# ejemplo:
planet = {
    'name':'Earth',
    'moons': 1
}

# Tenemos dos claves (name y moons), que se comportan como las variables, osea almacenan un valor
# pero se incluyen dentro de una variable más grande llamada (planet)
# 1 no esta entre comillas por ser un NUMERO

# -------------------------------------------------------------------------------------------------------------------

# Lectura de valores de diccionario

# Para leer los valores dentro de un diccionario. Los objetos del diccionario tienene un metodo [.get()]
# con el que podemos acceder a un valor mediante su clave.


# ejemplo para imprimir name:
print(planet.get('name'))
# Displays: Earth


# Podria ser muy parecido a los corchetes [], pero la diferencia principal es que si una clave no esta disponible
# get devuelve None y [] genera un KeyError

# ejemplo:
wibble = planet.get('wibble') # Returns None
wibble = planet['wibble'] # Throws KeyError

# --------------------------------------------------------------------------------------------------------------------

# Modificación de valores de diccionario

# Con el metodo [.update()] podemos hacer modificaciones
# ejemplo:
planet.update({'name': 'Makemake'})
# name is now set to Makemake


# De igual forma que podemos usar [] para leer valores, podemos usarlo para modificarlos,
# la diferencia es la sintaxis y usamos =
# ejemplo:
planet['name'] = 'Makemake'
# name is now set to Makemake


# SE RECOMIENDA EL USO DE [.update()] PORQUE PODEMOS MODIFICAR VARIOS VALORES A LA VEZ
# ejemplo:

# Using update
planet.update({
    'name': 'Jupiter',
    'moons': 79
})

# Using square brackets
planet['name'] = 'Jupiter'
planet['moons'] = 79

# --------------------------------------------------------------------------------------------------------------------

# Adicion y eliminación de claves

# No es necesario crear todas las claves al inicializar un diccionario
# Ejemplo, actualicemos planet para incluir periodo orbital en dias:
planet['orbital period'] = 4333
# planet dictionary now contains: {
#   name: 'jupiter'
#   moons: 79
#   orbital period: 4333
# }


# Para eliminar una clave usamos [.pop()], esto nos devueve el valor y quita la clave
# Ejemplo quitemos orbital period:
planet.pop('orbital period')
# planet dictionary now contains: {
#   name: 'jupiter'
#   moons: 79
# }

# --------------------------------------------------------------------------------------------------------------------

# Tipos de data complejos


# Los diccionarios almacenan todo tipo de valores, incluidos más diccionarios.
# Ejemplo almacenamos el diametro de planet, que podríamos medir alrededor de su ecuador o los polos.
# creamos otro diccionario dentro de planet

# Add address
planet ['diameter (km)'] = {
    'polar' : 133709,
    'equatorial' : 142984
}
# planet dictionary now contains: {
#   name: 'Jupiter'
#   moons: 79
#   diameter (km): {
#      polar: 133709
#      equatorial: 142984
#   }
# }


# Para recuperar valores en un diccionario anidado, debemos encadenar [] o llamadas a get
print(f'{planet["name"]} polar diameter: {planet["diameter (km)"]["polar"]}')
# Output: Jupiter polar diameter: 133709

# --------------------------------------------------------------------------------------------------------------------

# Recuperación de todas las claves y valores
# El método [keys()] devuelve el objetp de una lista que contiene todas las claves

# Ejmeplo: (Almacenamos los ultimos 3 meses de precipitaciones)
rainfall = {
    'october': 3.5,
    'november': 4.2,
    'december': 2.1
}


# Ahora queremos mostrar la lista de todas las precipitaciones pero seria tedioso:
for key in rainfall.keys():
    print(f'{key}: {rainfall[key]}cm')
# Output:
# october: 3.5cm
# november: 4.2cm
# december: 2.1cm

# -----------------------------------------------------------------------------------------------------------------------

# Determinación de la existencia de una clave en un diccionario
# Al actualizar un valor en un diccionario, Python sobrescribirá el valor existente o creará uno, si la clave no existe. 
# Si quiere agregar a un valor en lugar de sobrescribirlo, puede comprobar si la clave existe mediante (in)
if 'december' in rainfall:
    rainfall['december'] = rainfall['december'] + 1
else:
    rainfall['december'] = 1
# Because december exists, the value will be 3.1

# -------------------------------------------------------------------------------------------------------------------------

# Recuperación de todos los valores

# [values()] devuelve la lista de todos los valores de un diccionario sin sus claves correspondientes.
# values() puede resultar más util cuando se usa clave con fines de etiquetado, como el ejemplo anterior
# donde las claves son el nombre del mes

# Ejemplo, podemos usar values() para determinar el importe total de las precipitaciones:
total_rainfall = 0
for value in rainfall.values():
    total_rainfall = total_rainfall + value

print(f'There was {total_rainfall}cm in the last quarter')
# Output:
# There was 10.8cm in the last quarter


