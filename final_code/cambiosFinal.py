import RPi.GPIO as GPIO
import time
import pigpio

# Configuración de pines GPIO
BUTTON_PIN_ADD = 23
BUTTON_PIN_SUBTRACT = 24
SERVO_PIN = 12

# Configuración de GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_PIN_ADD, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(BUTTON_PIN_SUBTRACT, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Configuración de pigpio
pi = pigpio.pi()

# Configuración de PWM para el servomotor FT6335M
SERVO_PWM_FREQ = 50  # Frecuencia en Hz para el pulso PWM
SERVO_PWM_RANGE = 2000  # Rango para el pulso PWM (microsegundos)
pi.set_PWM_frequency(SERVO_PIN, SERVO_PWM_FREQ)
pi.set_PWM_range(SERVO_PIN, SERVO_PWM_RANGE)


# Función para mover el servo a un ángulo específico
def set_servo_angle(angle):
    duty_cycle = (angle / 360.0) * SERVO_PWM_RANGE
    pi.set_servo_pulsewidth(SERVO_PIN, duty_cycle)
    global current_angle
    current_angle = angle

vecCambios = [266,251,242,232,224,217,209,202]
posVec = 0
set_servo_angle(vecCambios[posVec])
print("El cambio actual es: " + str((posVec+1)) + " El angulo actual es: ", vecCambios[posVec])


while True:
    button_add_state = GPIO.input(BUTTON_PIN_ADD)
    button_subtract_state = GPIO.input(BUTTON_PIN_SUBTRACT)
        

    if (button_add_state == GPIO.LOW) and (posVec < 7):
        posVec += 1
        set_servo_angle(vecCambios[posVec])
        print("El cambio actual es: " + str((posVec+1)) + " El angulo actual es: ", vecCambios[posVec])
        time.sleep(0.3)  # Pequeña pausa para evitar rebotes

    if (button_subtract_state == GPIO.LOW) and (posVec > 0):
        posVec -= 1
        set_servo_angle(vecCambios[posVec])
        print("El cambio actual es: " + str((posVec+1)) + " El angulo actual es: ", vecCambios[posVec])
        time.sleep(0.3)  # Pequeña pausa para evitar rebotes
        


# Limpiar configuraciones al finalizar
pi.stop()
GPIO.cleanup()