banco = []
coluna_1 = []
coluna_2 = []
coluna_3 = []

banco.append(coluna_1)
banco.append(coluna_2)
banco.append(coluna_3)

for p_1 in range(0, 3):
 coluna_1.append(int(input(f'Coloque um numero na posição[0][{p_1}]:'))) 
for p_2 in range(0, 3):
 coluna_2.append(int(input(f'Coloque um numero na posição[1][{p_2}]:')))
for p_3 in range(0, 3):
 coluna_3.append(int(input(f'Coloque um numero na posição[2][{p_3}]:')))
  
print('~~~~'*30)
#coluna 1
print(f'[{banco[0][0]}]', end=" ")
print(f'[{banco[0][1]}]', end=" ")
print(f'[{banco[0][2]}]')

#coluna 2
print(f'[{banco[1][0]}]', end=" ")
print(f'[{banco[1][1]}]', end=" ")
print(f'[{banco[1][2]}]')

#coluna 3
print(f'[{banco[2][0]}]', end=" ")
print(f'[{banco[2][1]}]', end=" ")
print(f'[{banco[2][2]}]')
print('~~~~'*30)

soma_par = 0

for coluna in banco:
 for numeros in coluna:
  if numeros % 2 == 0:
   soma_par += numeros
 
  

print(f'A soma dos numeros pares é: {soma_par}')
print('~~~~'*10)

soma_clu3 = coluna_3[0] + coluna_3[1] + coluna_3[2]
print(f'A soma dos numeros da coluna 3 é: {soma_clu3}')
print('~~~~'*10)

print(f'O maior numero da coluna 2 é: {max(coluna_2)}')



    