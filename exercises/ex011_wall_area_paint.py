altura = float(input('Qual a altura da parede? '))
largura = float(input('Qual a largura da parede? '))
area = altura*largura
tinta = area/2
print ('Sua parede tem {:.2f}m², você precisa de {:.2f}l de tinta.'.format(area,tinta))
#ou com menos variaveis
print ('Sua parede tem {:.2f}m², você precisa de {:.2f}l de tinta.'. format(altura*largura,(altura*largura)/2))
