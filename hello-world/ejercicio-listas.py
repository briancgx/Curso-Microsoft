# Lists allow you to store multiple values in a single variable. 
# In this notebook you'll create a project to display information about the planets.

# Add all planets to a list
planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
number_planets = len(planets)
print("There are", str(number_planets), "planets")
planets.append("Pluto")
number_planets = len(planets)
print("Added Pluto, Actually there are", number_planets, "planets")
print(planets[-1], "is last planet")
