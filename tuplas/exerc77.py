palavras = (input('Coloque uma palavra: '))


print('Na palavra', palavras, 'temos as vogais: ')
for letras in palavras:
    if letras.lower() in 'aeiou':
      print(letras)