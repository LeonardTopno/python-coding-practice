"""
Ques: Bring an item to the beginning of the list, keeping the relative position of rest if the items intact
"""
fruits_list = ['Apple', 'Banana', 'Coconut', 'Durian', 'Elderberry', 'Fig', 'Grape']
print(fruits_list)


def bring_to_the_beginning_of_list():

    item1 = input("Type the item to be brought to the beginning of the list: ")

    # Get to know the index of the item in the list
    index_1 = fruits_list.index(item1)

    # Pop that item out (you will have that item in hand, stored in a variable)
    item_ = fruits_list.pop(index_1)  # pop takes index as argument and  

    # Now insert that item_ in hand which you obtained by pop(index_of_item)
    fruits_list.insert(0, item_)

    return fruits_list

"""
while True:
    print(bring_to_the_beginning_of_list())
"""

# One liner for the same function
item = "Durian"

fruits_list.insert(0, fruits_list.pop(fruits_list.index(item)))
print(fruits_list)



