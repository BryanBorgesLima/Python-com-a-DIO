numeros = []

while True:
    n = numeros.append(int(input("Coloque um numero: ")))
    afirmação = input("Quer continuar? [S/N]").lower()
    if afirmação != 's':
        break
print(f'Sua lista foi {n}\n')
numeros.sort(reverse=True)
print(f'Em ordem decresente foi {numeros}\n')

verifica = 0
while verifica < len(numeros):
    if n == 5:
        print('Existe numero 5 na lista')
        break
    verifica += 1
