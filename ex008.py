metro = float(input('Entre um valor em metros?: '))
km = metro / 100
hm = metro / 1000
dm = metro * 10
cm = metro * 1000
mm = cm * 10

print('A medida de {}m corresponde a : \n Que vale: {}km \n {}hm \n {:.0f}dm,\n {:.0f}cm, \n {:.0f}mm'.format(metro,km,hm,dm,cm,mm))
