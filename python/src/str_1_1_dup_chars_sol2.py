'''
Cracking the Coding Interview
Problem 1.1
Implement an algorithm to determine if a string has all unique
characters.  What if you cannot use additional structures?

Solution 2
This solution checks for duplicates in place. See the mathproofs/MATHPROOF.pdf
file for an explanation of how, and proof that, the algorithm works. This
solution has a time complexity of O(n^2) and a space complexity of O(1).

Functions:

    dup_char_in_str(string)

Misc variables:

    __all__
'''
__all__ = ["dup_char_in_str",]


def dup_char_in_str(_string):
    '''Determine if string has duplicate chars.'''
    if type(_string) != str:
        return False
    
    for i in range(len(_string)-1):
        for j in range(i+1, len(_string)):
            if _string[i] == _string[j]:
                return True
    return False