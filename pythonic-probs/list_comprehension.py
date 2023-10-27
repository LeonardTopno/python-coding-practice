# List Comprehension
odd_num = [x for x in range(0, 100) if x % 2 != 0]
print(odd_num)

# 2nd Method: Without List Comprehension

'''
odd_num = []
for num in range(0,100):
    if num%2:               # if num%2 != 0:
        odd_num.append(num)

print(odd_num)
'''

# ------------------------------- Problem Statement --------------------------------------
'''
Using List comprehension  find all the even numbers from 0 to 100
'''
#
print("Even Numbers between 0 qnd 100: \n", [x for x in range(0, 100 + 1) if x % 2 == 0])

# ------------------------------- Problem Statement --------------------------------------
"""
Using List Comprehension, find all Odd Numbers in between 0 and 100
"""

# Please note that it says 'in between' which means 0 amd 100 should be excluded

print("Odd Numbers between 0 and 100 is \n", [num for num in range(0 + 1, 100) if num % 2])
