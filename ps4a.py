
def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    perms = [] # empty list to be filled with all permutations of sequence
    if len(sequence) <= 1: # base case - if sequence is a single character,
        return list(sequence) # return list of just the character
    else: # recursive case
        new_seq = get_permutations(sequence[1:]) # make a new sequence, 
        # removing the first letter
        for s in new_seq:
            for i in range(len(s) + 1):
                perms.append(s[:i] + sequence[0] + s[i:])
    return perms
# first new_sq is two letter (e.g. bc), get_permutations called with sequence
# 'bc'.
# 'bc' length is greater than 1, so get_permutations called again with 
# sequence 'c'.
# c has length 1, so c is returned, we go back a level to get_permutations 
# where sequence was 'bc'.
# new_sq is equal to ['c'] 
    # - for i where i = 0:
        # perms appended with 'bc' - sequence[0] is 'b' and s[i:] is 'c'
    # - for i where i = 1:
        # perms appended with 'cb' - s[:i] is 'c' and sequence[0] is 'b'.
# go back a level to get_permutations where sequence was 'abc'.
# new_seq is ['bc', 'cb'] - for s in new_sq starts with 'bc'.
    # for s in new_sq = 'bc'
    # - for i where i = 0:
        # perms appended with 'abc' - s[:i] is '', sequence[0] is 'a' and 
        # s[i:] is 'bc'
    # - for i where i = 1:
        # perms appended with 'bac' - s[:i] is 'b', sequence[0] is 'a' and 
        # s[i:] is 'c'
    # - for i where i = 2:
        # perms appended with 'bca' - s[:i] is 'bc', sequence[0] is 'a' and 
        # s[i:] is ''
    # for s in new_sq = 'cb', and the for i loops again, adding 'acb', 'cab'
    # and 'cba'

if __name__ == '__main__':
    example_input = 'abc'
    print('Input:', example_input)
    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    print('Actual Output:', get_permutations(example_input))
    # Actual Output: ['abc', 'bac', 'bca', 'acb', 'cab', 'cba']
    
    example_input = 'jsi'
    print('Input:', example_input)
    print('Expected Output:', ['jsi', 'jis', 'sji', 'sij', 'ijs', 'isj'])
    print('Actual Output:', get_permutations(example_input))
    # Actual Output: ['jsi', 'sji', 'sij', 'jis', 'ijs', 'isj']
    
    example_input = 'hao'
    print('Input:', example_input)
    print('Expected Output:', ['hao', 'hoa', 'aho', 'aoh', 'oha', 'oah'])
    print('Actual Output:', get_permutations(example_input))
    # Actual Output: ['hao', 'aho', 'aoh', 'hoa', 'oha', 'oah']
    

