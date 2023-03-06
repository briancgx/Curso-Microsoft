# In this scenario, you will calculate both the total number of moons in the solar system and the average number of moons a planet has. 
# You will do this by using a dictionary object.

# Creating a variable
planet_moons = {
    'mercury': 0,
    'venus': 0,
    'earth': 1,
    'mars': 2,
    'jupiter': 79,
    'saturn': 82,
    'uranus': 27,
    'neptune': 14,
    'pluto': 5,
    'haumea': 2,
    'makemake': 1,
    'eris': 1
}

# Obtain a list of moons and number of planets
moons = planet_moons.values()
total_planets = len(planet_moons.keys())


#Determine the average number of moons
total_moons = 0
for moon in moons:
    total_moons = total_moons + moon
    
average = total_moons/total_planets
print(f'Each planet has an average of {average} moons')