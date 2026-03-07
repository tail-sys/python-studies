cel = float(input('Informe a temperatura em ºC: '))
print ('A temperatura de {:.1f}ºC corresponde a {:.1f}ºF.'.format(cel,cel*1.8+32))
#calculo fahrenheit ºC*1.8+32 ou 9*ºC/5+32 (já estão na ordem de precedência)
#ou
print ('A temperatura de {:.1f}ºC corresponde a {:.1f}ºF.'.format(cel,9*cel/5+32))
