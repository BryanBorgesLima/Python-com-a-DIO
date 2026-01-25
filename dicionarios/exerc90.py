dados = dict()
dados['nome'] = input('Qual o nome do aluno: ')
dados['media'] = float(input(f'Qual a media de {dados["nome"]}: '))
dados['situação'] = " "

if dados['media'] > 7:
    dados['situação'] = 'Aprovado'
else:
    dados['situação'] = 'Reprovado'

for k, v in dados.items():
    print(f'O {k} é {v}')