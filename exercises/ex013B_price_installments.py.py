produto = float(input('Qual o preço do produto? R$ '))
print ('O valor total do produto a vista fica R${:.2f} e parcelado fica R${:.2f}.'.format(produto-(produto*10/100), produto+(produto*8/100)))
