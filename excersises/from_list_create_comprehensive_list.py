
# From List
list1 = [1, 2, 5, 6]
# We will create comprehensive list which its values are tuples one is the initial value from list1, 
#   the second value in each tuple is going to be the same value power3.
res = list(map(lambda x: (x, x**3), list1))
print(res)