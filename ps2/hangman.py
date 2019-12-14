# Problem Set 2, hangman.py
# Name:
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
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



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    letter_count = 0
    for c in secret_word: # for every character in secret_word
        if c in letters_guessed: # if a character in letters_guessed is also
            # in secret_word
            letter_count += 1 # add 1 to letter_count
        else: # if any letter guessed is not in secret_word
            return False
    if letter_count == len(secret_word): # if the number of correctly guessed
        # letters equals the length of the secret word
        return True

def is_letter_in_word(secret_word, letter):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letter: which letter is being guessed
    returns: boolean, True if the letter is in secret_word, False otherwise
    '''
    for c in letter: # if the character (letter)
        if c in secret_word: # is in the secret word
            return True 
        else: # if the character is not in the secret word
            return False

def is_letter_valid(char):
    '''
    char: which character is being guessed
    returns: boolean, True if the character is a valid letter, False otherwise
    '''
    all_letters = 'abcdefghijklmnopqrstuvwxyz'
    if char in all_letters: # if the guessed character is a letter
        return True
    else: # if the guessed character is not a letter
        return False

def is_letter_vowel(char):
    '''
    char: which character is being guessed
    returns: boolean, True if the character is a vowel, False otherwise
    '''
    vowels = 'aeiou'
    if char in vowels: # if the guessed character is a vowel
        return True
    else: # if the guessed character is not a vowel
        return False

def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    letters_found = '' 
    for c in secret_word: # for every character in secret_word
        if c in letters_guessed: # if the character is also in letters_guessed
            letters_found += c # add that character to letters_found
            secret_word.replace(c, ' ', 1) # remove that character from
            # secret_word, so that multiple occurances of a letter can be
            # picked up
        else: # if that character is not in letters_guessed
            letters_found += '_ ' # add an underscore and space to indicate
            # that character still needs to be guessed
    return letters_found

def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which 
    letters have not yet been guessed.
    '''
    all_letters = 'abcdefghijklmnopqrstuvwxyz' # list of all letters
    for c in all_letters: # for every character in all_letters
        if c in letters_guessed: # if a character is also in letters_guessed
            all_letters = all_letters.replace(c, '') # update all_letters by
            # removing those letters which have already been guessed
    return all_letters   

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    
    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is', len(secret_word), 'letters long')
    guesses_remaining = 6
    print('You have', guesses_remaining, 'guesses left')
    print('Available letters:', get_available_letters(''))
    letter = input('Please guess a letter:')
    letters_guessed = []
    num_warn = 3
    score = guesses_remaining * len(list(set(secret_word)))
    winning = 'Congratulations! You won! Your total score for this game is:', str(score)
    losing = 'Sorry, you ran out of guesses. The word was:', str(secret_word)
    
    # first run
    while is_letter_valid(letter) is True: # while the guessed character is a
        # valid letter
        if is_letter_in_word(secret_word, letter) is True:
            # if the guessed letter is in the secret word
            for c in letter: 
                if c in letters_guessed: 
                    # if the guessed letter has already been guessed
                    print('Oops! You have already guessed that letter!')
                    if num_warn == 0: # if the user has run out of warnings
                        guesses_remaining = guesses_remaining - 1
                        print('You have no warnings remaining.')
                        print('You will now lose guesses instead.')
                        print(get_guessed_word(secret_word, letters_guessed))
                        print('----------------------------------------------')
                        break
                    else: # if the user has more than one guess remaining
                        letters_guessed += letter
                        num_warn = num_warn - 1
                        print('You now have', num_warn, 'warnings left:')
                        print(get_guessed_word(secret_word, letters_guessed))
                        print('----------------------------------------------')
                        break
                    break
                else: # if the guessed letter has not already been guessed
                    letters_guessed += letter # add it to guessed letters as 
                    # the guessed letter is in the secret word
                    if is_word_guessed(secret_word, letters_guessed) is True:
                    # if all guessed letters match the secret word
                        print('Good guess:', get_guessed_word(secret_word,
                                                              letters_guessed))
                        return winning # end game with congratulations message 
                        # and score
                    else: # if all the guessed letters do not match the word
                        print('Good guess:', get_guessed_word(secret_word,
                                                              letters_guessed))
                        break
                    break
                break
            break
        elif is_letter_in_word(secret_word, letter) is False:
            # if the guessed letter is not in the secret word
            for c in letter: 
                if c in letters_guessed: # if the guessed letter has already 
                    # been guessed
                    print('Oops! You have already guessed that letter!')
                    if num_warn == 0: # if the user has run out of warnings
                        guesses_remaining = guesses_remaining - 1
                        print('You have no warnings remaining.')
                        print('You will now lose guesses instead.')
                        print(get_guessed_word(secret_word, letters_guessed))
                        print('----------------------------------------------')
                        break
                    else: # if the user has more than one guess remaining
                        letters_guessed += letter
                        num_warn = num_warn - 1
                        print('You now have', num_warn, 'warnings left:')
                        print(get_guessed_word(secret_word, letters_guessed))
                        print('----------------------------------------------')
                        break
                    break
                else: # if the letter has not already been guessed
                    letters_guessed += letter # add it to guessed letters
                    print('Oops! That letter is not in my word!', 
                          get_guessed_word(secret_word, letters_guessed))
                        # because the guessed letter is not in the secret word
                    if is_letter_vowel(letter) is True: # if a vowel
                        guesses_remaining = guesses_remaining - 2 
                        # minus two from the number of guesses
                    else: # if not a vowel
                        guesses_remaining = guesses_remaining - 1 
                        # minus one from the number of guesses
                        break
                    break
                break
            break
        break
    else: # if the guessed character is not a valid letter
        letters_guessed += letter
        if num_warn == 0: # if the user has run out of warnings
            guesses_remaining = guesses_remaining - 1
            print('You have no warnings remaining.')
            print('You will now lose guesses instead.')
            print(get_guessed_word(secret_word, letters_guessed))
            print('------------------------------------------------------')
        else: # if the user has warnings remaining
            num_warn = num_warn - 1
            print('Oops! That is not a valid letter. You have', num_warn,
                  'warnings left:', get_guessed_word(secret_word, 
                                                     letters_guessed))
            print('------------------------------------------------------')
    # end of first run
    
    if int(guesses_remaining <= 0):
        return losing
    print('You have', guesses_remaining, 'guesses left')
    if num_warn >= 1:
        print('You have', num_warn, 'warnings left')
    print('Available letters:', get_available_letters(letters_guessed))
    letter = input('Please guess a letter:')
    
    # second run 
    while is_letter_valid(letter) is True: # while the guessed character is a
        # valid letter
        if is_letter_in_word(secret_word, letter) is True:
            # if the guessed letter is in the secret word
            for c in letter: 
                if c in letters_guessed: 
                    # if the guessed letter has already been guessed
                    print('Oops! You have already guessed that letter!')
                    if num_warn == 0: # if the user has run out of warnings
                        guesses_remaining = guesses_remaining - 1
                        print('You have no warnings remaining.')
                        print('You will now lose guesses instead.')
                        print(get_guessed_word(secret_word, letters_guessed))
                        print('----------------------------------------------')
                        break
                    else: # if the user has more than one guess remaining
                        letters_guessed += letter
                        num_warn = num_warn - 1
                        print('You now have', num_warn, 'warnings left:')
                        print(get_guessed_word(secret_word, letters_guessed))
                        print('----------------------------------------------')
                        break
                    break
                else: # if the guessed letter has not already been guessed
                    letters_guessed += letter # add it to guessed letters as 
                    # the guessed letter is in the secret word
                    if is_word_guessed(secret_word, letters_guessed) is True:
                    # if all guessed letters match the secret word
                        print('Good guess:', get_guessed_word(secret_word,
                                                              letters_guessed))
                        return winning # end game with congratulations message 
                        # and score
                    else: # if all the guessed letters do not match the word
                        print('Good guess:', get_guessed_word(secret_word,
                                                              letters_guessed))
                        break
                    break
                break
            break
        elif is_letter_in_word(secret_word, letter) is False:
            # if the guessed letter is not in the secret word
            for c in letter: 
                if c in letters_guessed: # if the guessed letter has already 
                    # been guessed
                    print('Oops! You have already guessed that letter!')
                    if num_warn == 0: # if the user has run out of warnings
                        guesses_remaining = guesses_remaining - 1
                        print('You have no warnings remaining.')
                        print('You will now lose guesses instead.')
                        print(get_guessed_word(secret_word, letters_guessed))
                        print('----------------------------------------------')
                        break
                    else: # if the user has more than one guess remaining
                        letters_guessed += letter
                        num_warn = num_warn - 1
                        print('You now have', num_warn, 'warnings left:')
                        print(get_guessed_word(secret_word, letters_guessed))
                        print('----------------------------------------------')
                        break
                        break
                else: # if the letter has not already been guessed
                    letters_guessed += letter # add it to guessed letters
                    print('Oops! That letter is not in my word!', 
                          get_guessed_word(secret_word, letters_guessed))
                        # because the guessed letter is not in the secret word
                    if is_letter_vowel(letter) is True: # if a vowel
                        guesses_remaining = guesses_remaining - 2 
                        # minus two from the number of guesses
                    else: # if not a vowel
                        guesses_remaining = guesses_remaining - 1 
                        # minus one from the number of guesses
                        break
                    break
                break
            break
        break
    else: # if the guessed character is not a valid letter
        letters_guessed += letter
        if num_warn == 0: # if the user has run out of warnings
            guesses_remaining = guesses_remaining - 1
            print('You have no warnings remaining.')
            print('You will now lose guesses instead.')
            print(get_guessed_word(secret_word, letters_guessed))
            print('------------------------------------------------------')
        else: # if the user has warnings remaining
            num_warn = num_warn - 1
            print('Oops! That is not a valid letter. You have', num_warn,
                  'warnings left:', get_guessed_word(secret_word, 
                                                     letters_guessed))
            print('------------------------------------------------------')
    # end of second run   
        
    if int(guesses_remaining <= 0):
        return losing
    print('You have', guesses_remaining, 'guesses left')
    if num_warn >= 1:
        print('You have', num_warn, 'warnings left')
    print('Available letters:', get_available_letters(letters_guessed))
    letter = input('Please guess a letter:')
    
    # third run
    while is_letter_valid(letter) is True: # while the guessed character is a
        # valid letter
        if is_letter_in_word(secret_word, letter) is True:
            # if the guessed letter is in the secret word
            for c in letter: 
                if c in letters_guessed: 
                    # if the guessed letter has already been guessed
                    print('Oops! You have already guessed that letter!')
                    if num_warn == 0: # if the user has run out of warnings
                        guesses_remaining = guesses_remaining - 1
                        print('You have no warnings remaining.')
                        print('You will now lose guesses instead.')
                        print(get_guessed_word(secret_word, letters_guessed))
                        print('----------------------------------------------')
                        break
                    else: # if the user has more than one guess remaining
                        letters_guessed += letter
                        num_warn = num_warn - 1
                        print('You now have', num_warn, 'warnings left:')
                        print(get_guessed_word(secret_word, letters_guessed))
                        print('----------------------------------------------')
                        break
                    break
                else: # if the guessed letter has not already been guessed
                    letters_guessed += letter # add it to guessed letters as 
                    # the guessed letter is in the secret word
                    if is_word_guessed(secret_word, letters_guessed) is True:
                    # if all guessed letters match the secret word
                        print('Good guess:', get_guessed_word(secret_word,
                                                              letters_guessed))
                        return winning # end game with congratulations message 
                        # and score
                    else: # if all the guessed letters do not match the word
                        print('Good guess:', get_guessed_word(secret_word,
                                                              letters_guessed))
                        break
                    break
                break
            break
        elif is_letter_in_word(secret_word, letter) is False:
            # if the guessed letter is not in the secret word
            for c in letter: 
                if c in letters_guessed: # if the guessed letter has already 
                    # been guessed
                    print('Oops! You have already guessed that letter!')
                    if num_warn == 0: # if the user has run out of warnings
                        guesses_remaining = guesses_remaining - 1
                        print('You have no warnings remaining.')
                        print('You will now lose guesses instead.')
                        print(get_guessed_word(secret_word, letters_guessed))
                        print('----------------------------------------------')
                        break
                    else: # if the user has more than one guess remaining
                        letters_guessed += letter
                        num_warn = num_warn - 1
                        print('You now have', num_warn, 'warnings left:')
                        print(get_guessed_word(secret_word, letters_guessed))
                        print('----------------------------------------------')
                        break
                        break
                else: # if the letter has not already been guessed
                    letters_guessed += letter # add it to guessed letters
                    print('Oops! That letter is not in my word!', 
                          get_guessed_word(secret_word, letters_guessed))
                        # because the guessed letter is not in the secret word
                    if is_letter_vowel(letter) is True: # if a vowel
                        guesses_remaining = guesses_remaining - 2 
                        # minus two from the number of guesses
                    else: # if not a vowel
                        guesses_remaining = guesses_remaining - 1 
                        # minus one from the number of guesses
                        break
                    break
                break
            break
        break
    else: # if the guessed character is not a valid letter
        letters_guessed += letter
        if num_warn == 0: # if the user has run out of warnings
            guesses_remaining = guesses_remaining - 1
            print('You have no warnings remaining.')
            print('You will now lose guesses instead.')
            print(get_guessed_word(secret_word, letters_guessed))
            print('------------------------------------------------------')
        else: # if the user has warnings remaining
            num_warn = num_warn - 1
            print('Oops! That is not a valid letter. You have', num_warn,
                  'warnings left:', get_guessed_word(secret_word, 
                                                     letters_guessed))
            print('------------------------------------------------------')
    # end of third run
    
    if int(guesses_remaining <= 0):
        return losing
    print('You have', guesses_remaining, 'guesses left')
    if num_warn >= 1:
        print('You have', num_warn, 'warnings left')
    print('Available letters:', get_available_letters(letters_guessed))
    letter = input('Please guess a letter:')
   
    # fourth run
    while is_letter_valid(letter) is True: # while the guessed character is a
        # valid letter
        if is_letter_in_word(secret_word, letter) is True:
            # if the guessed letter is in the secret word
            for c in letter: 
                if c in letters_guessed: 
                    # if the guessed letter has already been guessed
                    print('Oops! You have already guessed that letter!')
                    if num_warn == 0: # if the user has run out of warnings
                        guesses_remaining = guesses_remaining - 1
                        print('You have no warnings remaining.')
                        print('You will now lose guesses instead.')
                        print(get_guessed_word(secret_word, letters_guessed))
                        print('----------------------------------------------')
                        break
                    else: # if the user has more than one guess remaining
                        letters_guessed += letter
                        num_warn = num_warn - 1
                        print('You now have', num_warn, 'warnings left:')
                        print(get_guessed_word(secret_word, letters_guessed))
                        print('----------------------------------------------')
                        break
                    break
                else: # if the guessed letter has not already been guessed
                    letters_guessed += letter # add it to guessed letters as 
                    # the guessed letter is in the secret word
                    if is_word_guessed(secret_word, letters_guessed) is True:
                    # if all guessed letters match the secret word
                        print('Good guess:', get_guessed_word(secret_word,
                                                              letters_guessed))
                        return winning # end game with congratulations message 
                        # and score
                    else: # if all the guessed letters do not match the word
                        print('Good guess:', get_guessed_word(secret_word,
                                                              letters_guessed))
                        break
                    break
                break
            break
        elif is_letter_in_word(secret_word, letter) is False:
            # if the guessed letter is not in the secret word
            for c in letter: 
                if c in letters_guessed: # if the guessed letter has already 
                    # been guessed
                    print('Oops! You have already guessed that letter!')
                    if num_warn == 0: # if the user has run out of warnings
                        guesses_remaining = guesses_remaining - 1
                        print('You have no warnings remaining.')
                        print('You will now lose guesses instead.')
                        print(get_guessed_word(secret_word, letters_guessed))
                        print('----------------------------------------------')
                        break
                    else: # if the user has more than one guess remaining
                        letters_guessed += letter
                        num_warn = num_warn - 1
                        print('You now have', num_warn, 'warnings left:')
                        print(get_guessed_word(secret_word, letters_guessed))
                        print('----------------------------------------------')
                        break
                        break
                else: # if the letter has not already been guessed
                    letters_guessed += letter # add it to guessed letters
                    print('Oops! That letter is not in my word!', 
                          get_guessed_word(secret_word, letters_guessed))
                        # because the guessed letter is not in the secret word
                    if is_letter_vowel(letter) is True: # if a vowel
                        guesses_remaining = guesses_remaining - 2 
                        # minus two from the number of guesses
                    else: # if not a vowel
                        guesses_remaining = guesses_remaining - 1 
                        # minus one from the number of guesses
                        break
                    break
                break
            break
        break
    else: # if the guessed character is not a valid letter
        letters_guessed += letter
        if num_warn == 0: # if the user has run out of warnings
            guesses_remaining = guesses_remaining - 1
            print('You have no warnings remaining.')
            print('You will now lose guesses instead.')
            print(get_guessed_word(secret_word, letters_guessed))
            print('------------------------------------------------------')
        else: # if the user has warnings remaining
            num_warn = num_warn - 1
            print('Oops! That is not a valid letter. You have', num_warn,
                  'warnings left:', get_guessed_word(secret_word, 
                                                     letters_guessed))
            print('------------------------------------------------------')
    # end of fourth run
    
    if int(guesses_remaining <= 0):
        return losing
    print('You have', guesses_remaining, 'guesses left')
    if num_warn >= 1:
        print('You have', num_warn, 'warnings left')
    print('Available letters:', get_available_letters(letters_guessed))
    letter = input('Please guess a letter:')
    
    
    # fifth run
    while is_letter_valid(letter) is True: # while the guessed character is a
        # valid letter
        if is_letter_in_word(secret_word, letter) is True:
            # if the guessed letter is in the secret word
            for c in letter: 
                if c in letters_guessed: 
                    # if the guessed letter has already been guessed
                    print('Oops! You have already guessed that letter!')
                    if num_warn == 0: # if the user has run out of warnings
                        guesses_remaining = guesses_remaining - 1
                        print('You have no warnings remaining.')
                        print('You will now lose guesses instead.')
                        print(get_guessed_word(secret_word, letters_guessed))
                        print('----------------------------------------------')
                        break
                    else: # if the user has more than one guess remaining
                        letters_guessed += letter
                        num_warn = num_warn - 1
                        print('You now have', num_warn, 'warnings left:')
                        print(get_guessed_word(secret_word, letters_guessed))
                        print('----------------------------------------------')
                        break
                    break
                else: # if the guessed letter has not already been guessed
                    letters_guessed += letter # add it to guessed letters as 
                    # the guessed letter is in the secret word
                    if is_word_guessed(secret_word, letters_guessed) is True:
                    # if all guessed letters match the secret word
                        print('Good guess:', get_guessed_word(secret_word,
                                                              letters_guessed))
                        return winning # end game with congratulations message 
                        # and score
                    else: # if all the guessed letters do not match the word
                        print('Good guess:', get_guessed_word(secret_word,
                                                              letters_guessed))
                        break
                    break
                break
            break
        elif is_letter_in_word(secret_word, letter) is False:
            # if the guessed letter is not in the secret word
            for c in letter: 
                if c in letters_guessed: # if the guessed letter has already 
                    # been guessed
                    print('Oops! You have already guessed that letter!')
                    if num_warn == 0: # if the user has run out of warnings
                        guesses_remaining = guesses_remaining - 1
                        print('You have no warnings remaining.')
                        print('You will now lose guesses instead.')
                        print(get_guessed_word(secret_word, letters_guessed))
                        print('----------------------------------------------')
                        break
                    else: # if the user has more than one guess remaining
                        letters_guessed += letter
                        num_warn = num_warn - 1
                        print('You now have', num_warn, 'warnings left:')
                        print(get_guessed_word(secret_word, letters_guessed))
                        print('----------------------------------------------')
                        break
                        break
                else: # if the letter has not already been guessed
                    letters_guessed += letter # add it to guessed letters
                    print('Oops! That letter is not in my word!', 
                          get_guessed_word(secret_word, letters_guessed))
                        # because the guessed letter is not in the secret word
                    if is_letter_vowel(letter) is True: # if a vowel
                        guesses_remaining = guesses_remaining - 2 
                        # minus two from the number of guesses
                    else: # if not a vowel
                        guesses_remaining = guesses_remaining - 1 
                        # minus one from the number of guesses
                        break
                    break
                break
            break
        break
    else: # if the guessed character is not a valid letter
        letters_guessed += letter
        if num_warn == 0: # if the user has run out of warnings
            guesses_remaining = guesses_remaining - 1
            print('You have no warnings remaining.')
            print('You will now lose guesses instead.')
            print(get_guessed_word(secret_word, letters_guessed))
            print('------------------------------------------------------')
        else: # if the user has warnings remaining
            num_warn = num_warn - 1
            print('Oops! That is not a valid letter. You have', num_warn,
                  'warnings left:', get_guessed_word(secret_word, 
                                                     letters_guessed))
            print('------------------------------------------------------')
    # end of fifth run
    
    if int(guesses_remaining <= 0):
        return losing
    print('You have', guesses_remaining, 'guesses left')
    if num_warn >= 1:
        print('You have', num_warn, 'warnings left')
    print('Available letters:', get_available_letters(letters_guessed))
    letter = input('Please guess a letter:')
    
    # sixth run
    while is_letter_valid(letter) is True: # while the guessed character is a
        # valid letter
        if is_letter_in_word(secret_word, letter) is True:
            # if the guessed letter is in the secret word
            for c in letter: 
                if c in letters_guessed: 
                    # if the guessed letter has already been guessed
                    print('Oops! You have already guessed that letter!')
                    if num_warn == 0: # if the user has run out of warnings
                        guesses_remaining = guesses_remaining - 1
                        print('You have no warnings remaining.')
                        print('You will now lose guesses instead.')
                        print(get_guessed_word(secret_word, letters_guessed))
                        print('----------------------------------------------')
                        break
                    else: # if the user has more than one guess remaining
                        letters_guessed += letter
                        num_warn = num_warn - 1
                        print('You now have', num_warn, 'warnings left:')
                        print(get_guessed_word(secret_word, letters_guessed))
                        print('----------------------------------------------')
                        break
                    break
                else: # if the guessed letter has not already been guessed
                    letters_guessed += letter # add it to guessed letters as 
                    # the guessed letter is in the secret word
                    if is_word_guessed(secret_word, letters_guessed) is True:
                    # if all guessed letters match the secret word
                        print('Good guess:', get_guessed_word(secret_word,
                                                              letters_guessed))
                        return winning # end game with congratulations message 
                        # and score
                    else: # if all the guessed letters do not match the word
                        print('Good guess:', get_guessed_word(secret_word,
                                                              letters_guessed))
                        break
                    break
                break
            break
        elif is_letter_in_word(secret_word, letter) is False:
            # if the guessed letter is not in the secret word
            for c in letter: 
                if c in letters_guessed: # if the guessed letter has already 
                    # been guessed
                    print('Oops! You have already guessed that letter!')
                    if num_warn == 0: # if the user has run out of warnings
                        guesses_remaining = guesses_remaining - 1
                        print('You have no warnings remaining.')
                        print('You will now lose guesses instead.')
                        print(get_guessed_word(secret_word, letters_guessed))
                        print('----------------------------------------------')
                        break
                    else: # if the user has more than one guess remaining
                        letters_guessed += letter
                        num_warn = num_warn - 1
                        print('You now have', num_warn, 'warnings left:')
                        print(get_guessed_word(secret_word, letters_guessed))
                        print('----------------------------------------------')
                        break
                        break
                else: # if the letter has not already been guessed
                    letters_guessed += letter # add it to guessed letters
                    print('Oops! That letter is not in my word!', 
                          get_guessed_word(secret_word, letters_guessed))
                        # because the guessed letter is not in the secret word
                    if is_letter_vowel(letter) is True: # if a vowel
                        guesses_remaining = guesses_remaining - 2 
                        # minus two from the number of guesses
                    else: # if not a vowel
                        guesses_remaining = guesses_remaining - 1 
                        # minus one from the number of guesses
                        break
                    break
                break
            break
        break
    else: # if the guessed character is not a valid letter
        letters_guessed += letter
        if num_warn == 0: # if the user has run out of warnings
            guesses_remaining = guesses_remaining - 1
            print('You have no warnings remaining.')
            print('You will now lose guesses instead.')
            print(get_guessed_word(secret_word, letters_guessed))
            print('------------------------------------------------------')
        else: # if the user has warnings remaining
            num_warn = num_warn - 1
            print('Oops! That is not a valid letter. You have', num_warn,
                  'warnings left:', get_guessed_word(secret_word, 
                                                     letters_guessed))
            print('------------------------------------------------------')
    # end of sixth run
    
    if int(guesses_remaining <= 0):
        return losing
    print('You have', guesses_remaining, 'guesses left')
    if num_warn >= 1:
        print('You have', num_warn, 'warnings left')
    print('Available letters:', get_available_letters(letters_guessed))
    letter = input('Please guess a letter:')
    
    # seventh run
    while is_letter_valid(letter) is True: # while the guessed character is a
        # valid letter
        if is_letter_in_word(secret_word, letter) is True:
            # if the guessed letter is in the secret word
            for c in letter: 
                if c in letters_guessed: 
                    # if the guessed letter has already been guessed
                    print('Oops! You have already guessed that letter!')
                    if num_warn == 0: # if the user has run out of warnings
                        guesses_remaining = guesses_remaining - 1
                        print('You have no warnings remaining.')
                        print('You will now lose guesses instead.')
                        print(get_guessed_word(secret_word, letters_guessed))
                        print('----------------------------------------------')
                        break
                    else: # if the user has more than one guess remaining
                        letters_guessed += letter
                        num_warn = num_warn - 1
                        print('You now have', num_warn, 'warnings left:')
                        print(get_guessed_word(secret_word, letters_guessed))
                        print('----------------------------------------------')
                        break
                    break
                else: # if the guessed letter has not already been guessed
                    letters_guessed += letter # add it to guessed letters as 
                    # the guessed letter is in the secret word
                    if is_word_guessed(secret_word, letters_guessed) is True:
                    # if all guessed letters match the secret word
                        print('Good guess:', get_guessed_word(secret_word,
                                                              letters_guessed))
                        return winning # end game with congratulations message 
                        # and score
                    else: # if all the guessed letters do not match the word
                        print('Good guess:', get_guessed_word(secret_word,
                                                              letters_guessed))
                        break
                    break
                break
            break
        elif is_letter_in_word(secret_word, letter) is False:
            # if the guessed letter is not in the secret word
            for c in letter: 
                if c in letters_guessed: # if the guessed letter has already 
                    # been guessed
                    print('Oops! You have already guessed that letter!')
                    if num_warn == 0: # if the user has run out of warnings
                        guesses_remaining = guesses_remaining - 1
                        print('You have no warnings remaining.')
                        print('You will now lose guesses instead.')
                        print(get_guessed_word(secret_word, letters_guessed))
                        print('----------------------------------------------')
                        break
                    else: # if the user has more than one guess remaining
                        letters_guessed += letter
                        num_warn = num_warn - 1
                        print('You now have', num_warn, 'warnings left:')
                        print(get_guessed_word(secret_word, letters_guessed))
                        print('----------------------------------------------')
                        break
                        break
                else: # if the letter has not already been guessed
                    letters_guessed += letter # add it to guessed letters
                    print('Oops! That letter is not in my word!', 
                          get_guessed_word(secret_word, letters_guessed))
                        # because the guessed letter is not in the secret word
                    if is_letter_vowel(letter) is True: # if a vowel
                        guesses_remaining = guesses_remaining - 2 
                        # minus two from the number of guesses
                    else: # if not a vowel
                        guesses_remaining = guesses_remaining - 1 
                        # minus one from the number of guesses
                        break
                    break
                break
            break
        break
    else: # if the guessed character is not a valid letter
        letters_guessed += letter
        if num_warn == 0: # if the user has run out of warnings
            guesses_remaining = guesses_remaining - 1
            print('You have no warnings remaining.')
            print('You will now lose guesses instead.')
            print(get_guessed_word(secret_word, letters_guessed))
            print('------------------------------------------------------')
        else: # if the user has warnings remaining
            num_warn = num_warn - 1
            print('Oops! That is not a valid letter. You have', num_warn,
                  'warnings left:', get_guessed_word(secret_word, 
                                                     letters_guessed))
            print('------------------------------------------------------')
    # end of seventh run
    
    if int(guesses_remaining <= 0):
        return losing
    print('You have', guesses_remaining, 'guesses left')
    if num_warn >= 1:
        print('You have', num_warn, 'warnings left')
    print('Available letters:', get_available_letters(letters_guessed))
    letter = input('Please guess a letter:')
    
    # eighth run
    while is_letter_valid(letter) is True: # while the guessed character is a
        # valid letter
        if is_letter_in_word(secret_word, letter) is True:
            # if the guessed letter is in the secret word
            for c in letter: 
                if c in letters_guessed: 
                    # if the guessed letter has already been guessed
                    print('Oops! You have already guessed that letter!')
                    if num_warn == 0: # if the user has run out of warnings
                        guesses_remaining = guesses_remaining - 1
                        print('You have no warnings remaining.')
                        print('You will now lose guesses instead.')
                        print(get_guessed_word(secret_word, letters_guessed))
                        print('----------------------------------------------')
                        break
                    else: # if the user has more than one guess remaining
                        letters_guessed += letter
                        num_warn = num_warn - 1
                        print('You now have', num_warn, 'warnings left:')
                        print(get_guessed_word(secret_word, letters_guessed))
                        print('----------------------------------------------')
                        break
                    break
                else: # if the guessed letter has not already been guessed
                    letters_guessed += letter # add it to guessed letters as 
                    # the guessed letter is in the secret word
                    if is_word_guessed(secret_word, letters_guessed) is True:
                    # if all guessed letters match the secret word
                        print('Good guess:', get_guessed_word(secret_word,
                                                              letters_guessed))
                        return winning # end game with congratulations message 
                        # and score
                    else: # if all the guessed letters do not match the word
                        print('Good guess:', get_guessed_word(secret_word,
                                                              letters_guessed))
                        break
                    break
                break
            break
        elif is_letter_in_word(secret_word, letter) is False:
            # if the guessed letter is not in the secret word
            for c in letter: 
                if c in letters_guessed: # if the guessed letter has already 
                    # been guessed
                    print('Oops! You have already guessed that letter!')
                    if num_warn == 0: # if the user has run out of warnings
                        guesses_remaining = guesses_remaining - 1
                        print('You have no warnings remaining.')
                        print('You will now lose guesses instead.')
                        print(get_guessed_word(secret_word, letters_guessed))
                        print('----------------------------------------------')
                        break
                    else: # if the user has more than one guess remaining
                        letters_guessed += letter
                        num_warn = num_warn - 1
                        print('You now have', num_warn, 'warnings left:')
                        print(get_guessed_word(secret_word, letters_guessed))
                        print('----------------------------------------------')
                        break
                        break
                else: # if the letter has not already been guessed
                    letters_guessed += letter # add it to guessed letters
                    print('Oops! That letter is not in my word!', 
                          get_guessed_word(secret_word, letters_guessed))
                        # because the guessed letter is not in the secret word
                    if is_letter_vowel(letter) is True: # if a vowel
                        guesses_remaining = guesses_remaining - 2 
                        # minus two from the number of guesses
                    else: # if not a vowel
                        guesses_remaining = guesses_remaining - 1 
                        # minus one from the number of guesses
                        break
                    break
                break
            break
        break
    else: # if the guessed character is not a valid letter
        letters_guessed += letter
        if num_warn == 0: # if the user has run out of warnings
            guesses_remaining = guesses_remaining - 1
            print('You have no warnings remaining.')
            print('You will now lose guesses instead.')
            print(get_guessed_word(secret_word, letters_guessed))
            print('------------------------------------------------------')
        else: # if the user has warnings remaining
            num_warn = num_warn - 1
            print('Oops! That is not a valid letter. You have', num_warn,
                  'warnings left:', get_guessed_word(secret_word, 
                                                     letters_guessed))
            print('------------------------------------------------------')
    # end of eighth run
    
    if int(guesses_remaining <= 0):
        return losing
    print('You have', guesses_remaining, 'guesses left')
    if num_warn >= 1:
        print('You have', num_warn, 'warnings left')
    print('Available letters:', get_available_letters(letters_guessed))
    letter = input('Please guess a letter:')
    
    # ninth run
    while is_letter_valid(letter) is True: # while the guessed character is a
        # valid letter
        if is_letter_in_word(secret_word, letter) is True:
            # if the guessed letter is in the secret word
            for c in letter: 
                if c in letters_guessed: 
                    # if the guessed letter has already been guessed
                    print('Oops! You have already guessed that letter!')
                    if num_warn == 0: # if the user has run out of warnings
                        guesses_remaining = guesses_remaining - 1
                        print('You have no warnings remaining.')
                        print('You will now lose guesses instead.')
                        print(get_guessed_word(secret_word, letters_guessed))
                        print('----------------------------------------------')
                        break
                    else: # if the user has more than one guess remaining
                        letters_guessed += letter
                        num_warn = num_warn - 1
                        print('You now have', num_warn, 'warnings left:')
                        print(get_guessed_word(secret_word, letters_guessed))
                        print('----------------------------------------------')
                        break
                    break
                else: # if the guessed letter has not already been guessed
                    letters_guessed += letter # add it to guessed letters as 
                    # the guessed letter is in the secret word
                    if is_word_guessed(secret_word, letters_guessed) is True:
                    # if all guessed letters match the secret word
                        print('Good guess:', get_guessed_word(secret_word,
                                                              letters_guessed))
                        return winning # end game with congratulations message 
                        # and score
                    else: # if all the guessed letters do not match the word
                        print('Good guess:', get_guessed_word(secret_word,
                                                              letters_guessed))
                        break
                    break
                break
            break
        elif is_letter_in_word(secret_word, letter) is False:
            # if the guessed letter is not in the secret word
            for c in letter: 
                if c in letters_guessed: # if the guessed letter has already 
                    # been guessed
                    print('Oops! You have already guessed that letter!')
                    if num_warn == 0: # if the user has run out of warnings
                        guesses_remaining = guesses_remaining - 1
                        print('You have no warnings remaining.')
                        print('You will now lose guesses instead.')
                        print(get_guessed_word(secret_word, letters_guessed))
                        print('----------------------------------------------')
                        break
                    else: # if the user has more than one guess remaining
                        letters_guessed += letter
                        num_warn = num_warn - 1
                        print('You now have', num_warn, 'warnings left:')
                        print(get_guessed_word(secret_word, letters_guessed))
                        print('----------------------------------------------')
                        break
                        break
                else: # if the letter has not already been guessed
                    letters_guessed += letter # add it to guessed letters
                    print('Oops! That letter is not in my word!', 
                          get_guessed_word(secret_word, letters_guessed))
                        # because the guessed letter is not in the secret word
                    if is_letter_vowel(letter) is True: # if a vowel
                        guesses_remaining = guesses_remaining - 2 
                        # minus two from the number of guesses
                    else: # if not a vowel
                        guesses_remaining = guesses_remaining - 1 
                        # minus one from the number of guesses
                        break
                    break
                break
            break
        break
    else: # if the guessed character is not a valid letter
        letters_guessed += letter
        if num_warn == 0: # if the user has run out of warnings
            guesses_remaining = guesses_remaining - 1
            print('You have no warnings remaining.')
            print('You will now lose guesses instead.')
            print(get_guessed_word(secret_word, letters_guessed))
            print('------------------------------------------------------')
        else: # if the user has warnings remaining
            num_warn = num_warn - 1
            print('Oops! That is not a valid letter. You have', num_warn,
                  'warnings left:', get_guessed_word(secret_word, 
                                                     letters_guessed))
            print('------------------------------------------------------')
    # end of ninth run
    
    if guesses_remaining <= 0:
        return losing
    print('You have', guesses_remaining, 'guesses left')
    if num_warn >= 1:
        print('You have', num_warn, 'warnings left')
    print('Available letters:', get_available_letters(letters_guessed))
    letter = input('Please guess a letter:')
    
    # tenth run
    while is_letter_valid(letter) is True: # while the guessed character is a
        # valid letter
        if is_letter_in_word(secret_word, letter) is True:
            # if the guessed letter is in the secret word
            for c in letter: 
                if c in letters_guessed: 
                    # if the guessed letter has already been guessed
                    print('Oops! You have already guessed that letter!')
                    if num_warn == 0: # if the user has run out of warnings
                        guesses_remaining = guesses_remaining - 1
                        print('You have no warnings remaining.')
                        print('You will now lose guesses instead.')
                        print(get_guessed_word(secret_word, letters_guessed))
                        print('----------------------------------------------')
                        break
                    else: # if the user has more than one guess remaining
                        letters_guessed += letter
                        num_warn = num_warn - 1
                        print('You now have', num_warn, 'warnings left:')
                        print(get_guessed_word(secret_word, letters_guessed))
                        print('----------------------------------------------')
                        break
                    break
                else: # if the guessed letter has not already been guessed
                    letters_guessed += letter # add it to guessed letters as 
                    # the guessed letter is in the secret word
                    if is_word_guessed(secret_word, letters_guessed) is True:
                    # if all guessed letters match the secret word
                        print('Good guess:', get_guessed_word(secret_word,
                                                              letters_guessed))
                        return winning # end game with congratulations message 
                        # and score
                    else: # if all the guessed letters do not match the word
                        print('Good guess:', get_guessed_word(secret_word,
                                                              letters_guessed))
                        break
                    break
                break
            break
        elif is_letter_in_word(secret_word, letter) is False:
            # if the guessed letter is not in the secret word
            for c in letter: 
                if c in letters_guessed: # if the guessed letter has already 
                    # been guessed
                    print('Oops! You have already guessed that letter!')
                    if num_warn == 0: # if the user has run out of warnings
                        guesses_remaining = guesses_remaining - 1
                        print('You have no warnings remaining.')
                        print('You will now lose guesses instead.')
                        print(get_guessed_word(secret_word, letters_guessed))
                        print('----------------------------------------------')
                        break
                    else: # if the user has more than one guess remaining
                        letters_guessed += letter
                        num_warn = num_warn - 1
                        print('You now have', num_warn, 'warnings left:')
                        print(get_guessed_word(secret_word, letters_guessed))
                        print('----------------------------------------------')
                        break
                        break
                else: # if the letter has not already been guessed
                    letters_guessed += letter # add it to guessed letters
                    print('Oops! That letter is not in my word!', 
                          get_guessed_word(secret_word, letters_guessed))
                        # because the guessed letter is not in the secret word
                    if is_letter_vowel(letter) is True: # if a vowel
                        guesses_remaining = guesses_remaining - 2 
                        # minus two from the number of guesses
                    else: # if not a vowel
                        guesses_remaining = guesses_remaining - 1 
                        # minus one from the number of guesses
                        break
                    break
                break
            break
        break
    else: # if the guessed character is not a valid letter
        letters_guessed += letter
        if num_warn == 0: # if the user has run out of warnings
            guesses_remaining = guesses_remaining - 1
            print('You have no warnings remaining.')
            print('You will now lose guesses instead.')
            print(get_guessed_word(secret_word, letters_guessed))
            print('------------------------------------------------------')
        else: # if the user has warnings remaining
            num_warn = num_warn - 1
            print('Oops! That is not a valid letter. You have', num_warn,
                  'warnings left:', get_guessed_word(secret_word, 
                                                     letters_guessed))
            print('------------------------------------------------------')
    # end of tenth run
    
    if int(guesses_remaining <= 0):
        return losing
    print('You have', guesses_remaining, 'guesses left')
    if num_warn >= 1:
        print('You have', num_warn, 'warnings left')
    print('Available letters:', get_available_letters(letters_guessed))
    letter = input('Please guess a letter:')
    
    # eleventh run
    while is_letter_valid(letter) is True: # while the guessed character is a
        # valid letter
        if is_letter_in_word(secret_word, letter) is True:
            # if the guessed letter is in the secret word
            for c in letter: 
                if c in letters_guessed: 
                    # if the guessed letter has already been guessed
                    print('Oops! You have already guessed that letter!')
                    if num_warn == 0: # if the user has run out of warnings
                        guesses_remaining = guesses_remaining - 1
                        print('You have no warnings remaining.')
                        print('You will now lose guesses instead.')
                        print(get_guessed_word(secret_word, letters_guessed))
                        print('----------------------------------------------')
                        break
                    else: # if the user has more than one guess remaining
                        letters_guessed += letter
                        num_warn = num_warn - 1
                        print('You now have', num_warn, 'warnings left:')
                        print(get_guessed_word(secret_word, letters_guessed))
                        print('----------------------------------------------')
                        break
                    break
                else: # if the guessed letter has not already been guessed
                    letters_guessed += letter # add it to guessed letters as 
                    # the guessed letter is in the secret word
                    if is_word_guessed(secret_word, letters_guessed) is True:
                    # if all guessed letters match the secret word
                        print('Good guess:', get_guessed_word(secret_word,
                                                              letters_guessed))
                        return winning # end game with congratulations message 
                        # and score
                    else: # if all the guessed letters do not match the word
                        print('Good guess:', get_guessed_word(secret_word,
                                                              letters_guessed))
                        break
                    break
                break
            break
        elif is_letter_in_word(secret_word, letter) is False:
            # if the guessed letter is not in the secret word
            for c in letter: 
                if c in letters_guessed: # if the guessed letter has already 
                    # been guessed
                    print('Oops! You have already guessed that letter!')
                    if num_warn == 0: # if the user has run out of warnings
                        guesses_remaining = guesses_remaining - 1
                        print('You have no warnings remaining.')
                        print('You will now lose guesses instead.')
                        print(get_guessed_word(secret_word, letters_guessed))
                        print('----------------------------------------------')
                        break
                    else: # if the user has more than one guess remaining
                        letters_guessed += letter
                        num_warn = num_warn - 1
                        print('You now have', num_warn, 'warnings left:')
                        print(get_guessed_word(secret_word, letters_guessed))
                        print('----------------------------------------------')
                        break
                        break
                else: # if the letter has not already been guessed
                    letters_guessed += letter # add it to guessed letters
                    print('Oops! That letter is not in my word!', 
                          get_guessed_word(secret_word, letters_guessed))
                        # because the guessed letter is not in the secret word
                    if is_letter_vowel(letter) is True: # if a vowel
                        guesses_remaining = guesses_remaining - 2 
                        # minus two from the number of guesses
                    else: # if not a vowel
                        guesses_remaining = guesses_remaining - 1 
                        # minus one from the number of guesses
                        break
                    break
                break
            break
        break
    else: # if the guessed character is not a valid letter
        letters_guessed += letter
        if num_warn == 0: # if the user has run out of warnings
            guesses_remaining = guesses_remaining - 1
            print('You have no warnings remaining.')
            print('You will now lose guesses instead.')
            print(get_guessed_word(secret_word, letters_guessed))
            print('------------------------------------------------------')
        else: # if the user has warnings remaining
            num_warn = num_warn - 1
            print('Oops! That is not a valid letter. You have', num_warn,
                  'warnings left:', get_guessed_word(secret_word, 
                                                     letters_guessed))
            print('------------------------------------------------------')
    # end of eleventh run
    
    if int(guesses_remaining <= 0):
        return losing
    print('You have', guesses_remaining, 'guesses left')
    if num_warn >= 1:
        print('You have', num_warn, 'warnings left')
    print('Available letters:', get_available_letters(letters_guessed))
    letter = input('Please guess a letter:')
    
    # twelth run
    while is_letter_valid(letter) is True: # while the guessed character is a
        # valid letter
        if is_letter_in_word(secret_word, letter) is True:
            # if the guessed letter is in the secret word
            for c in letter: 
                if c in letters_guessed: 
                    # if the guessed letter has already been guessed
                    print('Oops! You have already guessed that letter!')
                    if num_warn == 0: # if the user has run out of warnings
                        guesses_remaining = guesses_remaining - 1
                        print('You have no warnings remaining.')
                        print('You will now lose guesses instead.')
                        print(get_guessed_word(secret_word, letters_guessed))
                        print('----------------------------------------------')
                        break
                    else: # if the user has more than one guess remaining
                        letters_guessed += letter
                        num_warn = num_warn - 1
                        print('You now have', num_warn, 'warnings left:')
                        print(get_guessed_word(secret_word, letters_guessed))
                        print('----------------------------------------------')
                        break
                    break
                else: # if the guessed letter has not already been guessed
                    letters_guessed += letter # add it to guessed letters as 
                    # the guessed letter is in the secret word
                    if is_word_guessed(secret_word, letters_guessed) is True:
                    # if all guessed letters match the secret word
                        print('Good guess:', get_guessed_word(secret_word,
                                                              letters_guessed))
                        return winning # end game with congratulations message 
                        # and score
                    else: # if all the guessed letters do not match the word
                        print('Good guess:', get_guessed_word(secret_word,
                                                              letters_guessed))
                        break
                    break
                break
            break
        elif is_letter_in_word(secret_word, letter) is False:
            # if the guessed letter is not in the secret word
            for c in letter: 
                if c in letters_guessed: # if the guessed letter has already 
                    # been guessed
                    print('Oops! You have already guessed that letter!')
                    if num_warn == 0: # if the user has run out of warnings
                        guesses_remaining = guesses_remaining - 1
                        print('You have no warnings remaining.')
                        print('You will now lose guesses instead.')
                        print(get_guessed_word(secret_word, letters_guessed))
                        print('----------------------------------------------')
                        break
                    else: # if the user has more than one guess remaining
                        letters_guessed += letter
                        num_warn = num_warn - 1
                        print('You now have', num_warn, 'warnings left:')
                        print(get_guessed_word(secret_word, letters_guessed))
                        print('----------------------------------------------')
                        break
                        break
                else: # if the letter has not already been guessed
                    letters_guessed += letter # add it to guessed letters
                    print('Oops! That letter is not in my word!', 
                          get_guessed_word(secret_word, letters_guessed))
                        # because the guessed letter is not in the secret word
                    if is_letter_vowel(letter) is True: # if a vowel
                        guesses_remaining = guesses_remaining - 2 
                        # minus two from the number of guesses
                    else: # if not a vowel
                        guesses_remaining = guesses_remaining - 1 
                        # minus one from the number of guesses
                        break
                    break
                break
            break
        break
    else: # if the guessed character is not a valid letter
        letters_guessed += letter
        if num_warn == 0: # if the user has run out of warnings
            guesses_remaining = guesses_remaining - 1
            print('You have no warnings remaining.')
            print('You will now lose guesses instead.')
            print(get_guessed_word(secret_word, letters_guessed))
            print('------------------------------------------------------')
        else: # if the user has warnings remaining
            num_warn = num_warn - 1
            print('Oops! That is not a valid letter. You have', num_warn,
                  'warnings left:', get_guessed_word(secret_word, 
                                                     letters_guessed))
            print('------------------------------------------------------')
    # end of twelth run
    
    if int(guesses_remaining <= 0):
        return losing
    print('You have', guesses_remaining, 'guesses left')
    if num_warn >= 1:
        print('You have', num_warn, 'warnings left')
    print('Available letters:', get_available_letters(letters_guessed))
    letter = input('Please guess a letter:')
    
    # thirteenth run
    while is_letter_valid(letter) is True: # while the guessed character is a
        # valid letter
        if is_letter_in_word(secret_word, letter) is True:
            # if the guessed letter is in the secret word
            for c in letter: 
                if c in letters_guessed: 
                    # if the guessed letter has already been guessed
                    print('Oops! You have already guessed that letter!')
                    if num_warn == 0: # if the user has run out of warnings
                        guesses_remaining = guesses_remaining - 1
                        print('You have no warnings remaining.')
                        print('You will now lose guesses instead.')
                        print(get_guessed_word(secret_word, letters_guessed))
                        print('----------------------------------------------')
                        break
                    else: # if the user has more than one guess remaining
                        letters_guessed += letter
                        num_warn = num_warn - 1
                        print('You now have', num_warn, 'warnings left:')
                        print(get_guessed_word(secret_word, letters_guessed))
                        print('----------------------------------------------')
                        break
                    break
                else: # if the guessed letter has not already been guessed
                    letters_guessed += letter # add it to guessed letters as 
                    # the guessed letter is in the secret word
                    if is_word_guessed(secret_word, letters_guessed) is True:
                    # if all guessed letters match the secret word
                        print('Good guess:', get_guessed_word(secret_word,
                                                              letters_guessed))
                        return winning # end game with congratulations message 
                        # and score
                    else: # if all the guessed letters do not match the word
                        print('Good guess:', get_guessed_word(secret_word,
                                                              letters_guessed))
                        break
                    break
                break
            break
        elif is_letter_in_word(secret_word, letter) is False:
            # if the guessed letter is not in the secret word
            for c in letter: 
                if c in letters_guessed: # if the guessed letter has already 
                    # been guessed
                    print('Oops! You have already guessed that letter!')
                    if num_warn == 0: # if the user has run out of warnings
                        guesses_remaining = guesses_remaining - 1
                        print('You have no warnings remaining.')
                        print('You will now lose guesses instead.')
                        print(get_guessed_word(secret_word, letters_guessed))
                        print('----------------------------------------------')
                        break
                    else: # if the user has more than one guess remaining
                        letters_guessed += letter
                        num_warn = num_warn - 1
                        print('You now have', num_warn, 'warnings left:')
                        print(get_guessed_word(secret_word, letters_guessed))
                        print('----------------------------------------------')
                        break
                        break
                else: # if the letter has not already been guessed
                    letters_guessed += letter # add it to guessed letters
                    print('Oops! That letter is not in my word!', 
                          get_guessed_word(secret_word, letters_guessed))
                        # because the guessed letter is not in the secret word
                    if is_letter_vowel(letter) is True: # if a vowel
                        guesses_remaining = guesses_remaining - 2 
                        # minus two from the number of guesses
                    else: # if not a vowel
                        guesses_remaining = guesses_remaining - 1 
                        # minus one from the number of guesses
                        break
                    break
                break
            break
        break
    else: # if the guessed character is not a valid letter
        letters_guessed += letter
        if num_warn == 0: # if the user has run out of warnings
            guesses_remaining = guesses_remaining - 1
            print('You have no warnings remaining.')
            print('You will now lose guesses instead.')
            print(get_guessed_word(secret_word, letters_guessed))
            print('------------------------------------------------------')
        else: # if the user has warnings remaining
            num_warn = num_warn - 1
            print('Oops! That is not a valid letter. You have', num_warn,
                  'warnings left:', get_guessed_word(secret_word, 
                                                     letters_guessed))
            print('------------------------------------------------------')
    # end of thirteenth run
    
    if int(guesses_remaining <= 0):
        return losing
    print('You have', guesses_remaining, 'guesses left')
    if num_warn >= 1:
        print('You have', num_warn, 'warnings left')
    print('Available letters:', get_available_letters(letters_guessed))
    letter = input('Please guess a letter:')
    
    # fourteenth run
    while is_letter_valid(letter) is True: # while the guessed character is a
        # valid letter
        if is_letter_in_word(secret_word, letter) is True:
            # if the guessed letter is in the secret word
            for c in letter: 
                if c in letters_guessed: 
                    # if the guessed letter has already been guessed
                    print('Oops! You have already guessed that letter!')
                    if num_warn == 0: # if the user has run out of warnings
                        guesses_remaining = guesses_remaining - 1
                        print('You have no warnings remaining.')
                        print('You will now lose guesses instead.')
                        print(get_guessed_word(secret_word, letters_guessed))
                        print('----------------------------------------------')
                        break
                    else: # if the user has more than one guess remaining
                        letters_guessed += letter
                        num_warn = num_warn - 1
                        print('You now have', num_warn, 'warnings left:')
                        print(get_guessed_word(secret_word, letters_guessed))
                        print('----------------------------------------------')
                        break
                    break
                else: # if the guessed letter has not already been guessed
                    letters_guessed += letter # add it to guessed letters as 
                    # the guessed letter is in the secret word
                    if is_word_guessed(secret_word, letters_guessed) is True:
                    # if all guessed letters match the secret word
                        print('Good guess:', get_guessed_word(secret_word,
                                                              letters_guessed))
                        return winning # end game with congratulations message 
                        # and score
                    else: # if all the guessed letters do not match the word
                        print('Good guess:', get_guessed_word(secret_word,
                                                              letters_guessed))
                        break
                    break
                break
            break
        elif is_letter_in_word(secret_word, letter) is False:
            # if the guessed letter is not in the secret word
            for c in letter: 
                if c in letters_guessed: # if the guessed letter has already 
                    # been guessed
                    print('Oops! You have already guessed that letter!')
                    if num_warn == 0: # if the user has run out of warnings
                        guesses_remaining = guesses_remaining - 1
                        print('You have no warnings remaining.')
                        print('You will now lose guesses instead.')
                        print(get_guessed_word(secret_word, letters_guessed))
                        print('----------------------------------------------')
                        break
                    else: # if the user has more than one guess remaining
                        letters_guessed += letter
                        num_warn = num_warn - 1
                        print('You now have', num_warn, 'warnings left:')
                        print(get_guessed_word(secret_word, letters_guessed))
                        print('----------------------------------------------')
                        break
                        break
                else: # if the letter has not already been guessed
                    letters_guessed += letter # add it to guessed letters
                    print('Oops! That letter is not in my word!', 
                          get_guessed_word(secret_word, letters_guessed))
                        # because the guessed letter is not in the secret word
                    if is_letter_vowel(letter) is True: # if a vowel
                        guesses_remaining = guesses_remaining - 2 
                        # minus two from the number of guesses
                    else: # if not a vowel
                        guesses_remaining = guesses_remaining - 1 
                        # minus one from the number of guesses
                        break
                    break
                break
            break
        break
    else: # if the guessed character is not a valid letter
        letters_guessed += letter
        if num_warn == 0: # if the user has run out of warnings
            guesses_remaining = guesses_remaining - 1
            print('You have no warnings remaining.')
            print('You will now lose guesses instead.')
            print(get_guessed_word(secret_word, letters_guessed))
            print('------------------------------------------------------')
        else: # if the user has warnings remaining
            num_warn = num_warn - 1
            print('Oops! That is not a valid letter. You have', num_warn,
                  'warnings left:', get_guessed_word(secret_word, 
                                                     letters_guessed))
            print('------------------------------------------------------')
    # end of fourteenth run
    
    if int(guesses_remaining <= 0):
        return losing
    print('You have', guesses_remaining, 'guesses left')
    if num_warn >= 1:
        print('You have', num_warn, 'warnings left')
    print('Available letters:', get_available_letters(letters_guessed))
    letter = input('Please guess a letter:')
    
    # fifteenth run
    while is_letter_valid(letter) is True: # while the guessed character is a
        # valid letter
        if is_letter_in_word(secret_word, letter) is True:
            # if the guessed letter is in the secret word
            for c in letter: 
                if c in letters_guessed: 
                    # if the guessed letter has already been guessed
                    print('Oops! You have already guessed that letter!')
                    if num_warn == 0: # if the user has run out of warnings
                        guesses_remaining = guesses_remaining - 1
                        print('You have no warnings remaining.')
                        print('You will now lose guesses instead.')
                        print(get_guessed_word(secret_word, letters_guessed))
                        print('----------------------------------------------')
                        break
                    else: # if the user has more than one guess remaining
                        letters_guessed += letter
                        num_warn = num_warn - 1
                        print('You now have', num_warn, 'warnings left:')
                        print(get_guessed_word(secret_word, letters_guessed))
                        print('----------------------------------------------')
                        break
                    break
                else: # if the guessed letter has not already been guessed
                    letters_guessed += letter # add it to guessed letters as 
                    # the guessed letter is in the secret word
                    if is_word_guessed(secret_word, letters_guessed) is True:
                    # if all guessed letters match the secret word
                        print('Good guess:', get_guessed_word(secret_word,
                                                              letters_guessed))
                        return winning # end game with congratulations message 
                        # and score
                    else: # if all the guessed letters do not match the word
                        print('Good guess:', get_guessed_word(secret_word,
                                                              letters_guessed))
                        break
                    break
                break
            break
        elif is_letter_in_word(secret_word, letter) is False:
            # if the guessed letter is not in the secret word
            for c in letter: 
                if c in letters_guessed: # if the guessed letter has already 
                    # been guessed
                    print('Oops! You have already guessed that letter!')
                    if num_warn == 0: # if the user has run out of warnings
                        guesses_remaining = guesses_remaining - 1
                        print('You have no warnings remaining.')
                        print('You will now lose guesses instead.')
                        print(get_guessed_word(secret_word, letters_guessed))
                        print('----------------------------------------------')
                        break
                    else: # if the user has more than one guess remaining
                        letters_guessed += letter
                        num_warn = num_warn - 1
                        print('You now have', num_warn, 'warnings left:')
                        print(get_guessed_word(secret_word, letters_guessed))
                        print('----------------------------------------------')
                        break
                        break
                else: # if the letter has not already been guessed
                    letters_guessed += letter # add it to guessed letters
                    print('Oops! That letter is not in my word!', 
                          get_guessed_word(secret_word, letters_guessed))
                        # because the guessed letter is not in the secret word
                    if is_letter_vowel(letter) is True: # if a vowel
                        guesses_remaining = guesses_remaining - 2 
                        # minus two from the number of guesses
                    else: # if not a vowel
                        guesses_remaining = guesses_remaining - 1 
                        # minus one from the number of guesses
                        break
                    break
                break
            break
        break
    else: # if the guessed character is not a valid letter
        letters_guessed += letter
        if num_warn == 0: # if the user has run out of warnings
            guesses_remaining = guesses_remaining - 1
            print('You have no warnings remaining.')
            print('You will now lose guesses instead.')
            print(get_guessed_word(secret_word, letters_guessed))
            print('------------------------------------------------------')
        else: # if the user has warnings remaining
            num_warn = num_warn - 1
            print('Oops! That is not a valid letter. You have', num_warn,
                  'warnings left:', get_guessed_word(secret_word, 
                                                     letters_guessed))
            print('------------------------------------------------------')
    # end of fifteenth run
    
    if int(guesses_remaining <= 0):
        return losing
    print('You have', guesses_remaining, 'guesses left')
    if num_warn >= 1:
        print('You have', num_warn, 'warnings left')
    print('Available letters:', get_available_letters(letters_guessed))
    letter = input('Please guess a letter:')
    
    # sixteenth run
    while is_letter_valid(letter) is True: # while the guessed character is a
        # valid letter
        if is_letter_in_word(secret_word, letter) is True:
            # if the guessed letter is in the secret word
            for c in letter: 
                if c in letters_guessed: 
                    # if the guessed letter has already been guessed
                    print('Oops! You have already guessed that letter!')
                    if num_warn == 0: # if the user has run out of warnings
                        guesses_remaining = guesses_remaining - 1
                        print('You have no warnings remaining.')
                        print('You will now lose guesses instead.')
                        print(get_guessed_word(secret_word, letters_guessed))
                        print('----------------------------------------------')
                        break
                    else: # if the user has more than one guess remaining
                        letters_guessed += letter
                        num_warn = num_warn - 1
                        print('You now have', num_warn, 'warnings left:')
                        print(get_guessed_word(secret_word, letters_guessed))
                        print('----------------------------------------------')
                        break
                    break
                else: # if the guessed letter has not already been guessed
                    letters_guessed += letter # add it to guessed letters as 
                    # the guessed letter is in the secret word
                    if is_word_guessed(secret_word, letters_guessed) is True:
                    # if all guessed letters match the secret word
                        print('Good guess:', get_guessed_word(secret_word,
                                                              letters_guessed))
                        return winning # end game with congratulations message 
                        # and score
                    else: # if all the guessed letters do not match the word
                        print('Good guess:', get_guessed_word(secret_word,
                                                              letters_guessed))
                        break
                    break
                break
            break
        elif is_letter_in_word(secret_word, letter) is False:
            # if the guessed letter is not in the secret word
            for c in letter: 
                if c in letters_guessed: # if the guessed letter has already 
                    # been guessed
                    print('Oops! You have already guessed that letter!')
                    if num_warn == 0: # if the user has run out of warnings
                        guesses_remaining = guesses_remaining - 1
                        print('You have no warnings remaining.')
                        print('You will now lose guesses instead.')
                        print(get_guessed_word(secret_word, letters_guessed))
                        print('----------------------------------------------')
                        break
                    else: # if the user has more than one guess remaining
                        letters_guessed += letter
                        num_warn = num_warn - 1
                        print('You now have', num_warn, 'warnings left:')
                        print(get_guessed_word(secret_word, letters_guessed))
                        print('----------------------------------------------')
                        break
                        break
                else: # if the letter has not already been guessed
                    letters_guessed += letter # add it to guessed letters
                    print('Oops! That letter is not in my word!', 
                          get_guessed_word(secret_word, letters_guessed))
                        # because the guessed letter is not in the secret word
                    if is_letter_vowel(letter) is True: # if a vowel
                        guesses_remaining = guesses_remaining - 2 
                        # minus two from the number of guesses
                    else: # if not a vowel
                        guesses_remaining = guesses_remaining - 1 
                        # minus one from the number of guesses
                        break
                    break
                break
            break
        break
    else: # if the guessed character is not a valid letter
        letters_guessed += letter
        if num_warn == 0: # if the user has run out of warnings
            guesses_remaining = guesses_remaining - 1
            print('You have no warnings remaining.')
            print('You will now lose guesses instead.')
            print(get_guessed_word(secret_word, letters_guessed))
            print('------------------------------------------------------')
        else: # if the user has warnings remaining
            num_warn = num_warn - 1
            print('Oops! That is not a valid letter. You have', num_warn,
                  'warnings left:', get_guessed_word(secret_word, 
                                                     letters_guessed))
            print('------------------------------------------------------')
    # end of sixteenth run
    
    if int(guesses_remaining <= 0):
        return losing
    print('You have', guesses_remaining, 'guesses left')
    if num_warn >= 1:
        print('You have', num_warn, 'warnings left')
    print('Available letters:', get_available_letters(letters_guessed))
    letter = input('Please guess a letter:')
    
    # seventeenth run
    while is_letter_valid(letter) is True: # while the guessed character is a
        # valid letter
        if is_letter_in_word(secret_word, letter) is True:
            # if the guessed letter is in the secret word
            for c in letter: 
                if c in letters_guessed: 
                    # if the guessed letter has already been guessed
                    print('Oops! You have already guessed that letter!')
                    if num_warn == 0: # if the user has run out of warnings
                        guesses_remaining = guesses_remaining - 1
                        print('You have no warnings remaining.')
                        print('You will now lose guesses instead.')
                        print(get_guessed_word(secret_word, letters_guessed))
                        print('----------------------------------------------')
                        break
                    else: # if the user has more than one guess remaining
                        letters_guessed += letter
                        num_warn = num_warn - 1
                        print('You now have', num_warn, 'warnings left:')
                        print(get_guessed_word(secret_word, letters_guessed))
                        print('----------------------------------------------')
                        break
                    break
                else: # if the guessed letter has not already been guessed
                    letters_guessed += letter # add it to guessed letters as 
                    # the guessed letter is in the secret word
                    if is_word_guessed(secret_word, letters_guessed) is True:
                    # if all guessed letters match the secret word
                        print('Good guess:', get_guessed_word(secret_word,
                                                              letters_guessed))
                        return winning # end game with congratulations message 
                        # and score
                    else: # if all the guessed letters do not match the word
                        print('Good guess:', get_guessed_word(secret_word,
                                                              letters_guessed))
                        break
                    break
                break
            break
        elif is_letter_in_word(secret_word, letter) is False:
            # if the guessed letter is not in the secret word
            for c in letter: 
                if c in letters_guessed: # if the guessed letter has already 
                    # been guessed
                    print('Oops! You have already guessed that letter!')
                    if num_warn == 0: # if the user has run out of warnings
                        guesses_remaining = guesses_remaining - 1
                        print('You have no warnings remaining.')
                        print('You will now lose guesses instead.')
                        print(get_guessed_word(secret_word, letters_guessed))
                        print('----------------------------------------------')
                        break
                    else: # if the user has more than one guess remaining
                        letters_guessed += letter
                        num_warn = num_warn - 1
                        print('You now have', num_warn, 'warnings left:')
                        print(get_guessed_word(secret_word, letters_guessed))
                        print('----------------------------------------------')
                        break
                        break
                else: # if the letter has not already been guessed
                    letters_guessed += letter # add it to guessed letters
                    print('Oops! That letter is not in my word!', 
                          get_guessed_word(secret_word, letters_guessed))
                        # because the guessed letter is not in the secret word
                    if is_letter_vowel(letter) is True: # if a vowel
                        guesses_remaining = guesses_remaining - 2 
                        # minus two from the number of guesses
                    else: # if not a vowel
                        guesses_remaining = guesses_remaining - 1 
                        # minus one from the number of guesses
                        break
                    break
                break
            break
        break
    else: # if the guessed character is not a valid letter
        letters_guessed += letter
        if num_warn == 0: # if the user has run out of warnings
            guesses_remaining = guesses_remaining - 1
            print('You have no warnings remaining.')
            print('You will now lose guesses instead.')
            print(get_guessed_word(secret_word, letters_guessed))
            print('------------------------------------------------------')
        else: # if the user has warnings remaining
            num_warn = num_warn - 1
            print('Oops! That is not a valid letter. You have', num_warn,
                  'warnings left:', get_guessed_word(secret_word, 
                                                     letters_guessed))
            print('------------------------------------------------------')
    # end of seventeenth run
    
    if int(guesses_remaining <= 0):
        return losing
    print('You have', guesses_remaining, 'guesses left')
    if num_warn >= 1:
        print('You have', num_warn, 'warnings left')
    print('Available letters:', get_available_letters(letters_guessed))
    letter = input('Please guess a letter:')
    
    # eighteenth run
    while is_letter_valid(letter) is True: # while the guessed character is a
        # valid letter
        if is_letter_in_word(secret_word, letter) is True:
            # if the guessed letter is in the secret word
            for c in letter: 
                if c in letters_guessed: 
                    # if the guessed letter has already been guessed
                    print('Oops! You have already guessed that letter!')
                    if num_warn == 0: # if the user has run out of warnings
                        guesses_remaining = guesses_remaining - 1
                        print('You have no warnings remaining.')
                        print('You will now lose guesses instead.')
                        print(get_guessed_word(secret_word, letters_guessed))
                        print('----------------------------------------------')
                        break
                    else: # if the user has more than one guess remaining
                        letters_guessed += letter
                        num_warn = num_warn - 1
                        print('You now have', num_warn, 'warnings left:')
                        print(get_guessed_word(secret_word, letters_guessed))
                        print('----------------------------------------------')
                        break
                    break
                else: # if the guessed letter has not already been guessed
                    letters_guessed += letter # add it to guessed letters as 
                    # the guessed letter is in the secret word
                    if is_word_guessed(secret_word, letters_guessed) is True:
                    # if all guessed letters match the secret word
                        print('Good guess:', get_guessed_word(secret_word,
                                                              letters_guessed))
                        return winning # end game with congratulations message 
                        # and score
                    else: # if all the guessed letters do not match the word
                        print('Good guess:', get_guessed_word(secret_word,
                                                              letters_guessed))
                        break
                    break
                break
            break
        elif is_letter_in_word(secret_word, letter) is False:
            # if the guessed letter is not in the secret word
            for c in letter: 
                if c in letters_guessed: # if the guessed letter has already 
                    # been guessed
                    print('Oops! You have already guessed that letter!')
                    if num_warn == 0: # if the user has run out of warnings
                        guesses_remaining = guesses_remaining - 1
                        print('You have no warnings remaining.')
                        print('You will now lose guesses instead.')
                        print(get_guessed_word(secret_word, letters_guessed))
                        print('----------------------------------------------')
                        break
                    else: # if the user has more than one guess remaining
                        letters_guessed += letter
                        num_warn = num_warn - 1
                        print('You now have', num_warn, 'warnings left:')
                        print(get_guessed_word(secret_word, letters_guessed))
                        print('----------------------------------------------')
                        break
                        break
                else: # if the letter has not already been guessed
                    letters_guessed += letter # add it to guessed letters
                    print('Oops! That letter is not in my word!', 
                          get_guessed_word(secret_word, letters_guessed))
                        # because the guessed letter is not in the secret word
                    if is_letter_vowel(letter) is True: # if a vowel
                        guesses_remaining = guesses_remaining - 2 
                        # minus two from the number of guesses
                    else: # if not a vowel
                        guesses_remaining = guesses_remaining - 1 
                        # minus one from the number of guesses
                        break
                    break
                break
            break
        break
    else: # if the guessed character is not a valid letter
        letters_guessed += letter
        if num_warn == 0: # if the user has run out of warnings
            guesses_remaining = guesses_remaining - 1
            print('You have no warnings remaining.')
            print('You will now lose guesses instead.')
            print(get_guessed_word(secret_word, letters_guessed))
            print('------------------------------------------------------')
        else: # if the user has warnings remaining
            num_warn = num_warn - 1
            print('Oops! That is not a valid letter. You have', num_warn,
                  'warnings left:', get_guessed_word(secret_word, 
                                                     letters_guessed))
            print('------------------------------------------------------')
    # end of eighteenth run
    
    if int(guesses_remaining <= 0):
        return losing
    print('You have', guesses_remaining, 'guesses left')
    if num_warn >= 1:
        print('You have', num_warn, 'warnings left')
    print('Available letters:', get_available_letters(letters_guessed))
    letter = input('Please guess a letter:')
    # Given that the longest possible word is 10 letters, 18 should be the
    # maximum number of needed runs (3 warnings, 9 correct guesses and 6 wrong)
    


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    my_word = my_word.replace('_ ', '_') # replace the underscore and space
    # with just an underscore, therefore keeping the length of the word
    if len(my_word) != len(other_word): # if the length of the guessed word is
        # not equal to the length of the actual word
        return False # the guessed word can not be the actual word
    for i in range(len(my_word)): # for each character in the guessed word
        if my_word[i] == other_word[i]: # if the character at index position i
            # is the same in both words
            i += 1 # add one to index counter
        else: # if the character at index position i is not the same 
            if my_word[i] == '_': # if the character is an underscore
                i += 1 # move to next character
            else: # if the character is a letter (which is also not in the
                # actual word)
                return False
    if len(my_word) == i: # if every letter has been checked
        return True # all letters in guessed word are in the actual word

def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.
    '''
    # copied from https://github.com/kaizenflow/6.0001-ps2/blob/master/hangman.py
    # after trying multiple times to get it working - it was easier than I thought!
    matches = [] # create empty list
    for other_word in wordlist: # essentially for every word in wordlist
        if match_with_gaps(my_word, other_word): # run match_with_gaps with
            # every single word from wordlist being the other_word
            matches.append(other_word) # add any True matches to the empty
            # matches list
    print(' '.join(matches)) # return all the matches
       

def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    print('Welcome to the game Hangman (with hints) !')
    print('I am thinking of a word that is', len(secret_word), 'letters long')
    guesses_remaining = 6
    print('You have', guesses_remaining, 'guesses left')
    print('Available letters:', get_available_letters(''))
    letter = input('Please guess a letter, or use * to show all possible words left:')
    letters_guessed = []
    num_warn = 3
    score = guesses_remaining * len(list(set(secret_word)))
    winning = 'Congratulations! You won! Your total score for this game is:', str(score)
    losing = 'Sorry, you ran out of guesses. The word was:', str(secret_word)
    
    # first run
    while is_letter_valid(letter) is True: # while the guessed character is a
        # valid letter
        if is_letter_in_word(secret_word, letter) is True:
            # if the guessed letter is in the secret word
            for c in letter: 
                if c in letters_guessed: 
                    # if the guessed letter has already been guessed
                    print('Oops! You have already guessed that letter!')
                    if num_warn == 0: # if the user has run out of warnings
                        guesses_remaining = guesses_remaining - 1
                        print('You have no warnings remaining.')
                        print('You will now lose guesses instead.')
                        print(get_guessed_word(secret_word, letters_guessed))
                        print('----------------------------------------------')
                        break
                    else: # if the user has more than one guess remaining
                        letters_guessed += letter
                        num_warn = num_warn - 1
                        print('You now have', num_warn, 'warnings left:')
                        print(get_guessed_word(secret_word, letters_guessed))
                        print('----------------------------------------------')
                        break
                    break
                else: # if the guessed letter has not already been guessed
                    letters_guessed += letter # add it to guessed letters as 
                    # the guessed letter is in the secret word
                    if is_word_guessed(secret_word, letters_guessed) is True:
                    # if all guessed letters match the secret word
                        print('Good guess:', get_guessed_word(secret_word,
                                                              letters_guessed))
                        return winning # end game with congratulations message 
                        # and score
                    else: # if all the guessed letters do not match the word
                        print('Good guess:', get_guessed_word(secret_word,
                                                              letters_guessed))
                        break
                    break
                break
            break
        elif is_letter_in_word(secret_word, letter) is False:
            # if the guessed letter is not in the secret word
            for c in letter: 
                if c in letters_guessed: # if the guessed letter has already 
                    # been guessed
                    print('Oops! You have already guessed that letter!')
                    if num_warn == 0: # if the user has run out of warnings
                        guesses_remaining = guesses_remaining - 1
                        print('You have no warnings remaining.')
                        print('You will now lose guesses instead.')
                        print(get_guessed_word(secret_word, letters_guessed))
                        print('----------------------------------------------')
                        break
                    else: # if the user has more than one guess remaining
                        letters_guessed += letter
                        num_warn = num_warn - 1
                        print('You now have', num_warn, 'warnings left:')
                        print(get_guessed_word(secret_word, letters_guessed))
                        print('----------------------------------------------')
                        break
                    break
                else: # if the letter has not already been guessed
                    letters_guessed += letter # add it to guessed letters
                    print('Oops! That letter is not in my word!', 
                          get_guessed_word(secret_word, letters_guessed))
                        # because the guessed letter is not in the secret word
                    if is_letter_vowel(letter) is True: # if a vowel
                        guesses_remaining = guesses_remaining - 2 
                        # minus two from the number of guesses
                    else: # if not a vowel
                        guesses_remaining = guesses_remaining - 1 
                        # minus one from the number of guesses
                        break
                    break
                break
            break
        break
    else: # if the guessed character is not a valid letter
        if letter == '*': # if the user asks for a hint
            print('Possible matches are:') 
            print(show_possible_matches(get_guessed_word(secret_word, 
                                                         letters_guessed)))
            # run the show possible matches function which returns all the 
            # possible words that could be guessed given what letters have 
            # already been guessed
        else: # if the character is not an asterisk for a hint, therefore it 
            # is an invalid character
            if num_warn == 0: # if the user has run out of warnings
                guesses_remaining = guesses_remaining - 1
                print('You have no warnings remaining.')
                print('You will now lose guesses instead.')
                print(get_guessed_word(secret_word, letters_guessed))
                print('------------------------------------------------------')
            else: # if the user has warnings remaining
                num_warn = num_warn - 1
                print('Oops! That is not a valid letter. You have', num_warn,
                      'warnings left:', get_guessed_word(secret_word,
                                                         letters_guessed))
                print('------------------------------------------------------')
    # end of first run
    
    if int(guesses_remaining <= 0):
        return losing
    print('You have', guesses_remaining, 'guesses left')
    if num_warn >= 1:
        print('You have', num_warn, 'warnings left')
    print('Available letters:', get_available_letters(letters_guessed))
    letter = input('Please guess a letter:')
    
    # second run 
    while is_letter_valid(letter) is True: # while the guessed character is a
        # valid letter
        if is_letter_in_word(secret_word, letter) is True:
            # if the guessed letter is in the secret word
            for c in letter: 
                if c in letters_guessed: 
                    # if the guessed letter has already been guessed
                    print('Oops! You have already guessed that letter!')
                    if num_warn == 0: # if the user has run out of warnings
                        guesses_remaining = guesses_remaining - 1
                        print('You have no warnings remaining.')
                        print('You will now lose guesses instead.')
                        print(get_guessed_word(secret_word, letters_guessed))
                        print('----------------------------------------------')
                        break
                    else: # if the user has more than one guess remaining
                        letters_guessed += letter
                        num_warn = num_warn - 1
                        print('You now have', num_warn, 'warnings left:')
                        print(get_guessed_word(secret_word, letters_guessed))
                        print('----------------------------------------------')
                        break
                    break
                else: # if the guessed letter has not already been guessed
                    letters_guessed += letter # add it to guessed letters as 
                    # the guessed letter is in the secret word
                    if is_word_guessed(secret_word, letters_guessed) is True:
                    # if all guessed letters match the secret word
                        print('Good guess:', get_guessed_word(secret_word,
                                                              letters_guessed))
                        return winning # end game with congratulations message 
                        # and score
                    else: # if all the guessed letters do not match the word
                        print('Good guess:', get_guessed_word(secret_word,
                                                              letters_guessed))
                        break
                    break
                break
            break
        elif is_letter_in_word(secret_word, letter) is False:
            # if the guessed letter is not in the secret word
            for c in letter: 
                if c in letters_guessed: # if the guessed letter has already 
                    # been guessed
                    print('Oops! You have already guessed that letter!')
                    if num_warn == 0: # if the user has run out of warnings
                        guesses_remaining = guesses_remaining - 1
                        print('You have no warnings remaining.')
                        print('You will now lose guesses instead.')
                        print(get_guessed_word(secret_word, letters_guessed))
                        print('----------------------------------------------')
                        break
                    else: # if the user has more than one guess remaining
                        letters_guessed += letter
                        num_warn = num_warn - 1
                        print('You now have', num_warn, 'warnings left:')
                        print(get_guessed_word(secret_word, letters_guessed))
                        print('----------------------------------------------')
                        break
                    break
                else: # if the letter has not already been guessed
                    letters_guessed += letter # add it to guessed letters
                    print('Oops! That letter is not in my word!', 
                          get_guessed_word(secret_word, letters_guessed))
                        # because the guessed letter is not in the secret word
                    if is_letter_vowel(letter) is True: # if a vowel
                        guesses_remaining = guesses_remaining - 2 
                        # minus two from the number of guesses
                    else: # if not a vowel
                        guesses_remaining = guesses_remaining - 1 
                        # minus one from the number of guesses
                        break
                    break
                break
            break
        break
    else: # if the guessed character is not a valid letter
        if letter == '*': # if the user asks for a hint
            print('Possible matches are:') 
            print(show_possible_matches(get_guessed_word(secret_word, 
                                                         letters_guessed)))
            # run the show possible matches function which returns all the 
            # possible words that could be guessed given what letters have 
            # already been guessed
        else: # if the character is not an asterisk for a hint, therefore it 
            # is an invalid character
            if num_warn == 0: # if the user has run out of warnings
                guesses_remaining = guesses_remaining - 1
                print('You have no warnings remaining.')
                print('You will now lose guesses instead.')
                print(get_guessed_word(secret_word, letters_guessed))
                print('------------------------------------------------------')
            else: # if the user has warnings remaining
                num_warn = num_warn - 1
                print('Oops! That is not a valid letter. You have', num_warn,
                      'warnings left:', get_guessed_word(secret_word,
                                                         letters_guessed))
                print('------------------------------------------------------')
    # end of second run   
        
    if int(guesses_remaining <= 0):
        return losing
    print('You have', guesses_remaining, 'guesses left')
    if num_warn >= 1:
        print('You have', num_warn, 'warnings left')
    print('Available letters:', get_available_letters(letters_guessed))
    letter = input('Please guess a letter:')
    
    # third run
    while is_letter_valid(letter) is True: # while the guessed character is a
        # valid letter
        if is_letter_in_word(secret_word, letter) is True:
            # if the guessed letter is in the secret word
            for c in letter: 
                if c in letters_guessed: 
                    # if the guessed letter has already been guessed
                    print('Oops! You have already guessed that letter!')
                    if num_warn == 0: # if the user has run out of warnings
                        guesses_remaining = guesses_remaining - 1
                        print('You have no warnings remaining.')
                        print('You will now lose guesses instead.')
                        print(get_guessed_word(secret_word, letters_guessed))
                        print('----------------------------------------------')
                        break
                    else: # if the user has more than one guess remaining
                        letters_guessed += letter
                        num_warn = num_warn - 1
                        print('You now have', num_warn, 'warnings left:')
                        print(get_guessed_word(secret_word, letters_guessed))
                        print('----------------------------------------------')
                        break
                    break
                else: # if the guessed letter has not already been guessed
                    letters_guessed += letter # add it to guessed letters as 
                    # the guessed letter is in the secret word
                    if is_word_guessed(secret_word, letters_guessed) is True:
                    # if all guessed letters match the secret word
                        print('Good guess:', get_guessed_word(secret_word,
                                                              letters_guessed))
                        return winning # end game with congratulations message 
                        # and score
                    else: # if all the guessed letters do not match the word
                        print('Good guess:', get_guessed_word(secret_word,
                                                              letters_guessed))
                        break
                    break
                break
            break
        elif is_letter_in_word(secret_word, letter) is False:
            # if the guessed letter is not in the secret word
            for c in letter: 
                if c in letters_guessed: # if the guessed letter has already 
                    # been guessed
                    print('Oops! You have already guessed that letter!')
                    if num_warn == 0: # if the user has run out of warnings
                        guesses_remaining = guesses_remaining - 1
                        print('You have no warnings remaining.')
                        print('You will now lose guesses instead.')
                        print(get_guessed_word(secret_word, letters_guessed))
                        print('----------------------------------------------')
                        break
                    else: # if the user has more than one guess remaining
                        letters_guessed += letter
                        num_warn = num_warn - 1
                        print('You now have', num_warn, 'warnings left:')
                        print(get_guessed_word(secret_word, letters_guessed))
                        print('----------------------------------------------')
                        break
                    break
                else: # if the letter has not already been guessed
                    letters_guessed += letter # add it to guessed letters
                    print('Oops! That letter is not in my word!', 
                          get_guessed_word(secret_word, letters_guessed))
                        # because the guessed letter is not in the secret word
                    if is_letter_vowel(letter) is True: # if a vowel
                        guesses_remaining = guesses_remaining - 2 
                        # minus two from the number of guesses
                    else: # if not a vowel
                        guesses_remaining = guesses_remaining - 1 
                        # minus one from the number of guesses
                        break
                    break
                break
            break
        break
    else: # if the guessed character is not a valid letter
        if letter == '*': # if the user asks for a hint
            print('Possible matches are:') 
            print(show_possible_matches(get_guessed_word(secret_word, 
                                                         letters_guessed)))
            # run the show possible matches function which returns all the 
            # possible words that could be guessed given what letters have 
            # already been guessed
        else: # if the character is not an asterisk for a hint, therefore it 
            # is an invalid character
            if num_warn == 0: # if the user has run out of warnings
                guesses_remaining = guesses_remaining - 1
                print('You have no warnings remaining.')
                print('You will now lose guesses instead.')
                print(get_guessed_word(secret_word, letters_guessed))
                print('------------------------------------------------------')
            else: # if the user has warnings remaining
                num_warn = num_warn - 1
                print('Oops! That is not a valid letter. You have', num_warn,
                      'warnings left:', get_guessed_word(secret_word,
                                                         letters_guessed))
                print('------------------------------------------------------')
    # end of third run
    
    if int(guesses_remaining <= 0):
        return losing
    print('You have', guesses_remaining, 'guesses left')
    if num_warn >= 1:
        print('You have', num_warn, 'warnings left')
    print('Available letters:', get_available_letters(letters_guessed))
    letter = input('Please guess a letter:')
   
    # fourth run
    while is_letter_valid(letter) is True: # while the guessed character is a
        # valid letter
        if is_letter_in_word(secret_word, letter) is True:
            # if the guessed letter is in the secret word
            for c in letter: 
                if c in letters_guessed: 
                    # if the guessed letter has already been guessed
                    print('Oops! You have already guessed that letter!')
                    if num_warn == 0: # if the user has run out of warnings
                        guesses_remaining = guesses_remaining - 1
                        print('You have no warnings remaining.')
                        print('You will now lose guesses instead.')
                        print(get_guessed_word(secret_word, letters_guessed))
                        print('----------------------------------------------')
                        break
                    else: # if the user has more than one guess remaining
                        letters_guessed += letter
                        num_warn = num_warn - 1
                        print('You now have', num_warn, 'warnings left:')
                        print(get_guessed_word(secret_word, letters_guessed))
                        print('----------------------------------------------')
                        break
                    break
                else: # if the guessed letter has not already been guessed
                    letters_guessed += letter # add it to guessed letters as 
                    # the guessed letter is in the secret word
                    if is_word_guessed(secret_word, letters_guessed) is True:
                    # if all guessed letters match the secret word
                        print('Good guess:', get_guessed_word(secret_word,
                                                              letters_guessed))
                        return winning # end game with congratulations message 
                        # and score
                    else: # if all the guessed letters do not match the word
                        print('Good guess:', get_guessed_word(secret_word,
                                                              letters_guessed))
                        break
                    break
                break
            break
        elif is_letter_in_word(secret_word, letter) is False:
            # if the guessed letter is not in the secret word
            for c in letter: 
                if c in letters_guessed: # if the guessed letter has already 
                    # been guessed
                    print('Oops! You have already guessed that letter!')
                    if num_warn == 0: # if the user has run out of warnings
                        guesses_remaining = guesses_remaining - 1
                        print('You have no warnings remaining.')
                        print('You will now lose guesses instead.')
                        print(get_guessed_word(secret_word, letters_guessed))
                        print('----------------------------------------------')
                        break
                    else: # if the user has more than one guess remaining
                        letters_guessed += letter
                        num_warn = num_warn - 1
                        print('You now have', num_warn, 'warnings left:')
                        print(get_guessed_word(secret_word, letters_guessed))
                        print('----------------------------------------------')
                        break
                    break
                else: # if the letter has not already been guessed
                    letters_guessed += letter # add it to guessed letters
                    print('Oops! That letter is not in my word!', 
                          get_guessed_word(secret_word, letters_guessed))
                        # because the guessed letter is not in the secret word
                    if is_letter_vowel(letter) is True: # if a vowel
                        guesses_remaining = guesses_remaining - 2 
                        # minus two from the number of guesses
                    else: # if not a vowel
                        guesses_remaining = guesses_remaining - 1 
                        # minus one from the number of guesses
                        break
                    break
                break
            break
        break
    else: # if the guessed character is not a valid letter
        if letter == '*': # if the user asks for a hint
            print('Possible matches are:') 
            print(show_possible_matches(get_guessed_word(secret_word, 
                                                         letters_guessed)))
            # run the show possible matches function which returns all the 
            # possible words that could be guessed given what letters have 
            # already been guessed
        else: # if the character is not an asterisk for a hint, therefore it 
            # is an invalid character
            if num_warn == 0: # if the user has run out of warnings
                guesses_remaining = guesses_remaining - 1
                print('You have no warnings remaining.')
                print('You will now lose guesses instead.')
                print(get_guessed_word(secret_word, letters_guessed))
                print('------------------------------------------------------')
            else: # if the user has warnings remaining
                num_warn = num_warn - 1
                print('Oops! That is not a valid letter. You have', num_warn,
                      'warnings left:', get_guessed_word(secret_word,
                                                         letters_guessed))
                print('------------------------------------------------------')
    # end of fourth run
    
    if int(guesses_remaining <= 0):
        return losing
    print('You have', guesses_remaining, 'guesses left')
    if num_warn >= 1:
        print('You have', num_warn, 'warnings left')
    print('Available letters:', get_available_letters(letters_guessed))
    letter = input('Please guess a letter:')
    
    
    # fifth run
    while is_letter_valid(letter) is True: # while the guessed character is a
        # valid letter
        if is_letter_in_word(secret_word, letter) is True:
            # if the guessed letter is in the secret word
            for c in letter: 
                if c in letters_guessed: 
                    # if the guessed letter has already been guessed
                    print('Oops! You have already guessed that letter!')
                    if num_warn == 0: # if the user has run out of warnings
                        guesses_remaining = guesses_remaining - 1
                        print('You have no warnings remaining.')
                        print('You will now lose guesses instead.')
                        print(get_guessed_word(secret_word, letters_guessed))
                        print('----------------------------------------------')
                        break
                    else: # if the user has more than one guess remaining
                        letters_guessed += letter
                        num_warn = num_warn - 1
                        print('You now have', num_warn, 'warnings left:')
                        print(get_guessed_word(secret_word, letters_guessed))
                        print('----------------------------------------------')
                        break
                    break
                else: # if the guessed letter has not already been guessed
                    letters_guessed += letter # add it to guessed letters as 
                    # the guessed letter is in the secret word
                    if is_word_guessed(secret_word, letters_guessed) is True:
                    # if all guessed letters match the secret word
                        print('Good guess:', get_guessed_word(secret_word,
                                                              letters_guessed))
                        return winning # end game with congratulations message 
                        # and score
                    else: # if all the guessed letters do not match the word
                        print('Good guess:', get_guessed_word(secret_word,
                                                              letters_guessed))
                        break
                    break
                break
            break
        elif is_letter_in_word(secret_word, letter) is False:
            # if the guessed letter is not in the secret word
            for c in letter: 
                if c in letters_guessed: # if the guessed letter has already 
                    # been guessed
                    print('Oops! You have already guessed that letter!')
                    if num_warn == 0: # if the user has run out of warnings
                        guesses_remaining = guesses_remaining - 1
                        print('You have no warnings remaining.')
                        print('You will now lose guesses instead.')
                        print(get_guessed_word(secret_word, letters_guessed))
                        print('----------------------------------------------')
                        break
                    else: # if the user has more than one guess remaining
                        letters_guessed += letter
                        num_warn = num_warn - 1
                        print('You now have', num_warn, 'warnings left:')
                        print(get_guessed_word(secret_word, letters_guessed))
                        print('----------------------------------------------')
                        break
                    break
                else: # if the letter has not already been guessed
                    letters_guessed += letter # add it to guessed letters
                    print('Oops! That letter is not in my word!', 
                          get_guessed_word(secret_word, letters_guessed))
                        # because the guessed letter is not in the secret word
                    if is_letter_vowel(letter) is True: # if a vowel
                        guesses_remaining = guesses_remaining - 2 
                        # minus two from the number of guesses
                    else: # if not a vowel
                        guesses_remaining = guesses_remaining - 1 
                        # minus one from the number of guesses
                        break
                    break
                break
            break
        break
    else: # if the guessed character is not a valid letter
        if letter == '*': # if the user asks for a hint
            print('Possible matches are:') 
            print(show_possible_matches(get_guessed_word(secret_word, 
                                                         letters_guessed)))
            # run the show possible matches function which returns all the 
            # possible words that could be guessed given what letters have 
            # already been guessed
        else: # if the character is not an asterisk for a hint, therefore it 
            # is an invalid character
            if num_warn == 0: # if the user has run out of warnings
                guesses_remaining = guesses_remaining - 1
                print('You have no warnings remaining.')
                print('You will now lose guesses instead.')
                print(get_guessed_word(secret_word, letters_guessed))
                print('------------------------------------------------------')
            else: # if the user has warnings remaining
                num_warn = num_warn - 1
                print('Oops! That is not a valid letter. You have', num_warn,
                      'warnings left:', get_guessed_word(secret_word,
                                                         letters_guessed))
                print('------------------------------------------------------')
    # end of fifth run
    
    if int(guesses_remaining <= 0):
        return losing
    print('You have', guesses_remaining, 'guesses left')
    if num_warn >= 1:
        print('You have', num_warn, 'warnings left')
    print('Available letters:', get_available_letters(letters_guessed))
    letter = input('Please guess a letter:')
    
    # sixth run
    while is_letter_valid(letter) is True: # while the guessed character is a
        # valid letter
        if is_letter_in_word(secret_word, letter) is True:
            # if the guessed letter is in the secret word
            for c in letter: 
                if c in letters_guessed: 
                    # if the guessed letter has already been guessed
                    print('Oops! You have already guessed that letter!')
                    if num_warn == 0: # if the user has run out of warnings
                        guesses_remaining = guesses_remaining - 1
                        print('You have no warnings remaining.')
                        print('You will now lose guesses instead.')
                        print(get_guessed_word(secret_word, letters_guessed))
                        print('----------------------------------------------')
                        break
                    else: # if the user has more than one guess remaining
                        letters_guessed += letter
                        num_warn = num_warn - 1
                        print('You now have', num_warn, 'warnings left:')
                        print(get_guessed_word(secret_word, letters_guessed))
                        print('----------------------------------------------')
                        break
                    break
                else: # if the guessed letter has not already been guessed
                    letters_guessed += letter # add it to guessed letters as 
                    # the guessed letter is in the secret word
                    if is_word_guessed(secret_word, letters_guessed) is True:
                    # if all guessed letters match the secret word
                        print('Good guess:', get_guessed_word(secret_word,
                                                              letters_guessed))
                        return winning # end game with congratulations message 
                        # and score
                    else: # if all the guessed letters do not match the word
                        print('Good guess:', get_guessed_word(secret_word,
                                                              letters_guessed))
                        break
                    break
                break
            break
        elif is_letter_in_word(secret_word, letter) is False:
            # if the guessed letter is not in the secret word
            for c in letter: 
                if c in letters_guessed: # if the guessed letter has already 
                    # been guessed
                    print('Oops! You have already guessed that letter!')
                    if num_warn == 0: # if the user has run out of warnings
                        guesses_remaining = guesses_remaining - 1
                        print('You have no warnings remaining.')
                        print('You will now lose guesses instead.')
                        print(get_guessed_word(secret_word, letters_guessed))
                        print('----------------------------------------------')
                        break
                    else: # if the user has more than one guess remaining
                        letters_guessed += letter
                        num_warn = num_warn - 1
                        print('You now have', num_warn, 'warnings left:')
                        print(get_guessed_word(secret_word, letters_guessed))
                        print('----------------------------------------------')
                        break
                    break
                else: # if the letter has not already been guessed
                    letters_guessed += letter # add it to guessed letters
                    print('Oops! That letter is not in my word!', 
                          get_guessed_word(secret_word, letters_guessed))
                        # because the guessed letter is not in the secret word
                    if is_letter_vowel(letter) is True: # if a vowel
                        guesses_remaining = guesses_remaining - 2 
                        # minus two from the number of guesses
                    else: # if not a vowel
                        guesses_remaining = guesses_remaining - 1 
                        # minus one from the number of guesses
                        break
                    break
                break
            break
        break
    else: # if the guessed character is not a valid letter
        if letter == '*': # if the user asks for a hint
            print('Possible matches are:') 
            print(show_possible_matches(get_guessed_word(secret_word, 
                                                         letters_guessed)))
            # run the show possible matches function which returns all the 
            # possible words that could be guessed given what letters have 
            # already been guessed
        else: # if the character is not an asterisk for a hint, therefore it 
            # is an invalid character
            if num_warn == 0: # if the user has run out of warnings
                guesses_remaining = guesses_remaining - 1
                print('You have no warnings remaining.')
                print('You will now lose guesses instead.')
                print(get_guessed_word(secret_word, letters_guessed))
                print('------------------------------------------------------')
            else: # if the user has warnings remaining
                num_warn = num_warn - 1
                print('Oops! That is not a valid letter. You have', num_warn,
                      'warnings left:', get_guessed_word(secret_word,
                                                         letters_guessed))
                print('------------------------------------------------------')
    # end of sixth run
    
    if int(guesses_remaining <= 0):
        return losing
    print('You have', guesses_remaining, 'guesses left')
    if num_warn >= 1:
        print('You have', num_warn, 'warnings left')
    print('Available letters:', get_available_letters(letters_guessed))
    letter = input('Please guess a letter:')
    
    # seventh run
    while is_letter_valid(letter) is True: # while the guessed character is a
        # valid letter
        if is_letter_in_word(secret_word, letter) is True:
            # if the guessed letter is in the secret word
            for c in letter: 
                if c in letters_guessed: 
                    # if the guessed letter has already been guessed
                    print('Oops! You have already guessed that letter!')
                    if num_warn == 0: # if the user has run out of warnings
                        guesses_remaining = guesses_remaining - 1
                        print('You have no warnings remaining.')
                        print('You will now lose guesses instead.')
                        print(get_guessed_word(secret_word, letters_guessed))
                        print('----------------------------------------------')
                        break
                    else: # if the user has more than one guess remaining
                        letters_guessed += letter
                        num_warn = num_warn - 1
                        print('You now have', num_warn, 'warnings left:')
                        print(get_guessed_word(secret_word, letters_guessed))
                        print('----------------------------------------------')
                        break
                    break
                else: # if the guessed letter has not already been guessed
                    letters_guessed += letter # add it to guessed letters as 
                    # the guessed letter is in the secret word
                    if is_word_guessed(secret_word, letters_guessed) is True:
                    # if all guessed letters match the secret word
                        print('Good guess:', get_guessed_word(secret_word,
                                                              letters_guessed))
                        return winning # end game with congratulations message 
                        # and score
                    else: # if all the guessed letters do not match the word
                        print('Good guess:', get_guessed_word(secret_word,
                                                              letters_guessed))
                        break
                    break
                break
            break
        elif is_letter_in_word(secret_word, letter) is False:
            # if the guessed letter is not in the secret word
            for c in letter: 
                if c in letters_guessed: # if the guessed letter has already 
                    # been guessed
                    print('Oops! You have already guessed that letter!')
                    if num_warn == 0: # if the user has run out of warnings
                        guesses_remaining = guesses_remaining - 1
                        print('You have no warnings remaining.')
                        print('You will now lose guesses instead.')
                        print(get_guessed_word(secret_word, letters_guessed))
                        print('----------------------------------------------')
                        break
                    else: # if the user has more than one guess remaining
                        letters_guessed += letter
                        num_warn = num_warn - 1
                        print('You now have', num_warn, 'warnings left:')
                        print(get_guessed_word(secret_word, letters_guessed))
                        print('----------------------------------------------')
                        break
                    break
                else: # if the letter has not already been guessed
                    letters_guessed += letter # add it to guessed letters
                    print('Oops! That letter is not in my word!', 
                          get_guessed_word(secret_word, letters_guessed))
                        # because the guessed letter is not in the secret word
                    if is_letter_vowel(letter) is True: # if a vowel
                        guesses_remaining = guesses_remaining - 2 
                        # minus two from the number of guesses
                    else: # if not a vowel
                        guesses_remaining = guesses_remaining - 1 
                        # minus one from the number of guesses
                        break
                    break
                break
            break
        break
    else: # if the guessed character is not a valid letter
        if letter == '*': # if the user asks for a hint
            print('Possible matches are:') 
            print(show_possible_matches(get_guessed_word(secret_word, 
                                                         letters_guessed)))
            # run the show possible matches function which returns all the 
            # possible words that could be guessed given what letters have 
            # already been guessed
        else: # if the character is not an asterisk for a hint, therefore it 
            # is an invalid character
            if num_warn == 0: # if the user has run out of warnings
                guesses_remaining = guesses_remaining - 1
                print('You have no warnings remaining.')
                print('You will now lose guesses instead.')
                print(get_guessed_word(secret_word, letters_guessed))
                print('------------------------------------------------------')
            else: # if the user has warnings remaining
                num_warn = num_warn - 1
                print('Oops! That is not a valid letter. You have', num_warn,
                      'warnings left:', get_guessed_word(secret_word,
                                                         letters_guessed))
                print('------------------------------------------------------')
    # end of seventh run
    
    if int(guesses_remaining <= 0):
        return losing
    print('You have', guesses_remaining, 'guesses left')
    if num_warn >= 1:
        print('You have', num_warn, 'warnings left')
    print('Available letters:', get_available_letters(letters_guessed))
    letter = input('Please guess a letter:')
    
    # eighth run
    while is_letter_valid(letter) is True: # while the guessed character is a
        # valid letter
        if is_letter_in_word(secret_word, letter) is True:
            # if the guessed letter is in the secret word
            for c in letter: 
                if c in letters_guessed: 
                    # if the guessed letter has already been guessed
                    print('Oops! You have already guessed that letter!')
                    if num_warn == 0: # if the user has run out of warnings
                        guesses_remaining = guesses_remaining - 1
                        print('You have no warnings remaining.')
                        print('You will now lose guesses instead.')
                        print(get_guessed_word(secret_word, letters_guessed))
                        print('----------------------------------------------')
                        break
                    else: # if the user has more than one guess remaining
                        letters_guessed += letter
                        num_warn = num_warn - 1
                        print('You now have', num_warn, 'warnings left:')
                        print(get_guessed_word(secret_word, letters_guessed))
                        print('----------------------------------------------')
                        break
                    break
                else: # if the guessed letter has not already been guessed
                    letters_guessed += letter # add it to guessed letters as 
                    # the guessed letter is in the secret word
                    if is_word_guessed(secret_word, letters_guessed) is True:
                    # if all guessed letters match the secret word
                        print('Good guess:', get_guessed_word(secret_word,
                                                              letters_guessed))
                        return winning # end game with congratulations message 
                        # and score
                    else: # if all the guessed letters do not match the word
                        print('Good guess:', get_guessed_word(secret_word,
                                                              letters_guessed))
                        break
                    break
                break
            break
        elif is_letter_in_word(secret_word, letter) is False:
            # if the guessed letter is not in the secret word
            for c in letter: 
                if c in letters_guessed: # if the guessed letter has already 
                    # been guessed
                    print('Oops! You have already guessed that letter!')
                    if num_warn == 0: # if the user has run out of warnings
                        guesses_remaining = guesses_remaining - 1
                        print('You have no warnings remaining.')
                        print('You will now lose guesses instead.')
                        print(get_guessed_word(secret_word, letters_guessed))
                        print('----------------------------------------------')
                        break
                    else: # if the user has more than one guess remaining
                        letters_guessed += letter
                        num_warn = num_warn - 1
                        print('You now have', num_warn, 'warnings left:')
                        print(get_guessed_word(secret_word, letters_guessed))
                        print('----------------------------------------------')
                        break
                    break
                else: # if the letter has not already been guessed
                    letters_guessed += letter # add it to guessed letters
                    print('Oops! That letter is not in my word!', 
                          get_guessed_word(secret_word, letters_guessed))
                        # because the guessed letter is not in the secret word
                    if is_letter_vowel(letter) is True: # if a vowel
                        guesses_remaining = guesses_remaining - 2 
                        # minus two from the number of guesses
                    else: # if not a vowel
                        guesses_remaining = guesses_remaining - 1 
                        # minus one from the number of guesses
                        break
                    break
                break
            break
        break
    else: # if the guessed character is not a valid letter
        if letter == '*': # if the user asks for a hint
            print('Possible matches are:') 
            print(show_possible_matches(get_guessed_word(secret_word, 
                                                         letters_guessed)))
            # run the show possible matches function which returns all the 
            # possible words that could be guessed given what letters have 
            # already been guessed
        else: # if the character is not an asterisk for a hint, therefore it 
            # is an invalid character
            if num_warn == 0: # if the user has run out of warnings
                guesses_remaining = guesses_remaining - 1
                print('You have no warnings remaining.')
                print('You will now lose guesses instead.')
                print(get_guessed_word(secret_word, letters_guessed))
                print('------------------------------------------------------')
            else: # if the user has warnings remaining
                num_warn = num_warn - 1
                print('Oops! That is not a valid letter. You have', num_warn,
                      'warnings left:', get_guessed_word(secret_word,
                                                         letters_guessed))
                print('------------------------------------------------------')
    # end of eighth run
    
    if int(guesses_remaining <= 0):
        return losing
    print('You have', guesses_remaining, 'guesses left')
    if num_warn >= 1:
        print('You have', num_warn, 'warnings left')
    print('Available letters:', get_available_letters(letters_guessed))
    letter = input('Please guess a letter:')
    
    # ninth run
    while is_letter_valid(letter) is True: # while the guessed character is a
        # valid letter
        if is_letter_in_word(secret_word, letter) is True:
            # if the guessed letter is in the secret word
            for c in letter: 
                if c in letters_guessed: 
                    # if the guessed letter has already been guessed
                    print('Oops! You have already guessed that letter!')
                    if num_warn == 0: # if the user has run out of warnings
                        guesses_remaining = guesses_remaining - 1
                        print('You have no warnings remaining.')
                        print('You will now lose guesses instead.')
                        print(get_guessed_word(secret_word, letters_guessed))
                        print('----------------------------------------------')
                        break
                    else: # if the user has more than one guess remaining
                        letters_guessed += letter
                        num_warn = num_warn - 1
                        print('You now have', num_warn, 'warnings left:')
                        print(get_guessed_word(secret_word, letters_guessed))
                        print('----------------------------------------------')
                        break
                    break
                else: # if the guessed letter has not already been guessed
                    letters_guessed += letter # add it to guessed letters as 
                    # the guessed letter is in the secret word
                    if is_word_guessed(secret_word, letters_guessed) is True:
                    # if all guessed letters match the secret word
                        print('Good guess:', get_guessed_word(secret_word,
                                                              letters_guessed))
                        return winning # end game with congratulations message 
                        # and score
                    else: # if all the guessed letters do not match the word
                        print('Good guess:', get_guessed_word(secret_word,
                                                              letters_guessed))
                        break
                    break
                break
            break
        elif is_letter_in_word(secret_word, letter) is False:
            # if the guessed letter is not in the secret word
            for c in letter: 
                if c in letters_guessed: # if the guessed letter has already 
                    # been guessed
                    print('Oops! You have already guessed that letter!')
                    if num_warn == 0: # if the user has run out of warnings
                        guesses_remaining = guesses_remaining - 1
                        print('You have no warnings remaining.')
                        print('You will now lose guesses instead.')
                        print(get_guessed_word(secret_word, letters_guessed))
                        print('----------------------------------------------')
                        break
                    else: # if the user has more than one guess remaining
                        letters_guessed += letter
                        num_warn = num_warn - 1
                        print('You now have', num_warn, 'warnings left:')
                        print(get_guessed_word(secret_word, letters_guessed))
                        print('----------------------------------------------')
                        break
                    break
                else: # if the letter has not already been guessed
                    letters_guessed += letter # add it to guessed letters
                    print('Oops! That letter is not in my word!', 
                          get_guessed_word(secret_word, letters_guessed))
                        # because the guessed letter is not in the secret word
                    if is_letter_vowel(letter) is True: # if a vowel
                        guesses_remaining = guesses_remaining - 2 
                        # minus two from the number of guesses
                    else: # if not a vowel
                        guesses_remaining = guesses_remaining - 1 
                        # minus one from the number of guesses
                        break
                    break
                break
            break
        break
    else: # if the guessed character is not a valid letter
        if letter == '*': # if the user asks for a hint
            print('Possible matches are:') 
            print(show_possible_matches(get_guessed_word(secret_word, 
                                                         letters_guessed)))
            # run the show possible matches function which returns all the 
            # possible words that could be guessed given what letters have 
            # already been guessed
        else: # if the character is not an asterisk for a hint, therefore it 
            # is an invalid character
            if num_warn == 0: # if the user has run out of warnings
                guesses_remaining = guesses_remaining - 1
                print('You have no warnings remaining.')
                print('You will now lose guesses instead.')
                print(get_guessed_word(secret_word, letters_guessed))
                print('------------------------------------------------------')
            else: # if the user has warnings remaining
                num_warn = num_warn - 1
                print('Oops! That is not a valid letter. You have', num_warn,
                      'warnings left:', get_guessed_word(secret_word,
                                                         letters_guessed))
                print('------------------------------------------------------')
    # end of ninth run
    
    if guesses_remaining <= 0:
        return losing
    print('You have', guesses_remaining, 'guesses left')
    if num_warn >= 1:
        print('You have', num_warn, 'warnings left')
    print('Available letters:', get_available_letters(letters_guessed))
    letter = input('Please guess a letter:')
    
    # tenth run
    while is_letter_valid(letter) is True: # while the guessed character is a
        # valid letter
        if is_letter_in_word(secret_word, letter) is True:
            # if the guessed letter is in the secret word
            for c in letter: 
                if c in letters_guessed: 
                    # if the guessed letter has already been guessed
                    print('Oops! You have already guessed that letter!')
                    if num_warn == 0: # if the user has run out of warnings
                        guesses_remaining = guesses_remaining - 1
                        print('You have no warnings remaining.')
                        print('You will now lose guesses instead.')
                        print(get_guessed_word(secret_word, letters_guessed))
                        print('----------------------------------------------')
                        break
                    else: # if the user has more than one guess remaining
                        letters_guessed += letter
                        num_warn = num_warn - 1
                        print('You now have', num_warn, 'warnings left:')
                        print(get_guessed_word(secret_word, letters_guessed))
                        print('----------------------------------------------')
                        break
                    break
                else: # if the guessed letter has not already been guessed
                    letters_guessed += letter # add it to guessed letters as 
                    # the guessed letter is in the secret word
                    if is_word_guessed(secret_word, letters_guessed) is True:
                    # if all guessed letters match the secret word
                        print('Good guess:', get_guessed_word(secret_word,
                                                              letters_guessed))
                        return winning # end game with congratulations message 
                        # and score
                    else: # if all the guessed letters do not match the word
                        print('Good guess:', get_guessed_word(secret_word,
                                                              letters_guessed))
                        break
                    break
                break
            break
        elif is_letter_in_word(secret_word, letter) is False:
            # if the guessed letter is not in the secret word
            for c in letter: 
                if c in letters_guessed: # if the guessed letter has already 
                    # been guessed
                    print('Oops! You have already guessed that letter!')
                    if num_warn == 0: # if the user has run out of warnings
                        guesses_remaining = guesses_remaining - 1
                        print('You have no warnings remaining.')
                        print('You will now lose guesses instead.')
                        print(get_guessed_word(secret_word, letters_guessed))
                        print('----------------------------------------------')
                        break
                    else: # if the user has more than one guess remaining
                        letters_guessed += letter
                        num_warn = num_warn - 1
                        print('You now have', num_warn, 'warnings left:')
                        print(get_guessed_word(secret_word, letters_guessed))
                        print('----------------------------------------------')
                        break
                    break
                else: # if the letter has not already been guessed
                    letters_guessed += letter # add it to guessed letters
                    print('Oops! That letter is not in my word!', 
                          get_guessed_word(secret_word, letters_guessed))
                        # because the guessed letter is not in the secret word
                    if is_letter_vowel(letter) is True: # if a vowel
                        guesses_remaining = guesses_remaining - 2 
                        # minus two from the number of guesses
                    else: # if not a vowel
                        guesses_remaining = guesses_remaining - 1 
                        # minus one from the number of guesses
                        break
                    break
                break
            break
        break
    else: # if the guessed character is not a valid letter
        if letter == '*': # if the user asks for a hint
            print('Possible matches are:') 
            print(show_possible_matches(get_guessed_word(secret_word, 
                                                         letters_guessed)))
            # run the show possible matches function which returns all the 
            # possible words that could be guessed given what letters have 
            # already been guessed
        else: # if the character is not an asterisk for a hint, therefore it 
            # is an invalid character
            if num_warn == 0: # if the user has run out of warnings
                guesses_remaining = guesses_remaining - 1
                print('You have no warnings remaining.')
                print('You will now lose guesses instead.')
                print(get_guessed_word(secret_word, letters_guessed))
                print('------------------------------------------------------')
            else: # if the user has warnings remaining
                num_warn = num_warn - 1
                print('Oops! That is not a valid letter. You have', num_warn,
                      'warnings left:', get_guessed_word(secret_word,
                                                         letters_guessed))
                print('------------------------------------------------------')
    # end of tenth run
    
    if int(guesses_remaining <= 0):
        return losing
    print('You have', guesses_remaining, 'guesses left')
    if num_warn >= 1:
        print('You have', num_warn, 'warnings left')
    print('Available letters:', get_available_letters(letters_guessed))
    letter = input('Please guess a letter:')
    
    # eleventh run
    while is_letter_valid(letter) is True: # while the guessed character is a
        # valid letter
        if is_letter_in_word(secret_word, letter) is True:
            # if the guessed letter is in the secret word
            for c in letter: 
                if c in letters_guessed: 
                    # if the guessed letter has already been guessed
                    print('Oops! You have already guessed that letter!')
                    if num_warn == 0: # if the user has run out of warnings
                        guesses_remaining = guesses_remaining - 1
                        print('You have no warnings remaining.')
                        print('You will now lose guesses instead.')
                        print(get_guessed_word(secret_word, letters_guessed))
                        print('----------------------------------------------')
                        break
                    else: # if the user has more than one guess remaining
                        letters_guessed += letter
                        num_warn = num_warn - 1
                        print('You now have', num_warn, 'warnings left:')
                        print(get_guessed_word(secret_word, letters_guessed))
                        print('----------------------------------------------')
                        break
                    break
                else: # if the guessed letter has not already been guessed
                    letters_guessed += letter # add it to guessed letters as 
                    # the guessed letter is in the secret word
                    if is_word_guessed(secret_word, letters_guessed) is True:
                    # if all guessed letters match the secret word
                        print('Good guess:', get_guessed_word(secret_word,
                                                              letters_guessed))
                        return winning # end game with congratulations message 
                        # and score
                    else: # if all the guessed letters do not match the word
                        print('Good guess:', get_guessed_word(secret_word,
                                                              letters_guessed))
                        break
                    break
                break
            break
        elif is_letter_in_word(secret_word, letter) is False:
            # if the guessed letter is not in the secret word
            for c in letter: 
                if c in letters_guessed: # if the guessed letter has already 
                    # been guessed
                    print('Oops! You have already guessed that letter!')
                    if num_warn == 0: # if the user has run out of warnings
                        guesses_remaining = guesses_remaining - 1
                        print('You have no warnings remaining.')
                        print('You will now lose guesses instead.')
                        print(get_guessed_word(secret_word, letters_guessed))
                        print('----------------------------------------------')
                        break
                    else: # if the user has more than one guess remaining
                        letters_guessed += letter
                        num_warn = num_warn - 1
                        print('You now have', num_warn, 'warnings left:')
                        print(get_guessed_word(secret_word, letters_guessed))
                        print('----------------------------------------------')
                        break
                    break
                else: # if the letter has not already been guessed
                    letters_guessed += letter # add it to guessed letters
                    print('Oops! That letter is not in my word!', 
                          get_guessed_word(secret_word, letters_guessed))
                        # because the guessed letter is not in the secret word
                    if is_letter_vowel(letter) is True: # if a vowel
                        guesses_remaining = guesses_remaining - 2 
                        # minus two from the number of guesses
                    else: # if not a vowel
                        guesses_remaining = guesses_remaining - 1 
                        # minus one from the number of guesses
                        break
                    break
                break
            break
        break
    else: # if the guessed character is not a valid letter
        if letter == '*': # if the user asks for a hint
            print('Possible matches are:') 
            print(show_possible_matches(get_guessed_word(secret_word, 
                                                         letters_guessed)))
            # run the show possible matches function which returns all the 
            # possible words that could be guessed given what letters have 
            # already been guessed
        else: # if the character is not an asterisk for a hint, therefore it 
            # is an invalid character
            if num_warn == 0: # if the user has run out of warnings
                guesses_remaining = guesses_remaining - 1
                print('You have no warnings remaining.')
                print('You will now lose guesses instead.')
                print(get_guessed_word(secret_word, letters_guessed))
                print('------------------------------------------------------')
            else: # if the user has warnings remaining
                num_warn = num_warn - 1
                print('Oops! That is not a valid letter. You have', num_warn,
                      'warnings left:', get_guessed_word(secret_word,
                                                         letters_guessed))
                print('------------------------------------------------------')
    # end of eleventh run
    
    if int(guesses_remaining <= 0):
        return losing
    print('You have', guesses_remaining, 'guesses left')
    if num_warn >= 1:
        print('You have', num_warn, 'warnings left')
    print('Available letters:', get_available_letters(letters_guessed))
    letter = input('Please guess a letter:')
    
    # twelth run
    while is_letter_valid(letter) is True: # while the guessed character is a
        # valid letter
        if is_letter_in_word(secret_word, letter) is True:
            # if the guessed letter is in the secret word
            for c in letter: 
                if c in letters_guessed: 
                    # if the guessed letter has already been guessed
                    print('Oops! You have already guessed that letter!')
                    if num_warn == 0: # if the user has run out of warnings
                        guesses_remaining = guesses_remaining - 1
                        print('You have no warnings remaining.')
                        print('You will now lose guesses instead.')
                        print(get_guessed_word(secret_word, letters_guessed))
                        print('----------------------------------------------')
                        break
                    else: # if the user has more than one guess remaining
                        letters_guessed += letter
                        num_warn = num_warn - 1
                        print('You now have', num_warn, 'warnings left:')
                        print(get_guessed_word(secret_word, letters_guessed))
                        print('----------------------------------------------')
                        break
                    break
                else: # if the guessed letter has not already been guessed
                    letters_guessed += letter # add it to guessed letters as 
                    # the guessed letter is in the secret word
                    if is_word_guessed(secret_word, letters_guessed) is True:
                    # if all guessed letters match the secret word
                        print('Good guess:', get_guessed_word(secret_word,
                                                              letters_guessed))
                        return winning # end game with congratulations message 
                        # and score
                    else: # if all the guessed letters do not match the word
                        print('Good guess:', get_guessed_word(secret_word,
                                                              letters_guessed))
                        break
                    break
                break
            break
        elif is_letter_in_word(secret_word, letter) is False:
            # if the guessed letter is not in the secret word
            for c in letter: 
                if c in letters_guessed: # if the guessed letter has already 
                    # been guessed
                    print('Oops! You have already guessed that letter!')
                    if num_warn == 0: # if the user has run out of warnings
                        guesses_remaining = guesses_remaining - 1
                        print('You have no warnings remaining.')
                        print('You will now lose guesses instead.')
                        print(get_guessed_word(secret_word, letters_guessed))
                        print('----------------------------------------------')
                        break
                    else: # if the user has more than one guess remaining
                        letters_guessed += letter
                        num_warn = num_warn - 1
                        print('You now have', num_warn, 'warnings left:')
                        print(get_guessed_word(secret_word, letters_guessed))
                        print('----------------------------------------------')
                        break
                    break
                else: # if the letter has not already been guessed
                    letters_guessed += letter # add it to guessed letters
                    print('Oops! That letter is not in my word!', 
                          get_guessed_word(secret_word, letters_guessed))
                        # because the guessed letter is not in the secret word
                    if is_letter_vowel(letter) is True: # if a vowel
                        guesses_remaining = guesses_remaining - 2 
                        # minus two from the number of guesses
                    else: # if not a vowel
                        guesses_remaining = guesses_remaining - 1 
                        # minus one from the number of guesses
                        break
                    break
                break
            break
        break
    else: # if the guessed character is not a valid letter
        if letter == '*': # if the user asks for a hint
            print('Possible matches are:') 
            print(show_possible_matches(get_guessed_word(secret_word, 
                                                         letters_guessed)))
            # run the show possible matches function which returns all the 
            # possible words that could be guessed given what letters have 
            # already been guessed
        else: # if the character is not an asterisk for a hint, therefore it 
            # is an invalid character
            if num_warn == 0: # if the user has run out of warnings
                guesses_remaining = guesses_remaining - 1
                print('You have no warnings remaining.')
                print('You will now lose guesses instead.')
                print(get_guessed_word(secret_word, letters_guessed))
                print('------------------------------------------------------')
            else: # if the user has warnings remaining
                num_warn = num_warn - 1
                print('Oops! That is not a valid letter. You have', num_warn,
                      'warnings left:', get_guessed_word(secret_word,
                                                         letters_guessed))
                print('------------------------------------------------------')
    # end of twelth run
    
    if int(guesses_remaining <= 0):
        return losing
    print('You have', guesses_remaining, 'guesses left')
    if num_warn >= 1:
        print('You have', num_warn, 'warnings left')
    print('Available letters:', get_available_letters(letters_guessed))
    letter = input('Please guess a letter:')
    
    # thirteenth run
    while is_letter_valid(letter) is True: # while the guessed character is a
        # valid letter
        if is_letter_in_word(secret_word, letter) is True:
            # if the guessed letter is in the secret word
            for c in letter: 
                if c in letters_guessed: 
                    # if the guessed letter has already been guessed
                    print('Oops! You have already guessed that letter!')
                    if num_warn == 0: # if the user has run out of warnings
                        guesses_remaining = guesses_remaining - 1
                        print('You have no warnings remaining.')
                        print('You will now lose guesses instead.')
                        print(get_guessed_word(secret_word, letters_guessed))
                        print('----------------------------------------------')
                        break
                    else: # if the user has more than one guess remaining
                        letters_guessed += letter
                        num_warn = num_warn - 1
                        print('You now have', num_warn, 'warnings left:')
                        print(get_guessed_word(secret_word, letters_guessed))
                        print('----------------------------------------------')
                        break
                    break
                else: # if the guessed letter has not already been guessed
                    letters_guessed += letter # add it to guessed letters as 
                    # the guessed letter is in the secret word
                    if is_word_guessed(secret_word, letters_guessed) is True:
                    # if all guessed letters match the secret word
                        print('Good guess:', get_guessed_word(secret_word,
                                                              letters_guessed))
                        return winning # end game with congratulations message 
                        # and score
                    else: # if all the guessed letters do not match the word
                        print('Good guess:', get_guessed_word(secret_word,
                                                              letters_guessed))
                        break
                    break
                break
            break
        elif is_letter_in_word(secret_word, letter) is False:
            # if the guessed letter is not in the secret word
            for c in letter: 
                if c in letters_guessed: # if the guessed letter has already 
                    # been guessed
                    print('Oops! You have already guessed that letter!')
                    if num_warn == 0: # if the user has run out of warnings
                        guesses_remaining = guesses_remaining - 1
                        print('You have no warnings remaining.')
                        print('You will now lose guesses instead.')
                        print(get_guessed_word(secret_word, letters_guessed))
                        print('----------------------------------------------')
                        break
                    else: # if the user has more than one guess remaining
                        letters_guessed += letter
                        num_warn = num_warn - 1
                        print('You now have', num_warn, 'warnings left:')
                        print(get_guessed_word(secret_word, letters_guessed))
                        print('----------------------------------------------')
                        break
                    break
                else: # if the letter has not already been guessed
                    letters_guessed += letter # add it to guessed letters
                    print('Oops! That letter is not in my word!', 
                          get_guessed_word(secret_word, letters_guessed))
                        # because the guessed letter is not in the secret word
                    if is_letter_vowel(letter) is True: # if a vowel
                        guesses_remaining = guesses_remaining - 2 
                        # minus two from the number of guesses
                    else: # if not a vowel
                        guesses_remaining = guesses_remaining - 1 
                        # minus one from the number of guesses
                        break
                    break
                break
            break
        break
    else: # if the guessed character is not a valid letter
        if letter == '*': # if the user asks for a hint
            print('Possible matches are:') 
            print(show_possible_matches(get_guessed_word(secret_word, 
                                                         letters_guessed)))
            # run the show possible matches function which returns all the 
            # possible words that could be guessed given what letters have 
            # already been guessed
        else: # if the character is not an asterisk for a hint, therefore it 
            # is an invalid character
            if num_warn == 0: # if the user has run out of warnings
                guesses_remaining = guesses_remaining - 1
                print('You have no warnings remaining.')
                print('You will now lose guesses instead.')
                print(get_guessed_word(secret_word, letters_guessed))
                print('------------------------------------------------------')
            else: # if the user has warnings remaining
                num_warn = num_warn - 1
                print('Oops! That is not a valid letter. You have', num_warn,
                      'warnings left:', get_guessed_word(secret_word,
                                                         letters_guessed))
                print('------------------------------------------------------')
    # end of thirteenth run
    
    if int(guesses_remaining <= 0):
        return losing
    print('You have', guesses_remaining, 'guesses left')
    if num_warn >= 1:
        print('You have', num_warn, 'warnings left')
    print('Available letters:', get_available_letters(letters_guessed))
    letter = input('Please guess a letter:')
    
    # fourteenth run
    while is_letter_valid(letter) is True: # while the guessed character is a
        # valid letter
        if is_letter_in_word(secret_word, letter) is True:
            # if the guessed letter is in the secret word
            for c in letter: 
                if c in letters_guessed: 
                    # if the guessed letter has already been guessed
                    print('Oops! You have already guessed that letter!')
                    if num_warn == 0: # if the user has run out of warnings
                        guesses_remaining = guesses_remaining - 1
                        print('You have no warnings remaining.')
                        print('You will now lose guesses instead.')
                        print(get_guessed_word(secret_word, letters_guessed))
                        print('----------------------------------------------')
                        break
                    else: # if the user has more than one guess remaining
                        letters_guessed += letter
                        num_warn = num_warn - 1
                        print('You now have', num_warn, 'warnings left:')
                        print(get_guessed_word(secret_word, letters_guessed))
                        print('----------------------------------------------')
                        break
                    break
                else: # if the guessed letter has not already been guessed
                    letters_guessed += letter # add it to guessed letters as 
                    # the guessed letter is in the secret word
                    if is_word_guessed(secret_word, letters_guessed) is True:
                    # if all guessed letters match the secret word
                        print('Good guess:', get_guessed_word(secret_word,
                                                              letters_guessed))
                        return winning # end game with congratulations message 
                        # and score
                    else: # if all the guessed letters do not match the word
                        print('Good guess:', get_guessed_word(secret_word,
                                                              letters_guessed))
                        break
                    break
                break
            break
        elif is_letter_in_word(secret_word, letter) is False:
            # if the guessed letter is not in the secret word
            for c in letter: 
                if c in letters_guessed: # if the guessed letter has already 
                    # been guessed
                    print('Oops! You have already guessed that letter!')
                    if num_warn == 0: # if the user has run out of warnings
                        guesses_remaining = guesses_remaining - 1
                        print('You have no warnings remaining.')
                        print('You will now lose guesses instead.')
                        print(get_guessed_word(secret_word, letters_guessed))
                        print('----------------------------------------------')
                        break
                    else: # if the user has more than one guess remaining
                        letters_guessed += letter
                        num_warn = num_warn - 1
                        print('You now have', num_warn, 'warnings left:')
                        print(get_guessed_word(secret_word, letters_guessed))
                        print('----------------------------------------------')
                        break
                    break
                else: # if the letter has not already been guessed
                    letters_guessed += letter # add it to guessed letters
                    print('Oops! That letter is not in my word!', 
                          get_guessed_word(secret_word, letters_guessed))
                        # because the guessed letter is not in the secret word
                    if is_letter_vowel(letter) is True: # if a vowel
                        guesses_remaining = guesses_remaining - 2 
                        # minus two from the number of guesses
                    else: # if not a vowel
                        guesses_remaining = guesses_remaining - 1 
                        # minus one from the number of guesses
                        break
                    break
                break
            break
        break
    else: # if the guessed character is not a valid letter
        if letter == '*': # if the user asks for a hint
            print('Possible matches are:') 
            print(show_possible_matches(get_guessed_word(secret_word, 
                                                         letters_guessed)))
            # run the show possible matches function which returns all the 
            # possible words that could be guessed given what letters have 
            # already been guessed
        else: # if the character is not an asterisk for a hint, therefore it 
            # is an invalid character
            if num_warn == 0: # if the user has run out of warnings
                guesses_remaining = guesses_remaining - 1
                print('You have no warnings remaining.')
                print('You will now lose guesses instead.')
                print(get_guessed_word(secret_word, letters_guessed))
                print('------------------------------------------------------')
            else: # if the user has warnings remaining
                num_warn = num_warn - 1
                print('Oops! That is not a valid letter. You have', num_warn,
                      'warnings left:', get_guessed_word(secret_word,
                                                         letters_guessed))
                print('------------------------------------------------------')
    # end of fourteenth run
    
    if int(guesses_remaining <= 0):
        return losing
    print('You have', guesses_remaining, 'guesses left')
    if num_warn >= 1:
        print('You have', num_warn, 'warnings left')
    print('Available letters:', get_available_letters(letters_guessed))
    letter = input('Please guess a letter:')
    
    # fifteenth run
    while is_letter_valid(letter) is True: # while the guessed character is a
        # valid letter
        if is_letter_in_word(secret_word, letter) is True:
            # if the guessed letter is in the secret word
            for c in letter: 
                if c in letters_guessed: 
                    # if the guessed letter has already been guessed
                    print('Oops! You have already guessed that letter!')
                    if num_warn == 0: # if the user has run out of warnings
                        guesses_remaining = guesses_remaining - 1
                        print('You have no warnings remaining.')
                        print('You will now lose guesses instead.')
                        print(get_guessed_word(secret_word, letters_guessed))
                        print('----------------------------------------------')
                        break
                    else: # if the user has more than one guess remaining
                        letters_guessed += letter
                        num_warn = num_warn - 1
                        print('You now have', num_warn, 'warnings left:')
                        print(get_guessed_word(secret_word, letters_guessed))
                        print('----------------------------------------------')
                        break
                    break
                else: # if the guessed letter has not already been guessed
                    letters_guessed += letter # add it to guessed letters as 
                    # the guessed letter is in the secret word
                    if is_word_guessed(secret_word, letters_guessed) is True:
                    # if all guessed letters match the secret word
                        print('Good guess:', get_guessed_word(secret_word,
                                                              letters_guessed))
                        return winning # end game with congratulations message 
                        # and score
                    else: # if all the guessed letters do not match the word
                        print('Good guess:', get_guessed_word(secret_word,
                                                              letters_guessed))
                        break
                    break
                break
            break
        elif is_letter_in_word(secret_word, letter) is False:
            # if the guessed letter is not in the secret word
            for c in letter: 
                if c in letters_guessed: # if the guessed letter has already 
                    # been guessed
                    print('Oops! You have already guessed that letter!')
                    if num_warn == 0: # if the user has run out of warnings
                        guesses_remaining = guesses_remaining - 1
                        print('You have no warnings remaining.')
                        print('You will now lose guesses instead.')
                        print(get_guessed_word(secret_word, letters_guessed))
                        print('----------------------------------------------')
                        break
                    else: # if the user has more than one guess remaining
                        letters_guessed += letter
                        num_warn = num_warn - 1
                        print('You now have', num_warn, 'warnings left:')
                        print(get_guessed_word(secret_word, letters_guessed))
                        print('----------------------------------------------')
                        break
                    break
                else: # if the letter has not already been guessed
                    letters_guessed += letter # add it to guessed letters
                    print('Oops! That letter is not in my word!', 
                          get_guessed_word(secret_word, letters_guessed))
                        # because the guessed letter is not in the secret word
                    if is_letter_vowel(letter) is True: # if a vowel
                        guesses_remaining = guesses_remaining - 2 
                        # minus two from the number of guesses
                    else: # if not a vowel
                        guesses_remaining = guesses_remaining - 1 
                        # minus one from the number of guesses
                        break
                    break
                break
            break
        break
    else: # if the guessed character is not a valid letter
        if letter == '*': # if the user asks for a hint
            print('Possible matches are:') 
            print(show_possible_matches(get_guessed_word(secret_word, 
                                                         letters_guessed)))
            # run the show possible matches function which returns all the 
            # possible words that could be guessed given what letters have 
            # already been guessed
        else: # if the character is not an asterisk for a hint, therefore it 
            # is an invalid character
            if num_warn == 0: # if the user has run out of warnings
                guesses_remaining = guesses_remaining - 1
                print('You have no warnings remaining.')
                print('You will now lose guesses instead.')
                print(get_guessed_word(secret_word, letters_guessed))
                print('------------------------------------------------------')
            else: # if the user has warnings remaining
                num_warn = num_warn - 1
                print('Oops! That is not a valid letter. You have', num_warn,
                      'warnings left:', get_guessed_word(secret_word,
                                                         letters_guessed))
                print('------------------------------------------------------')
    # end of fifteenth run
    
    if int(guesses_remaining <= 0):
        return losing
    print('You have', guesses_remaining, 'guesses left')
    if num_warn >= 1:
        print('You have', num_warn, 'warnings left')
    print('Available letters:', get_available_letters(letters_guessed))
    letter = input('Please guess a letter:')
    
    # sixteenth run
    while is_letter_valid(letter) is True: # while the guessed character is a
        # valid letter
        if is_letter_in_word(secret_word, letter) is True:
            # if the guessed letter is in the secret word
            for c in letter: 
                if c in letters_guessed: 
                    # if the guessed letter has already been guessed
                    print('Oops! You have already guessed that letter!')
                    if num_warn == 0: # if the user has run out of warnings
                        guesses_remaining = guesses_remaining - 1
                        print('You have no warnings remaining.')
                        print('You will now lose guesses instead.')
                        print(get_guessed_word(secret_word, letters_guessed))
                        print('----------------------------------------------')
                        break
                    else: # if the user has more than one guess remaining
                        letters_guessed += letter
                        num_warn = num_warn - 1
                        print('You now have', num_warn, 'warnings left:')
                        print(get_guessed_word(secret_word, letters_guessed))
                        print('----------------------------------------------')
                        break
                    break
                else: # if the guessed letter has not already been guessed
                    letters_guessed += letter # add it to guessed letters as 
                    # the guessed letter is in the secret word
                    if is_word_guessed(secret_word, letters_guessed) is True:
                    # if all guessed letters match the secret word
                        print('Good guess:', get_guessed_word(secret_word,
                                                              letters_guessed))
                        return winning # end game with congratulations message 
                        # and score
                    else: # if all the guessed letters do not match the word
                        print('Good guess:', get_guessed_word(secret_word,
                                                              letters_guessed))
                        break
                    break
                break
            break
        elif is_letter_in_word(secret_word, letter) is False:
            # if the guessed letter is not in the secret word
            for c in letter: 
                if c in letters_guessed: # if the guessed letter has already 
                    # been guessed
                    print('Oops! You have already guessed that letter!')
                    if num_warn == 0: # if the user has run out of warnings
                        guesses_remaining = guesses_remaining - 1
                        print('You have no warnings remaining.')
                        print('You will now lose guesses instead.')
                        print(get_guessed_word(secret_word, letters_guessed))
                        print('----------------------------------------------')
                        break
                    else: # if the user has more than one guess remaining
                        letters_guessed += letter
                        num_warn = num_warn - 1
                        print('You now have', num_warn, 'warnings left:')
                        print(get_guessed_word(secret_word, letters_guessed))
                        print('----------------------------------------------')
                        break
                    break
                else: # if the letter has not already been guessed
                    letters_guessed += letter # add it to guessed letters
                    print('Oops! That letter is not in my word!', 
                          get_guessed_word(secret_word, letters_guessed))
                        # because the guessed letter is not in the secret word
                    if is_letter_vowel(letter) is True: # if a vowel
                        guesses_remaining = guesses_remaining - 2 
                        # minus two from the number of guesses
                    else: # if not a vowel
                        guesses_remaining = guesses_remaining - 1 
                        # minus one from the number of guesses
                        break
                    break
                break
            break
        break
    else: # if the guessed character is not a valid letter
        if letter == '*': # if the user asks for a hint
            print('Possible matches are:') 
            print(show_possible_matches(get_guessed_word(secret_word, 
                                                         letters_guessed)))
            # run the show possible matches function which returns all the 
            # possible words that could be guessed given what letters have 
            # already been guessed
        else: # if the character is not an asterisk for a hint, therefore it 
            # is an invalid character
            if num_warn == 0: # if the user has run out of warnings
                guesses_remaining = guesses_remaining - 1
                print('You have no warnings remaining.')
                print('You will now lose guesses instead.')
                print(get_guessed_word(secret_word, letters_guessed))
                print('------------------------------------------------------')
            else: # if the user has warnings remaining
                num_warn = num_warn - 1
                print('Oops! That is not a valid letter. You have', num_warn,
                      'warnings left:', get_guessed_word(secret_word,
                                                         letters_guessed))
                print('------------------------------------------------------')
    # end of sixteenth run
    
    if int(guesses_remaining <= 0):
        return losing
    print('You have', guesses_remaining, 'guesses left')
    if num_warn >= 1:
        print('You have', num_warn, 'warnings left')
    print('Available letters:', get_available_letters(letters_guessed))
    letter = input('Please guess a letter:')
    
    # seventeenth run
    while is_letter_valid(letter) is True: # while the guessed character is a
        # valid letter
        if is_letter_in_word(secret_word, letter) is True:
            # if the guessed letter is in the secret word
            for c in letter: 
                if c in letters_guessed: 
                    # if the guessed letter has already been guessed
                    print('Oops! You have already guessed that letter!')
                    if num_warn == 0: # if the user has run out of warnings
                        guesses_remaining = guesses_remaining - 1
                        print('You have no warnings remaining.')
                        print('You will now lose guesses instead.')
                        print(get_guessed_word(secret_word, letters_guessed))
                        print('----------------------------------------------')
                        break
                    else: # if the user has more than one guess remaining
                        letters_guessed += letter
                        num_warn = num_warn - 1
                        print('You now have', num_warn, 'warnings left:')
                        print(get_guessed_word(secret_word, letters_guessed))
                        print('----------------------------------------------')
                        break
                    break
                else: # if the guessed letter has not already been guessed
                    letters_guessed += letter # add it to guessed letters as 
                    # the guessed letter is in the secret word
                    if is_word_guessed(secret_word, letters_guessed) is True:
                    # if all guessed letters match the secret word
                        print('Good guess:', get_guessed_word(secret_word,
                                                              letters_guessed))
                        return winning # end game with congratulations message 
                        # and score
                    else: # if all the guessed letters do not match the word
                        print('Good guess:', get_guessed_word(secret_word,
                                                              letters_guessed))
                        break
                    break
                break
            break
        elif is_letter_in_word(secret_word, letter) is False:
            # if the guessed letter is not in the secret word
            for c in letter: 
                if c in letters_guessed: # if the guessed letter has already 
                    # been guessed
                    print('Oops! You have already guessed that letter!')
                    if num_warn == 0: # if the user has run out of warnings
                        guesses_remaining = guesses_remaining - 1
                        print('You have no warnings remaining.')
                        print('You will now lose guesses instead.')
                        print(get_guessed_word(secret_word, letters_guessed))
                        print('----------------------------------------------')
                        break
                    else: # if the user has more than one guess remaining
                        letters_guessed += letter
                        num_warn = num_warn - 1
                        print('You now have', num_warn, 'warnings left:')
                        print(get_guessed_word(secret_word, letters_guessed))
                        print('----------------------------------------------')
                        break
                    break
                else: # if the letter has not already been guessed
                    letters_guessed += letter # add it to guessed letters
                    print('Oops! That letter is not in my word!', 
                          get_guessed_word(secret_word, letters_guessed))
                        # because the guessed letter is not in the secret word
                    if is_letter_vowel(letter) is True: # if a vowel
                        guesses_remaining = guesses_remaining - 2 
                        # minus two from the number of guesses
                    else: # if not a vowel
                        guesses_remaining = guesses_remaining - 1 
                        # minus one from the number of guesses
                        break
                    break
                break
            break
        break
    else: # if the guessed character is not a valid letter
        if letter == '*': # if the user asks for a hint
            print('Possible matches are:') 
            print(show_possible_matches(get_guessed_word(secret_word, 
                                                         letters_guessed)))
            # run the show possible matches function which returns all the 
            # possible words that could be guessed given what letters have 
            # already been guessed
        else: # if the character is not an asterisk for a hint, therefore it 
            # is an invalid character
            if num_warn == 0: # if the user has run out of warnings
                guesses_remaining = guesses_remaining - 1
                print('You have no warnings remaining.')
                print('You will now lose guesses instead.')
                print(get_guessed_word(secret_word, letters_guessed))
                print('------------------------------------------------------')
            else: # if the user has warnings remaining
                num_warn = num_warn - 1
                print('Oops! That is not a valid letter. You have', num_warn,
                      'warnings left:', get_guessed_word(secret_word,
                                                         letters_guessed))
                print('------------------------------------------------------')
    # end of seventeenth run
    
    if int(guesses_remaining <= 0):
        return losing
    print('You have', guesses_remaining, 'guesses left')
    if num_warn >= 1:
        print('You have', num_warn, 'warnings left')
    print('Available letters:', get_available_letters(letters_guessed))
    letter = input('Please guess a letter:')
    
    # eighteenth run
    while is_letter_valid(letter) is True: # while the guessed character is a
        # valid letter
        if is_letter_in_word(secret_word, letter) is True:
            # if the guessed letter is in the secret word
            for c in letter: 
                if c in letters_guessed: 
                    # if the guessed letter has already been guessed
                    print('Oops! You have already guessed that letter!')
                    if num_warn == 0: # if the user has run out of warnings
                        guesses_remaining = guesses_remaining - 1
                        print('You have no warnings remaining.')
                        print('You will now lose guesses instead.')
                        print(get_guessed_word(secret_word, letters_guessed))
                        print('----------------------------------------------')
                        break
                    else: # if the user has more than one guess remaining
                        letters_guessed += letter
                        num_warn = num_warn - 1
                        print('You now have', num_warn, 'warnings left:')
                        print(get_guessed_word(secret_word, letters_guessed))
                        print('----------------------------------------------')
                        break
                    break
                else: # if the guessed letter has not already been guessed
                    letters_guessed += letter # add it to guessed letters as 
                    # the guessed letter is in the secret word
                    if is_word_guessed(secret_word, letters_guessed) is True:
                    # if all guessed letters match the secret word
                        print('Good guess:', get_guessed_word(secret_word,
                                                              letters_guessed))
                        return winning # end game with congratulations message 
                        # and score
                    else: # if all the guessed letters do not match the word
                        print('Good guess:', get_guessed_word(secret_word,
                                                              letters_guessed))
                        break
                    break
                break
            break
        elif is_letter_in_word(secret_word, letter) is False:
            # if the guessed letter is not in the secret word
            for c in letter: 
                if c in letters_guessed: # if the guessed letter has already 
                    # been guessed
                    print('Oops! You have already guessed that letter!')
                    if num_warn == 0: # if the user has run out of warnings
                        guesses_remaining = guesses_remaining - 1
                        print('You have no warnings remaining.')
                        print('You will now lose guesses instead.')
                        print(get_guessed_word(secret_word, letters_guessed))
                        print('----------------------------------------------')
                        break
                    else: # if the user has more than one guess remaining
                        letters_guessed += letter
                        num_warn = num_warn - 1
                        print('You now have', num_warn, 'warnings left:')
                        print(get_guessed_word(secret_word, letters_guessed))
                        print('----------------------------------------------')
                        break
                    break
                else: # if the letter has not already been guessed
                    letters_guessed += letter # add it to guessed letters
                    print('Oops! That letter is not in my word!', 
                          get_guessed_word(secret_word, letters_guessed))
                        # because the guessed letter is not in the secret word
                    if is_letter_vowel(letter) is True: # if a vowel
                        guesses_remaining = guesses_remaining - 2 
                        # minus two from the number of guesses
                    else: # if not a vowel
                        guesses_remaining = guesses_remaining - 1 
                        # minus one from the number of guesses
                        break
                    break
                break
            break
        break
    else: # if the guessed character is not a valid letter
        if letter == '*': # if the user asks for a hint
            print('Possible matches are:') 
            print(show_possible_matches(get_guessed_word(secret_word, 
                                                         letters_guessed)))
            # run the show possible matches function which returns all the 
            # possible words that could be guessed given what letters have 
            # already been guessed
        else: # if the character is not an asterisk for a hint, therefore it 
            # is an invalid character
            if num_warn == 0: # if the user has run out of warnings
                guesses_remaining = guesses_remaining - 1
                print('You have no warnings remaining.')
                print('You will now lose guesses instead.')
                print(get_guessed_word(secret_word, letters_guessed))
                print('------------------------------------------------------')
            else: # if the user has warnings remaining
                num_warn = num_warn - 1
                print('Oops! That is not a valid letter. You have', num_warn,
                      'warnings left:', get_guessed_word(secret_word,
                                                         letters_guessed))
                print('------------------------------------------------------')
    # end of eighteenth run
    
    if int(guesses_remaining <= 0):
        return losing
    print('You have', guesses_remaining, 'guesses left')
    if num_warn >= 1:
        print('You have', num_warn, 'warnings left')
    print('Available letters:', get_available_letters(letters_guessed))
    letter = input('Please guess a letter:')
    # Given that the longest possible word is 10 letters, 18 should be the
    # maximum number of needed runs (3 warnings, 9 correct guesses and 6 wrong)

# run the following two lines to play the normal game
secret_word = choose_word(wordlist)
hangman(secret_word)

# run the following two lines to play with hints enabled
secret_word = choose_word(wordlist)
hangman_with_hints(secret_word)