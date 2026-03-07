#Teorema de Pitágoras (a²+b²=c²) no python (a**2+b**2)**(1/2)
from math import hypot
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = hypot (co, ca)
print ('A medida da hipotenusa de {} + {} é {:.2f}.'.format(co, ca, hi))
#ou matemática
co2 = float(input('Comprimento do cateto oposto: '))
ca2 = float(input('Comprimento do cateto adjacente: '))
hi2 = (co2 ** 2 + ca2 ** 2) ** (1/2)
print('A hipotenusa vai medir {:.2f}:'.format(hi2))
