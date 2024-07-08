"""
Approach 3: Using Hash set
Mantra: Set (Hash set) cannot have duplicate elements.
        The approach is to use a Hash Set (Introducing a DS) to store the encountered elements.
        While iterating through the elements in the array, check if it is already present in the set. 
        If yes, we found a duplicate, hence return True
        If no, then add the elem to the set.  
        Leo's Note: In List we have list.append(elem) and in set we have set.add(elem)  

Time Complexity: O(n) as we are iterating the array once.
Space Complexity: O(n) as we are introducing a Data Structure - set which can have a max of n elems  
"""

from typing import List
 
def has_duplicates(arr:List[int])->bool:
    seen_set = set()
    
    for elem in arr:
        if elem in seen_set:
            return True
        else:  # if elem is not in seen_set, then add it
            seen_set.add(elem)
    
    return False


'''
using continue to save a couple of milisec
'''
def has_duplicates_improvised(arr: List[int]) -> bool: 
    seen_set = set()

    for elem in arr:
        if elem not in seen_set:
            seen_set.add(elem)
            continue    # used 'continue' to save a couple of milisec
        
        else:  # elem is in set seen_set
            return True

    return False 


# Drive code
if __name__ == "__main__":
    #arr = [1,2,3,1]
    #arr = [1,2,3,4]
    arr = [1,1,1,3,3,4,3,2,4,2]
    print(has_duplicates(arr))
    print(has_duplicates_improvised(arr))


""""
Time Complexity: O(n) where n is the length of the array
    Reason: Iterating through the array takes O(n)
            The elems are stored in a HashSet (or Set, in Python) which allows O(1) lookups.
            So O(n) + O(1) = (n)

Space Complexity: O(n)
    Reason: An additional Data Structure has been introduced - Set, which can at max contain n elements (if no duplucates found)


Note(If Any): 

Intuition: Hash set or (Pythonic set) can not contain duplicates. 
            So use a set to store encountered elements. 
            While iterating through the arr, check if the elem is alreay in the set.
            If yes: We have found a duplicate, hence return True.
            If no: Add the elem to the set. syntax: set.add(elem)
            
            Mantra:  Hash Set (Pythonic set) can not have a duplicate element. 
                        Also we the keys of the hash map are unique, hence the we can use that also. (next approach 4. - Over Engineered)

Algorithm: 

SOl URL: https://leetcode.com/problems/contains-duplicate/solutions/3672475/4-method-s-c-java-python-beginner-friendly/
        
""" 