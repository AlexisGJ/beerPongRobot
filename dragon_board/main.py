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

motorPin1.dir(mraa.DIR_OUT)
motorPin2.dir(mraa.DIR_OUT)
motorPin3.dir(mraa.DIR_OUT)
motorPin4.dir(mraa.DIR_OUT)

motorPin1.write(0)
motorPin2.write(0)
motorPin3.write(0)
motorPin4.write(0)


while True:
    motorPin1.write(0)
    motorPin2.write(0)
    motorPin3.write(0)
    motorPin4.write(1)

    time.sleep(TIME)
    if TIME > 0.0005:
        TIME = TIME - 0.0005
    motorPin1.write(0)
    motorPin2.write(0)
    motorPin3.write(1)
    motorPin4.write(1)

    time.sleep(TIME)
    if TIME > 0.0005:
        TIME = TIME - 0.0005
    motorPin1.write(0)
    motorPin2.write(0)
    motorPin3.write(1)
    motorPin4.write(0)

    time.sleep(TIME)
    if TIME > 0.0005:
        TIME = TIME - 0.0005
    motorPin1.write(0)
    motorPin2.write(1)
    motorPin3.write(1)
    motorPin4.write(0)

    time.sleep(TIME)
    if TIME > 0.0005:
        TIME = TIME - 0.0005
    motorPin1.write(0)
    motorPin2.write(1)
    motorPin3.write(0)
    motorPin4.write(0)

    time.sleep(TIME)
    if TIME > 0.0005:
        TIME = TIME - 0.0005
    motorPin1.write(1)
    motorPin2.write(1)
    motorPin3.write(0)
    motorPin4.write(0)

    time.sleep(TIME)
    if TIME > 0.0005:
        TIME = TIME - 0.0005
    motorPin1.write(1)
    motorPin2.write(0)
    motorPin3.write(0)
    motorPin4.write(0)

    time.sleep(TIME)
    if TIME > 0.0005:
        TIME = TIME - 0.0005

    motorPin1.write(1)
    motorPin2.write(0)
    motorPin3.write(0)
    motorPin4.write(1)

    time.sleep(TIME)
    if TIME > 0.0005:
        TIME = TIME - 0.0005
