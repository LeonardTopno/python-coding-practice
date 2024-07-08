'''
Leetcode 287: Find the Duplicate Number. 
'''

def findDuplicateNum(arr):
    
    for num in range(1, len(arr)):      #    num_max = len(arr)-1 = (n+1)-1 = n
        if arr.count(num) > 1:          #    This is more of a Pythonic Soln as we are using the List count func
            return num
    

# Driver code
arr1 = [1,2,3,2]    # Arr of size 4 (3+1), Total distict num 3: 1,2,3, elem - n+1 should not be there in the array
# arr1 = [1,2,4,2,2]
# arr1 = [3,1,3,4,2]
print("Duplicate Number:", findDuplicateNum(arr1))


'''
--- 1. Given Info
i) Array Size: n+1
ii) Elems are from 1 to n(inc) only. 
iii) Given that there is only 1 duplicate number

--- 2. Given Contrait 
i) You must not modify the array. => You can solve this problem by sorting (Swap Sorting), but you should not use it as it is said that array must not be modified
ii) You must use only constant O(1) extra(Aux) space
    => No additinal DS/Space is to be used.
    => Solve in-place but make no-changes to array
iii) Your time complexity should be less than O(n^2)
    => No nested loops.
    => Only Traversals are permitted. 
iv) There is only one duplicate, but it can repeated.

--- 3. Complexity Analysis
i) Time Complexity: O(n); Why? Only Traversal (that too single) and no nested loop.
ii) Aux Space Complexity: O(1); No additonal DS/space was used.

--- 4. Problem Tagging
i)Company: Amazon, VMWare, Riverbed

--- 5. Problem Attempt
i) Date: 24th August 2021 

'''