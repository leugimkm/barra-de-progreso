import sys
from time import sleep

def progreso(items,total,ancho=20):
	barra_full = int(round(ancho*items/float(total)))
	porcentaje = round(100*items/float(total),1)
	barra = '='*barra_full + '-'*(ancho-barra_full)
	sys.stdout.write(f'\rProgreso: [{barra}] {porcentaje:.0f}% Completado\r')
	sys.stdout.flush()

def test():
    procesos = 50
    for i in range(1,procesos+1):
        progreso(i,procesos)
        sleep(0.15)
    sys.stdout.write('\n')
    print('Fin')

test()