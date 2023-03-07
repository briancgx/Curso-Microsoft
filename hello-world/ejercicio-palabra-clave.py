# In the prior exercise you created a report for a ship with three fuel tanks. 
# What happens if the ship has multiple tanks? 
# Keyword arguments can be a perfect solution for this type of a situation. 
# With keyword arguments a caller can provide multiple values which your code can interact with.

# Create an update fuel report function
def fuel_report (**fuel_tanks):
    for name, value in fuel_tanks.items():
        print(f"{name}: {value}")

# Call the function
fuel_report(main =50, external = 100, emergency = 60)
        