jogador = dict()
jogador['nome'] = input('Nome do jogador: ')
aux = int(input('Quantas partidas jogadas: '))
gols = list()
soma_gols = 0

for partida in range(aux):
    gols.append(int(input(f'Quantos gols na partida {partida}? ')))
    jogador['gols'] = gols[:]
soma_gols += sum(gols)
jogador['total'] = soma_gols

print(jogador)
print('~~~~'*10)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor: {v}')
print('~~~~'*10)

print(f'O jogador {jogador['nome']} jogou {aux} partidas')
for p, g in enumerate(jogador['gols']):
    print(f'Na partida {p} ele marcou {g} gols')
print(f'Foi um total de {jogador["total"]} gols')