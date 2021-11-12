function winorlose(status,pLives,CLives) {
    Console.log("you" + status)

    let choice = prompt("do you want to play again? y/n:")

    if (choice == "n") {
        console.log("========== see ya!(loser) ==============")
        return;
    } else if (choice == "y") {
        pLives = 5
        cLives = 5
    }
}

export {winorlose }