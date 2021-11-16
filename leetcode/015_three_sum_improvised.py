'''
Given an UNSORTED int array, find a triplet with a given sum in it.
'''

'''
The problem is a standard variation of 3SUM problem, where instead of looking for numbers whose sum is 0,
We look for numbers whose sum is any constant C.
''' 

# Naive RECURSIVE FUNCTION to check if triplet exists in a list with given target

def getTripletSum(arr, target):

    
    look_up = {}
    '''
    for index, num in enumerate(arr):
        look_up[num]=index # repeated nums would be lost, the key(num) will be overridden with new value(index)
    '''
    #look_up = {index:num for index, num in enumerate(arr)}

    print("look_up: ", look_up)

    triplets = []

    #arr.sort()
    
    for i in range(len(arr)-1): # i_max = n-2, where n = len(arr)

        # start from i'th elem until last       # This is also ensuring i!=j
        for j in range(i+1, len(arr)): # i_max = n-1, where n = len(arr)

            # remianing sum 
            elem3 = target - (arr[i]+arr[j])        # elem1 = arr[i]    # elem2 = arr[j]

            # if remaining sum is found, we have a triplet
            if elem3 in look_up:

                if look_up[elem3] != i and look_up[elem3] !=j:  # ensuring elem3_index != i and elem3_index != j, there by ensuring all 3 indices are distinct (i != j != k)
                    triplets.append([arr[i], arr[j], elem3]) 
            
            else:
                look_up[arr[i]] = i     # look_up[elem1] = i
                look_up[arr[j]] = j     # look_up[elem2] = j
                print(look_up)
    
    return triplets

# Driver Code
if __name__ == "__main__":
    arr =  [2,7,4,0,9,5,1,3] #[-1,0,1,2,-1,-4]
    target = 6 #0   

    print(getTripletSum(arr, target))

    '''
    if getTripletSum(arr, target):
        print("Triplet exists")
    else:
        print("Triplet does not exists")
    '''



# Tuple has no .sort() func, only List has .sort()