principal = [[], []]

aux = 0
for p in range(0, 7):
    aux = (int(input(f'Coloque um nuemro na posição {p}°:  ')))
    if aux % 2 == 0:
     principal[0].append(aux)
    else:
       principal[1].append(aux)
    
principal[0].sort()
principal[1].sort()


print('~~~~' *30)
print(f'Os numeros impares são {principal[1]}\n')
print(f'Os numeros pares são {principal[0]}')
