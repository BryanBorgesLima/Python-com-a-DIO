from random import randint
from operator import itemgetter
jogadores = {'jogaor1': randint(1, 6), ''
             'jogaor2': randint(1, 6), 
             'jogaor3': randint(1, 6), 
             'jogaor4': randint(1, 6) }
for k, v in jogadores.items():
    print(f'O {k} tirou {v}')

ranking = list()
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
print(ranking)