# Suma:
answer = 30 + 12
print(answer)
# Output: 42


# Resta:
difference = 30 - 12
print(difference)
# Output: 18


# Multiplicación:
product = 30 * 12
print(product)
# Output: 360


# Division: 
quotient = 30 / 12
print(quotient)
# Output: 2.5


# Existen varias formas de obtener respuestas con la división
# ejemplo:
seconds = 1042
display_minutes = 1042 / 60
print(display_minutes)
# Output: 17.3666667

# Pero si en lugar de usar (/), usamos (//), obtenemos:
seconds = 1042
display_minutes = 1042 // 60
print(display_minutes)
# Output: 17


# Residuo %
seconds = 1042
display_minutes = 1042 // 60
display_seconds = 1042 % 60

print(display_minutes)
print(display_seconds)

# Output:
# 17 (division)
# 22 (Residuo)

# ------------------------------------------------------------------------------

# Python respeta el orden de las operaciones.
# Este es:
# 1.- Paréntesis
# 2.- Exponentes
# 3.- Multiplicación y división
# 4.- Suma y Resta

# ejemplo:
result_1 = 1032 + 26 * 2
result_2 = 1032 + (26 * 2)
# The answer is the same in both cases - 1084

# ------------------------------------------------------------------------------

