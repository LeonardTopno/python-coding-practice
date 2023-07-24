"""
Ques: Bring an item to the beginning of the list, keeping the relative position of rest if the items intact
"""
fruitslist = ['Apple', 'Banana', 'Coconut', 'Durian', 'Elderberry', 'Fig', 'Grape']
print(fruitslist)


def bring_to_the_beginning_of_list():

    item1 = input("Type the item to be brought to the beginning of the list: ")

    # Get to know the index of the item in the list
    index_1 = fruitslist.index(item1)

    # Pop that item out (you will have that item in hand, stored in a variable)
    item_ = fruitslist.pop(index_1)

    # Now insert that item_ in hand which you obtained by pop(index_of_item)
    fruitslist.insert(0, item_)

    return fruitslist


while True:
    print(bring_to_the_beginning_of_list())


