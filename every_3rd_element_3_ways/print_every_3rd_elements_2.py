# List Comprehension

given_list = [2,4,6,8,10,12,14,16,18]
print("Given List: ", given_list)

new_list = [given_list[index] for index in range(len(given_list)) if index >= 2 and index%2==0]

print("List containing every 3rd item in the list: ", new_list)

#------------------------------- Problem Statement --------------------------------------
'''
Fetch every 3rd item in the list: List Comprehension 
'''
