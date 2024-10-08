import sys
import random
from enum import Enum # just mention the name of item

def rps():
    game_count = 0
    player_wins = 0
    python_wins = 0

    def play_rps():
        nonlocal player_wins
        nonlocal python_wins

        class RPS(Enum):
            ROCK =1 # constant data value enumerate the name of that value
            PAPPER =2
            SCISSOR =3
    
        playerchoice = input("\nEnter...\n1 for rock,\n2 for paper,or \n3 for scissors : \n\n")

        if playerchoice not in ["1","2","3"]:
            nonlocal player_wins
            nonlocal python_wins
            print("You must enter 1,2 or 3 .")
            return play_rps() # return to ask the user again

        player = int(playerchoice)
    
        computerchoice = random.choice("123")
        computer = int(computerchoice)
        
        print(f"\nyou choose {str(RPS(player)).replace("RPS.","").title()}")
        #print(f"python choose" +" "+ str(RPS(computer)).strip("RPS.") +".") # it removes R form rock
        print(f"python choose  {str(RPS(computer)).replace( "RPS.","").title()}.\n")
        print("")
        def decide_winner(player,computer):
            nonlocal player_wins
            nonlocal python_wins
            if player ==1 and computer ==3:
                player_wins +=1
                print("\U0001F606you win!")
            elif player ==2 and computer ==1:
                player_wins +=1
                print("\U0001F606you win!")
            elif player ==3 and computer ==2:
                player_wins +=1
                print("\U0001F606you win!")
            elif player ==computer:
                print("\U0001F910try again!")
            else:
                python_wins +=1
                print("python wins!")
        game_result = decide_winner(player,computer)
        print(game_result)
        nonlocal game_count
        game_count +=1
        print(f"\nGame count : {str(game_count)} ")
        print(f"\nplayer wins :  {str(player_wins)}")
        print(f"\npython wins :  {str(python_wins)}")

        print("\nplay again")

        
        while True:
            playagain = input("\ny for yes or \nq to quite\n\n")
            if playagain.lower() not in ["y","q"]:
                continue
            else:
                break
        
        if playagain.lower() =="y":
            return play_rps()
            
            
        else :
            print("thank you for playing!\n")
            print("bye")
        sys.exit("bye ")
    return play_rps()

game =rps()
game()