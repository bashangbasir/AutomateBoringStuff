# Define an encrypt_message function that accepts a string.
# The input string will consist of only alphabetic characters.
# The function should return a string where all characters have been moved
# "up" two spots in the alphabet. For example, "a" will become "c".
#
# EXAMPLES
# encrypt_message("abc") => "cde"
# encrypt_message("xyz") => "zab"
# encrypt_message("")    => ""

def encrypt_message(phrase):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    encrypt = ""
    
    for char in phrase:
        #modulus is used to check the position of the index if the index value is more than 26 if add by 2 since it give the reminder of divided by 26.
        index_encrypt = (alphabet.index(char) + 2) % 26
        encrypt +=alphabet[index_encrypt]
    return encrypt
    
        
        