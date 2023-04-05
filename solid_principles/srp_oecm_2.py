from abc import ABC, abstractmethod


class Employee(ABC):

    def __init__(self, name: str, salary:str):
        self.name = name
        self.salary = salary

    @abstractmethod
    def get_worker(self):
        pass


class Developer(Employee):

    def __init__(self, name:str, salary: str):
        super().__init__(name, salary)

    def get_developer(self):
        print("{} is an excellent developer".format(self.name))

    def get_worker(self):
        self.get_developer()


class Tester(Employee):

    def __init__(self, name: str, salary: str):
        super().__init__(name, salary)

    def get_tester(self):
        print("{} is a tester".format(self.name))

    def get_worker(self):
        self.get_tester()


class Company:

    def __init__(self, name:str):
        self.name = name 
        
    def get_employee(self, employee: Employee):
        employee.get_worker()
    

company = Company("HCL")
developer = Developer("Akhil", "15,00,000")
tester = Tester("Leo", "8,00,000")

company.get_employee(developer) 
company.get_employee(tester) 