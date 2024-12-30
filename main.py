# blackjack game

import random 

# variables

player = 0
comp = 0 

# loop

while True:
    if comp > 21:
        print("Player automatically wins, the computer bust!")
        break
    if player > 21:
        print("Computer automatically wins, the player bust!")
        break
    hit = input("Would you like to hit? Y or N: ")
    crand = random.randint(1,11)
    comp = comp + crand
   
    # conditionals

    if hit == "Y":
        rand = random.randint(1,11)
        player = player + rand
        print("You got " + str(rand))
        print("The computer is currently at " + str(comp))
        print("You're at " + str(player))
    else:
        print("You're at " + str(player) + " while the computer is at " + str(comp))
        if comp > player:
            print("Computer Wins!")
        elif player > comp:
            print("Player Wins!")
        else:
            print("It's a tie, play another rouund!")