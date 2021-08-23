'''
1. Given an integer array, move all zeros present in it to the end.
2. The solution should maintain the relative order in the array
3. And should not use constant space
'''

'''Using Single Traversal - One Scan of the array'''
'''Do not return anything, modify arr in-place instead'''
def swap(A, i, j):
    '''
    temp = A[i]
    A[i] = A[j]
    A[j] = temp
    '''
    A[i], A[j] = A[j], A[i] # Pythonic Way

# Func to move all zeros present in the list to the end

def partition(arr):

    # Leo: 0 is the pivot here, we could have used pivot = 0, and arr[i]>pivot
    j = 0  # j is pivotIndex

    # each time we encounter a non-zero elem, that non-zero element is placed before Pivot (zero here); And then anIndex is incremented

    for i in range(len(arr)):
        
        if arr[i]:                #if A[i] is non-zero, i.e. element at current position is non-zeo,  Leo's note: We are never changing/updating the Pivot as we do in QuickSort
            swap(arr, i, j)       # In First time, i=0 and j=0
            j+=1                # j is incremented before i increments becoz of for loop
    
    
    return arr

# Driver Code
if __name__=='__main__':
    A = [6,0,8,2,3,0,4,0,1]

    x = partition(A)
    print (x)

