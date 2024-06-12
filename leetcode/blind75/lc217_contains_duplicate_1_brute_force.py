"""
LC 217
Approach 1: The brute force (naive approach) involves comparing each element in the array with every other element if it is same element.
If any dupicate is found, return True

Time Complexity: O(n^2) or O(nxn)
"""

from typing import List 

def has_duplicates(arr: List[int]) -> bool:
    for i in range(len(arr)-1):
        for  j in range(i+1, len(arr)):
            if arr[i] == arr [j]:
                return True
    return False    


# Driver Code
if __name__ == "__main__":
    #arr = [1,2,3,1]
    #arr = [1,2,3,4]
    arr = [1,1,1,3,3,4,3,2,4,2]
    print(has_duplicates(arr))

""""
Time Complexity: O(n^2) where n is the length of the array
    Reason: We have two nested for loops and we are comparing each element of the array with every other element.

Space Complexity: O(1)
    Reason:  No additional Data Structure has been used

Note: The brute force approach compares each element with every other element in the array to check for duplicates. 
        If any duplicates are found, it returns True.
        
        This approach is straightforward but has a time complexity of O(n^2), making it less efficient for large arrays.
        This leads to TLE (Time Limit Exceeded)


Intuition: 
   
Algorithm:
    

SOl URL: https://leetcode.com/problems/contains-duplicate/solutions/3672475/4-method-s-c-java-python-beginner-friendly/
        
"""      
   