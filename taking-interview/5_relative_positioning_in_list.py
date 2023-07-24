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


while True:
    print(bring_to_the_beginning_of_list())


# ------ One liner for the same function ---------

""""
item = "Durian"
fruits_list.insert(0, fruits_list.pop(fruits_list.index(item)))
print(fruits_list)
"""

# Leo's: Takeaways from this problem
"""
1) list.insert() func takes two positional arguments - index and item_to_be_inserted
it does not alter the relative position of the rest of the elements.

2) list.pop() func takes index (not item) as its argument. 
    fruits_list.pop(3) : Correct
    fruits_list.pop("Coconut") : Incorrect
    
3) the output of .pop(index_) is the item at INDEX index_. It is can stored in a variable at used later.

4) use of list.index() func. 
    fruits_list.index("Coconut")
 
"""


