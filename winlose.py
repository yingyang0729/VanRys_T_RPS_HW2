 from gameComponents import gameVars


 def winorlose(status):
     print("you"+status)

     choice = input("do you want to play again? y/n: ")

     if choice == "n":
         print("========= see ya! (loser) =========")
         exit()
    elif choice == "y":
        gameVars.playerLives = 5
        gameVars.computerLives = 5
        gameVars.player = False