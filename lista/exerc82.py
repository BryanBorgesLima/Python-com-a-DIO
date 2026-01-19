nuemros = []
tupla_par = []
tupla_impar = []

while True:
    nuemros.append(int(input("Coloque um numero: ")))   
    afirm = input('Quer colocar mais? [S/N]')
    if afirm != 's':
        break
for par in nuemros:
    if par % 2 == 0:
        tupla_par.append(par)
for impar in nuemros:
    if impar % 2 != 0:
        tupla_impar.append(impar)     

nuemros.sort()
tupla_impar.sort()
tupla_par.sort()

print(f'A primeira tupla é {nuemros}\n')
print(f'A tupla impar é {tupla_impar}\n')
print(f'A tupla par é {tupla_par}\n')
