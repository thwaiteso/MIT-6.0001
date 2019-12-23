# 6.0001 Problem Set 3
#
# The 6.0001 Word Game
# Created by: Kevin Luu <luuk> and Jenna Wiens <jwiens>
#
# Name          : <your name>
# Collaborators : <your collaborators>
# Time spent    : <total time>

import math
import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

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
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq
	

# (end of helper code)
# -----------------------------------

#
# Problem #1: Scoring a word
#
def get_word_score(word, n):
    """
    Returns the score for a word. Assumes the word is a
    valid word.

    You may assume that the input word is always either a string of letters, 
    or the empty string "". You may not assume that the string will only contain 
    lowercase letters, so you will have to handle uppercase and mixed case strings 
    appropriately. 

	The score for a word is the product of two components:

	The first component is the sum of the points for letters in the word.
	The second component is the larger of:
            1, or
            7*wordlen - 3*(n-wordlen), where wordlen is the length of the word
            and n is the hand length when the word was played

	Letters are scored as in Scrabble; A is worth 1, B is
	worth 3, C is worth 3, D is worth 2, E is worth 1, and so on.

    word: string
    n: int >= 0
    returns: int >= 0
    """
    word = word.lower() # make the word lowercase
    wordlen = len(word) # get a value for the length of the word
    comp1 = 0 # component 1, the sum of the points for the letter in the word
    comp2 = 7 * wordlen - 3 * (n - wordlen) # component 2
    
    # run a loop adding the value of each letter in word to comp1
    for character in word: # for every character in the word
        if character in SCRABBLE_LETTER_VALUES: # look for the value associated
            # with that character
            comp1 += SCRABBLE_LETTER_VALUES[character] # add the value to comp1
    if comp2 > 1: # if comp2 is greater than 1
        return comp1 * comp2
    else: # if comp2 is less than 1
        return comp1 * 1
#
# Make sure you understand how this function works and what it does!
#
        
def display_hand(hand):
    """
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    
    for letter in hand.keys():
        for j in range(hand[letter]):
             print(letter, end=' ')      # print all on the same line
    print()                              # print an empty line
    # each key (letter) has a value (number of times it appears in the hand).
    # this will look at each letter in the hand, printing that letter the 
    # number of times it is in the hand.
#
# Make sure you understand how this function works and what it does!
# You will need to modify this for Problem #4.
#
    
def deal_hand(n):
    """
    Returns a random hand containing n lowercase letters.
    ceil(n/3) letters in the hand should be VOWELS (note,
    ceil(n/3) means the smallest integer not less than n/3).

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    
    hand = {}
    num_vowels = int(math.ceil(n / 3))
    # ceil function returns the smallest interger value which is greater than
    # or equal to the specified expression.
    # e.g. 7 / 3 is 2.333, therefore the smallest interger which is greater 
    # than that is 3.
    for i in range(num_vowels - 1):
        x = random.choice(VOWELS) # chooses a random vowel
        hand[x] = hand.get(x, 0) + 1 # add the random vowel to hand and add
        # one to the number of times it has been added    
    for i in range(num_vowels, n):    
        x = random.choice(CONSONANTS) # choose a random consonant
        hand[x] = hand.get(x, 0) + 1 # add the random consonant to hand and 
        # add one to the number of times it has been added
    hand['*'] = 1
    return hand

#
# Problem #2: Update a hand by removing letters
#
def update_hand(hand, word):
    """
    Does NOT assume that hand contains every letter in word at least as
    many times as the letter appears in word. Letters in word that don't
    appear in hand should be ignored. Letters that appear in word more times
    than in hand should never result in a negative count; instead, set the
    count in the returned hand to 0 (or remove the letter from the
    dictionary, depending on how your code is structured). 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    new_hand = hand.copy()
    word = word.lower()
    for letter in new_hand:
        if letter in word:
            new_hand[letter] = new_hand.get(letter) - word.count(letter)
    return new_hand

#
# Problem #3: Test word validity
#   
def is_valid_word(word, hand, word_list):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.
   
    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    returns: boolean
    """
    new_hand = hand.copy()
    word = word.lower()
    d_vals = new_hand.values()
    vowels = 'aeiou'
    ind = word.find('*')
    
    if '*' in word: # if the user has used a wildcard in guessing a word
        for letter in vowels: # use every vowel
            new_word = word[:ind] + letter + word[ind + 1:] # make new word
            # substituting the asterisk for the vowel
            while new_word in word_list: # if the word is in the wordlist
                for letter in new_hand: # for each letter in the hand
                    if letter in word: # if that letter is in the word
                        new_hand[letter] = new_hand.get(letter) - word.count(letter) 
                        # remove the letter from the hand by the number of
                        # times it appears in the word
                        word = word.replace(letter, '', word.count(letter))
                        # remove the letter from the word
                    if letter == '*': # if the letter in the hand is a wildcard
                        for letter in vowels: # for each vowel
                            if letter not in new_hand: # if the vowel is also
                                # not already in the hand 
                                new_hand['*'] = new_hand.get('*') - word.count(letter) 
                                # remove the asterisk from the hand
                                word = word.replace(letter, '', word.count(
                                        letter)) # remove the letter from word                           
                if new_hand == hand: # if new_hand has not changed, no letters
                    # have been used to guess the word, so word cannot be fully
                    # guessed
                    return False
                else: # if new_hand has changed, letters have been guessed
                    for i in d_vals: # for every value in the new_hand 
                        if i < 0: # if a letter has been used in the hand more
                            # times than it was available
                            return False
                    if word == '': # if the word has been completely guessed
                        return True
                    else: # if the word has not been completely guessed
                        return False
    else: # if the user has not used a wildcard in guessing a word
        while word in word_list: # if the word is in the wordlist
            for letter in new_hand: # for each letter in the hand
                if letter in word: # if that letter is in the word
                    new_hand[letter] = new_hand.get(letter) - word.count(letter)
                    # remove the letter from the hand by the number of times 
                    # it appears in the word
                    word = word.replace(letter, '', word.count(letter))    
                    # remove the letter from word                        
            if new_hand == hand: # if new_hand has not changed, no letters
                    # have been used to guess the word, so word cannot be fully
                    # guessed
                return False
            else: # if new_hand has changed, letters have been guessed
                for i in d_vals: # for every value in the new_hand 
                    if i < 0: # if a letter has been used in the hand more
                        # times than it was available
                        return False
                if word == '': # if the word has been completely guessed
                    return True
                else: # if the word has not been completely guessed
                    return False
        else: # if the word is not in the wordlist
            return False
#
# Problem #5: Playing a hand
#
def calculate_handlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string-> int)
    returns: integer
    """
    d_vals = hand.values()
    sum_d_vals = 0
    for i in d_vals:
        sum_d_vals += i
    return sum_d_vals

def play_hand(hand, word_list):

    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    
    * The user may input a word.

    * When any word is entered (valid or invalid), it uses up letters
      from the hand.

    * An invalid word is rejected, and a message is displayed asking
      the user to choose another word.

    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.

    * The sum of the word scores is displayed when the hand finishes.

    * The hand finishes when there are no more unused letters.
      The user can also finish playing the hand by inputing two 
      exclamation points (the string '!!') instead of a word.

      hand: dictionary (string -> int)
      word_list: list of lowercase strings
      returns: the total score for the hand
      
    """
    # Keep track of the total score
    total_score = 0
    
    # As long as there are still letters left in the hand:
    while calculate_handlen(hand) > 0:
        # Display the hand
        display_hand(hand)
        # Ask user for input
        guess = str(input('Enter word, or !! to indicate that you are finished:'))
        # If the input is two exclamation points:
        if guess == '!!':
            # End the game (break out of the loop)
            print('Total score:', total_score)
            return total_score
            
        # Otherwise (the input is not two exclamation points):
        else:
            # If the word is valid:
            if is_valid_word(guess, hand, word_list) is True:
                # Tell the user how many points the word earned,
                # and the updated total score
                print(guess, 'earned', get_word_score(
                        guess, calculate_handlen(hand)), 'points')
                total_score += get_word_score(guess, calculate_handlen(hand))
                print('Total:', total_score)
            # Otherwise (the word is not valid):
            else:
                # Reject invalid word (print a message)
                print('That is not a valid word. Please choose another word.')
                
            # update the user's hand by removing the letters of their inputted word
            hand = update_hand(hand, guess)

    # Game is over (user entered '!!' or ran out of letters),
    # so tell user the total score
    # Return the total score as result of function
    print('Ran out of letters. Total score:', total_score)
    return total_score

#
# Problem #6: Playing a game
# 
#
# procedure you will use to substitute a letter in a hand
#

def substitute_hand(hand, letter):
    """ 
    Allow the user to replace all copies of one letter in the hand (chosen by user)
    with a new letter chosen from the VOWELS and CONSONANTS at random. The new letter
    should be different from user's choice, and should not be any of the letters
    already in the hand.

    If user provide a letter not in the hand, the hand should be the same.

    Has no side effects: does not mutate hand.

    For example:
        substitute_hand({'h':1, 'e':1, 'l':2, 'o':1}, 'l')
    might return:
        {'h':1, 'e':1, 'o':1, 'x':2} -> if the new letter is 'x'
    The new letter should not be 'h', 'e', 'l', or 'o' since those letters were
    already in the hand.
    
    hand: dictionary (string -> int)
    letter: string
    returns: dictionary (string -> int)
    """
    new_hand = hand
    while letter in hand: # if the user has the letter in their hand
        while letter in VOWELS: # if the letter is a vowel
            vowels = VOWELS.replace(letter, '') # remove the vowel so that it
            # does not get replaced by itself
            rand_vowel = random.choice(vowels) # choose a random vowel
            while rand_vowel not in hand: # make sure the random vowel is not
                # already in the hand
                new_hand[rand_vowel] = new_hand[letter] # add the random vowel
                # to the hand, assigning it the value of the letter being
                # replaced
                del(new_hand[letter]) # delete the letter being replaced
                return new_hand
        else: # if the letter is not a vowel
            cons = CONSONANTS.replace(letter, '') # remove the consonant so 
            # that it does not get replaced by itself
            rand_cons = random.choice(cons) # choose a random consonant
            while rand_cons not in hand: # make sure the random consonant is 
                # not already in the hand
                new_hand[rand_cons] = new_hand[letter] # add the random consonant
                # to the hand, assigning it the value of the letter being
                # replaced
                del(new_hand[letter]) # delete the letter being replaced
                return new_hand
    else: # if the user does not have the letter in their hand
        return hand   
    
def play_game(word_list):
    """
    Allow the user to play a series of hands

    * Asks the user to input a total number of hands

    * Accumulates the score for each hand into a total score for the 
      entire series
 
    * For each hand, before playing, ask the user if they want to substitute
      one letter for another. If the user inputs 'yes', prompt them for their
      desired letter. This can only be done once during the game. Once the
      substitue option is used, the user should not be asked if they want to
      substitute letters in the future.

    * For each hand, ask the user if they would like to replay the hand.
      If the user inputs 'yes', they will replay the hand and keep 
      the better of the two scores for that hand.  This can only be done once 
      during the game. Once the replay option is used, the user should not
      be asked if they want to replay future hands. Replaying the hand does
      not count as one of the total number of hands the user initially
      wanted to play.

            * Note: if you replay a hand, you do not get the option to substitute
                    a letter - you must play whatever hand you just had.
      
    * Returns the total score for the series of hands

    word_list: list of lowercase strings
    """
    # input number of hands
    # total score across all hands
    # substitute yes/no, ask for letter, once per game
    # replay hand when !! or out of letters, once per game, take highest score
    # cannot substitute if replaying hand
    # return total score for hands
    hand_num = int(input('Enter total number of hands:'))
    total_score = 0
    replays = 1
    subs = 1
    
    while hand_num > 0: # while there are still hands left to play
        hand1 = deal_hand(HAND_SIZE) # deal a hand
        print('Current hand:', end = '')
        display_hand(hand1) # display the hand
        if subs > 0: # if you have substitutions available
            sub = input('Would you like to substitute a letter (yes / no)?')
            if sub == 'yes': # if user requests a substitution
                replace = input('Which letter would you like to replace?')
                hand1 = substitute_hand(hand1, replace) # replace letter
                score = play_hand(hand1, word_list) # play hand
                total_score += score # add score to total
                hand_num -= 1 # one hand played
                subs -= 1 # one substitution used
            else: # if user does not request a substitutuion
                score = play_hand(hand1, word_list) # play hand
                total_score += score # add score to total
                hand_num -= 1 # one hand played
            if replays > 0: # if user has replays remaining
                replay = input('Would you like to replay the hand (yes / no)?')
                if replay == 'yes': # if user would like a replay
                    replays -= 1 # replay used
                    score1 = play_hand(hand1, word_list) # play replayed hand
                    if score > score1: # if score in original play is higher
                        total_score += score # add it to total
                    else: # if score in replayed hand is higher
                        total_score += score1 # add it to total
                else: # if user would not like a replay
                    while hand_num > 0: # while there are still hands left 
                        hand1 = deal_hand(HAND_SIZE) # deal new hand
                        print('Current hand:', end = '')
                        display_hand(hand1) # display the hand
                        score = play_hand(hand1, word_list) # play game
                        total_score += score # add score to total
                        hand_num -= 1 # hand played
                        break # goes back to first while loop
            else: # if user does not have replays remaining
                while hand_num > 0: # while there are still hands left 
                    hand1 = deal_hand(HAND_SIZE) # deal new hand
                    print('Current hand:', end = '')
                    display_hand(hand1) # display the hand
                    score = play_hand(hand1, word_list) # play game
                    total_score += score # add score to total
                    hand_num -= 1 # hand played
        else: # no subs remaining
            if replays > 0: # if user has replays remaining
                replay = input('Would you like to replay the hand (yes / no)?')
                if replay == 'yes': # if user would like a replay
                    replays -= 1 # replay used
                    score1 = play_hand(hand1, word_list) # play replayed hand
                    if score > score1: # if score in original play is higher
                        total_score += score # add it to total
                    else: # if score in replayed hand is higher
                        total_score += score1 # add it to total
                else: # if user would not like a replay
                    while hand_num > 0: # while there are still hands left 
                        hand1 = deal_hand(HAND_SIZE) # deal new hand
                        print('Current hand:', end = '')
                        display_hand(hand1) # display the hand
                        score = play_hand(hand1, word_list) # play game
                        total_score += score # add score to total
                        hand_num -= 1 # hand played
            else: # if user does not have replays remaining
                while hand_num > 0: # while there are still hands left 
                    hand1 = deal_hand(HAND_SIZE) # deal new hand
                    print('Current hand:', end = '')
                    display_hand(hand1) # display the hand
                    score = play_hand(hand1, word_list) # play game
                    total_score += score # add score to total
                    hand_num -= 1 # hand played
    return print('Total score over all hands:', total_score)

#
# Build data structures used for entire session and play game
# Do not remove the "if __name__ == '__main__':" line - this code is executed
# when the program is run directly, instead of through an import statement
#
if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)
