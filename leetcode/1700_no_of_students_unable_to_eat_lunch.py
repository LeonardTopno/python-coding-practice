import collections  # from collections import deque


def count_students(students, sandwiches):
    queue = collections.deque(students)
    # queue = deque(students) #Doubly ended queue

    for sandwich in sandwiches:

        if sandwich in queue:
            while queue[0] != sandwich:
                x = queue.popleft()
                queue.append(x)  # append is always right side
                
            queue.popleft()   # student took sandwich of his choice and left. At the end, it is better to count the num of students left.
            
        else:      
            return len(queue)

    return 0   # if sandwich hi nahi hai toh students bhi nahi bache hain, isliye hungry students = 0


# Driver Code
if __name__ == "__main__":
    students = [1, 1, 1, 0, 0, 1]
    sandwiches = [1, 0, 0, 0, 1, 1]

    studentsUnableToEatLunch = count_students(students, sandwiches)
    print("Student Unable to Eat Lunch: ", studentsUnableToEatLunch)

