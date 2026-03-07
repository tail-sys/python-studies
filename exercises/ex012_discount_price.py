preco = float(input('Qual é o preço atual do produto? R$'))
s = preco*0.95
print ('O produto de R${:.2f} com 5% de desconto sai por R${:.2f}.'.format(preco,s))
#ou
print ('O produto de R${:.2f} com 5% de desconto sai por R${:.2f}.'.format(preco, preco*0.95))
#porcentagem ex: 15% de 875 == 875*15/100==131.25
print ('O produto de R${:.2f} com 5% de desconto sai por R${:.2f}.'.format(preco, preco - (preco*5/100)))
