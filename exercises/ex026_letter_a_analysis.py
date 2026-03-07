phrase = str(input('Digite uma frase: ')).lower().strip().replace(' ','')
print ('A letra "a" aparece {} vezes na frase.'.format(phrase.count('a')))
print ('A primeira ocorrência da letra "a" foi na {} posição.'.format(phrase.find('a')+1))
print ('A última ocorrência da letra "a" foi na {} posição.'.format(phrase.rfind('a')+1))
