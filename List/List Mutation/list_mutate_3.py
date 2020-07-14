# Define a long_strings function that accepts a list of strings. 
# It should return a new list consisting of only the strings that have 5 characters or more.
#
# EXAMPLES
# long_strings(["Hello", "Goodbye", "Sam"])  => ["Hello", "Goodbye"]
# long_strings(["Ace", "Cat", "Job"])        => []
# long_strings([])                           => []

def long_strings(phrases):
    long_phrases = []
    for phrase in phrases:
        if len(phrase) > 4: 
            long_phrases.append(phrase)
    return long_phrases
    