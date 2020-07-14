# Define a nested_sum function that accepts a list of lists of numbers
# The function should return the sum of the values
# The list may contain empty lists
#
# EXAMPLES
# nested_sum([[1, 2, 3], [4, 5]])            => 15
# nested_sum([[1, 2, 3], [], [], [4], [5]])  => 15
# nested_sum([[]])                           => 0

def nested_sum(lists_numbers):
    sum = 0
    for list_numbers in lists_numbers:
        if len(list_numbers) == 0 :
            continue
        for number in list_numbers:
            sum += number
    return sum