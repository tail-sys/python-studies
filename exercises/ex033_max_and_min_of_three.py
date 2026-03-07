num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceido número: '))
# verificando quem é maior:
if num1 >= num2 and num1 >= num3:
    print ('O número {} é maior que {} e {}'.format(num1, num2, num3))
if num2 >= num1 and num2 >= num3:
    print ('O número {} é maior que {} e {}'.format(num2, num1, num3))
if num3 >= num1 and num3 >= num2:
    print ('O número {} é maior que {} e {}'.format(num3, num1, num2))
# verificando quem é menor:
if num1 <= num2 and num1 <= num3:
    print ('O número {} é menor que {} e {}'.format(num1, num2, num3))
if num2 <= num1 and num2 <= num3:
    print ('O número {} é menor que {} e {}'.format(num2, num1, num3))
if num3 <= num1 and num3 <= num2:
    print ('O número {} é menor que {} e {}'.format(num3, num1, num2))
#
#ou
print (f'Maior: {max(num1, num2, num3):.0f}')
print (f'Menor: {min(num1, num2, num3):.0f}')
#
#ou
a = int(input('Digite o primeiro valor: '))
b = int(input('Digite o segundo valor: '))
c = int(input('Digite o terceiro valor: '))
#verificando menor:
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
#verificando maior:
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print (f'O maior número é {maior} e o menor número é {menor}')
