banco = []
while True:
    aux = []
    aux.append(input("Coloque seu nome: "))
    aux.append(int(input('Coloque seu peso: ')))
    banco.append(aux[:])
    conti = input('Existem mais pessoas? [S/N]')
    if conti != 's':
        break
godinho = max(banco, key=lambda pessoas: pessoas[1])
magrinho = min(banco, key=lambda pessoas: pessoas[1])

#print(f'As pessoas da lista são {banco}')
#print(f'O mais gordinho é {godinho[0]}, com {godinho[1]}Kg')
#print(f'O mais magrinho é {magrinho[0]}, com {magrinho[1]}Kg')

for pessoas in banco:
    if pessoas[1] == godinho[1]:
     print(f'O mais gordinho é {pessoas[0]}, com {pessoas[1]}Kg')
  
    if pessoas[1] == magrinho[1]:
     print(f'O mais magrinho é {pessoas[0]}, com {pessoas[1]}Kg')
