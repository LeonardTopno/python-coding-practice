def flatten_nested_list(lst):
    flat_list = []
    for elem in lst:
        if isinstance(elem, list):
            flat_list.extend(flatten_nested_list(elem))  # use of recursion (flattening nestest list)
        else:
            flat_list.append(elem)
    return flat_list


# Driver code
if __name__ == "__main__":
    my_list = [[1, 2], [3, 4], [5, 6], [7, 8]]
    print(flatten_nested_list(my_list))  # Output: [1, 2, 3, 4, 5, 6, 7, 8]
    
    """  # 2nd Test
    my_list = [[1, 2], [3, 4], [5, 6], [7, 8], 9]
    print(flatten_nested_list(my_list))  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
    """