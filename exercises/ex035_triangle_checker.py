ra = float(input('Valor da primeira reta: '))
rb = float(input('Valor da segunda reta: '))
rc = float(input('Valor da terceira reta: '))
if ra < rb + rc and rb < ra + rc and rc < ra + rb:
    print('Essas retas formam um triângulo!')
else:
    print('Essas retas não formam um triângulo!')
# quando 3 retas formam um triângulo?
# a soma de 2 retas tem que ser > que o 1 reta (a < b + c)
# se a soma de b + c = a não tem mais triângulo
# se b + c < a também não tem triângulo
# ou seja a < b + c, b < a + c, c < a + b
