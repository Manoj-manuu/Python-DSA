def has_unique_chars(string):
    
    # char_set = list(set(string))
    # if len(string) != len(char_set):
    #     return False
    # return True
    
    char_set = set()
    for ch in string:
        if ch in char_set:
            return False
        char_set.add(ch)
    return True



print(has_unique_chars('abcdefg')) # should return True
print(has_unique_chars('hello')) # should return False
print(has_unique_chars('')) # should return True
print(has_unique_chars('0123456789')) # should return True
print(has_unique_chars('abacadaeaf')) # should return False



