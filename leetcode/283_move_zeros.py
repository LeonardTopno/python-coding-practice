def move_zeros_to_end(arr_):

    j = 0  # j stores the (next available_ index for storing non-zero numbers

    for elem in arr_:
        # check if elem is non-zero, move it towards the lower index in the array
        if elem:
            arr_[j] = elem
            j += 1

    # The above loop will fill the lower index of the array with non-zero element, keeping their relative order intact
    # The loop below will fill the remaining index with zeros
    for k in range(j, len(arr_)):
        arr_[k] = 0


#  Driver Code
if __name__ == "__main__":
    arr_ = [6, 0, 8, 2, 3, 0, 4, 0, 1]
    move_zeros_to_end(arr_)
    print(arr_)


