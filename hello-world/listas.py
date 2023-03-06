# Crear una lista

# Cada valor se separa por una coma y esta entre corchetes []
# ejemplo:
planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]


# Acceso a los elementos de lista por índice

# Podemos acceder a cualquier elemnto de la lista por su indice
# entre corchetes [], los indicen van a partir de 0, por tanto si 
# usamos planets [0], es el primer elemento de la lista
# ejemplos:
print("The first planet is", planets[0])
# Output: The first planet is Mercury
print("The second planet is", planets[1])
# Output: The second planet is Venus
print("The third planet is", planets[2])
# Output: The third planet is Earth


# También podemos usar modificar los valores de una lista mediante su índice.
# Para esto le asignamos un nuevo valor como lo hariamos comunmente.
# por ejemplo:
planets[3] = "Red Planet"
print("Mars is also known as", planets[3])
# Output: Mars is also known as Red Planet

# ---------------------------------------------------------------------------------

# Determinación de la longitud de una lista

# Para obtener la longitud de una lista se usa la función [len()]
# ejemplo.
number_of_planets = len(planets)
print("There are", number_of_planets, "planets in the solar system.")
# Output: There are 8 planets in the solar system

# ---------------------------------------------------------------------------------

# Incorporación de valores a listas

# Las listas de python son dinamicas, osea que podemos agregar y quitar elementos 
# despues de crearlas. Para ello usamos el metodo [.append(value)]
# ejemplo:
planets.append("pluto")
number_of_planets = len(planets)
print("There are actually", number_of_planets, "planets in solar system.")
# Output: There are actually 9 planets in the solar system.

# ----------------------------------------------------------------------------------

# Eliminación de valores de listas

# Podemos quitar el ultimo elemento de la lista con el metodo [.pop()]
# ejemplo:
planets.pop()  # Goodbye, Pluto
number_of_planets = len(planets)
print("No, there are definitely", number_of_planets, "planets in the solar system.")
# Output: No, there are definitely 8 planets in the solar system

# ----------------------------------------------------------------------------------

# Uso de índices negativos

# Los índices comienzan en cero y van en aumento. 
# Los índices negativos comienzan al final de la lista y van hacia atrás.

# Osea que un índice -1 devuelve el último elemento de una lista, -2 el penultimo, etc.
# ejemplo:
print("The last planet is", planets[-1])
# Output: The last planet is Neptune
print("The penultimate planet is", planets[-2])
# Output: The penultimate planet is Uranus

# -----------------------------------------------------------------------------------

# Búsqueda de un valor en una lista

# Para ubicar donde se almacena el valor en una lista usamos el método (index). Este metodo
# busca el valor y nos devuelve el indice del mismo.
# ejemplo:
jupiter_index = planets.index("Jupiter")
print("Jupiter is the", jupiter_index + 1, "planet from the sun")
# Output: Jupiter is the 5 planet from the sun

# NOTA: Dado que la indexación comienza por 0, debe agregar 1 para mostrar el número adecuado.