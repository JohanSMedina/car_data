####################
# Prueba Odometria #
####################
import random
from dataBase import changeOdometry, readData
from time import sleep

km_per_hour = 0.0
rpm = 0.0
dist_meas = 0.0

while True:
    km_per_hour = random.uniform(0, 65)
    rpm = random.uniform(0, 720)
    dist_meas = random.uniform(0, 2000)
    changeOdometry(f"{km_per_hour:.3f}",f"{rpm:.3f}" ,f"{dist_meas:.3f}")
    #print(readData())
    sleep(0.02)