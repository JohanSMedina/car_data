import sqlite3 as sql

def createDB():
    conection = sql.connect("VTE.db")
    conection.commit()
    conection.close()

def createTable():
    conection = sql.connect("VTE.db")
    cursor = conection.cursor()
    cursor.execute(
        """CREATE TABLE valoresActuales(
            id INTEGER PRIMARY KEY,
            cambio INTEGER,
            velocidad FLOAT,
            distancia FLOAT,
            rpmRueda FLOAT,
            rpmMotor FLOAT,
            voltaje FLOAT,
            corriente FLOAT
        )"""
    )
    conection.commit()
    conection.close()

def createTable1():
    conection = sql.connect("VTE.db")
    cursor = conection.cursor()
    cursor.execute(
        """CREATE TABLE allData(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cambio INTEGER,
            velocidad FLOAT,
            distancia FLOAT,
            rpmRueda FLOAT,
            rpmMotor FLOAT,
            voltaje FLOAT,
            corriente FLOAT,
            fecha_hora TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )"""
    )
    conection.commit()
    conection.close()

def firstData(id, cambio, velocidad, distancia, rpmRueda, rpmMotor, voltaje, corriente):
    conection = sql.connect("VTE.db")
    cursor = conection.cursor()
    instruction = f"INSERT INTO valoresActuales VALUES ({id}, {cambio}, {velocidad}, {distancia}, {rpmRueda}, {rpmMotor}, {voltaje}, {corriente})"
    cursor.execute(instruction)
    conection.commit()
    conection.close()

def readData():
    conection = sql.connect("VTE.db")
    cursor = conection.cursor()
    instruction = f"SELECT * FROM valoresActuales"
    cursor.execute(instruction)
    datos = cursor.fetchall()
    conection.commit()
    conection.close()
    return(datos[0])

def changeGear(cambio):
    conection = sql.connect("VTE.db")
    cursor = conection.cursor()
    instruction = f"UPDATE valoresActuales SET cambio={cambio}  WHERE id = 0"
    cursor.execute(instruction)
    conection.commit()
    conection.close()
    pass

def changeOdometry(km_per_hour, rpm, dist_meas):
    conection = sql.connect("VTE.db")
    cursor = conection.cursor()
    instruction = f"UPDATE valoresActuales SET velocidad={km_per_hour}, distancia={dist_meas}, rpmRueda={rpm} WHERE id = 0"
    cursor.execute(instruction)
    conection.commit()
    conection.close()

def insertAllData(cambio, velocidad, distancia, rpmRueda, rpmMotor, voltaje, corriente):
    try:
        conection = sql.connect("VTE.db")
        cursor = conection.cursor()
        cursor.execute(
            "INSERT INTO allData (cambio, velocidad, distancia, rpmRueda, rpmMotor, voltaje, corriente) VALUES (?, ?, ?, ?, ?, ?, ?)",
            (cambio, velocidad, distancia, rpmRueda, rpmMotor, voltaje, corriente)
        )
        conection.commit()
        conection.close()
    except sql.Error as e:
        pass
    

if __name__=="__main__":
    createDB()
    createTable()
    createTable1()
    firstData(0,1,0.0,0.0,0.0,0.0,0.0,0.0)
    pass