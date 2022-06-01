from random import choice

done = False
options = ["rock", "paper", "scissors"]
CPU_score = 0
player_score = 0

while not done:
    options_made = None
    CPU_input = choice(options)
    player_input = input("Enter r for Rock, p for Paper or s for Scissors: ")

    if player_input == "r":
        player_option = "rock"
        options_made = "valid"

    elif player_input == "p":
        player_option = "paper"
        options_made = "valid"
    
    elif player_input == "s":
        player_option = "scissors"
        options_made = "valid"
    
    else:
        print("invalid iput. Please try again!")

    if options_made == "valid":
        print(f"Player ({player_option}), CPU ({(CPU_input)})")

        if player_option == CPU_input:
            print("Its a tie!. Play again!")
            continue
        else:
            if player_option == "rock":
                if CPU_input == "paper":
                    print("Computer wins!")
                else:
                    print("Player wins")
                    
        
                
            if player_option == "paper":
                if CPU_input == "scissors":
                    print("Computer wins!")
                else:
                    print("Player wins")
                    
       
            
            if player_option == "scissors":
                if CPU_input == "rock":
                    print("Computer wins!")
                else:
                    print("Player wins")
            break

    
       
        
        

    
        
        
