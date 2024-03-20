# Python3 code to demonstrate working of
# Assigning Subsequent Rows to Matrix first row elements
# Using zip() + list slicing + dict()

# The Matrix is (N + 1)*N
 
# initializing list
test_list = [[5, 8, 9], [2, 0, 9], [5, 4, 2], [2, 3, 9]]
 
# printing original list
print("The original list : " + str(test_list))
 
# dict() to convert back to dict type
# slicing and pairing using zip() and list slicing
res = dict(zip(test_list[0], test_list[1:]))
 
# printing result
print("The Assigned Matrix : " + str(res))