'''
In-place Merge Two Sorted array
'''

def mergeTwoSortedArrays(arr1, m, arr2, n): # No return as it in an inplace-solution

    # 1. get the last index of arr1
    updateIndex = m + n - 1    # start from last index in arr1 
    
    # 2. start merging them in reverse order
    # Both the arrays are sorted. So the largest of both the arrays would be towards the last of each arr

    while m>0 and n>0:                  # We will keep going left, while there are elems left in both the arrays
        if arr1[m-1] > arr2[n-1]:
            arr1[updateIndex] = arr1[m-1]
            m -= 1
        else:                   #arr2[n] >= arr1[m] # else will cover equal to as well along with less than
            arr1[updateIndex] = arr2[n-1]
            n -= 1
        
        updateIndex -= 1 #regardless of which index we decrement, we will be decrementing the updateIndex 
    
    # 3. Edge Case we need to take care. Another Important Case to handle: Fill arr1 with leftover elems in arr2 (leftovers are also sorted)   
    # Smallest number is already in the postion we wanted i.e. arr1[0]. What if the overall smallest numners are still in arr2?
    while n > 0:
        arr1[updateIndex] = arr2[n-1]
        updateIndex-=1                 #updateIndex, n = updateIndex-1, n-1
        n=-1

    print(arr1)
    print(arr2)


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
Leo's note:
In/For this approach:
    1. we are traversing from right to left (largest elem to smallest elem), hence the two pointers (m,n) are decremented and not incremented
    2. Leo: In the naive approach, when we had to traverse form left to right, we overserved the initialing and while-loop conditioning 
            i,j = 0,0
            while i<m and j<n:
                i+=1
                j+=1
    3. Leo: Observe the initializing and while-loop conditioning if one has to traverse from right to left (larger to smaller), pointers would be decremented and not incremented
            i,j = m,n
            while i>0 and j>0:
                i-=1
                j-=1
            
            -- or directly use m and n
            
            while m>0 and n>0:
                m-=1
                n-=1
Analysis:
Here the Time complexity is:
                             0(m+n); basicsally O(no. of elements being dealt with), in general O(N)
Space Complexity: 
                            0(1); No extra space used

This is the best appraoch
Thought Process:
1) It is given that the given 2 arrays are SORTED
        which means the smaller elems would be on left (towards the start) of the array
                    the larger elems would be on the right (towards the end) of the array

2) We have a kind of empty space(though filled with 0) towards the end of arr1.
    The question to ask is why should I begin from the begin from the left(start) of array
    - It is given that arrays are sorted, and there is empty space in arr1 towards the end, and it is guaranted that there is enough space to store all elem of arr2
    - Wouldn't it be easier to begin filling from the end of arr1
    [Include the two array illustration in copy]

2) The main logic behind this appraoch is to start filling the largest(er) elems (among both arrays) to the back od the arr1

3) We will compare the elems at the end of each arrays and whichever is larger will be kept at the index we are updating.
4) Then we will decrement the respective pointer, and also the index which wr are updating needs to be decremented




'''