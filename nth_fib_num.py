
def getNthFib(n):
    '''
    gets nth number in Fibonacci Series
    '''

    if n==1:
        return 0

    if n<=3:
        return 1

    return getNthFib(n-1) + getNthFib(n-2)

#Driver Program
print(getNthFib(3))

#-----------------------------------------------------------------------

# 2nd Method [Same Logic but using dictionary instead of if condition]
def getNthFib2(n, calculated = {1:0, 2:1, 3:1} ): # calculated is a dictionary

    if n in calculated:
        return calculated[n] # This is how we access the dictionary elements

    return getNthFib2(n-1) + getNthFib2(n-2) 

# Driver Program
print(getNthFib2(3))

#-----------------------------------------------------------------------
'''
# Nth number in Fibonacci Sequence.
The Fibonacci sequence is defined as follows:
The first number of the sequence is 0,
The second number of the sequence is 1,
the nth number is the sum of the (n-1)th and (n-2)th numbers.

Write a function that takes an integer n and returns nth number in Fibonacci Sequence

'''