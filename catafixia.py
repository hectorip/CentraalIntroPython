import random

gifts = ["Sala troncoso", "Viaje para toda la familia", "Boleto gigante del metro"]

# Sacar un número aleatoreo entre 0 y 2
selection = random.randint(0, 2)
print(gifts[selection])
# selection = random.randint(0, 2)
# print(gifts[selection])
# selection = random.randint(0, 2)
# print(gifts[selection])

# gifts[0]
seleccion = random.choice(gifts)
print(seleccion)

print(random.choice(gifts))
print(random.choice(gifts))
