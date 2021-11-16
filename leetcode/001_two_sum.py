'''
Given an array of integers 'nums' and an integer 'target', 
return indices of two numbers that add uptp target.

You may assume that EACH INPUT WOULD HAVE EXACTLY ONE SOLUTION, 
and you may not use the same element twice.

You can return the answer in any order.
'''

def getIndicesOfTwoSum(nums, target):
    look_up = {}                                    # An empty dict just to be use and throw

    for index, elem in enumerate(nums):
        if (target - elem) in look_up:
            print("look_up:", look_up)
            return [index, look_up[target-elem]]    # Not storing in a sequece, but directly returning the indices pair, as is it given that there is ONLY one such pair
        else:                                       # can do without else also, but using it for readibility and easy understanding
            look_up[elem]=index
    
    return [] # In case not found, returning empty list just to maintain the type of return


# Driver Code
if __name__ == "__main__":
    nums = [2,7,11,15]         #nums = [3,2,4]             #nums = [3,3]           #nums = [3,3,4,5]
    target = 9                 #target = 6                 #target = 6             #target = 7

    print(getIndicesOfTwoSum(nums, target))


'''
--- 1. Approach: 

        1. Maintain a mapping
                    num --> index
        2. Check if (target - num) has been already found, And stored in mapping

        3. It is given that there exists only 1 pair such that elem1 + elem2 = target. => elem2 = target - elem1
        
        3. Since we know the target, as long as we maintain a record of all previous values encountered, we can compare the current elem to its only pair

--- 2. Leo's Ananlysis

        1. # use look_up : {num:index}  #num --> index

        # Leo's introspective question: How to conclude that elems are not repeated, and hence can be used as keys in a dict as look_up
        # Got the hint: There can be duplicates, and that does not restrict us from using them as keys in dict(hashmap), IN THIS CASE. AS IT IS GIVEN THAT WE WILL NOT USE THE SAME ELEM TWICE.
        # Usually in other problems, we define look_up at the top IN COMPLETENESS, before starting to solve the problem.  
        # Here we are just initializing it. And Not defining it IN COMPLETENESS.
        # If we get repeated numbers(elems), the key i.e. num will be updated with new index. That's it.

        Time Complexity: O(n) for the single pass using for 1 for-loop (One iteration)
        Space Complexity: O(n) for the dictionary

--- 3. Things to learn:
        1. use of enumerate() func to get index and the elem together.
        2. use of dict/hast table (empty one) as look_up

--- 4. Problem Tagging
        1. Problem Type: Array / List, Hash Table
        2. Level: Easy

--- 5. To do: Take thought process from
'''
