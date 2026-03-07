salario = float(input('Qual o seu salário? R$'))
if salario > 1250:
    print ('Seu salário aumentou 10%, ficando R${:.2f}.'.format(salario*1.10))
else:
    print ('Seu salário aumentou 15%, ficando R${:.2f}'.format(salario*1.15))
#
#ou
salario2 = float(input('Qual é o seu salário? '))
if salario2 <=1250:
    novo = salario2 + (salario2 * 15 / 100)
else:
    novo = salario2 + (salario2 * 10 / 100)
print ('Seu salário agora será de R${:.2f}'.format(novo))
