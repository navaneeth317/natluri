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


class Developer(Employee):
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang
    

class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
    
    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def rem_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
        
    def print_emps(self):
        for emp in self.employees:
            print('--->', emp.fullname())

    
    


dev_1 = Developer('Nav', 'Atluri', 50000, 'python')
dev_2 = Developer('test', 'user', 60000, 'java')

mgr_1 = Manager('sue', 'smith', 90000, [dev_1])

# print(mgr_1.email)

# print(isinstance(mgr_1, Manager))

# print(issubclass(Developer, Manager))


# print(dev_1.prog_lang)
# print(dev_2.prog_lang)

print(str.__add__('a', 'b'))