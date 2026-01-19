numeros = list()

while True:
   escolhido = int(input('Coloque um numero: '))
   if escolhido in numeros:
      print("Este numero ja esta na lista")
   else:
      numeros.append(escolhido)
   afirmação = input('Deseja continuar? S/N: ').lower()
   if afirmação != 's':
      break

numeros.sort()
print(numeros)
