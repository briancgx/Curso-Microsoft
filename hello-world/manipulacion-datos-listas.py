# Segmentación de listas

# Esta se usa de la misma manera que un indice[i], sin embargo esta usa 2
# el indice inicial y el final. [ii:if]
# Ejemplo, obtener los dos planetas antes de la tierra:
planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
planets_before_earth = planets[0:2]
print(planets_before_earth)
# Output: ['Mercury', 'Venus']

# Podemos observar que la tierra que esta en el indice [2] no aparece y es que apesar de estr escrito
# en la segmentación, este ultimo no se incluye por ser el final.

# Si quisieramos obtener los planetas despues de la tierra, usamos:
planets_after_earth = planets[3:8]
print(planets_after_earth) 
# Output: ['Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']

# Aqui pudimos obtener todos los planetas porque añadimos +1 al indice final, osea en vez de 7 es 8.

# -----------------------------------------------------------------------------------------------------------------------------------------------

# Combinación de listas

# Para unir dos listas, debe usar el otro operador (+) con dos listas para devolver una nueva.
# ejemplo:
amalthea_group =  ["Metis", "Adrastea", "Amalthea", "Thebe"]
galilean_group = ["Io", "Europa", "Ganymede", "Callisto" ]

regular_satelite_moons = amalthea_group + galilean_group
print("The regular satellite moon of Jupiter are", regular_satelite_moons)
# Output: The regular satellite moons of Jupiter are ['Metis', 'Adrastea', 'Amalthea', 'Thebe', 'Io', 'Europa', 'Ganymede', 'Callisto']

# -----------------------------------------------------------------------------------------------------------------------------------------------

# Ordenación de listas

# Para ordenar una lista, usamos el método [.sort()] de la lista
# python las ordenará en orden alfabetico y los numeros en numerico

# ejemplo:
regular_satelite_moons.sort()
print("The regular satellite moons of Jupiter are", regular_satelite_moons)
# Output: The regular satellite moons of Jupiter are ['Adrastea', 'Amalthea', 'Callisto', 'Europa', 'Ganymede', 'Io', 'Metis', 'Thebe']


# Para ordenar una lista en orden inverso usamos [.sort(reverse=True)] en la lista
# ejemplo:
regular_satelite_moons.sort(reverse=True)
print("The regular satellite moons of Jupiter are", regular_satelite_moons)
# Output: The regular satellite moons of Jupiter are ['Thebe', 'Metis', 'Io', 'Ganymede', 'Europa', 'Callisto', 'Amalthea', 'Adrastea']