def move_zeros_to_end(given_arr):

    j = 0  # j stores the (next available_ index for storing non-zero numbers

    for elem in given_arr:
        # check if elem is non-zero, move it towards the lower index in the array
        if elem:
            given_arr[j] = elem
            j += 1

    # The above loop will fill the lower index of the array with non-zero element, keeping their relative order intact
    # The loop below will fill the remaining index with zeros
    for k in range(j, len(given_arr)):
        given_arr[k] = 0


#  Driver Code
if __name__ == "__main__":
    arr = [6, 0, 8, 2, 3, 0, 4, 0, 1]
    move_zeros_to_end(arr)
    print(arr)


