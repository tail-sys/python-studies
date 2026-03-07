velocidade = float(input('Digite a velocidade do carro: '))
print ('A velocidade do carro foi {}.'.format(velocidade))
if velocidade > 80:
    print ('Você foi multado! Valor da multa: R${:.2f}'.format((velocidade-80)*7))
else:
    print ('Tenha um bom dia! Siga com segurança!')
