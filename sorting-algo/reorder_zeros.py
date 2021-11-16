'''
1. Given an integer array, move all zeros present in it to the end.
2. The solution should maintain the relative order in the array
3. And should not use constant space
'''

'''Do not return anything, modify arr in-place instead'''
#Function to move all zeros present in the list to the end

def reorder(arr):

    avIndex = 0 # Introduced a var 'avIndex' which stores the index of the next available position; initialized it to zero to start with 

    for elem in arr:    # Traversing the array

        if elem:        # In the current elem is non-zero, put that element at the next available position
            arr[avIndex] = elem
            avIndex+=1

    '''After all the non-zero elements are processed, fill (populate) the remaining indices by 0'''
    for i in range(avIndex, len(arr)): #from Next Available index to len(arr) - 1
        arr[i] = 0

    return arr
# Driver Code
if __name__=='__main__':
    A = [6,0,8,2,3,0,4,0,1]

    reorder(A)
    print(A)
