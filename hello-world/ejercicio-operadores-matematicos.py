# Let's explore how we can create a program that can calculate the distance between two planets. 
# We'll start by using two planet distances: Earth (149,597,870 km) and Jupiter (778,547,200 km).

first_planet = 149597870
second_planet = 778547200
distance_km = second_planet - first_planet
distance_mi = distance_km / 1.609344
print(str(distance_km) + " km of distance")
print(str(distance_mi) + " mi of distance")
