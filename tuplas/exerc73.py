tabela_brasileirao = (
    '', # índice 0 vazio
    "Palmeiras",
    "Flamengo",
    "Cruzeiro",
    "RB Bragantino",
    "Ceará",
    "Bahia",
    "Fluminense",
    "Corinthians",
    "Atlético-MG",
    "Botafogo",
    "São Paulo",
    "Mirassol",
    "Vasco da Gama",
    "Fortaleza",
    "Internacional",
    "Vitória",
    "Grêmio",
    "Juventude",
    "Santos",
    "Sport"
)

print(f'Tabela atualmente: {tabela_brasileirao[1:]}')

print(f'Primeiros 5 colocados: {tabela_brasileirao[1:6]}')

print(f'Os 4 últimos:{tabela_brasileirao[17:21]}')

print(f'Organizado em ordem alfabetica: {sorted(tabela_brasileirao)}')

print(f'O corinthias esta na: {tabela_brasileirao.index("Corinthians")}° posição')


