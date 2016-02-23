# John Swain
import random

# this is the generateNumber function
#'topLimit' which is the top limit for the random number generator
# the function returns the random number generated to its caller

def generateNumber( topLimit ):  
    return random.randint(1,topLimit)

# this is the askUserToGuess function
# the function returns one of two values:
#   return True if the user guessed the answer correctly
#   return False if the user did not guess the answer correctly

def askUserToGuess( times, secretNumber ):

    # this loop cycles through all the user guesses
    for guessesTaken in range(1, times+1):
        
        print('Take your guess #' + str(guessesTaken) + ': ')
        guess = int(input())

        if evaluateAnswer( guess, secretNumber ) == True:
            return True
        
    return False

# this is the evaluateAnswer function
# it has two parameters:
#   the 'userGuess' parameter is the answer entered by the user
#   the 'userSecretNumber' parameter is the randomly generated number
def evaluateAnswer( userGuess, userSecretNumber ):
    
    if userGuess > userSecretNumber:
        print("too high")
        return False
    
    if userGuess < userSecretNumber:
        print("too low")
        return False
    
    else:
        return True


# this is the playGame function
# it has one parameter:
#   'showAnswer' is a Boolean value, if that Boolean value is:
#       True, we'll show the right answer on the screen
#       False, we won't show the right answer on the screen
def playGame( showAnswer ):

    topLimit = int(input("Hello player, welcome to the guessing game!\nPlease pick a maximum number.\n"))

    totalGuesses = int(input("Before you start guessing how many tries do you think you'll take?\n"))

    theNumber = generateNumber( topLimit )

    print("Now guess a number between 1 and " + str(topLimit)+ " ." +" You have " + str(totalGuesses) + " guesses.")

    # you don't need to change anything below this comment ##############
    # ///////////////////////////////////////////////////////////////////
    # this if statement allows us to show the hidden number to the user
    if( showAnswer == True ):
        print('--shhh, the real number is ' + str(theNumber) + '.')
    
    #this gives a sucess/fail message if the user guessed correctly in the allotted attempts
    if askUserToGuess(totalGuesses,theNumber) == True:
        print('Good job! You guessed my number!')
    else:
        print('Nope. The number I was thinking of was ' + str(theNumber))
