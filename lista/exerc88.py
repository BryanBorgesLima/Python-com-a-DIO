import random
teste = int(input('Coloque um numero: '))
banco = []
for i in range(0, teste):
  jogos = []
  numeros = random.sample(range(1, 61), 6)
  jogos.append(numeros)
  banco.append(jogos)

numeros.sort()
quant_jogos = 0
for passando in banco:
 quant_jogos += 1
 for numeros in passando:
   print(f'Jogo {quant_jogos}:', *numeros)
   print('----' *5)





