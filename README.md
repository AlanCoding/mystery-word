# Mystery Word

## How to use

With Python installed on your system,
run this in the command line

     $ python3 mystery_word.py

This should invoke the program and you will see the
greeting message if it worked.

## Description

"Mystery Word" is a game where you guess letters in a word
hidden from you by the computer.
If you guess a letter that the word has, it reveals
all of the instances of that letter.
However, if you guess a letter that is not in the word
the number of remaining tries is decreased by 1
Also, to add tension, a cartoon person loses one
body part.

## How to play

After the game starts, you will select your difficulty
level by tying a word or letter and hitting enter.
If that input starts with an "e", then the mystery word
will be between 4 and 6 letters long.
If that input starts with a "n" then it will be 6 to 8
characters long.
If the input starts with an "h" then the word will be 8
or more characters long.

After the difficulty is selected, the computer will let
you know how many characters the word has and you can
begin guessing letters.

Example, the word is "sheep"
and you have guessed e and s
the computer will display

     S _ E E _

Additionally, it will give the number of remaining guesses
and some other helpful textual details.

If you guess a letter which has already been guessed,
you have to guess again (for that round) and you are
not penalized for the wrong guess.

You have 8 tries to guess all the letters in the word.
If you guess all the letters before the counter runs out
you win, but if the word still contains uncovered letters
after 8 tries, you lose.

After you win or lose you can choose to play again by
typing "y" or leave the program by typing "n". But if you
need to exit at some other time, hit ctl+c.

###Hard Mode

The "Satanic" mode adheres to a method which doesn't hold
a specific word in memory as guesses are made. Instead,
the working dictionary is narrowed down in a way such that
every letter reveal is truthful, but the work selection is
adjusted on the fly so that it makes it extra difficult for
the user.

Note: As an extension of the work requirements, the
processing of narrowing the remaining dictionary isn't
based only on the number of words in the dictionary, but
also the number of letters.

Advanced improvements may be tried at a later time. 
