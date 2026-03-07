from math import trunc
num = float(input('Digite um número inteiro: '))
print ('O número {} e a sua porção inteira é {}.'.format(num, trunc(num)))
#ou :.0f (não é válido se for usar o valor depois)
num2 = float(input('Digite um valor: '))
print ('O valor digitado foi {} e a sua porção inteira é {:.0f}.'.format(num2, num2))
#ou int
num3 = float(input('Digite um valor: '))
print ('O valor digitado foi {} e a sua porção inteira é {}.'.format(num3, int(num3)))
