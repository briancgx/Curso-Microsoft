# Creating reusable applications
# Having a program with hard-coded values limits its flexibility. 
# Your first officer likes the program you built to convert parsecs to lightyears, but wants the ability to specify a value for parsecs.
# She wants you to create a program which can accept user input.

print("Persecs exercise")
persecs_input = input('Ingrese cuantos persecs desea convertir: ')
lightyears = int(persecs_input) * 3.26
print((str(persecs_input) + " parsecs is " + str(lightyears) + " lightyears"))
