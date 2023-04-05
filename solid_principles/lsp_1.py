from abc import ABC, abstractmethod


class Member(ABC):
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    @abstractmethod
    def save_database(self):
        pass


class Teacher(Member):
    def __init__(self, name: str, age: int, teacher_id: str):
        super().__init__(name, age)
        self.teacher_id = teacher_id

    def save_database(self):
        print("Saving teacher data to database")


class Student(Member):
    def __init__(self, name: str, age: int , student_id: str):
        super().__init__(name, age)
        self.student_id = student_id

    def save_database(self):
        print("Saving student data to database")


# Driver code
from typing import List
members: List[Member] = []
members.append(Student('nusret',23,"12345"))
members.append(Teacher('Teacher_nusret',23,"12345"))

for member in members:
	member.save_database()