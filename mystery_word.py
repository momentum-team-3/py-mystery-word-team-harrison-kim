
mysteryWord = ""
guessedLetters = ""
guessesRemaining = 8
gameMode = ""
approvedLetters = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"



pickRandomWord("difficulty"):
    if difficulty == "e"
        #choose from dictionary word between 4 and 6 letters
        #set chosenword value to mysteryWord
    elif difficulty == "m"
        #choose from dictionary word between 6 and 8 letters
        #set chosenword value to mysteryWord
    elif difficulty == "h"
        #choose from dictionary word that's more than 8 letters
        #set chosenword value to mysteryWord

guessLetter("inputLetter"):
    if letter not in approvedLetters:
        pass
    else:
        letter = inputLetter.lower()
        if letter in mysteryWord:
            pass
        elif letter not in mysteryWord:
            print("Sorry! That letter is not in mysteryWord.")
            guessesRemaining -= 1
            pass



gameStart():
    print("Welcome to Mystery Word!\n")
    print("You can choose between 3 modes of difficulty -- 'e' for easy, 'm' for medium, or 'h' for hard.\n")
    gameMode = input("Enter difficulty level: ")
    if gameMode != "e" or "m" or "h"
        raise CustomError ("Error in loading game mode. Please input either 'e', 'm', or 'h'.")
        gameMode()
    elif gameMode == "e"
        pickRandomWord("e")
    elif gameMode == "m"
        pickRandomWord("m")
    elif gameMode == "h"
        pickRandomWord("h")


if __name__ == __main:
    






