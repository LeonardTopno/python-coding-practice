'''
In-place Merge Two Sorted array
'''

def mergeTwoSortedArrays(arr1, m, arr2, n):

    del arr1[m:]        # Delete elems from arr1 from index-m onwards (Leo learnt new thing here)
    arr1.extend(arr2)   # .extend() is a LIST func which extend arr1 to arr2 
    arr1.sort()         # .sort() is a LIST function
    print(arr1)
    
    # SORTING it would take O(nlogn) time.
    # Technically this shouls be slower, but if you look into actual details, it is faster.
    # That is something to do with how the built-in function `.sort()` sorts


# Driver Code
if __name__ == "__main__":
    arr1 = [1,2,3,0,0,0]
    m=3
    arr2 = [2,5,6]
    n=3

    #arr1 = [1]
    #m=1
    #arr2 = []
    #n=0

    #arr1 = [0]
    #m=0
    #arr2 = [1]
    #n=1

    mergeTwoSortedArrays(arr1, m, arr2, n)




'''
Given: 2 arrays with their sizes
arr1 -> m
arr2 -> n

Maintain the Sorting after Merging

Requirement: Do this in O(1) Space Complexity
             i.e. Do the conversion "IN-PLACE" and without using any other DS
             No return statment as the solution has to be IN-PLACE
     
0 is not an interger.
integer begins from 1. This is by looking at the solution. Establish this.
Leo: 0 is an integer

Leo's note:
In/For this approach:
    1) Here we are able to solve it in Contant Space; Space Compexity: O(1)
    2) But technically Time Complexity increases to 0(N log N); actually (n+m)log(n+m); Any Sorting Algo in worst case will take O(NlogN)
    3) Can we reduce the Time Complexity further(keeping the Space Complexity same), yes using 2-Pointer Approach.


'''