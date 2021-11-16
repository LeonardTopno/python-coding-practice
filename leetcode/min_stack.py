'''
Design a stack that returns the minimum element in constant time
LeetCode: 155
'''
class MinStack:

    def __init__(self):
        self.stack = []         # Main Stack to store elem #Using List as Stack, collections.deque(), self.stack = deque() could be used if there is a need to use popleft()
        self.auxStack = []      # Auxiliary Stack to store min_elem on the Top always


    def push(self, x):

        self.stack.append(x)                # push the given elem in the main Stack

        if not self.auxStack:
            self.auxStack.append(x)
        else:
            if self.auxStack[-1] >= x:
                self.auxStack.append(x)
    
    
    def pop(self):
        
        if not self.stack:                  # Originally if self.isEmpty():  # if not self.stack: # This will remove dependency from other function - isEmpty()
            print("Main Stack Underflow")
            return -1                       # return

        top_elem = self.stack.pop()
        
        if self.auxStack[-1] == top_elem:
            self.auxStack.pop()
        
        return top_elem         # return the poped element
    
    def isEmpty(self):
        return not self.stack   # This is a smart way to check if a Stack or any DS is empty (not ==> empty)
    
    def top(self):              # Equivalent of peep in Stack
        return self.stack[-1]
    
    def getMin(self):

        if not self.auxStack:
            print("Stack Underlow")
            return              # return -1

        return self.auxStack[-1]

    

        
# Driver Code
if __name__ == "__main__":
    obj = MinStack()
    obj.push(1)
    obj.push(5)
    obj.push(3)
    obj.push(9)
    obj.push(7)
    obj.pop()
    obj.push(1)
    print("Is Empty: ", obj.isEmpty())
    print(obj.getMin())
    print("Top Elem: ", obj.top())
    print("Poped Elem: ", obj.pop())