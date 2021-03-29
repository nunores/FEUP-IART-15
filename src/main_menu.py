import sys
from enum import Enum

sys.tracebacklimit=0

def main_menu():
    game_type = "N/A"
    current_difficulty = "Medium"

    while(True):
        print("\n\n\n\n\n\n\n\n\n\n")
        print("Current Difficulty: " + current_difficulty)
        print("[1] Play")
        print("[2] Choose Difficulty")
        print("[3] Exit")
        try:
            option1 = int(input("Choose the destination: "))
            if(option1 == 1):
                game_type = choose_type()
                if(game_type == "back"):
                    continue
                # TODO Chamar outros game modes
            elif(option1 == 2):
                current_difficulty = difficulty()
                if(current_difficulty == "back")
                    continue
                # TODO Chamar outros difficulties 
            elif(option1 == 3):
                return
            
        except ValueError:
            print("Input not valid, try again...")
    
    
def choose_type():
    print("\n\n\n\n\n\n\n\n\n\n")
        
    print("[0] Go Back")
    print("[1] Human vs Human")
    print("[2] Human vs PC")
    print("[3] PC vs PC")

    try:
        option1 = int(input("Choose the destination: "))
        if(option1 == 0):
            return "back"
        elif(option1 == 1):
            return "hvh"
        elif(option1 == 2): 
            return "hvb"
        elif(option1 == 3): 
            return "bvb"    
            
    except ValueError:
        print("Input not valid, try again...")


def difficulty():
    while(True):
        print("\n\n\n\n\n\n\n\n\n\n")
        print("Choose difficulty")
        print("[0] Go Back")
        print("[1] Easy")
        print("[2] Medium")
        print("[3] Hard")
        try:
            option2 = int(input("Choose the destination: "))
            if(option2 == 0):
                return "back"
            elif(option2 == 1):
                return "Easy"
            elif(option2 == 2):
                return "Medium"
            elif(option2 ==3):
                return "Hard"
        except ValueError:
            print("\n\n\n Input not valid, try again...")

# main_menu()