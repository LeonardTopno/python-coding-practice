# Given an array containing only 0's 1's & 2's, sort it in Linear Time and in Constant Space.
def swap(arr, i, j):
    '''
    temp = Arr[i]
    Arr[i] = Arr[j]
    Arr[j] = temp
    '''

    arr[i], arr[j] = arr[j], arr[i] # Pythonic Way             # Leo's Note: If Swapping is to be written/used more than once in a routine(as in this case), better to use a utility func 'swap' to do the same to avoid in consistencies


# Linear time partition routine to sort a list containing 0, 1, and 2.
# It is similar to 3–way partitioning for the Dutch national flag problem.
def threeWayPartitionSort(arr):                                # dutchNationalFlagAlgo  uses 3 pointers: start,mid,end or low, mid, high
    start = 0
    mid = 0
    end = len(arr)-1
    pivot = 1                                                   # Pivot is constant unlike QuickSort Algo

    while mid <= end:                                           # Can we do this in for loop? NO. better to do using while because `end` pointer value also changes(decreases)
    
        if arr[mid] < pivot:                                    # if the curr elem is < pivot(1) i.e curr elem = 0
            
            swap(arr, start, mid)                               # At the beginning, both of them are at 0, so swapping will be ineffective
            start+=1
            mid+=1
        
        elif arr[mid] > pivot:                                  # if the curr elem is > pivot(1) i.e curr elem = 2
            
            swap(arr, mid, end)
            end-=1

        else:                                                   #if the curr elem is == pivot(1), i.e. curr elem = 1
            mid+=1

    #return  '''No return statement as it is given that it should be  solved in constant space 0(1), i.e. 'IN-PLACE' 


#Driver Code
if __name__ == "__main__":
    arr1 = [0,1,2,2,1,0,0,2,0,1,1,0]
    threeWayPartitionSort(arr1)
    print("Sorted Array", arr1)


'''
-- Approach
i) It is given that the problem needs to be solved in Linear Time i.e. O(n), this means we should avoid nested loops.
ii) Traversing Loop is allowed

iii) Problem needs to solved in constant space i.e. O(1), this means 
        - No additional DS is to be used, the Problem has to be solved in-place, changes(swapping) has be be done in the existing DS (array) only while traversing
        - and no return statement
        

-- Leo's Analysis:
i) The Time Complexity of Above Solution is O(n), where n is the number of elems in the input array. And it has been solved in one pass only.
ii) Space Complexity is O(1)


'''