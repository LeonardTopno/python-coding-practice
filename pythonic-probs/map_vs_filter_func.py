# Leo's special notes
# Let's see some ideal uses of map() and filter() function

"""
map() function should ideally be used with function which does not return boolean results,
but actual values. like here in the example.
"""

# Print the doubles of numbers from 0 to 10(excluding 10)
print(list(map(lambda var: var * 2, range(0, 10))))
# Output: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]


"""
filter() has be used with a user-defined function which returns boolean results
filter() func - Returns a sequence comprising of those elements of the iterables, for which the function returns True
"""
# Print all the even numbers from 0 to 10(excluding 10)
print(list(filter(lambda var: var % 2 == 0, range(0, 10))))
# Output: [0, 2, 4, 6, 8]
"""
Here lambda function is checking if a number is an even number or not (boolean result)
Here the original iterable was [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
Filter returned a subset of the original iterable [1, 2, 4, 6, 8]
"""

# --------------------
"""
If is known that in filter() func, the user-defined function which is passed in as 1st argument, should be a function 
which should be returning boolean result (True/False), actual use of filter().

Ques: Can filter() function be used with a user defined-function which does not returns boolean result?
Ans: Yes, technically one can use such function in filter() func, but that would not
be the most effective use of filter() func. That function will be treated as function which returns 
boolean results. See the example below.

"""

print(list(filter(lambda var: var * 2, range(0, 10))))
# Output:  [1, 2, 3, 4, 5, 6, 7, 8, 9]

"""
Explanation:
Technically  the expression var*2 is not a boolean expression(but a mathematical),
but here inside filter() func, it is being treated as boolean expression.

It is checking in var*2 is a non-zero number. If True, print.
For 0, var*2 is 0. Hence it not included. 

"""

# --------------------
"""
Now it is know that with filter() func, one should necessarily use a user-defined function which returns
boolean results.
What happens if we use such functions with map() func.?
Let's check that out.
"""

print(list(map(lambda var: var % 2 == 0, range(0, 10))))
# Output: [True, False, True, False, True, False, True, False, True, False]

'''
When we use a function (actually a  user defined function) which returns boolean results,
with map() func, we get the results, but practically it cannot used directly. eg - just above this.
'''
