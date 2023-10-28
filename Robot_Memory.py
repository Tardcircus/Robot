import Robot_ChatGPT
import Robot_Movment
import Robot_Sounds
import Robot_Questions
import Robot_Talk

from time import sleep

line = print("")

def wakeup():
    global wake
    wake = False

    # Check wake word
    if words[0] == "shitbox" or words[0] == "jukebox" or words[0] == "Showbox":
        wake = True
        print("-Wake word found")
    else:
        pass

# Vocabulary
def commands():
    GPT = True
    for word in words:

        # Robot_Movment.py
        if word == "move" or word == "turn" or word == "stop":
            Robot_Movment.move_command(words)
            GPT = False
        if word == "claw" or word == "arm":
            Robot_Movment.arm_command(words)
            GPT = False
        if word == "go away" or word == "cruise" or word =="patrol":

            Robot_Movment.Auto_Pilot(word)
            GPT = False

        if word == "do you know":
            Robot_Questions.Robot_Knows(user_input)
            GPT = False

        if word == "kids":
            print(user_input)
            Robot_Talk.playsound("deadly.mp3")
            GPT = False
            
            
    # Robot_ChatGPT.py
    if GPT == True:
        Robot_ChatGPT.Send_to_GPT(user_input)

# Main function
def main():
    global user_input
    global words
    while True:
        print("")
        Robot_Talk.listen_to_microphone()
        #user_input = input("Give shitbox a command: ")
        # Split user input
        user_input = Robot_Talk.user_input
        print(user_input)
        words = user_input.split()        
        wakeup()
        if wake:
            commands()
            

main()

