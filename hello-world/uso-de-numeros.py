# Al convertir cadenas en numeros, debemos indicar que tipo de numero será
# (int) para enteros o (float) para punto flotante/decimal

# ejemplo:
demo_int = int('215')
print(demo_int)
# Output: 215
demo_float = float('215.3')
print(demo_float)
# Output: 215.3

# -----------------------------------------------------------------------------------

# Valores absolutos

# Use (abs) para convertir valores negativos en absolutos
# osea da igual el orden, siempre obtendremos positivos. 
# ejemplo:
print(abs(39 - 16))
# Output. 23
print(abs(16 - 39))
# Output: 23

# -----------------------------------------------------------------------------------

# Redondeo

# Use (round) para redondear hacia arriba el enter mas cercano si es 1.5 o mayor.
# Y también hacia abajo si el numero es menor que 1.5
# ejemplo: 
print(round(14.5))
# Output: 15

# -----------------------------------------------------------------------------------

# Biblioteca matemática

# La biblioteca (math) permite hacer redondeos (floor) y (ceil), proporcionar pi, etc.
# (ceil) se usa para redonder hacia arriba
# (floor) se usa para redondear hacia abajo

# OJO: DEBEMOS IMPORTAR ANTES LA BIBLIOTECA

# ejemplo: 
from math import ceil, floor
# Importacion de biblioteca
round_up = ceil(12.5)
print(round_up)
# Output: 13
round_down = floor(12.5)
print(round_down)
# Output: 12