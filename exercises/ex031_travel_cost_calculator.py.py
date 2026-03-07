km = float(input('Qual a distância da viagem em Km? '))
if km <= 200:
    valor = km * 0.50
else:
    valor = km * 0.45
print ('Sua passagem custa: R${:.2f}'.format(valor))
#OU
print (f'Valor: R${km * 0.50 :.2f}' if km <= 200 else f'Valor: R${km * 0.45 :.2f}')
