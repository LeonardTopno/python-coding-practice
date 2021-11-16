'''
In-place Merge Two Sorted array: A naive aproach
'''

def mergeTwoSortedArrays(arr1, m, arr2, n):

    i, j, updateIndex = 0,0,0  # i -> pointer for arr1 (meant for aa1 but it will be used for temp_arr)
                               # j -> pointer for arr2
                               # we will be traversing from left to right --> smaller elem to larger elem

    temp_arr = arr1.copy()     # not temp_arr = arr1 becoz we don't want to do by reference otherwise it will update if arr1 updates                             
                               
                               # Leo's note: from hereonwards temp_arr to be treated as arr1( we know it is a copy of arr1), 
                               # and sorted (&merged) elem to be stored in arr1
                               # If we don't follow this, then at the end, we will have to copy back temp_arr to arr1, becoz the final result should be in arr1
    
    # Apprach: traversing from left to right (beginning to end), and keeping the smaller no towards the left.
    # Note: traversing from left to right (beginning to end), hence increment of pointers
    while i<m and j<n:
        if temp_arr[i] < arr2[j]: #i and j are 0 initially #imagine temp_arr as arr1
            arr1[updateIndex] = temp_arr[i] #placing the smaller, starting from left(beginning)
            
            i+=1
        
        else:                       # elif temp_arr[i] > = arr[j]
            arr1[updateIndex] = arr2[j]
            
            j+=1
        
        # irrespective of whatever pointer gets incremented, we need to increment updateIndex
        updateIndex+=1

    # So now whatever is left (either arr1(i.e. temp_arr) or aar2), the elems needs to be added to the rest of arr1
    while i<m:
        arr1[updateIndex] = temp_arr[i]
        i+=1
        updateIndex+=1      # i, updateIndex = i+1, updateIndex+1
    
    while j<n:
        arr1[updateIndex] = arr2[j]
        j+=1
        updateIndex+=1


    print(arr1)

# Driver Code
if __name__ == "__main__":
    arr1 = [1,2,3,0,0,0]
    m=3
    arr2 = [2,5,6]
    n=3

    '''
    arr1 = [1]
    m=1
    arr2 = []
    n=0

    arr1 = [0]
    m=0
    arr2 = [1]
    n=1
    '''

    mergeTwoSortedArrays(arr1, m, arr2, n)




'''
Given: 2 arrays with their sizes
arr1 -> m
arr2 -> n

Maintain the Sorting after Merging

Requirement: Do this in O(1) Space Complexity
             i.e. Do the conversion "IN-PLACE" and without using any other DS
             No return statment as the solution has to be IN-PLACE

We are using INSERTION SORT TECHNIQUE       

Is 0  not an interger?
integer begins from 1. This is by looking at the solution. Need to be established.
Leo: 0 is an integer.

Leo's note:
In/For this approach:
    1. we are traversing from left to right (smallest elem to largest elem), hence the 2 - pointers (i,j) are incremented and not decremented
    2. Leo: overserve the initialing and while-loop conditioning if one has to traverse form left to right
            i,j = 0,0
            while i<m and j<n:
                i+=1
                j+=1
    3. Leo: Observe the initializing and while-loop conditioning (two pointer approach) if one has to traverse from right to left (larger to smaller), pointers would be decremented and not incremented
            i,j = m,n
            while i>0 and j>0:
                i-=1
                j-=1
    4. Here we are creating an temp_arr and copying elems of aar1
       Other possibility is we could have created temp_arr and kept it empty initially and then do merging and sorting in temp_arr, but later we will have to copy it to arr1 as result is expected in arr1
       In any case, copying is involved, whether you copy in the begining or at end

Analysis:
Here the Time complexity is:
                             0(m+n); basicsally O(no. of elements being dealt with), in general O(N)
Space Complexity: 
                            0(m+n); basically O(no. of elems we are storing) in temp_arr, in general O(N)

But the question says(hints): Do this in O(1) Space Complexity .i.e. constant space
For this refer Pythonic Solution - TC: O(nlogn); SC: O(1)

'''