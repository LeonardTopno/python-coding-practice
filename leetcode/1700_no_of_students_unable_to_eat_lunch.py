import collections  # from collections import deque


def count_hungry_students(students, sandwiches):
    students_queue = collections.deque(students)
    # students_queue = deque(students) #Doubly ended queue

    for sandwich in sandwiches:

        if sandwich in students_queue:
            while students_queue[0] != sandwich:
                x = students_queue.popleft()
                students_queue.append(x)  # append is always right side
                
            students_queue.popleft()   # student took sandwich of his choice and left. At the end, it is better to count the num of students left.
            
        else:      
            return len(students_queue)

    return 0   # if sandwich hi nahi hai toh students bhi nahi bache hain, isliye hungry students = 0


# Driver Code
if __name__ == "__main__":
    students = [1, 1, 1, 0, 0, 1]
    sandwiches = [1, 0, 0, 0, 1, 1]

    students_unable_to_eat_lunch = count_hungry_students(students, sandwiches)
    print("Student Unable to Eat Lunch: ", students_unable_to_eat_lunch)

