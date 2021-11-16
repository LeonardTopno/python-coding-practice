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
    triplets = []
    n=len(arr)



    # check if triplet is formed by `arr[i]` and a pair from sublist arr(i+1,...,n)

    for i in range(n): 
        
        """ This is when target is 0 -------------------
        # since the arr is sorted, if arr[i] > 0, then arr[j] with j>i are positives as well.
        # And we cannot have 3 positives numbers sum upto 0. So return immediately
        '''
        if arr[i] > 0:
            break           # break out of for loop and return the result
        '''
        ------------------- """
        # Avoid Duplicates
        # The arr[i] == arr[i-1] condition helps us to avoid duplicates.
        # If in Sorted Array, the consecutive elem are same, then the array contains duplicates. We can avoid this iteration where arr[i]==arr[i-1], and thus avoid duplicate

        
        # Avoid negative index
        # The i > 0 condition is to avoid negative index
        # when i=0 and arr[i-1] is actually arr[-1], - A neg index, and you don't want to skip this iteration
        
        #Skip All duplicates
        if i > 0  and arr[i] == arr[i-1]: 
           continue                       # The continue statement in Python returns the control to the beginning of the while loop

        #remaining sum
        k = target - arr[i]

        # classic two pointer solution 
        left = i+1 
        right = n-1
        

        while left < right:

            # increment `left` index if the total is less than the remainging sum
            if arr[left] + arr[right] < k:
                left += 1

                while left < right and arr[left] == arr[left+1]:
                    left+=1

            # decrement `right` index if the total is more than remaining sum
            elif arr[left] + arr[right] > k:
                right -= 1
                
                while left < right and arr[right] == arr[right-1]:
                    right-=1

            # triplet is found i.e arr[left] + arr[right] == k:
            else:
                print(arr[i], arr[left], arr[right])
                triplets.append((arr[i], arr[left], arr[right]))
            
                # increment `left` index and decrement `right`
                left += 1
                right -= 1


                # We need to skip elem that are identical to our current solution,
                # Otherwise we will have duplicated triplets
                while left < right and arr[left] == arr[left+1]:
                    left+=1

                while left < right and arr[right] == arr[right-1]:
                    right-=1
                
                

    return triplets

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
# This is the most time optimized and memory optimized solution

# Avoiding duplicates actually makes this algorithm 3 times faster than the algorithm wherein I first let the duplicates in and later remove them from the list.
'''