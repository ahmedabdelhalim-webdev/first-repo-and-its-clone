# closure => function has scope to its parent
# function after the parent function returned to it
# to avoid creating global variable in nested function
def parent_function(person,coins):
    #coins = 3
    def play_game():
        nonlocal coins # to able to modify it
        coins -=1
        if coins > 0 :
            print("\n" + person + " has " + str(coins) + "coins left.")
        elif coins == 1:
            print("\n" + person + " has " + str(coins) + "coins left.")
        else :
            print("\n" + person +" is out of coins")
    return play_game # return of parent func is to execute child function
ahma = parent_function("ahma",3)  # transform variable into function
ziad = parent_function("ziad",5)
ahma()
ziad()
ahma()