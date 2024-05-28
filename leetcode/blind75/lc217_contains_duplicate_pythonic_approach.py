"""
Pythonic Approach
"""

from typing import List

def has_duplicates(arr: List[int]) -> bool:
    if len(set(arr)) == len(arr):
        # if the lengths are same, there are no duplicates in the arr
        return False
    
    return True

# Driver Code
if __name__ == "__main__":
    #arr = [1,2,3,1]
    #arr = [1,2,3,4]
    arr = [1,1,1,3,3,4,3,2,4,2]
    print(has_duplicates(arr)) 

