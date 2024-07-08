""""
Merge two sorted array such that the merged array is also sorted
"""


def merge_two_sorted_array(arr1, arr2, m, n):
    """
    2 Pointer Solution
    Time Complexity: o(N), here N = m+n where m and n are size of the array
    Parameters:
        @param arr1:
        @param arr2:
        @param m: size of arr1
        @param n: size of arr2
    Return
        @return: None. Do not return anything, modify arr1 in-place
    """

    # Declare 2 pointers
    pointer1 = m - 1
    pointer2 = n - 1

    # initialize a var to keep a track of index being updated in arr1
    arr1_index_to_update = m + n - 1  # starting from the last index of arr1

    while pointer1 >= 0 and pointer2 >= 0:
        if arr2[pointer2] >= arr1[pointer1]:
            arr1[arr1_index_to_update] = arr2[pointer2]  # arr2 ka koi khayal nahi rakhna hai. Jarurat nahi hai
            pointer2 -= 1
        else:  # elem at the extreme end of arr1 is larger
            arr1[arr1_index_to_update] = arr1[pointer1]  # shayad arr1[left_pointer ka khayal rakhna padega]
            pointer1 -= 1

        arr1_index_to_update -= 1  # One of above condition will be satisfied and then this step must follow.

    return None  # Why because the question demands in-place solution, hence no return (return None)


def merge_two_sorted_arr_pythonic_approach(arr1, arr2, m, n):
    """
    Pythonic approach: using in-built python function list.sort().  (only 2 line of code)
    Time Complexity: N(logN), here N=m+n

    @param arr1:
    @param arr2:
    @param m: size of arr1
    @param n: size of arr2
    @return:
    """
    arr1[m:] = arr2  # Leo: Py Pro Tip - Everything in arr1 till index m-1 (not size m; moreover for list of size m, index starts from 0 and ends at m-1) then from index m onwards will be the elements of arr2
    # Leo: This can be added in python one liner. The is like append funtion of List. Ignore whatever is there (or not there) from index m onwards and append the all the elems of arr2, irrespective of size of arr1
    print(arr1)
    arr1.sort()  # Built-in function of LIST which sorts the list itself (in-place sorting)

    # Leo: revise List.sort() vs sorted(iterable)



if __name__ == "__main__":
    arr1 = [1, 2, 7, 0, 0, 0]
    arr2 = [2, 5, 6]

    m = 3
    n = 3
    # merge_two_sorted_array(arr1, arr2, m, n)
    print("arr1: ", arr1)
    print("arr2: ", arr2)
    merge_two_sorted_arr_pythonic_approach(arr1, arr2, m, n)
    print(arr1)


"""
Why should I begin from the end of the of the arrays (arr1 actually)?
It is given that both are arrays are sorted, which implies that array1 is also sorted and there are just enough empty spaces(actually filled with zeros) to 
accommodate all the elements of the array2.

It will be easier to fill in from the end of array1, rather than beginning of array1.

2 Pointer method | Without using extra space 
--------
It is given that the 2 arrays are sorted (in non-decreasing order),
which means the smaller elems would be on the left (towards the beginning of the array)
and larger elems would be on the right side of the array (towards the end).

The main logic behind is to start filling m+n-1 index of arr1 (i.e. last index of arr1).
We are guaranteed that there is enough space in arr1 for every elem in the arr2 to inserted.
And we want to ensure that they are sorted (in non-decreasing order) even after being merged.

The main logic behind this approach is to start placing the largest elem (among the two arrays) at the back of
arr1 (starting from the last index of arr1), then keep shifting towards left and keep placing the next largest elem (among the two arrays) in that index
 

Since the two given arrays are sorted, the largest elem for each array should be at the extreme right.

We will compare the elements present at the end of each array and whichever is larger will be 
kept arr1 at the index we are updating (starting from last index of arr1).

Then we decrement the respective index(pointer), and the index we are updating also needs to be decremented.

This solution is using 2 pointer method, with Time Complexity: O(N), here N = m+n
Where m and n are the sizes of arr1 and arr2. 


"""
