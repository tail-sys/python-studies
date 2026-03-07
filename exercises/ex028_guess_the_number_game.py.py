from random import choice,randint
from time import sleep
print ('-o-' * 14)
print ('Vou pensar em um número, tente acertar!')
print ('-o-' * 14)
escolhido = int(input('Digite um número de 0 até 5: '))
print ('PROCESSANDO...')
sleep(3)
numeros = [0, 1, 2, 3, 4, 5]
escolha = choice(numeros)
print ('Eu escolhi {}.'.format(escolha))
if escolha == escolhido:
    print ('Você venceu! PARABÉNS!!! :D')
else:
    print ('Você perdeu... :(')
#ou
print ('Vou pensar em um número, tente acertar!')
escolhido1 = int(input('Digite um número de 0 até 5: '))
escolha1 = randint(0,5)
if escolha1 == escolhido1:
    print('Parabéns, você venceu!!! :D')
else:
    print('Você errou... :(')
print ('O número esolhido era {}!'.format(escolha1))
#ou simplificado
print ('Venceu! :D' if escolha1 == escolhido1 else 'Perdeu! :(')