"""
Approach 4: Using Hash Map
Mantra: The keys of the hash Map Set will necessarly have to be unique (no duplicates).

        The approach is similar to Hash Set (Introducing a DS) approach but uses keys of the hash map to store the encountered elements.

        While iterating through the elements in the array, check if it is already present in the hash map (Pythonic dictionary). 
        If yes, we found a duplicate, hence return True
        If no, then add the elem to dictionary. Use my_dict.get(key, default_value) function.
        
        Leo's Opinion: In my opinion, this approach is over engineered. And should be avoided. It just gives extra information which is not asked in the question.
        The extra information is: It keeps a track of the count of occurances of each elem.

Time Complexity: O(n) as we are iterating the array once and lookup in the dictionary takes O(1). Hence O(n) + O(1) = O(n)
Space Complexity: O(n) as we are introducing a Data Structure - set which can have a max of n elems  
"""



from typing import List


def has_duplicate(arr: List[int]) -> bool:
    
    lookup = {}

    for elem in arr:
        if elem in lookup:   # The solution had:   if elem in lookup and lookup[elem] >=1:   I guess the statement after and is not reqd
            return True
        else:  # elem is not in the lookup
            lookup[elem] = lookup.get(elem, 0) + 1   # here we are learning the use of  my_dict.get(key, default_value)
          
    return False


# Driver Code
if __name__ == "__main__":
    #arr = [1,2,3,1]
    #arr = [1,2,3,4]
    arr = [1,1,1,3,3,4,3,2,4,2]
    print(has_duplicate(arr))



""""
Time Complexity: O(n) where n is the length of the array
    Reason: Iterating through the array takes O(n)
            The elems are stored in a hash map (or dictionary, in Python) which allows O(1) lookups.
            So O(n) + O(1) = (n)

Space Complexity: O(n)
    Reason: An additional Data Structure has been introduced - dictionary, which can at max contain n elements (if no duplucates found)


Note(If Any): 

Intuition: Dictionary can not contain duplicate keys. 
            So use a dictionary (hash-map) to store encountered elements. 
            While iterating through the arr, check if the elem is alreay in the dict.
            If yes: We have found a duplicate, hence return True.
            If no: Add the elem to the dictionary. syntax: my_dict.get(key, default_key)
            
            Mantra:  In a Hash Map (Pythonic Dictionary), the keys are suppose to be unique.  
        

Algorithm: 

SOl URL: https://leetcode.com/problems/contains-duplicate/solutions/3672475/4-method-s-c-java-python-beginner-friendly/
        
""" 