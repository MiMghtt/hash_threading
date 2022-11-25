
from threading import Thread
import time

def carro(velocidade, piloto):
    trajeto = 0
    while trajeto <= 100:
        trajeto+=velocidade
        time.sleep(0.75)
        print('Piloto: {} Km {}:'.format(piloto,  trajeto))


t_carro1 = Thread(target=carro, args=[1, 'Michel' ])
t_carro2 = Thread(target=carro, args=[1.5, 'Maria'])

t_carro1.start()
t_carro2.start()