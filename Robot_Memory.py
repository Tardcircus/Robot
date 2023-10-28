import Robot_ChatGPT
import Robot_Movment
import Robot_Sounds
import Robot_Questions

from time import sleep

line = print("")

def wakeup():
    global wake
    wake = False

    # Check wake word
    if words[0] == "shitbox":
        wake = True
        print("-Wake word found")
    else:
        pass

# Vocabulary
def commands():
    GPT = True
    for word in words:

        # Robot_Movment.py
        if word == "move" or word == "turn":
            Robot_Movment.move_command(words)
            GPT = False
        if word == "claw" or word == "arm":
            Robot_Movment.arm_command(words)
            GPT = False
        if word == "go away" or word == "cruise" or word =="patrol":

            Robot_Movment.Auto_Pilot(word)
        if word == "do you know":
            Robot_Questions.Robot_Knows(user_input)
            
            
    # Robot_ChatGPT.py
    if GPT == True:
        Robot_ChatGPT.Send_to_GPT(user_input)

# Main function
def main():
    global user_input
    global words
    while True:
        print("")
        user_input = input("Give shitbox a command: ")
        print("")
        # Split user input
        words = user_input.split()        
        wakeup()
        if wake:
            commands()
            

main()

