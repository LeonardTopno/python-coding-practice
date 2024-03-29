# using list comprehension, find all the even numbers from 0 to 100
print([num for num in range(0, 100+1) if num % 2 == 0])
print([num for num in range(0, 100+1) if not num % 2])
# Leo's personal coding tip
"""
Use 'elem' in case of elements in a list or array 
Here use 'num' as we are dealing with numbers using the built-in function range 
""" 

#  ---------------------

# Q2: Flatten this multidimensional list

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

