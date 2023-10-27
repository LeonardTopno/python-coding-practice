"""
Date: 25th OCt 2023
Motive: Practising for Interview
"""



#  ---------------------
"""
# Flatten this nested list
"""

nested_list = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]

flattened_list = []
for mylist in nested_list:
    for elem in mylist:
        flattened_list.append(elem)
print("Given nested list\n", nested_list)
print("flattened list: \n", flattened_list)

# Doing the same question using list comprehension
flattened_list_using_list_comprehension = [elem for temp in nested_list for elem in temp]
print(flattened_list_using_list_comprehension)











