numeros = []

while True:
    numeros.append(int(input("Coloque um numero: ")))
    afirmação = input("Quer continuar? [S/N]").lower()
    if afirmação != 's':
        break
print(f'Sua lista foi {numeros}\n')
numeros.sort(reverse=True)
print(f'Em ordem decresente foi {numeros}\n')
if 5 in numeros:
    print(f'O valor 5 esta na lista; Na posição {numeros.index(5)}°')
else:
    print('O valor 5 não esta na lista')