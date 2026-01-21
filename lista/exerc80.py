lista = list()
for c in range(5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        #vai para o final da lista
    else:
        verifica = 0
        while verifica < len(lista):
            if n <= lista[verifica]:
                lista.insert(verifica, n)
                break
            verifica += 1
print(lista)