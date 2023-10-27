"""
Prints every 3rd element in the List, using For Loop
"""

given_list = [2, 4, 6, 8, 10, 12, 14, 16, 18]
print("Given List: ", given_list)
print(enumerate(given_list))
print("Every 3rd element in the List: ", end=" ")
for counter, item in enumerate(given_list):
    if counter >= 2 and counter % 2 == 0:
        print(item, end=" ")

# ------------------------------- Problem Statement --------------------------------------
'''
Fetch every 3rd item in the list: For Loop
'''
