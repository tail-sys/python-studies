num = int(input('Digite um número: '))
if num % 2 == 0:
    print ('O número {} é PAR.'.format(num))
else:
    print ('O número {} é ÍMPAR.'.format(num))
#simplificado
print (f'{num} é PAR' if num % 2 == 0 else f'{num} ÍMPAR ')
