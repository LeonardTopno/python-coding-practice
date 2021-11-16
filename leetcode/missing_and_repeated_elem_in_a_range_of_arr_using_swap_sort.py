'''
Info given: elem are from 1 to n
'''
def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


def swapSortToFindMissingAndDuplicateElem(arr):
    
    for i in range(len(arr)):

        while arr[i] != i+1:
            curr_elem = arr[i]

            if arr[curr_elem-1] != curr_elem:
                swap(arr, i, curr_elem-1)
            else:
                break                               # come out of while loop, And no need to increase the value of i as it is done by for-loop
            
    print("Swap Sorted Array: ", arr)

    # Printing the Missing Elem and duplicate elem
    for i in range(len(arr)):
        if arr[i] != i+1:
            print("Missing Elem:", i+1)
            print("Repeated Elem:", arr[i])
    

#Driver code
if __name__=="__main__":
    arr1 = [4,3,6,5,2,4] # Expandable: [4,3,6,5,2,4,2]
    swapSortToFindMissingAndDuplicateElem(arr1)


'''
---

1) It is given that the elems are from 1 to n; label: 1 to n problem

2) We will make use of the fact that if the array is ideal (no elem is missing and no elem is repeated), 
and if array is sorted, then arr[i] will contain the elem i+1. i.e. arr[0] will contanin 1, arr[1] will contain 2, and so on and so forth

3) After sorting, if arr[i] is not equal to i+1, 
        then duplicate elem is arr[i]        # becoz we couldn't find appropriate place for the elem at arr[i], as its right place (index - arr[i]+1) was already occupied by its first(earlier) occurance
        and missing elem is i+1              # becoz that is what should ideally be at i-th index of arr; elem: arr[i]    

4) Time Complexity: 0(n) + O(n) = 0(2n) = O(n)
   Space Complexity: Constant i.e. O(1), as no extra space/ DS was used.        

5) strategy while traversing the array
   i) curr_elem (= arr[i]) to be kept at correct index in the arr
   ii) if arr[i] contains the correct elem, increment i to next index (or to say move to next elem)


'''