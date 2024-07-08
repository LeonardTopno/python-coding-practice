# Proiblem 1: Print reverse of the follwing list
list1 = [100, 200, 300, 400, 500]

# Reversing the list
reversed_list = list1[::-1]  # using slicing
print(reversed_list)


## --------------------------------------- 
# Problem 2
list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]

# Iterating over both lists simultaneously
for item1, item2 in zip(list1, list2):
    print(f"{item1}, {item2}")


## --------------------------------------- 

# Problem 3: Get a list of squares 
list1 = [2, 3, 4, 5, 6]

'''
Expected logic:
a) using for loop
b) without using for loop
'''

# a) Using a for loop
squares = []
for item in list1:
    squares.append(item ** 2)

print(squares)
  
  

# b) Using list comprehension
squares = [item ** 2 for item in list1]

print(squares)

## --------------------------------------- 
# Problem 4:

list1 = [10, 20]
list2 = [100, 200]

combinations = []
for item1 in list1:
    for item2 in list2:
        combinations.append(int(f"{item1}{item2}"))
        #combinations.append(int(f"{item2}{item1}"))

print(combinations)

## --------------------------------------- 
# Problem 5: Convert the following lists to dictionary

keys = ['a', 'b', 'c']
values = [1, 2, 3]

# Using zip and dict to create a dictionary
dictionary = dict(zip(keys, values))

print(dictionary)

""" Solution
{'a': 1, 'b': 2, 'c': 3}

"""

## --------------------------------------- Use of unpacking

# Problem 6: Merge the dictionaries 
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

# Using dictionary unpacking
merged_dict = {**dict1, **dict2}

print(merged_dict)

"""
Output
{'Ten': 10, 'Twenty': 20, 'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
"""

"""Leo's note:
# If the question was to update dict 1 itself, then we would use the update method
dict1.update(dict2)

print(dict1)
"""

## ---------------------------------------
# Problem 9: Print the union and intersection of the two sets 

set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}

# Union of set1 and set2
union_set = set1.union(set2)

# Intersection of set1 and set2
intersection_set = set1.intersection(set2)

print("Union:", union_set)
print("Intersection:", intersection_set)


""" 
Solution:

Union: {1, 2, 3, 4, 5, 6, 7}
Intersection: {3, 4, 5}

"""


## ---------------------------------------

set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}

# Difference of set1 and set2
difference_set = set1.difference(set2)   # difference_set = set1 - set 2

print("Difference:", difference_set)


# Wec an also do the same by doing this





#---------------------------------------
set1 = {1, 2, 3}
set2 = {1, 2, 3, 4, 5}

# Check if set1 is a subset of set2
is_subset = set1.issubset(set2)

print("Is set1 a subset of set2?", is_subset)

