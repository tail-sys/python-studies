n1 = float(input('Quantos R$ você tem? R$'))
n2 = float(input('Quanto está o US$ hoje? US$'))
s = n1/n2
print ('Você pode comprar US${:.2f} com R${:.2f}.'.format(s,n1))
#ou
n3 = float(input('Quantos R$ você tem? R$'))
n4 = float(input('Quanto está o US$ hoje? US$'))
print ('Você pode comprar US${:.2f} com R${:.2f}.'.format(n3/n4, n3))
