'''
1. Given an integer array, move all zeros present in it to the end.
2. The solution should maintain the relative order in the array
3. And should not use constant space [Means the solution should be in-place]
'''

'''Using Single Traversal'''
'''Do not return anything, modify arr in-place instead'''
def moveZerosToEnd(arr):                         
    
    j = 0 # Records the position of "0"

    for i in range(len(arr)):   # i will also start from zero and i's max value will be (len(arr)-1)
        if arr[i]:              # if elem is non-zero
            arr[i], arr[j] = arr[j], arr[i]  # In the first iter, both i and j will have same value 0, thereafter j is incremented everytime a a non-zero elem is encountered
            j+=1


# Driver Code
if __name__=='__main__':
    A = [6,0,8,2,3,0,4,0,1]
    moveZerosToEnd(A)
    print(A)

