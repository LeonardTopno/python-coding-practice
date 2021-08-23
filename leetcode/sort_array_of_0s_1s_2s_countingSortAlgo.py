def sortArrUsingElemCount(arr):
    count_0 = arr.count(0)
    count_1 = arr.count(1)
    # count_2 = arr.count(2)            # Optional because rest will be 2 Only and that will form the else part

    
    for i in range(count_0):
        arr[i]=0

    for i in range(count_0, len(arr)):
        if i < count_0 + count_1:
            arr[i]=1

        else:
            arr[i]=2
    
    '''
    # Same thing in Single Pass
    for i in range(len(arr)):
        if i < count_0:
            arr[i]=0
        elif i >=count_0 and i < (count_0 + count_1):
            arr[i]=1
        else:
            arr[i]=2 
    '''

   
# Driver code
if __name__ == "__main__":
    arr1 = [0,1,2,2,1,0,0,2,0,1,1,0]
    sortArrUsingElemCount(arr1)
    print(arr1)

'''
--- Leo's Analysis:
1) Time Complexity of this sol is O(n), and 2nd option is single pass
2) Space Cpmnplexity is this sol in o(1), i.e. Contant Space
'''