# Declare a delete_all function that accepts a list of strings and a target string
# Remove all occurrences of the target string from the list and return it
#
# EXAMPLES
# delete_all([1, 3, 5], 3)  => [1, 5]
# delete_all([5, 3, 5], 5)  => [3]
# delete_all([4, 4, 4], 4)  => []
# delete_all([4, 4, 4], 6)  => [4, 4, 4]

def delete_all(numbers, target):
   while target in numbers:
       numbers.remove(target)
   return numbers
        