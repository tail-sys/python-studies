salario = float(input('Qual o seu salário atual? R$'))
s = salario*1.15
print ('Seu salário atual é R${:.2f}, e com 15% de aumento fica R${:.2f}.'.format(salario,s))
#ou menos variaveis
#porcentagem ex salário+(20*25/100==5)==25
print ('Seu salário atual é R${:.2f}, e com 15% de aumento fica R${:.2f}.'.format(salario, salario+(salario*15/100)))
