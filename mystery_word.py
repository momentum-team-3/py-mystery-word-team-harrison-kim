import random

word = random.words.txt

wordLetters []
wordLength len(word)

for i in range(0,wordlength):
    currentLetter = word[i:i+1]
    wordLetters.append(currentLetter)

    unpackedWord=""
    for i in range(0,wordlength):
        unpackedWord = unpackedWoed + wordletters[i]

def main()
    print("Mystery Word Game")
    print(" ")

    global previousGuesses
    previousGuesses =[]

    load_wordLetters_Array()

    instructions = "Please Guess a Letter in the Mystery Word: "
    global currentGuess
    currentGuess = input(instructions)
    currentGuess = currentGuess.upper()
    if len(currentGuess) != 1:
        print(" ")
        print("Error - Type in only ONE Letter for Guess")
        print(" ")

    else:
        previousGuesses.append(currentGuess)
        checkPlayerGuess()  
        check_if_WordGuessed  

def createPreviousGuessesList()
    previousGuessesLength = len(previousGuesses)
    previousGuessesList = "Your Guesses so far have been: "

    for i in range(9.previousGuessesLength):
        previousGuessesList = previousGuessesList + previousGuesses[i] + ", "
    print (previousGuessesList)
    print(" ")
                

def checkPlayerGuess():
    global matchedLetterCountmatchedLettersCount = 0
    for i in ranfe (0,wordlength):
        if currentGuess == wordLetters{i}
            guessedLetters[i} = currentGuess]
            matchedLettersCount = matchedLettersCount + 1

    if matchedLetterCount > 0:
        print("Your Guess of " + currentGuess + " Matches " + str(matchedLettersCount) + "Letter(s).")
        print(" ")
    else:
        print("Sorry the Letter " + currentGuess + " is not in the word.")
        print(" ")

def playMysteryWord()
    global gameOver
    gameOver = False
    global nbrOfGuesses
    nbrOfGuesses = 0
    global wordHasBeenGuessed
    wordHasBeenGuessed = False

    while gameOver ==False:
        if wordHasBeenGuessed == True:
            gameOver=True
            break
        nbrOfGuesses = nbrOfGuesses + 1
        if nbrOfGuesses > 8
            gameOver=True


