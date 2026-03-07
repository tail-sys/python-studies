name = str(input('Digite seu nome completo: '))
print ('Em maiúsculas: {}'.format(name.upper()))
print ('Em minúsculas: {}'.format(name.lower()))
print ('Seu nome completo tem {} letras.'.format(len(name.replace(' ',''))))
print ('Seu primeiro nome tem {} letras.'. format(len(name.split()[0])))
#ou
name2 = str(input('Digite seu nome completo: ')).strip()
print ('Em maiúsculas: {}'.format(name2.upper()))
print ('Em minúsculas: {}'.format(name2.lower()))
print ('Seu nome completo tem {} letras.'.format(len(name2) - name2.count(' ')))
print ('Seu primeiro nome tem {} letras.'.format(name2.find(' ')))
#ou
separa = name2.split()
print ('Seu primeiro nome é {} e ele tem {} letras.'.format(separa[0], len(separa[0])))
