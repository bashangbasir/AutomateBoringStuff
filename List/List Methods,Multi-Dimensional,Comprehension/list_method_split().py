# Define a word_lengths function that accepts a string. 
# It should return a list with the lengths of each word.
#
# EXAMPLES
# word_lengths("Mary Poppins was a nanny")  => [4, 7, 3, 1, 5]
# word_lengths("Somebody stole my donut")   => [8, 5, 2, 5]

def word_lengths(phrase):
    words = phrase.split(" ")
    words_length = []
    for word in words:
        words_length.append(len(word))
    return words_length
    