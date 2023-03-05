# ejemplo de cadena común:
fact = "The Moon has no atmosphere."
fact += "No sound can be heard on the Moon."
print(fact)

# --------------------------------------------------------------------------------------------------------
# El uso de las comillas dependerá de las cadenas, subcadenas, aóstrofo (Moon's), entre otros
# ejemplo:
quotation_marks = 'The "near side" is the part of the Moon that faces the Earth'

# Cuando el texto tiene combinacion de comillas simples y dobles, podemos usar triples
# ejemplo:
quotation_marks_3= """We only see about 60% of the Moon's surface, this is known as the "near side"."""

# --------------------------------------------------------------------------------------------------------

# Texto multilinea
# Existen varias maneras, pero las mas comunes son:
# (\n) Usar un caracter de nueva linea
# (""") Usar comillas triples

#ejemplo:
multiline = "Facts about the Moon:\n There is no atmosphere.\n There is no sound."
print(multiline)

# Tendriamos como resultado:
#           Facts about the Moon:
#            There is no atmosphere.
#            There is no sound.

# o de esta manera
multiline = """Facts about the Moon:
...  There is no atmosphere.
...  There is no sound."""
print(multiline)
# Tendriamos como resultado:
#           Facts about the Moon:
#            There is no atmosphere.
#            There is no sound.

#------------------------------------------------------------------------------------------------------------