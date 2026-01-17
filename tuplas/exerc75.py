numeros = (int(input('Coloque um numero: ')), 
           int(input('Coloque um numero: ')), 
           int(input('Coloque um numero: ')), 
           int(input('Coloque um numero: ')), 
           int(input('Coloque um numero: ')))

encontrar = False
for i, valor in enumerate(numeros):
    if valor == 3:
        print(f'O três apareceu nas posição {i}', end="...")
        encontrar = True
print()
for par in numeros:
    if par % 2 == 0:
        print(par)


if not encontrar:
    print('Não ha três')


if 9 in numeros:
    print(f'O nove apareceu {numeros.count(9)}° vezes ')
else:
    print('Não ha numero nove')

