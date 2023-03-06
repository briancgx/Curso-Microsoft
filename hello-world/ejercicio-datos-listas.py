# You might need to work different sections of a list. 
# In this notebook, you will create a project to display planets closer 
# to and farther away from the sun than a planet that the user enters.

# Create the list of planets
planets = ["Mercury", "Venus","Earth", "Mars","Jupiter","Saturn","Uranus","Neptune"]

# Prompt the user for the reference planet
user_planet = input("Please enter the name of the planet (with a capital letter to start): ")

# Find the location of the planet
planet_index = planets.index(user_planet)

# Display planets closer the sun
print("Here are the planets closer than " + user_planet)
print(planets[planet_index + 1:])

# Si no escribimos el indice final, se imprime el resto de la lista 
