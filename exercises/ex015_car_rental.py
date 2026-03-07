dias = int(input('Por quantos dias o carro foi alugado? '))
km = float(input('Quantos Km o carro rodou? '))
d = dias*60
k = km*0.15
total = d+k
print ('Você ficou com o carro por {} dias, rodou {:.1f}km, deve pagar R${:.2f}.'.format(dias, km, total))
#ou
print ('Você ficou com o carro por {} dias, rodou {:.1f}km, deve pagar R${:.2f}.'.format(dias, km, (dias*60)+(km*0.15)))
