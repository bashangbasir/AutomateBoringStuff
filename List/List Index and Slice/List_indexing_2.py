# Define a product_of_even_indices function that accepts a list of numbers. 
# The list will always have 6 total elements. 
# The function should return the product (multiplied total) of all numbers at an even index (0, 2, 4).
#
# product_of_even_indices([1, 2, 3, 4, 5, 6])    =>  15
# product_of_even_indices([3, 4, 3, 5, 3, 6])    =>  27

def product_of_even_indices(list_num):
    return list_num[0]*list_num[2]*list_num[4]