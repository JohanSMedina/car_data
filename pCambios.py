##################
# Prueba cambios #
##################
import random
from dataBase import changeGear
from time import sleep

cambio = 0

while True:
    cambio = random.randint(0, 7)+1
    changeGear(cambio)
    sleep(2)