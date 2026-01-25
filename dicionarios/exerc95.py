elenco = list()
while True:
    jogadores = dict()
    jogadores['nome'] = input('Coloque seu nome: ')
    aux = int(input(f'Quantas partidas {jogadores["nome"]} jogou? '))
    gols = []
    soma_gols = 0
    for partidas in range(aux):
        gols.append(int(input(f'Quantos gols na partida {partidas}? ')))
        jogadores['gols'] = gols[:]
    soma_gols += sum(gols)
    jogadores['total'] = soma_gols
    elenco.append(jogadores.copy())
    
    afirm = input('Quer continuar? [S/N]')
    print('---'*10)
    if afirm != 's':
        break
print('cod nome', end='  ')
print('gols', end='  ')
print('total')
print('---'*10)

for posição, jogador in enumerate(elenco):
    print(f'{posição} {jogador['nome']} {jogador['gols']} {jogador['total']}')

while True:
    print('---'*10)
    opc = int(input('Quer ver os dados de qual jogador? '))
    if opc <= len(elenco) - 1:
        print(f'O jogador {elenco[opc]['nome']}: ')
        for p, g in enumerate(elenco[opc]['gols']):
            print(f'Na partida {p} ele marcou {g}')
    if opc == 999:
        print('OBRIGADO')
        break
    if opc > len(elenco):
        print('Não tem esse jogador')
  