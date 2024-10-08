import sys
import random
from enum import Enum # just mention the name of item
class RPS(Enum):
    ROCK =1 # constant data value enumerate the name of that value
    PAPPER =2
    SCISSOR =3

# print(RPS(2)) # refer to papper by its value
# print(RPS["ROCK"]) # refer to Rock
# print(RPS.ROCK) # refer to rock
# print(RPS.ROCK.value)
# game using condition and input function
print(" ")
#playerchoice = int(input("Enter...\n1 for rock,\n2 for paper,or \n3 for scissors : \n\n"))
playerchoice = input("Enter...\n1 for rock,\n2 for paper,or \n3 for scissors : \n\n")
player = int(playerchoice)
if player < 1 | player > 3:
    sys.exit("You must enter 1,2 or 3 .") # exit and print
computerchoice = random.choice("123")
computer = int(computerchoice)
print("")
print("you choose" +" "+ str(RPS(player)).replace("RPS.","") +".")
#print("python choose" +" "+ str(RPS(computer)).strip("RPS.","") +".") # it removes R form rock
print("python choose" +" "+ str(RPS(computer)).replace("RPS.","") +".")
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