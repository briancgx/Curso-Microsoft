# Python dictionaries allow you to model more complex data. 
# Dictionaries are a collection of key/value pairs, and are very common in Python programs. 
# Their flexibility allows you to dynamically work with related values without having to create classes or objects.

# Managing planet data
planet = {
    'name' : 'Mars',
    'moons' : 2
}

# Display planet data
print(planet.get('name'),"has",planet.get('moons'), "moon(s)")

# Add circumference information
planet['circumference (km)'] = ({
    'polar' : 6752,
    'equatorial' : 6792
})

print(f'{planet["name"]} has a polar circumference of {planet["circumference (km)"]["polar"]}')