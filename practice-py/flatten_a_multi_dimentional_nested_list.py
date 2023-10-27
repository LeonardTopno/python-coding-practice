"""
Given a multi-dimensional list, flatten the list recursively
"""


def flatten_nested_list(lst):
    flat_list = []
    for elem in lst:
        if isinstance(elem, list):  # checking if the 'elem' is a list itself
            flat_list.extend(flatten_nested_list(elem))
        else:
            flat_list.append(elem)
    return flat_list


# Driver Code
if __name__ == "__main__":
    my_list = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]
    print(flatten_nested_list(my_list))

    """ 2nd Test
    my_list = [[10, 20, [22, 25], 30], [40, 50, [55, [56, 57, [59]]], 60], [70, 80, 90]]
    print(flatten_nested_list(my_list))
    """

# --------------------------------------------------------------------------------------

"""
Takeaways:
What does this question test:
1) Check if one knows how and when a recursion is used
2) To check if an object is an instance of a Class (Remember that in Python everything is a calls)
    i) Use of isinstance() to check if an object is an instance of a CLass(here list)
    ii) isinstance(elem, list)
3) mylist.append(elem)
4) mylist.extend(another_list)

Difficulty Level:
1) 4 Star
2) Multi Concept
"""
