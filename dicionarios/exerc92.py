dados = {}
dados['Nome'] = input('Nome: ')
dados['idade'] = int(input('Ano de nascimento: '))
idade = 2026 - dados['idade']
dados['idade'] = idade
dados['Ctps'] = int(input('Carteira de trabalho (0 não tem): '))

if dados['Ctps'] != 0:
    dados['Contratação'] = int(input("Seu ano de contratação: "))
    dados['Salario'] = float(input('Seu salario: '))
    dados['Aposentadoria'] = ''
    aposentadoria = 2026 - dados['Contratação'] - 35 + dados['idade']
    dados['Aposentadoria'] = aposentadoria
    print('~~~~~~'*20)
    print(dados)

    for k, v in dados.items():
        print(f'{k} tem valor {v}')
else:
    print('~~~~~~'*20)
    for k, v in dados.items():
        print(f'O valor de {k} é {v}')