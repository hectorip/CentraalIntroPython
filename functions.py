# Función
# Reutilizar código

ingresos = [1200, 1290, 2900, 1292, 239]
total = 0
for ingreso in ingresos:
    total += ingreso

total = sum(ingresos)


# Suma del uno al 10

to_10 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
total = 0

for n in to_10:
    total += n

# print(total)

total = sum(range(11))
# print(total)

# 5
# a -> b
# b -> c
# y -> a
# z- > b
"""
esto también puede ser un comentario
"""
def cifrar(cadena):
    """
    Esta función cifra
    """
    respuesta = ""
    return respuesta

# tareas:
def cesar(cadena, key):
    pass

res_cifrado = cifrar("hector")
print(cifrar("holi")) # "jqnk"
