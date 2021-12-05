
class Employee:
    
    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay 
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'. format(self.first, self.last)
    
    def applyraise(self):
        self.pay = int(self.pay * self.raise_amt)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)
    
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


emp_1 = Employee('Nav', 'Atluri', 50000)
emp_2 = Employee('test', 'user', 60000)

import datetime

my_date = datetime.date(2016, 7, 10)

print(Employee.is_workday(my_date))



#emp_str_1 = 'John-Doe-70000'
#emp_str_2 = 'ram-bantu-40000'
#
#new_emp_1 = Employee.from_string(emp_str_1)
#
#print(new_emp_1.email)
#print(new_emp_1.pay)



#Employee.set_raise_amt(1.05)
#
#print(Employee.raise_amt)
#print(emp_1.raise_amt)
#print(emp_2.raise_amt)



#emp_1.first =  'Nav'
#emp_1.last = 'Atluri'
#emp_1.email =  'nav.atluri@company.com'
#emp_1.pay = 50000
#
#
#emp_2.first =  'test'
#emp_2.last = 'user'
#emp_2.email =  'test.user@company.com'
#emp_2.pay = 60000

