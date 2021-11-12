from random import randint

choices = ["rock","paper","scissors"]

# player will be the weapon the player chooses via input
# Boolean values are True or False - you can use these to check state
# and then make programming choices based on their value
player = False

# these lives need to decrement when a player loses a round
playerLives = 5
computerLives = 5

# create an infinite loop (for now) so that we can keep playing
while player is False:

    player = input("choose your weapon: rock,paper or scissors: ")
    computer = choices[randint(0,2)]

    print("player chose: " + player)
    print("computer chose: " +computer)

    if (computer == player):
        # tie - nothing else to compare, so it'll exit
        print("tie! try again")
    
    elif (player == "rock"):
        if (computer == "paper"):
            print("you lose!")
            playLives = playerLives - 1
        else:
            print("you win")
            computerLives = computerLives - 1

    elif (player == "paper"):
        if (computer == "scissors"):
            print("you lose!")
            playerLives = playerLives -1 
        else:
            print("you win!")
            computerLives = computerLives -1

    elif (player == "scissors"):
        if (computer == "rock"):
            print("you lose!")
            playerLives = playerLives -1 
        else:
            print("you win!")
            computerLives = computerLives -1

    print("player life count:" + str(playerLives))
    print("computer life count:" + str(computerLives))

    if playerLives == 0:
        print("you lost! would you like to play again?")
        choice = input(" Y / N? ")
   
        if choice == 'n':
            print("better luck next time!")
            exit()
        else:
            # reset and restart the game
            playerLives = 5
            computerLives = 5
            player = False

    elif computerLives == 0:
        print("you won!")
    
    player = False
