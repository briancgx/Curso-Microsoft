# Los métodos de cadena forman parte del tipo str. 
# Esto significa que los métodos existen como variables de cadena o directamente como parte de la cadena. 
# Por ejemplo, el método .title() se puede usar directamente con una cadena:

example_title =  "temperatures and facts about the moon".title()
print(example_title)
# Esto nos imprimiría:
#   Temperatures And Facts About The Moon

# tambien podemos usarlo en la variable:
example_title_2 = "temperatures and facts about the moon"
print(example_title_2.title())
# Esto nos imprimiría:
#   Temperatures And Facts About The Moon

# --------------------------------------------------------------------------------------------------------

# Division de una cadena

# Un metodo comun es .split() Sin argumentos, el metodo separará la cadena en cada espacio.

# ejemplo:
temperatures = """Daylight: 260 F
Nighttime: -280 F"""
print(str(temperatures.split()))
# Esto nos imprimiría:
#   ['Daylight:', '260', 'F', 'Nighttime:', '-280', 'F']


# Si a esto le añadimos el caracter de nueva linea implícito se puede usar para divir
# la cadena al final de cada linea y crear lineas unicas:  .split(\n)
# ejemplo:
temperatures = """Daylight: 260 F
Nighttime: -280 F"""
print(str(temperatures.split('\n')))
# Esto nos imprimiría: 
#    ['Daylight: 260 F', 'Nighttime: -280 F']

# --------------------------------------------------------------------------------------------------------

# Busqueda de cadena




