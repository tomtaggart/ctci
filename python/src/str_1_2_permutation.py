'''Given two strings, s1 & s2, define a function that determines whether a
s2 is a permutation of s1.

Solution 1
As a first step you check both string lengths. If the strings are not the same
length they are not permutations of one another. If string lengths are equal,
the solution utilizes a hash table initialized as empty. The hash table will
have a string:int format. As you iterate through s1 if the char is not in the
hash table you add the char with a value of 1. If the char is in the hash table,
you increment the value of that char +1. You will wind up with a table of unique
chars and their occurance count.

Next you iterate through s2. The following checks are made:
  - If a char in s2 is not in the hash table, then the char is unique to s2 and
  the strings are not permutations.
  - If the char is in the hash table, check the value. If the value is equal to
  zero, then there are 1 too many of the particular char in s2 and the strings
  are not permutations.
  - if the value is greater than 0, subtract 1 from the value.

Inevitably, iterating s2 will bring all values down to 0.

This solution has a time and space complexity of O(n).


Solution 2
A second solution exists where you can use an array instead of a hashmap in
cases where the char set is small, e.g., ASCII. I am not implementing that here
as it is trivial to do so and Python does not have a builtin array data
structure.

Functions:

    permutation_of_str(string)

Misc variables:

    __all__
'''
__all__ = ["permutation_of_str",]


def permutation_of_str(_str1, _str2):
    '''Determine if str1 is a permutation of str2.'''
    if type(_str1) != str or type(_str2) != str:
        return False
    
    if len(_str1) != len(_str2):
        return False
    
    _char_db = {}
    # Fill hashmap with _str1 char counts
    for _char in _str1:
        if _char_db.get(_char):
            _char_db[_char] += 1
        else:
            _char_db[_char] = 1
    
    for _char in _str2:
        if _char not in _char_db:
            return False
        else:
            if _char_db[_char] == 0:
                return False
            else:
                _char_db[_char] -= 1
    
    return True