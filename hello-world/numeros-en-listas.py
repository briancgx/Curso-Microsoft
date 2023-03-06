# Se declaran de la misma manera
# ejemplo, este crea una lista en la que se muestran las fuerzas G de los planetas:
gravity_on_planets = [0.378, 0.907, 1, 0.377, 2.36, 0.916, 0.889, 1.12]


# Podemos ubicarlos de la misma manera, con su indice [i]
# Y hacer operaciones cuando los ubiquemos
# ejemplo:
bus_weight = 12650 # in kilograms, on Earth
print("On Earth, a double-decker bus weighs", bus_weight, "kg")
# Output: On Earth, a double-decker bus weighs 12650 kg
print("On Mercury, a double-decker bus weighs", bus_weight * gravity_on_planets[0], "kg")
# Output: On Mercury, a double-decker bus weighs 4781.7 kg

# ---------------------------------------------------------------------------------------------

# Uso de [min()] y [max()] con listas

# La funcion max() devuelve el numero más grande de la lista
# La funcion min() devuelve el numero más pequeño de la lista

# ejemplo:
print(min(gravity_on_planets))
#Output: 0,377

# En este otro ejemplo miremos pesos máximos y minimos del sistema solar:
bus_weight = 12650 # in kilograms, on Earth
print("On Earth, a double-decker bus weighs", bus_weight, "kg")
# Output: On Earth, a double-decker bus weighs 12650 kg
print("The lightest a bus would be in the solar system is", bus_weight * min(gravity_on_planets), "kg")
# Output: The lightest a bus would be in the solar system is 4769.05 kg
print("The heaviest a bus would be in the solar system is", bus_weight * max(gravity_on_planets), "kg")
# Output: The heaviest a bus would be in the solar system is 29854 kg