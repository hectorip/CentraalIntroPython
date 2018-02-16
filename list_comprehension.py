#  List comprehensions
# Completado de listas

group = ["Doli", "Manuel", "Raúl"] # lista base

group_upper = []
for student in group:
    group_upper.append(student.upper())

print(group_upper)


group_upper_comprehension = [student.upper() for student in group]
# [resultado for elemento in coleeccion]
no_m_students = [student for student in group if not student.startswith("D")]

print(no_m_students)


