#You'll frequently need to convert string values into numbers to properly perform different operations, or determine the absolute value of a number. 
#In this exercise, you will create a project to calculate the distance between two planets based on user input.

# Read the values from the user
first_planet_input = int(input("Enter the distance from the sun for the first planet in KM: "))
second_planet_input = int(input("Enter the distance from the sun for the second planet in KM: "))
distance_km = abs(first_planet_input - second_planet_input)
print("The distance in km between first planet and second planet is: "+str(distance_km))