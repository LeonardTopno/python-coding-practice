def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]
    

def swapSortToFindMissingAndRepeatedElem(arr):
    # SWAP SORT ROUTINE

    for i in range(len(arr)):   # 0 to n-1
        
        while arr[i] != i+1:    # Condition of Sorted (1-n) array: If array is sorted, then at i-th index, the elem would be i+1, becoz it is given that elem are from 1 to n (1 to n Problem) 
            curr_elem = arr[i]  # Ensuring that each index should have correct elem, # So basically this is a way to sort an array containing elem 1 to n

            if arr[curr_elem-1] != curr_elem:  # curr_elem is already at arr[i], so if curr_elem is not the repeated elem then it will definitely not be at index (curr_elem-1), then it will enter the loop, hence Swap
                swap(arr, i, curr_elem-1)
            
            else:       # this implies curr_elem is also at index curr_elem-1 which means it is at two places (repeated elem) #Do nothing
                break   # just break and come out of while loop, no need to increment the value of i as it is being done by outer for-loop 
    
    
    '''
    So basically we were Sorting the array using SWAP SORT as we know the elem are from 1 to n
    '''
    print("Swap Sorted Array:", arr)

    # ITERATE THROUGH THE SORTED 1-n ARRAY TO PRINT THE DUPLICATE AND MISSING
    for i in range(len(arr)):   #i_max = n-1
        if arr[i]!=i+1:
            print("Missing Elem", i+1)
            print("Repeated Elem", arr[i])


# Driver code
if __name__ == "__main__":
    arr = [4,3,6,5,2,4]
    swapSortToFindMissingAndRepeatedElem(arr) 


'''
-- Approach
i) It is given that the problem needs to be solved in Linear Time i.e. O(n), this means we should avoid nested loops.
ii) Traversing Loop is allowed

iii) Problem needs to solved in constant space i.e. O(1), this means 
        - No additional DS is to be used, the Problem has to be solved in-place, changes(swapping) has be be done in the existing DS (array) only while traversing
        - and no return statement

iv) Condition of SORTED 1-n ARRAY; i-th index with contain the elem i+1; becoz it is given that elem are from 1 to n (1 to n Problem)
v) We are basically SORTING the 1-n array
        

-- Leo's Analysis:
i) The Time Complexity of Above Solution is O(n), where n is the number of elems in the input array. And it has been solved in 2 passes only.
    O(n) + O(n) = O(2n) which is effectively O(n)
ii) Space Complexity is O(1)
    In-place operation (the array got sorted though)
    No Extra space / DS was used
    No return statement

'''
