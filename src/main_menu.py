import sys
sys.tracebacklimit=0



def main_menu():
    global main_menu_state 
    main_menu_state = True
    current_difficulty = "Medium"
    game_type = 0

    while(main_menu_state):
        print("\n\n\n\n\n\n\n\n\n\n")
        print("Current Difficulty: " + current_difficulty)
        print("[1] Play")
        print("[2] Choose Difficulty")
        print("[3] Exit")
        try:
            option1 = int(input("Choose the destination: "))
            if(option1 == 1):
                choose_type()
                main_menu_state = False
            elif(option1 == 2):
                current_difficulty = difficulty()
            elif(option1 == 3):
                exit()
            
        except ValueError:
            print("Input not valid, try again...")
    
    
def choose_type():
    print("\n\n\n\n\n\n\n\n\n\n")
        
    print("[1] Human vs Human")
    print("[2] Human vs PC")
    print("[3] PC vs PC")
    try:
        option1 = int(input("Choose the destination: "))
        if(option1 == 1):
            return 1
        elif(option1 == 2): 
            return 2
        elif(option1 == 3): 
            return 3
        
            
    except ValueError:
        print("Input not valid, try again...")


def difficulty():
    difficulty_menu = True

    while(difficulty_menu):
        print("\n\n\n\n\n\n\n\n\n\n")
        print("Choose difficulty")
        print("[1] Easy")
        print("[2] Medium")
        print("[3] Hard")
        print("[4] Exit")
        try:
            option2 = int(input("Choose the destination: "))
            if(option2 == 1):
                return "Easy"
            elif(option2 == 2):
                return "Medium"
            elif(option2 ==3):
                return "Hard"
            elif(option2 == 4):
                exit()
            difficulty_menu = False
        except ValueError:
            print("\n\n\n Input not valid, try again...")
    

main_menu()