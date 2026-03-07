metros = float(input('Digite o valor em metros: '))
m100 = metros*100
m1000 = metros*1000
print ('{} metros tem {} centímetro e {} milímetros.'.format(metros,m100,m1000))
#ou
m = float(input('Digite um valor em metros: '))
km = m*0.001
hm = m*0.01
dam = m*0.1
dm = m*10
cm = m*100
mm = m*1000
print ('{:.3f}km'.format(km))
print ('{:.2f}hm'.format(hm))
print ('{:.1f}dam'.format(dam))
print ('{}dm'.format(dm))
print ('{}cm'.format(cm))
print ('{}mm'.format(mm))
