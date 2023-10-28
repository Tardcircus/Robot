import RPi.GPIO as GPIO
import time
from Motor import *
from servo import *
from Ultrasonic import *
from Action import *
from Line_Tracking import *
from time import sleep

PWM=Motor()
servo=Servo() 
ultrasonic=Ultrasonic() 

def WakeUp():
    servo.setServoPwm('0',150)
    servo.setServoPwm('1',90)   

def test_Motor():

    PWM.setMotorModel(2000,2000)       #Forward
    sleep(3)

    PWM.setMotorModel(2000,-2000)
    sleep(2)

    PWM.setMotorModel(2000,2000)
    sleep(3)

    PWM.setMotorModel(0,0)

def Road_Ultrasonic():
    global Road
    data=ultrasonic.get_distance()   #Get the value
    distance=int(data)
    InRoad = str(distance)
    if InRoad <= '12':
        Road = "Blocked"
    else:
        Road = "Clear"

def Cruise():
    while True:
        Road_Ultrasonic()
        if Road == "Clear":
            PWM.setMotorModel(2000,2000)
            sleep(0.1)
        elif Road == "Blocked":
            PWM.setMotorModel(2000,-2000)
            sleep(1)





WakeUp()
test_Motor()