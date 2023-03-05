# Knowing how to format strings is essential when you're presenting information from a program. 
# There are a few different ways to accomplish this in Python. 
# In this exercise, you use variables that hold key facts about gravity on various moons and then use them to format and print the information.

# Start by creating three variables, name, gravity, and planet, and set them to the following values:
name = 'Ganymede'
planet = 'Mars'
gravity = 1.43

# Create a template
template = """Gravity Facts about {name}
Planet Name: {planet}
Gravity on {name}: {gravity} m/s2"""

# Use the template
print(template.format(name = name , planet = planet, gravity = gravity))