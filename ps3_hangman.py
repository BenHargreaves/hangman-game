
import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program


def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    count = 0
    
    for char in secretWord:
        if char in lettersGuessed:
            count += 1
    
    return count == len(secretWord)


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    returnString = ''
    for char in secretWord:
        if char in lettersGuessed:
            returnString = returnString + ' ' + char + ' '
        else:
            returnString = returnString + ' _ '
            
            
    return returnString



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    returnString = ''
    for char in alphabet:
        if char not in lettersGuessed:
            returnString = returnString + char
            
    return returnString
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    print('Welcome to the game, Hangman!')
    print(' I am thinking of a word that is', len(secretWord),'letters long.')
    guesses = 8
    lettersGuessed = []
    #availableLetters = string.ascii_lowercase
    while guesses >= 0:
        print('------------')
        if guesses == 0:
            print('Sorry, you ran out of guesses. The word was', secretWord)
            break
        if isWordGuessed(secretWord, lettersGuessed):
            print('Congratulations, you won!')
            break
        else:
            print('You have', guesses, 'guesses left.')
            print('Available letters: ' + getAvailableLetters(lettersGuessed))
            userInput = input('Please guess a letter: ')
            if userInput in lettersGuessed:
                print("Oops! You've already guessed that letter:", getGuessedWord(secretWord, lettersGuessed))
            else:
                lettersGuessed.append(userInput)
                if userInput in secretWord:
                    print('Good guess:', getGuessedWord(secretWord, lettersGuessed))
                else:
                    guesses -= 1
                    print('Oops! That letter is not in my word:', getGuessedWord(secretWord, lettersGuessed))



wordlist = loadWords()
secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
