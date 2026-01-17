
numeros = list()

for c in range(5):
     numeros.append(int(input(f'Coloque um numro na posição {c}: ')))

print(numeros)
print(f'O maior numero é {max(numeros)}; Esta na posição {numeros.index(max(numeros))}')
print(f'O menor numero é {min(numeros)}; Esta na posição {numeros.index(min(numeros))}')

