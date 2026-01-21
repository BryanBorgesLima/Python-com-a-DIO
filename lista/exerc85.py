principal = []
lista_par = []
lista_impar = []

for p in range(0, 7):
    principal.append(int(input(f'Coloque um nuemro na posição {p}°:  ')))
    

for par in principal:
    if par % 2 == 0:
        lista_par.append(par)
    

for impar in principal:
    if impar % 2 != 0:
        lista_impar.append(impar)
   

principal.append(lista_par[:])
principal.append(lista_impar[:])

print('~~~~' *30)
print(f'Os numeros impares são {lista_impar}\n')
print(f'Os numeros pares são {lista_par}')
