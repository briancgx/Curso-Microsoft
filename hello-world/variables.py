planets_in_solar_system = 8 # int, pluto used to be the 9th planet, but is too small
distance_to_alpha_centauri = 4.367 # float, lightyears
can_liftoff = True
shuttle_landed_on_the_moon = "Apollo 11" #string
# Usando type = type(distance_to_alpha_centauri) ## <class 'float'>


# Operadores = <left side> <operator> <right side>
# Ejemplo:
left_side = 10
right_side = 5
left_side / right_side # 2
# x += 2   x incrementa en 2. Si antes contenía 2, ahora contiene 4
# x -= 2   x reducido en 2. Si antes contenía 2, ahora contiene 0
# x /= 2   x divido por 2. Si antes contenía 2, ahora contiene 1
# x *= 2   x multiplicado por dos. Si antes contenía 2, ahora contiene 4


# Para trabajar con una fecha, debe importar el módulo date:
from datetime import date

# A continuación, puede llamar a las funciones con las que quiere trabajar.
# Para obtener la fecha de hoy, puede llamar a la función today():
date.today()

# Para mostrar la fecha:
print(date.today())

# Fecha con una cadena (pata que funcione debemos convertir la fecha en un string)
print("Today's date is: " + str(date.today()))



