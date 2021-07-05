# List Comprehension
odd_num = [x for x in range(0,100) if x%2!=0]
print(odd_num)


# 2nd Method: Without List Comprehension

'''
odd_num = []
for num in range(0,100):
    if num%2:               # if num%2 != 0:
        odd_num.append(num)

print(odd_num)
'''

#------------------------------- Problem Statement --------------------------------------
'''
Using LIST COMPREHENSION, print the odd numbers between 0 and 100
'''