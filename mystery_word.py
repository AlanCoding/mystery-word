from random import randrange


def load_dict():
    with open("/usr/share/dict/words") as dictFile:
        dictString = dictFile.read()
    return dictString.split()

def easy_words(word_list):
    return [x for x in word_list if len(x)>=4 and len(x)<=6]
def medium_words(word_list):
    return [x for x in word_list if len(x)>=6 and len(x)<=8]
def hard_words(word_list):
    return [x for x in word_list if len(x)>=8]
def random_word(word_list):
    return word_list[randrange(len(word_list))]

def display_word(word, charsGuessed):
    dispWord = ""
    for char in word:
        if char in charsGuessed:
            dispWord += char.upper()
        else:
            dispWord += "_"
    dispWord = " ".join(dispWord)
    return dispWord

def is_word_complete(word, charsGuessed):
    for char in word:
        if char not in charsGuessed:
            return False
    return True

def start_game():
    print("\n Welcome to Hangman!")
    print("   select your difficultity level")
    print("      -Easy  -Normal  -Hard")
    difficultity = input("    enter a selection:")
    print("")
    return difficultity

def state_print(word, charsGuessed, ct):
    if (ct>1):
        print("   o    ")
    else:
        print("        ")
    if (ct>4):
        print("  /|\   ",end="")
    elif (ct>3):
        print("   |\   ",end="")
    elif (ct>2):
        print("   |    ",end="")
    else:
        print("        ",end="")
    print("Remaining Guesses: "+str(ct))
    if (ct>5):
        print("   |    ",end="")
    else:
        print("        ",end="")
    print("Word: "+display_word(word,charsGuessed))
    if ct>7:
        print("   /\   ")
    elif ct>6:
        print("   /    ")
    else:
        print("        ")

def letter_input(charGuesses):
    c = input("Input your next letter guess:")
    while c[0].lower() in charGuesses:
        print(" You already guessed that!",end="")
        c = input("  make a new guess:")
    print("")
    return c


if __name__ == '__main__':
    fullDict = load_dict()
    print("Dictionary has "+str(len(fullDict))+" words\n")
    discouragingWords = [
        "fear not the reaper",
        "okay maybe panic now",
        "you can still win. maybe.",
        "ouch, maybe the next letter?",
        "just go with vowels",
        "on the bright side... high scrabble score",
        "a few setbacks, it'll be alright",
        "keep calm and keep guessing",
        "no need to panic, you'll be ok",
    ]

    while True:

        difficultity = start_game()
        if difficultity[0].lower() == 'e':
            useDict = easy_words(fullDict)
        elif difficultity[0].lower() == 'h':
            useDict = hard_words(fullDict)
        else:
            useDict = medium_words(fullDict)
        hiddenWord = random_word(useDict)
        print("The word contains "+str(len(hiddenWord))+" letters")
        charGuesses = []

        guesses = 8
        while guesses > 0:
            charGuess = letter_input(charGuesses)[0].lower()
            charGuesses.append(charGuess)
            state_print(hiddenWord,charGuesses,guesses)
            if is_word_complete(hiddenWord,charGuesses):
                print('You Won!')
                print(' --- '+hiddenWord*5+' --- ')
                break
            elif charGuess not in hiddenWord:
                guesses -= 1
                print("Uh oh! That letter isn't in the word")
                print("   "+discouragingWords[guesses])
            elif guesses >0:
                print("Congrats, you guessed a letter!")
                print("  your doom is temporarly delayed")
            else:
                print('You Lost :(')
                print('  the word was '+hiddenWord)

        print("")
        playAgain = input("Do you want to play again? (y/n)")
        if playAgain[0].lower() == 'y':
            continue
        else:
            break
