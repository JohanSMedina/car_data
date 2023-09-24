from dataBase import readData
from time import sleep

while True:
    data = readData()
    cambio = data[1]
    velocidad = data[2]
    distancia = data[3]
    rpmRueda = data[4]
    rpmMotor = data[5]
    voltaje = data[6]
    corriente = data[7]
    print("Cambio:\t\t", cambio)
    print("Velocidad:\t", velocidad)
    print("Distancia:\t", distancia)
    print("RPM Rueda:\t", rpmRueda)
    print("RPM Motor:\t", rpmMotor)
    print("Voltaje:\t", voltaje)
    print("Corriente:\t", corriente)
    print("---------------------------------------")
    #sleep(1)