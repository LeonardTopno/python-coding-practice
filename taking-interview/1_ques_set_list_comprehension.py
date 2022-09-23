# using list comprehension, find all the even numbers from 0 to 100
print([elem for elem in range(0, 100+1) if elem % 2 == 0])
print([elem for elem in range(0, 100+1) if not elem % 2])


# Q2: Flatten this multidimensional list

list_1 = [[10, 20, 20], [30, 40, 50], [60, 70, 80]]
