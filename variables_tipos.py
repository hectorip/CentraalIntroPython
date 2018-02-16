# Variables y tipos

# HEREDOC
"""
    Linea 1
    Linea 2
    Linea 3 
"""

# Otra forma
'''
    Otro Documento
'''

texto_largo = """
eprehenderit pariatur aute nostrud excepteur reprehenderit aute ipsum amet qui non exercitation.
"""

print(texto_largo)


# Cadenas o Strings

name = "Hector Patricio"
last_name = 'Patricio'

# Funciones

name_parts = name.split(" ")
print(name_parts)

print(name.capitalize())  # Primera letra mayúscula
print(name.lower())  # minúsculas
print(name.upper())  # mayúsculas

print(name.startswith('Hec'))
print(name.startswith('piojo'))

print(name.endswith('io'))
print(name.endswith('IO'))


# for caracter in name:
#     print(caracter)
    # Esto es parte del for
# esto ya no es parte del FOR

print("\nTexto sin vocales: ") 
vocales = ["a", "e", "i", "o", "u"]  # lista
for c in name: # iteracion sobre colecciones
    if not (c in vocales): # 
        print(c)



