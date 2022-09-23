# Quiz 2 | 5*
"""
What will be the output of following?
"""
x = [1, 2, 3, 4]
y = [sum(x[0: i-1]) for i in range(0, 4)]  # List Comprehension
print(y)


"""
Output
[6,0,1,3]

# Things to know:
1) Square brackets at the end implies that is list comprehension question, and final outcome will be a list
2) How many elements will be there in the final list?
    i) sum gives one elem, but we have i which ranges from 0 to 4(excluding 4), so i will be from 0 to 3, i.e total 4.
    ii) therefore there will be 4 outputs of sums, hence 4 elements in the list
3) How did the fist element 6 come?
    i) In first iteration i=0, so the list inside sum will be x[0,-1], and elem at -1 (i.e. 4) is to be excluded, and
        by default step is 1 in forward direction, So list will be [1,2,3], hence the expression will be sum([1,2,3]) 

"""


#  -------------------------------------------------------------------------------------------------------
# Quiz 1 | 2*
"""
What will be the output of following?
"""

string = "Python Pi Py Pip"
print(string.count('P', 4))

""" Output
3

# Things to know.
count(substring_to_count, start_index(opt), end_index(opt) )
So here the 'P' should be counted from index 4, i.e. from o 
"""
