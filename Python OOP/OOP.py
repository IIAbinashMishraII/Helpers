# Classes help to group data and function. (for reusability)
# Data are called attributes and functions are called methods in classes.
# regular methods automatically pass instance as first argument, 
# classmethods automatically passes class as first argument,
# staticmethod passes nothing, nada... nada 
class Employee: 
    # class variables - accessible by the class, and instance for the instance
    raise_amount = 1.05
    num_of_employees = 0

    def __init__(self, first, last, pay): # Constructor method/ Initialize
        # Instance variables
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first+'.'+last+'@test.com'
        # If we put self.num_of_employee, everytime it will default to 0
        Employee.num_of_employees += 1

    def fullname(self):
        return (f'{self.first} {self.last}')
    
    # We can use self.raise_amount or Employee.raise_amount. 
    # 1st one is through instance, 2nd one is through class
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount) 

    # Instead of using self, we use cls as a convention for the class methods
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        x,y,z = emp_str.split('-')
        return cls(x,y,z)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

# class is basically a blueprint to create instance. 
# Instance of class 
emp1 = Employee('pest', 'best', 400)
emp2 = Employee('rest', 'lest', 500)
print(emp1.email)
print(emp2.email)
print(emp1.fullname()) 
print(Employee.fullname(emp1)) # both are similar but we have to pass the 
# instance as argument to justify why we need self in the upper print statement.
print(emp2.fullname())

# <__main__.Employee object at 0x102fd09a0> 
# <__main__.Employee object at 0x102fd0be0> This shows 2 different class 
# with differnet location in memory

# Both are same, but using class name instead of instance is better practiec
Employee.set_raise_amt(1.1)
emp1.raise_amount = 1.2

# Both works because, it checks the inheritance of class and 
# go above the scope of instance to find the variable
# any change made to the class variable through the instance will apply
# the changes only to that instance and not others. 
print(emp1.raise_amount)
print(Employee.raise_amount)
print(Employee.num_of_employees)


import datetime
my_date = datetime.date(2024, 8, 14)

print(Employee.is_workday(my_date))