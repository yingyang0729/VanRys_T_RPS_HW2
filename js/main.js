import { winorlose } from "./gameComponents/winLose.js";
 
(( ) => {
    // self-invoking anonymous function

    const choices = ["rock", "paper", "sciossors"];

    // player will be the weapon the player chooses via input
    let playerLives = 2,
        computerLives = 2
        gameButton = document.querySelector('button');

    // start the main game loop
    function gameloop() {
        let player = prompt("Choose your weapon: rock, paper or scissors: ");

        // generate a random number between 0 and 2 for the choice
        let computer = choices[Math.floor(Math.random() * 3)];

        console.log("player chose: " + player);
        console.log("computer chose:" + computer);

        if (computer === player) {
            // tie - nothing else to compare, so it'll exit
        console.log("tie! try again");
        return;
    }
    
    if (player == "rock") {
        if (computer == "paper") {
            console.log("you lose!")
            gameVars.playLives --; // double minus is the decrement operator (minus 1)
            } else {
            console.log("you win")
            computerLives --
        }
    }

    if (player == "paper") {
        if (computer == "scissors") {
            console.log("you lose!")
            playerLives = playerLives -1 
        } else {
            console.log("you win!")
            computerLives --
        }
    }    

    if (player == "scissors") {
        if (computer == "rock") {
            console.log("you lose!")
            playerLives = playerLives -1 
        } else {
            console.log("you win!")
            computerLives --
        }
    }        
           
}

gameButton.addEventListener("click", gameLoop);

})()
