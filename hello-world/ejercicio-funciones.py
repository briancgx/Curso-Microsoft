# Required arguments in functions are used when functions need those arguments to work properly. 
# In this exercise, you'll construct a fuel report that requires information from several fuel locations 
# throughout the rocket ship.

# Create a report generation function
def generate_report (main_tank, external_tank, hydrogen_tank):
    output = f"""Fuel report:
    Main tank: {main_tank}
    External tank: {external_tank}
    Hydrogen tank: {hydrogen_tank}"""
    print(output)
    
    
# extra:
main_t = int(input("Ingrese cuanta gasolina hay en main: "))
external_t = int(input("Ingrese cuanta gasolina hay en external: "))
hydrogen_t = int(input("Ingrese cuanta gasolina hay en hydrogen: "))

 
generate_report(main_t, external_t, hydrogen_t)