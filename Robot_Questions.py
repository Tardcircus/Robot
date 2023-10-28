
def Robot_Knows(var):
    user_input = var
    words = user_input.split
    print("Robot KNows Function in Robot_Questions Module")
    for word in words:
        if word == "joke":
            Joke()

def Joke():
    print("Joke")