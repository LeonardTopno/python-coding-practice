import collections  # from collections import deque


def count_hungry_students(students, sandwiches):
    students_queue = collections.deque(students)  # Doubly ended queue

    for sandwich in sandwiches:

        if sandwich in students_queue:
            while students_queue[0] != sandwich:
                x = students_queue.popleft()
                students_queue.append(x)  # append is always right side

            students_queue.popleft()  # Student took the sandwich and left, at the end it is better to count the num of students left in the queue

        else:
            return len(students_queue)

    # if there are no sandwich, it means there are no students (hence no hungry students)
    return 0


# Driver Code
if __name__ == "__main__":
    students = [1, 1, 0, 0, 1]
    sandwiches = [1, 0, 0, 0, 1, 1]

    students_unable_to_eat_lunch = count_hungry_students(students, sandwiches)
    print(students_unable_to_eat_lunch)



