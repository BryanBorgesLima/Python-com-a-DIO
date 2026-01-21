nuemros = []
lista_par = []
lista_impar = []

while True:
    nuemros.append(int(input("Coloque um numero: ")))   
    afirm = input('Quer colocar mais? [S/N]')
    if afirm != 's':
        break
for par in nuemros:
    if par % 2 == 0:
        lista_par.append(par)
for impar in nuemros:
    if impar % 2 != 0:
        lista_impar.append(impar)     

nuemros.sort()
lista_impar.sort()
lista_par.sort()

print(f'A primeira lista é {nuemros}\n')
print(f'A lista impar é {lista_impar}\n')
print(f'A lista par é {lista_par}\n')
