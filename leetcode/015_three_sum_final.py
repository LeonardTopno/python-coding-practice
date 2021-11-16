'''
Given an UNSORTED int array, find a triplet with a given sum in it.
'''

'''
The problem is a standard variation of 3SUM problem, where instead of looking for numbers whose sum is 0,
We look for numbers whose sum is any constant C.
''' 

# Function to print all distinct triplets in the arr with given target

def getTripletSum(arr, target):

    arr.sort()
    
    n=len(arr)

    triplets = set()

    # check if triplet is formed by `arr[i]` and a pair from sublist arr(i+1,...,n)

    for i in range(n-2): #Why did we leave 2: Figure out Leo

        #remaining sum
        k = target - arr[i]


        # classic two pointer solution 
        # maintain two indices pointing to endpoints of the sublist arr[i+1,...,n]
        left = i+1 
        right = n-1
        

        # loop if `left` < `right`
        while left < right:

            # increment `left` index if the total is less than the remainging sum
            if arr[left] + arr[right] < k:
                 left += 1

            # decrement `right` index if the total is more than remaining sum
            elif arr[left] + arr[right] > k:
                right -= 1

            # triplet is found
            else:
                print(arr[i], arr[left], arr[right])
                triplets.add((arr[i], arr[left], arr[right])) # will not add if it is same
            
                # increment `left` index and decrement `right`
                left += 1
                right -= 1

    return list(triplets)  # Another way to do is use list instead of set, duplicates triplets will be added, then typecast to set to remove duplicates and then typecast back to list 

# Driver Code
if __name__ == "__main__":
    arr =   [2,7,4,0,9,5,1,3] #[-1,0,1,2,-1,-4]
    target = 6 #0

    print(getTripletSum(arr, target))

'''
 --- Notes:
# Tuple has no .sort() func, only List has .sort()
# List has append(), set has add(), set has update() if adding elements from List or tuple or sets or frozen-set
# You can add tuple in a set, but I think you cannot add List in a set - throwing error. Test this later

Time Complexity is O(n^2)
Space Complexity:  Doesn't require any extra space.

# 2-Pointer Problem
'''