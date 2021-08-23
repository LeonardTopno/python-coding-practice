def findMissingAndRepeatedElem(arr):
    left_end = right_end = arr[0]
    
    repeated_elem = None
    missing_elem = None

    while left_end >= 1:
        
        if left_end not in arr:
            missing_elem = left_end
        
        elif arr.count(left_end) > 1:
            repeated_elem = left_end

        left_end-=1
    
    while right_end <= len(arr):            # len(arr) = n 
        
        if right_end not in arr:
            missing_elem = right_end

        elif arr.count(right_end) > 1:
            repeated_elem = right_end
                    
        right_end+=1

    print("Repeated Elem:", repeated_elem)   # Printing at the end for we have only 1 repeated and missing elem
    print("Missing Elem:", missing_elem)

# Driver Code
if __name__ == "__main__":
    arr1 = [4,3,6,5,2,4]
    findMissingAndRepeatedElem(arr1) 

'''
# else is not compulsory after elif:

Time Complexity of this solution is O(n) according to Leo; we are not visiting the elem again, once we have visited it
Space Complexity of this solution is O(1), i.e. contant time as no extra space/DS was used

label: 1 to N problem
'''