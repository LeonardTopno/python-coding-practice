# We are attempting to solve this problem in 1 scan using the Modified version of Quick Sort Algo

"""
The logic is to use 0 as a PIVOT elem and make one pass of the array.
The PARTITIONING LOGIC reads all the elem_s and swaps every non-zero (non-pivot) elem with the first occurrence of pivot
, first time and thereafter whenever non-pivot(non-zero) elem is encountered while scanning
"""


def move_zeros_to_end(arr):
    j = 0  # 'j' is supposedly meant to store the index of pivot(zero) (first occurrence of)

    for k in range(len(arr)):
        if arr[k]:  # checking if the elem is non-zero, if True, Swap
            arr[k], arr[j] = arr[j], arr[k]
            j += 1


# Driver Code:
if __name__ == "__main__":
    arr = [6, 0, 8, 2, 3, 0, 4, 0, 1]
    move_zeros_to_end(arr)
    print(arr)


"""
Point to note: 
1. 'arr' is not a reserved keyword in Python3 
"""
