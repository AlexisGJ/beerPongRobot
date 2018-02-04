import mraa
import time

MOTOR_GPIO_PIN_1 = 23
MOTOR_GPIO_PIN_2 = 24
MOTOR_GPIO_PIN_3 = 25
MOTOR_GPIO_PIN_4 = 26

TIME = 0.05


motorPin1 = mraa.Gpio(MOTOR_GPIO_PIN_1)
motorPin2 = mraa.Gpio(MOTOR_GPIO_PIN_2)
motorPin3 = mraa.Gpio(MOTOR_GPIO_PIN_3)
motorPin4 = mraa.Gpio(MOTOR_GPIO_PIN_4)

def setAngle (angle):
    dutyCycle = (angle + 90) / 180.0 + 1
    if dutyCycle > 1:
        return

    for i in range(0,10):
        motorPin1.write(1)
        time.sleep(dutyCycle/1000.0)
        motorPin1.write(0)
        time.sleep((20-dutyCycle)/1000.0)

    return

setAngle(0)
setAngle(90)
setAngle(-90)
