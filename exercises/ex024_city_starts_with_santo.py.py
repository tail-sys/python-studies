city = str(input('Digite o nome de uma cidade: ')).strip()
print ('Sua cidade começa com nome "Santo"? {}.'.format(city[:5].lower() == 'santo'))