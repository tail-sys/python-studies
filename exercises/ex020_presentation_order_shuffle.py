#shuffle embaralha a lista, conta a partir de 0
from random import shuffle
n1 = input('Primeiro nome: ')
n2 = input('Segundo nome: ')
n3 = input('Terceiro nome: ')
n4 = input('Quarto nome: ')
lista = [n1, n2, n3, n4]
shuffle(lista)
print ('A ordem de apresentação será:')
print (lista)
#ou
print ('Ordem de apresentação:')
print ('1º', lista[0])
print ('2º', lista[1])
print ('3º', lista[2])
print ('4º', lista[3])
#ou
print ('Ordem de apresentação:')
print ('1º - {}, 2º - {}, 3º - {}, 4º - {}.'.format(lista[0],lista[1],lista[2],lista[3]))
