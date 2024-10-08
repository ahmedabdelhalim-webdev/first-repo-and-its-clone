import sys
import random
from enum import Enum # just mention the name of item
class RPS(Enum):
    ROCK =1 # constant data value enumerate the name of that value
    PAPPER =2
    SCISSOR =3
playagain = True
while playagain:

    # print(RPS(2)) # refer to papper by its value
    # print(RPS["ROCK"]) # refer to Rock
    # print(RPS.ROCK) # refer to rock
    # print(RPS.ROCK.value)
    # game using condition and input function
    
    #playerchoice = int(input("Enter...\n1 for rock,\n2 for paper,or \n3 for scissors : \n\n"))
    playerchoice = input("\nEnter...\n1 for rock,\n2 for paper,or \n3 for scissors : \n\n")
    player = int(playerchoice)
    if player < 1 | player > 3:
        sys.exit("You must enter 1,2 or 3 .") # print and exit
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
        print("\U0001F612python wins!")
    playagain = input("\nplay again \ny for yes or \nq to quite\n\n")
    if playagain.lower() =="q":
        print("game over , thank you for playing")
        playagain = False
        break
        
    else :
        continue
sys.exit("bye U+1F60B")