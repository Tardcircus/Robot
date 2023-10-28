import Robot_Talk as RT

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


# Move commands for robot
def move_command(words):
    print("--Move command found")
    for word in words:

        if word == "left":
            print("---Robot turns 90 degrees left")
            RT.TTS("Im Turning left")
            PWM.setMotorModel(-2000,2000)       #Left 
            time.sleep(1)
            PWM.setMotorModel(0,0)              #Stop
        
        elif word == "right":
            print("----Robot turns 90 degrees right")
            RT.TTS("Im turning right")
            PWM.setMotorModel(2000,-2000)       #Left 
            time.sleep(1)
            PWM.setMotorModel(0,0)              #Stop

        elif word == "forward":
            print("----Robot travels forward")
            RT.TTS("ill go forward i guess")
            PWM.setMotorModel(2000,2000)
            time.sleep(1)
            PWM.setMotorModel(0,0)              #Stop

        elif word == "backwards":
            print("----Robot moved backwards")
            RT.TTS("Ill go backwards")
            PWM.setMotorModel(-2000,-2000)       #Left 
            time.sleep(1)
            PWM.setMotorModel(0,0)              #Stop

        elif word == "stop":
            print("----Robot moved backwards")
            RT.TTS("Stop what?")
            PWM.setMotorModel(0,0)       #Left 
            time.sleep(1)
            PWM.setMotorModel(0,0)              #Stop
            # Program MUST mutithread and exit when new command is recieved

# Move the arm and claw
def arm_command(words):
    badcom = True
    print("--arm/claw command found")
    for word in words:
        if word == "claw":
            print("---Claw command found")
            for word in words:
                if word == "open":
                    print("----Open Claw")
                    badcom = False
                if word == "close":
                    print("----Close Claw")
                    badcom = False
            if badcom:    
                print("Claw command not found. Try: close claw or open claw")

        if word == "arm":
            print("---arm command found")
            for word in words:
                if word == "up" or word =="lift":
                    print("----lift arm up")
                    badcom = False
                if word == "lower" or word == "down":
                    print("----lower arm down")
                    badcom = False
            if badcom:
                print("arm command not found. try: Lift arm up or lift arm down")

def Auto_Pilot(var):
    print("Robot Spin 90 degrees random")
    if var == "patrol":
        print("Roger that seek and destroy children")
    if var == "go away":
        print("Fine i knwo wwhen im not wanted")
    if var == "cruise":
        # PLay low rider song in multithread 
        print(" helll yea")
    print("Robot Move about while using sensors and scripts")