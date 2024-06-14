"""
Approach 2: Approach is to sort the array in-place using list.sort(). Then check if any of the ADJACENT ELEMENTS are same (equal). 
Mantra:  SORTING helps in bringing duplicates together, hence simplifies the check.

Time Complexity: Sorting the arr - O(nlog n)   +   Iterating the arr - O(n)       = O(n log n) 
"""

from typing import List

def has_duplicates(arr:List[int])->bool:
    arr.sort()  # In-place sorting of the array | Tim Sort algorithm (named after Tim Peters) | TC = O(n log n)
    
    for i in range(len(arr)-1):
        if arr[i] == arr[i+1]:
            return True
    
    return False

# Drive code
if __name__ == "__main__":
    #arr = [1,2,3,1]
    #arr = [1,2,3,4]
    arr = [1,1,1,3,3,4,3,2,4,2]
    print(has_duplicates(arr))
    

""""
Time Complexity: O(n log n) where n is the length of the array
    Reason: Sorting the array takes O(n logn) 
            Iterating through the array takes O(n)
            Time Complexity: O(n log n) + O(n) = O(n log n)

Space Complexity: O(1)
    Reason:  No additional Data Structure has been used

Note: 

Intuition: This sorting approach sorts the array in ascending order ( TC: O(nlogn) ), 
            and then checks for ADJACENT ELEMENTS that are same.
            If any of the ADJANCENT ELEMENTS are found to be same, it means the array has duplicates, hence return TRUE.

            Mantra:  SORTING helps in bringing duplicates together, hence simplifies the check.
   
Algorithm (Leo: Ignore this, kept only for template reference):
    The optimized algorithm contains only two changes from the brute force approach:
    i) The numbers are stored in a HashSet (or Set, in Python) to allow O(1) lookups, 
    ii) and we only attempt to build sequences from numbers that are not already a part of longer sequence 
        This is accomplished by first ensuring that the number that would immediately preceed the current number is a 
        sequence is not present, as that number would necessarily be part of a longer sequence.

Sol URL: https://leetcode.com/problems/contains-duplicate/solutions/3672475/4-method-s-c-java-python-beginner-friendly/
        
""" 