
from ps4a import get_permutations

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


### END HELPER CODE ###

WORDLIST_FILENAME = 'words.txt'

# you may find these constants helpful
VOWELS_LOWER = 'aeiou'
VOWELS_UPPER = 'AEIOU'
CONSONANTS_LOWER = 'bcdfghjklmnpqrstvwxyz'
CONSONANTS_UPPER = 'BCDFGHJKLMNPQRSTVWXYZ'

class SubMessage(object):
    def __init__(self, text):
        '''
        Initializes a SubMessage object
                
        text (string): the message's text

        A SubMessage object has two attributes:
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
                
    def build_transpose_dict(self, vowels_permutation):
        '''
        vowels_permutation (string): a string containing a permutation of vowels (a, e, i, o, u)
        
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to an
        uppercase and lowercase letter, respectively. Vowels are shuffled 
        according to vowels_permutation. The first letter in vowels_permutation 
        corresponds to a, the second to e, and so on in the order a, e, i, o, u.
        The consonants remain the same. The dictionary should have 52 
        keys of all the uppercase letters and all the lowercase letters.

        Example: When input "eaiuo":
        Mapping is a->e, e->a, i->i, o->u, u->o
        and "Hello World!" maps to "Hallu Wurld!"

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        
        low_letters = {'a': 'a', 'b': 'b', 'c': 'c', 'd': 'd', 'e': 'e', 
                       'f': 'f', 'g': 'g', 'h': 'h', 'i': 'i', 'j': 'j', 
                       'k': 'k', 'l': 'l', 'm': 'm', 'n': 'n', 'o': 'o', 
                       'p': 'p', 'q': 'q', 'r': 'r', 's': 's', 't': 't', 
                       'u': 'u', 'v': 'v', 'w': 'w', 'x': 'x', 'y': 'y', 
                       'z': 'z'}
        cap_letters = {'A': 'A', 'B': 'B', 'C': 'C', 'D': 'D', 'E': 'E', 
                       'F': 'F', 'G': 'G', 'H': 'H', 'I': 'I', 'J': 'J', 
                       'K': 'K', 'L': 'L', 'M': 'M', 'N': 'N', 'O': 'O', 
                       'P': 'P', 'Q': 'Q', 'R': 'R', 'S': 'S', 'T': 'T', 
                       'U': 'U', 'V': 'V', 'W': 'W', 'X': 'X', 'Y': 'Y', 
                       'Z': 'Z'}
        special_dict = {}
        special = list(" 1234567890!£$%^&*()-_=+[]{};:'@,.<>/?\|`¬")
        low = 0
        cap = 0
        for char in VOWELS_LOWER: # for each lower case vowel
            low_letters[char] = vowels_permutation[low] # replace the value at 
            # the key (char) with the character at index (low) in vowels_perm
            low += 1 # add one to index position
        for char in VOWELS_UPPER: # for each upper case vowel
            cap_letters[char] = vowels_permutation[cap] # replace the value at 
            # the key (char) with the character at index (low) in vowels_perm
            cap += 1 # add one to index position
        for char in special: # for every character in the special characters 
            special_dict[char] = char # match it to the key
        letters = {**low_letters, **cap_letters, **special_dict}
        # merge all dicts into one
        return letters
    
    def apply_transpose(self, transpose_dict):
        '''
        transpose_dict (dict): a transpose dictionary
        
        Returns: an encrypted version of the message text, based 
        on the dictionary
        '''
        
        encrypt = ''
        for char in self.get_message_text(): # for each character in the text
            # needed to be encrypted
            if char in transpose_dict: # if that character is in the transpose
                # dictionary
                encrypt += transpose_dict[char] # add the value (letter)
                # associated with the key (char) to encrypt
            else: # if that character is not in the transpose dictionary
                encrypt += char # add the character to encrypt
        return encrypt
        
class EncryptedSubMessage(SubMessage):
    def __init__(self, text):
        '''
        Initializes an EncryptedSubMessage object

        text (string): the encrypted message text

        An EncryptedSubMessage object inherits from SubMessage and has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        SubMessage.__init__(self, text)
        self.valid_words = load_words(WORDLIST_FILENAME)

    def decrypt_message(self):
        '''
        Attempt to decrypt the encrypted message 
        
        Idea is to go through each permutation of the vowels and test it
        on the encrypted message. For each permutation, check how many
        words in the decrypted text are valid English words, and return
        the decrypted message with the most English words.
        
        If no good permutations are found (i.e. no permutations result in 
        at least 1 valid word), return the original string. If there are
        multiple permutations that yield the maximum number of words, return any
        one of them.

        Returns: the best decrypted message    
        
        Hint: use your function from Part 4A
        '''
        vowel_perm = get_permutations('aeiou')
        valid_words = self.get_valid_words()
        for i in range(len(vowel_perm)): # for each permutation of the sequence
            # of vowels
            t_dict = self.build_transpose_dict(vowel_perm[i]) # build the 
            # transpose dictionary using the permutation of vowels at index i
            decrypt_text = self.apply_transpose(t_dict) # decrypt the text
            decrypt_word = decrypt_text.split() # split the text into words
            real_words = 0
            for word in decrypt_word: # for each word in the decrypted text
                if is_word(valid_words, word): # if the word is real
                    real_words += 1 # add one to real_words
            if i == 0: # on the first run through
                best_decrypt = (decrypt_text, real_words) # make that the best
                # decryption
            else: # on subsequent run throughs
                if best_decrypt[1] < real_words: # if the number of real words
                    # found by the previous best decryption is lower than the
                    # number of real words in this run through
                    best_decrypt = (decrypt_text, real_words) # make this run
                    # through the new best
        return best_decrypt[0] # return the best decrypted text
    

if __name__ == '__main__':

    # Example test cases
    message = SubMessage("Hello World!")
    permutation = "eaiuo"
    enc_dict = message.build_transpose_dict(permutation)
    print("Original message:", message.get_message_text(), "Permutation:", permutation)
    print("Expected encryption:", "Hallu Wurld!")
    print("Actual encryption:", message.apply_transpose(enc_dict))
    enc_message = EncryptedSubMessage(message.apply_transpose(enc_dict))
    print("Decrypted message:", enc_message.decrypt_message())
    
    message2 = SubMessage('I really hope this works')
    permutation2 = "iuoae"
    enc_dict2 = message2.build_transpose_dict(permutation2)
    print("Original message:", message2.get_message_text(), 
          "Permutation:", permutation2)
    print("Expected encryption:", 'o ruilly hapu thos warks')
    print("Actual encryption:", message2.apply_transpose(enc_dict2))
    enc_message2 = EncryptedSubMessage(message2.apply_transpose(enc_dict2))
    print("Decrypted message:", enc_message2.decrypt_message())
    # Decrypted message: u really hope thus works
    
    message3 = SubMessage('It does work, but not all words are perfect!')
    permutation3 = "oaieu"
    enc_dict3 = message3.build_transpose_dict(permutation3)
    print("Original message:", message3.get_message_text(), 
          "Permutation:", permutation3)
    print("Expected encryption:", 'it deas werk, but net oll werds ora parfact!')
    print("Actual encryption:", message3.apply_transpose(enc_dict3))
    enc_message3 = EncryptedSubMessage(message3.apply_transpose(enc_dict3))
    print("Decrypted message:", enc_message3.decrypt_message())
    # Decrypted message: at does work, but not ill words ire perfect!