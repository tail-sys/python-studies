#tem que tranformar o valor do ângulo em radianos primeiro
#sin cos e tan só trabalham com radianos
from math import sin,cos,tan,radians
ang = float(input('Digite um ângulo: '))
rad = radians(ang)
s = sin(rad)
c = cos(rad)
t = tan(rad)
print ('O ângulo {} tem seno {:.2f}, cosseno {:.2f}, tangente {:.2f}.'.format(ang, s, c, t))
#ou
ang2 = float(input('Digite um ângulo: '))
seno = sin(radians(ang2))
cosseno = cos(radians(ang2))
tangente = tan(radians(ang2))
print ('SENO: {:.2f}; COSSENO: {:.2f}; TANGENTE: {:.2f}.'.format(seno, cosseno, tangente))
