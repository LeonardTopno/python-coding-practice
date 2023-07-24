"""
Ques: Given a list, bring an item to the beginning of the list,
keeping the relative positions of the rest of the items intact
"""
fruits_list = ['Apple', 'Banana', 'Coconut', 'Durian', 'Elderberry', 'Fig', 'Grape']
print(f"Original fruits list: {fruits_list}")


def bring_to_the_beginning_of_list():

    item = input("Type the item to be brought to the beginning of the list: ")

    # i) Get to know the index of the item to be brought to the first
    index_ = fruits_list.index(item)

    # ii) Pop that item out (you will have that item in hand, stored in a variable)
    item_ = fruits_list.pop(index_)  # pop takes index as argument and returns the item pop-ed out

    # iii) Now insert that item_ in hand which you obtained by pop(index_of_item)
    fruits_list.insert(0, item_)

    return fruits_list


while True:
    print("\n", bring_to_the_beginning_of_list(), "\n")


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
    Simultaneously list.pop(index_) has altered the list, as in it has removed the item at INDEX index_.
    So list now contains one element less.

4) use of list.index() func. 
    fruits_list.index("Coconut")
5) Additional info on list and tuple: tuple has no .sort() inbuilt func, only list has.
 
"""


