# Declare a same_index_values function that accepts two lists.
# The function should return a list of the index positions in which the two lists have equal elements
#
# EXAMPLES
# same_index_values([1, 2, 3], [3, 2, 1])                         => [1]
# same_index_values(["a", "b", "c", "d"], ["c", "b", "a", "d"])   => [1, 3]

def same_index_values(values1, values2):
    
    same_index = []
    for index1,value1 in enumerate(values1):
        if value1 == values2[index1]:
            same_index.append(index1)
            
    return same_index
            
                
            