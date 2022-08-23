import time as tm


hora_actual = tm.strftime('%H:%M:%S')
hora_salida = ('19:00:00','%H:%M:%S')
hora = tm.strftime('%H') 
minuto = tm.strftime('%M')
segundo = tm.strftime('%S')



if hora_actual >= hora_salida[0]:
	print ("Es hora de irse a casa") 
else:
	print ("Te quedan {} hours, {} minutes y {} segundos para irte a casa".format(18-int(hour), 59-int(minute), 59-int(second)))
