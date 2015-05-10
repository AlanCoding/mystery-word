from random import randrange


def load_dict():
    """Returns a dictionary based on Mac spellcheck dictionary"""
    with open("/usr/share/dict/words") as dictFile:
        dictString = dictFile.read()
    return dictString.split()

def easy_words(word_list):
    """Narrows dictionary to between 4 and 6 letters"""
    return [x for x in word_list if len(x)>=4 and len(x)<=6]
def medium_words(word_list):
    """Narrows dictionary to between 6 and 8 letters"""
    return [x for x in word_list if len(x)>=6 and len(x)<=8]
def hard_words(word_list):
    """Narrows dictionary to 8 or more letters"""
    return [x for x in word_list if len(x)>=8]
def random_word(word_list):
    """Gives one randon word in dictionary"""
    return word_list[randrange(len(word_list))]

def display_word(word, charsGuessed):
    """Gives string to print with hidden non-guessed letters"""
    dispWord = ""
    for char in word:
        if char in charsGuessed:
            dispWord += char.upper()
        else:
            dispWord += "_"
    dispWord = " ".join(dispWord)
    return dispWord

def is_word_complete(word, charsGuessed):
    """Determines if word contains no unguessed characters"""
    for char in word:
        if char not in charsGuessed:
            return False
    return True

def start_game():
    """UI for the initial difficultity selection of game"""
    print("\n Welcome to Mystery Word! Compare to name brand Hangman.")
    print("   select your difficultity level")
    print("      -[E]asy  -[N]ormal  -[H]ard  -[S]atanic")
    difficultity = input("    enter a selection:")
    print("")
    return difficultity

def state_print(wordString, ct):
    """Gives game info update and cartoon man"""
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
    print("Word: "+wordString)
    if ct>7:
        print("   /\   ")
    elif ct>6:
        print("   /    ")
    else:
        print("        ")

def letter_input(charGuesses):
    """Gets a character guess from user"""
    c = input("Input your next letter guess:")
    if len(c)==0:
        c = " "
    while c[0].lower() in charGuesses:
        print(" You already guessed that!",end="")
        c = input("  make a new guess:")
        if len(c)==0:
            c = " "
    print("")
    return c

def wrong_guess(ct):
    """Prints message when guess is wrong"""
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
    print("Uh oh! That letter isn't in the word")
    ct2 = ct
    if ct >= 8:
        ct2 = 7
    print("   "+discouragingWords[ct2])

def dictFOM(dict):
    """Figure of merit for difficultity of a dictionary"""
    if len(dict) == 0:
        return 0
    else:
        return len(dict)*len(dict[0])

def narrow_words(dict,charsGuessed):
    """Gives subset dictionary to be more difficult"""
    dictDict = {}
    for word in dict:
        tag = display_word(word,charsGuessed)
        if tag in dictDict:
            dictDict[tag].append(word)
        else:
            dictDict[tag] = [word]
    dictLargest = []
    for dict in dictDict:
        if dictFOM(dictDict[dict]) > dictFOM(dictLargest):
            dictLargest = dictDict[dict]
    return dictLargest

def game_block(useDict,evil):
    """Exeutes game Mystery Word one time"""
    hiddenWord = random_word(useDict)
    print("The word contains "+str(len(hiddenWord))+" letters")
    charGuesses = []

    guesses = 8
    while True:
        charGuess = letter_input(charGuesses)[0].lower()
        if (len(charGuess)==0):
            charGuess = " "
        charGuesses.append(charGuess)

        if evil:
            useDict = narrow_words(useDict,charGuesses)
            if len(useDict)==1:
                evil = False
                hasWon = is_word_complete(hiddenWord,charGuesses)
            elif len(useDict)<1:
                raise SystemExit(0)
            else:
                hasWon = False
            hiddenWord = useDict[0]
            print("Dictionary has "+str(len(useDict))+" words\n")
        else:
            hasWon = is_word_complete(hiddenWord,charGuesses)
        wordString = display_word(hiddenWord,charGuesses)
        state_print(wordString,guesses)
        if hasWon:
            print('You Won!')
            print(' --- '+(hiddenWord+" ")*5+' --- ')
            break
        if charGuess not in hiddenWord:
            guesses -= 1
            wrong_guess(guesses)
        elif guesses >0:
            print("Congrats, you guessed a letter!")
            print("  your doom is temporarly delayed")
        else:
            print('You Lost :(')
            print('  the word was '+hiddenWord)
            break

if __name__ == '__main__':
    fullDict = load_dict()
    print("Dictionary has "+str(len(fullDict))+" words\n")

    while True:

        evil = False
        difficultity = start_game()
        if difficultity[0].lower() == 'e':
            useDict = easy_words(fullDict)
        elif difficultity[0].lower() == 'h':
            useDict = hard_words(fullDict)
        elif difficultity[0].lower() == 'n':
            useDict = medium_words(fullDict)
        elif difficultity[0].lower() == 's':
            evil = True
            useDict = narrow_words(fullDict,[])
            print(" words "+str(len(useDict))+" "+str(useDict[0]))
        else:
            print("error: difficultity not understood")
            break

        game_block(useDict,evil)

        print("")
        playAgain = input("Do you want to play again? (y/n)")
        if len(playAgain)==0:
            playAgain = " "
        if playAgain[0].lower() == 'y':
            continue
        else:
            break
