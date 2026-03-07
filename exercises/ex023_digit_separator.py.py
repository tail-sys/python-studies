num = str(input('Digite um número inteiro com 4 digitos: '))
print ('Unidade: {}'.format(num[-1]))
print ('Dezena: {}'.format(num[-2]))
print ('Centena: {}'.format(num[-3]))
print ('Milhar: {}'.format(num[-4]))
#ou
num3 = int(input('Digite um número inteiro com 4 digitos: '))
n = str(num3)
print ('Analisando o número {}'.format(num3))
print ('Unidade: {}'.format(n[3]))
print ('Dezena: {}'.format(n[2]))
print ('Centena: {}'.format (n[1]))
print ('Milhar: {}'.format (n[0]))
#ou numérico
num2 = int(input('Digite um número de 0 a 9999: '))
print ('Unidade: {}'.format(num2%10))
print ('Dezena: {}'.format((num2//10)%10))
print ('Centena: {}'.format((num2//100)%10))
print ('Milhar: {}'.format((num2//1000)%10))
#ou ***melhor
num4 = int(input('Digite um número: '))
u = num4 // 1 % 10
d = num4 // 10 % 10
c = num4 // 100 % 10
m = num4 // 1000 % 10
print ('Analisando o número {}'.format(num4))
print ('Unidade: {}'.format(u))
print ('Dezena: {}'.format(d))
print ('Centena: {}'.format(c))
print ('Milhar: {}'.format(m))