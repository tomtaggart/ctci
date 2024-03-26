'''Define a function that determines whether a string has duplicate characters.

Solution 1
This solution utilizes a hash table initialized as empty. As you iterate through
the string you check the hash table for the char. If the char is in the table
it has occured in the string before and you exit the algorithm. If the char is
not in the table you add it to the table and move on to the next char in the
string for evaluation.

This solution has a time and space complexity of O(n).

Functions:

    dup_char_in_str(string)

Misc variables:

    __all__
'''
__all__ = ["dup_char_in_str",]


def dup_char_in_str(_string):
    '''Determine if a string has duplicate chars.'''
    if type(_string) != str:
        return False
    
    _char_db = {}
    for _char in _string:
        if _char_db.get(_char):
            return True
        else:
            _char_db[_char] = True
    return False