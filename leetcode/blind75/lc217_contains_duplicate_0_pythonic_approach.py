"""
Approach: Two Pythonic Approach. Prefer the First One (set one).

Time Complexity: 
    Approach 1: O(n) Converting to set and comparing its len with len of original arr
    Approach 2: O(n) x O(n) = O(n^2)
"""


from typing import List

def has_duplicate(arr:List[int]) -> bool: 
    if len(set(arr)) == len(arr):
        return False
    
    return True


def has_duplicate_using_my_list_count(arr: List[int]) -> bool:

    for elem in arr:
        if arr.count(elem)>1:   #Leo Note: Time Complexity of my_list.count(elem) is O(n) as it involves the scanning of the entire list to count the occurences of 'elem'
            return True
        
        return False
    

# Driver code:
if __name__ == "__main__":
    #arr = [1,2,3,1]
    # arr = [1,2,3,4]
    arr = [1,1,1,3,3,4,3,2,4,2]
    print(has_duplicate(arr))
    print(has_duplicate_using_my_list_count(arr))

""""
1st Approach:
Time Complexity: O(n) where n is the length of the array
    Reason: 
    The key operations to cosider for time complaxities are:
        1. Creating a set from the list - O(n)
           This involves iterating over the list (O(n)) and inseting adding each elem into  a set.
           Adding into a set has an avg Time Complexity of O(1)
           So, creating a set from a list of len n has a Time Complexity of O(n) + O (1) = O(n)

        2. Comapring the lengths: The lengths of the list abd the set can be compared in constant time, O(1).    
    
        Overall, the Time Complexity is dominated by creation of the set:
        O(n)

        i.e. O(n) + O(1) = O(n) 
    
Space Complexity: O(n)
    Reason:  An additonal Data Structure has been introduced  i.e. set, where in the worst case (where all the elements in the list are unique), 
                the set will store n elements.

===================

2nd Approach:
Time Complexity: O(n^2) where n is the length of the array
    Reason: 
    The key operations to cosider for time complaxities are:
        1. Looping through the list - O(n)
           
        2. Counting Occurances: O(n) 
            The `my_list.count(elem)` method is called WITHIN THE LOOP.
            The my_list.count() method itself iterates through the entire list to count occurances of `elem`
            and this takes O(n) time. 

        Overall, the Time Complexity is domianted by creation of the set:
        O(n)

        i.e. O(n) x O(n) = O(n^2)   
    
Space Complexity: O(1)
    Reason:  No additonal Data Structure has been introduced.  so the Space Complxity of the algorithm is O(1) 

====================
Note: 

Intuition: 

Algorithm:

SOl URL: 
        
""" 