
mysteryWord = ""
guessedLetters = ""
guessesRemaining = 8
gameMode = ""
approvedLetters = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
import random
from math import inf


def readDictionary(difficulty):
    if difficulty == "e":
        lower, upper = 4, 6
    elif difficulty == "m":
        lower, upper = 6, 8
    else:
        lower, upper = 8, inf
    with open("words.txt") as infile:
        return [word.strip() for word in infile if lower <= len(word.strip()) <= upper]


# difficulty = get_user_difficulty()
# word = pickRandomWord(difficulty)


def pickRandomWord(difficulty):
    return random.choice(readDictionary(difficulty))


def guessLetter():
    # input_v = False
    # 
    # while not input_v:
    #    user_input = input(...)
    #    if ... :
    #        input_v = True
    #    else:
    #        print("you screwed it all up!")
    # 
    letter = ""
    while letter not in approvedLetters:
        print("That is not an approved character.")
        inputLetter = input("Guess letter: ")
    else:
        letter = inputLetter.lower()
        if letter in mysteryWord:
            pass
        elif letter not in mysteryWord:
            print("Sorry! That letter is not in mysteryWord.")
            guessesRemaining -= 1
            pass

# keep input validation separate; return their guess 
#then separately test whether in the word
# 1- is it a letter; 2 - is it in previously guessed letters; 3 - if not, add it to guessed letters 4 - return it 
# 5 - add to guessed letters 6 - return it 7 - 


def gameStart():
    print("Welcome to Mystery Word!\n")
    print("You can choose between 3 modes of difficulty -- 'e' for easy, 'm' for medium, or 'h' for hard.\n")
    gameMode = input("Enter difficulty level: ")
    #also need to reset counter to 8 on start
    if gameMode != "e" or "m" or "h"
        raise CustomError ("Error in loading game mode. Please input either 'e', 'm', or 'h'.")
        gameMode()
    elif gameMode == "e"
        pickRandomWord("e")
    elif gameMode == "m"
        pickRandomWord("m")
    elif gameMode == "h"
        pickRandomWord("h")
    pass


if __name__ == "__main__":
    gameStart()
