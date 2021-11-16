def productOfArrExceptSelf(arr):

    product = [1]*len(arr)

    '''
    idea is to create an arr of cumulative array from start to end (left to right), and then right to left 
    '''
    prod_left = 1 # Setting product of all elems to the left of extreme start elem to 1

    for i in range(len(arr)):
        product[i]*=prod_left
        prod_left*=arr[i]

    prod_right = 1 # Setting product of all elems to the right of end elem to 1. Why (Anything multiplied by 1 = same number; If addition, set it to 0)
    
    for i in range(len(arr)-1, -1, -1):
        product[i]*=prod_right
        prod_right*=arr[i]

    return product

def productOfArrExceptSelf1(arr):
    product = [1]

    return product

# Driver Code
if __name__=="__main__":
    arr_ = [1,2,3,4]
    res = productOfArrExceptSelf(arr_)
    print(res)

'''
--- Approach: 

res_arr_left[i] should contain the product to all the elements to the left.
res_arr_right[i] should contain the product of all elements to the right. 
res_arr[i] = res_arr_left[i] * res_arr_right[i]



--- Leo's Ananlysis

1. We are asked to do this in O(n) => which means we have to traverse the array once (single pass) or more than once but NOT NESTED. 
Nesting will make it O(n^2) or O(n^3) based on the num of times it has been nested. 

2. If we are asked to do it in constant space  which is O(1), which means we are not to use any additional array.
It is given that resultant product arr will not be considered while evaluating space complexity.
Solution should be IN-PLACE arroach. 

3. It is given that 32-bit, the int numbers will be able to accomodate int data type. 

4. It is given that division operatir should not be used. Easiest approach

'''

    


    