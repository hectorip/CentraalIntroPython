#  List comprehensions
# Completado de listas

group = ["Doli", "Manuel", "Raúl", "Ryu", "Nabucodonosor"]  # lista base

group_upper = []
for student in group:
    group_upper.append(student.upper())

print(group_upper)


group_upper_comprehension = [student.upper() for student in group]
# [resultado for elemento in coleeccion]
no_m_students = [student for student in group if not student.startswith("D")]

print(no_m_students)


# lista de estudiantes con nomrbes en mayúscula y que no termine en 'l' el nombre
#Estilos de nombrado

# camelCase
estoEsUnaVariable = 1
EstoTambienEsCamelCase = 1

# snake_case
esto_es_una_variable = 1