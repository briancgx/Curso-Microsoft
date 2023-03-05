# Formato de signo de porcentaje (%)
# El marcador de posición de la variable de cadena es [%s]
# despues de la cadena se usa otro carácter [%] seguido de la variable.
# ejemplo:
mass_percentage = "1/6"
print("On the Moon, you would weigh about %s of your weight on Earth" % mass_percentage)
# Esto nos imprime 'On the Moon, you would weigh about 1/6 of your weight on Earth'


# Al usar varios de estos valores puede cambiar la sintaxsis, por tanto
# debemos colocar parentesis para especificar
# ejemplo:
print("""Both sides of the %s get the same amount of sunlight,
but only one side is seen from %s because
the %s rotates around its own axis when it orbits %s.""" % ("Moon", "Earth", "Moon", "Earth"))
# Esto nos imprime 'Both sides of the Moon get the same amount of sunlight,
# but only one side is seen from Earth because
# the Moon rotates around its own axis when it orbits Earth.'


# -----------------------------------------------------------------------------------------------------------------------

# El método [.format()]
# Este metodo usa llaves {} como marcadores de posición dentro de una cadena 
# y utiliza la asignacion de variables para reemplazar el texto.
# ejemlo:
mass_percentage = "1/6"
print("On the Moon, you would weigh about {} of your weight on Earth".format(mass_percentage))
# Esto nos imrime 'On the Moon, you would weigh about 1/6 of your weight on Earth'


# Aqui no es necesario asignar variables repetidas varias veces, lo que hace que sea menos
# detallado y más sencillo
# Usamos numeros dentro de las {}, el numero que se escribe dentro es el indice del argumento
# que queremos asignar
# ejemplo:
mass_percentage = "1/6"
print("""You are lighter on the {0}, because on the {0} 
you would weigh about {1} of your weight on Earth""".format("Moon", mass_percentage))
#Esto nos imprime 'You are lighter on the Moon, because on the Moon you would weigh about 1/6 of your weight on Earth'

# Y de esta manera podriamos sustituir los numeros por palabras clave
# ejemplo:
mass_percentage = "1/6"
print("""You are lighter on the {moon}, because on the {moon} 
you would weigh about {mass} of your weight on Earth""".format(moon="Moon", mass=mass_percentage))
# Esto nos imprime 'You are lighter on the Moon, because on the Moon you would weigh about 1/6 of your weight on Earth'

# -----------------------------------------------------------------------------------------------------------------------

# Cadenas f-strings
# Estas cadenas parecen plantillas y se aplican con el nombre dela variable dentr del codigo, pero con el prefijo [f]
# ejemplo:
mass_percentage = "1/6"
print(f"On the Moon, you would weigh about {mass_percentage} of your weight on Earth")
# Esto imprime 'On the Moon, you would weigh about 1/6 of your weight on Earth'


# Ademas que las f-strings son menos detalladas, podemos usar expresiones entre llaves:
# ejemplo: queremos representar 1/6 en porcentaje, lo hacemos con [round()]
print(round(100/6, 1))
# Esto divide 100 entre 6 y despues de la ',' colocamos los decimales que queremos, en este caso 1
# Y esto imprime '16.7'


# Con f-strings tampoco necesitamos asignar variables
# ejemplo:
print(f"On the Moon, you would weigh about {round(100/6, 1)}% of your weight on Earth")
# Nos imprime 'On the Moon, you would weigh about 16.7% of your weight on Earth'


# Para usar una expresion no necesitamos una llamada de funcion.
# Cualquier metodo de cadena es valido.
# Ejemplo, la cadena podría apicar un uso especifico de mayúsculas y minusculas para crear un titulo:
subject = "interesting facts about the moon"
print(f"{subject.title()}")
# Esto imprime 'Interesting Facts About The Moon'