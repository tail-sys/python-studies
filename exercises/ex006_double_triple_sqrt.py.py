n = int(input('Digite um número: '))
m2 = n*2
m3 = n*3
r2 = n**(1/2)
print ('O dobro de {} é {}, o triplo é {}, e a raiz quadrada é {:.2f}'.format(n,m2,m3,r2))
#o resultado da raiz quadrada só pode ter 2 casas decimais {:.2f}
#ou
n2 = int(input('Digite um número: '))
print ('O dobro de {} é {} \nO triplo de {} é {} \nA raiz quadrada de {} é {:.2f}'.format(n2, (n2*2), n2, (n2*3), n2, (n2**(1/2))))
#a raiz/potenciação pode ser escrita assim pow(x,1/2)
print ('A raiz quadrada de {} é {:.2f}'.format(n2, pow(n2,1/2)))

