from num2words import num2words

#numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

entrada = int(input('coloque um numero de 0 a 20: '))

if entrada < 0 or entrada > 20:
    print('Coloque de 0 a 20')
else:
  print(num2words(entrada, lang='pt_BR'))
