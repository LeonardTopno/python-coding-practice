"""
Let's say we have a list
"""
my_list = [5, 10, 15, 20, 25, 30]
print(my_list)


# Q1 : Can you make another list from which contains first 3 elements of my_list

new_list_1 = my_list[0:3]
print(new_list_1)

# Q1-(i): What will be the output of the following 
print(my_list[:3])
print(my_list[:3:])

# Q2: Can you make another list which contains 3rd and 4th elem of my_list
new_list_2 = my_list[2:4]
print(new_list_2)

# Q3: What will be the output of this 
new_list_3 = my_list[::]
print(new_list_3)


# Q4: Make a list which is the reverse of my_list without altering my_list
new_list_4_i = my_list[::-1]
print(new_list_4_i)

new_list_4_ii = reversed(my_list) # This gives list_reverseiterator object
new_list_4_ii=list(new_list_4_ii)
print(new_list_4_ii)

print(my_list)


# Q5: Can you update the first three elem of my_list to it's negative value (all at once)
my_list[:3] = [elem * -1 for elem in my_list[:3]] 
print(my_list) 




"""
my_list.reverse() # This operates on origianl list itself 
print(my_list)
"""
