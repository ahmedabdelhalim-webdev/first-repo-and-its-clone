import sys
import random
from enum import Enum # just mention the name of item

def play_rps():

    class RPS(Enum):
        ROCK =1 # constant data value enumerate the name of that value
        PAPPER =2
        SCISSOR =3
   
    playerchoice = input("\nEnter...\n1 for rock,\n2 for paper,or \n3 for scissors : \n\n")

    if playerchoice not in ["1","2","3"]:
        print("You must enter 1,2 or 3 .")
        return play_rps() # return to ask the user again

    player = int(playerchoice)
  
    computerchoice = random.choice("123")
    computer = int(computerchoice)
    
    print("\nyou choose" +" "+ str(RPS(player)).replace("RPS.","") +".")
    #print("python choose" +" "+ str(RPS(computer)).strip("RPS.") +".") # it removes R form rock
    print("python choose" +" "+ str(RPS(computer)).replace("RPS.","") +".\n")
    print("")
    if player ==1 and computer ==3:
        print("\U0001F606you win!")
    elif player ==2 and computer ==1:
        print("\U0001F606you win!")
    elif player ==3 and computer ==2:
        print("\U0001F606you win!")
    elif player ==computer:
        print("\U0001F910try again!")
    else:
        print("python wins!")

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

play_rps()