dados = {'nome': 'Bryan', 'idade': 32 }
print(dados['nome'], end=" ")
print(dados['idade'])
dados['sexo'] = 'Masculino'
print(dados['sexo'])
print(dados.keys())
print(dados.values())
print(dados.items())
for k in dados.items():
    print(f'O {k} é')

locadora = [{'titulo': 'star wars', 'ano': 1977}, {'titulo': 'Taxi drave', 'ano': 2002}]

print(f"O {dados["nome"]} tem {dados['idade']} anos")