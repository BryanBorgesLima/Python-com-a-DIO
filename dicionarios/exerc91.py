import random
jogadores = {'jogaor1': '', 'jogaor2': '', 'jogaor3': '', 'jogaor4': '' }

for chave in jogadores:
    jogadores[chave] = random.sample(range(1, 7), 1)
for k, v in jogadores.items():
    print(f'O {k} tirou', *v)
'''''
ordena = dict(
    sorted(jogadores.items(), key=lambda item: item[1], reverse=True)
)
'''

