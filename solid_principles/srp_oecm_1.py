class Employee:

    def __init__(self, name: str, salary: str):
        self.name = name
        self.salary = salary


class Developer(Employee):

    def __init__(self, name: str, salary: str):
        super().__init__(name, salary)

    def get_developer(self):
        print("{} is an excellent developer".format(self.name))


class Tester(Employee):

    def __init__(self, name:str, salary: str):
        super().__init__(name, salary)              #ToDO

    def get_tester(self):
        print("{} is a tester". format(self.name))


class Company:

    def __init__(self, name: str):
        self.name = name
    
    def get_employee(self, employee):
        if isinstance(employee, Developer):
            employee.get_developer()
        elif isinstance(employee, Tester):
            employee.get_tester()
        else:
            raise Exception("Unknown Employee")s
    

company = Company("HCL")
developer = Developer("Akhil", "15,00,000")
tester = Tester("Leo", "8,00,000")

company.get_employee(developer) # will print Akhil is developing
comp.get_employee(tester)  # will print Leo is testing