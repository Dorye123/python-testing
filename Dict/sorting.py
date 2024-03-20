# https://www.geeksforgeeks.org/python-sort-python-dictionaries-by-key-or-value/
# sorting by key
myDict = {'ravi': 10, 'rajnish': 9,
        'sanjeev': 15, 'yash': 2, 'suraj': 32}
 
myKeys = list(myDict.keys())
myKeys.sort()
sorted_dict = {i: myDict[i] for i in myKeys}
 
print(sorted_dict)

