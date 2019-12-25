
import string

### HELPER CODE ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    print("Loading word list from file...")
    # inFile: file
    inFile = open(file_name, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.extend([word.lower() for word in line.split(' ')])
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    
    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list

def get_story_string():
    """
    Returns: a story in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story

### END HELPER CODE ###

WORDLIST_FILENAME = 'words.txt'

class Message(object):
    def __init__(self, text):
        '''
        Initializes a Message object
                
        text (string): the message's text

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)

    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        return self.message_text

    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class.
        This helps you avoid accidentally mutating class attributes.
        
        Returns: a COPY of self.valid_words
        '''
        valid_words = self.valid_words
        return valid_words

    def build_shift_dict(self, shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.        
        
        shift (integer): the amount by which to shift every letter of the 
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        low_letters = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0,
                       'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0,
                       'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0,
                       'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}
        cap_letters = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 
                       'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 
                       'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 
                       'V': 0, 'W': 0, 'X': 0, 'Y': 0, 'Z': 0}
        special_dict = {}
        s_low = string.ascii_lowercase[shift:] + string.ascii_lowercase[:shift]
        s_cap = string.ascii_uppercase[shift:] + string.ascii_uppercase[:shift]
        special = list(" 1234567890!£$%^&*()-_=+[]{};:'@,.<>/?\|`¬")
        low = 0
        cap = 0
        for char in low_letters: # for every character in lower case letters
            low_letters[char] = s_low[low] # replace the value at the key (char)
            # with the character at index (low) in s_low
            low += 1 # add one to index position
        for char in cap_letters: # for every character in upper case letters
            cap_letters[char] = s_cap[cap] # replace the value at the key (char)
            # with the character at index (cap) in s_cap
            cap += 1 # add one to index position
        for char in special: # for every character in the special characters 
            special_dict[char] = char # match it to the key
        letters = {**low_letters, **cap_letters, **special_dict}
        # merge all dicts into one
        return letters
        

    def apply_shift(self, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift        
        
        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''
        shift_dict = self.build_shift_dict(shift)
        shift_text = ''
        text = Message.get_message_text(self)
        for char in text: # for every character in the text
            letter = shift_dict[char] # replace the char with its shifted letter
            shift_text += letter # add the letter to shifted text
        return shift_text

class PlaintextMessage(Message):
    def __init__(self, text, shift):
        '''
        Initializes a PlaintextMessage object        
        
        text (string): the message's text
        shift (integer): the shift associated with this message

        A PlaintextMessage object inherits from Message and has five attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
            self.shift (integer, determined by input shift)
            self.encryption_dict (dictionary, built using shift)
            self.message_text_encrypted (string, created using shift)

        '''
        Message.__init__(self, text)
        self.shift = shift
        self.get_encryption_dict = self.build_shift_dict(shift)
        self.message_text_encrypted = self.apply_shift(shift)

    def get_shift(self):
        '''
        Used to safely access self.shift outside of the class
        
        Returns: self.shift
        '''
        return self.shift

    def get_encryption_dict(self):
        '''
        Used to safely access a copy self.encryption_dict outside of the class
        
        Returns: a COPY of self.encryption_dict
        '''
        encrypt = self.get_encryption_dict
        return encrypt

    def get_message_text_encrypted(self):
        '''
        Used to safely access self.message_text_encrypted outside of the class
        
        Returns: self.message_text_encrypted
        '''
        return self.message_text_encrypted

    def change_shift(self, shift):
        '''
        Changes self.shift of the PlaintextMessage and updates other 
        attributes determined by shift.        
        
        shift (integer): the new shift that should be associated with this message.
        0 <= shift < 26

        Returns: nothing
        '''
        self.shift = shift


class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object
                
        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        Message.__init__(self, text)
        self.valid_words = load_words(WORDLIST_FILENAME)

    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value 
        for decrypting it.

        Note: if multiple shifts are equally good such that they all create 
        the maximum number of valid words, you may choose any of those shifts 
        (and their corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''
        best = 0
        max_real_words = 0
        for i in range(26): # max possible shift is 26
            real_words = 0
            shift_applied = self.apply_shift(26 - i) # apply the shift
            for word in shift_applied.split(' '): # separate into words by ' ',
                # for each word found
                if is_word(self.get_valid_words(), word) is True: # if the word
                    # is valid
                    real_words += 1 # add one to number of real words
                if real_words >= max_real_words: # when completed, if the 
                    # number of real words is greater than or equal to the 
                    # maximum number of real words found
                    max_real_words = real_words # make this the new maximum
                    best = i # make this shift the new best
        return (26 - best, self.apply_shift(26 - best))
    # return the best shit, and apply it
    
if __name__ == '__main__':

    #Example test cases (PlaintextMessage)
    plaintext = PlaintextMessage('hello', 2)
    print('Expected Output: jgnnq')
    print('Actual Output:', plaintext.get_message_text_encrypted())
    # Actual Output: jgnnq
    
    plaintext2 = PlaintextMessage('I really hope this works', 17)
    print('Expected Output: Z ivrccp yfgv kyzj nfibj')
    print('Actual Output:', plaintext2.get_message_text_encrypted())
    # Actual Output: Z ivrccp yfgv kyzj nfibj
    
    #Example test cases (CiphertextMessage)
    ciphertext = CiphertextMessage('jgnnq')
    print('Expected Output:', (24, 'hello'))
    print('Actual Output:', ciphertext.decrypt_message())
    # Actual Output: (24, 'hello')
    
    ciphertext2 = CiphertextMessage('Qbokd, sd nyoc gybu')
    print('Expected Output:', (16, 'Great, it does work'))
    print('Actual Output:', ciphertext2.decrypt_message())
    # Actual Output: (16, 'Great, it does work')
    
    cipher_story = CiphertextMessage(get_story_string())
    print(cipher_story.decrypt_message())
    # (12, 'Jack Florey is a mythical character created on the spur of a moment
    # to help cover an insufficiently planned hack. He has been registered for 
    # classes at MIT twice before, but has reportedly never passed aclass. 
    # It has been the tradition of the residents of East Campus to become Jack
    # Florey for a few nights each year to educate incoming students in the 
    # ways, means, and ethics of hacking.')
