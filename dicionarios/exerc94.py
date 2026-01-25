banco = []
while True:
    aux = dict()
    aux['nome'] = input('Coloque seu nome: ')
    aux['idade'] = int(input('Coloque sua idade: '))
    aux['sexo'] = input('Coloque seu sexo: ')
    banco.append(aux.copy())
    afirm = input('Quer continuar? [S/N]').lower()
    if afirm != 's':
        break

soma_m = 0
numeros = list()
for n in banco:
  numeros.append(n['idade'])
soma_m += sum(numeros)

print(f'{len(banco)} pessoas foram cadastras')
print('~~~~'*10)
media = soma_m / len(banco)
print(f'A media do grupo é {media}')
print('~~~~'*10)

mulheres = list()
for s in banco:
   if s['sexo'] == 'f':
    mulheres.append(s['nome'])
print(f'As mulheres cadastradas são', *mulheres)
print('~~~~'*10)

print('Cadastros acima da media: ')
for i in banco:
   if i['idade'] > media:
    print(f'Nome = {i['nome']}; Sexo = {i['sexo']}; Idade = {i['idade']}')
    