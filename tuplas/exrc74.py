import random 

numeros = (random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10))
print(f'Os numeros são {numeros}')
print(f'Os maiores numeros são {max(numeros)} e o menor é {min(numeros)}')