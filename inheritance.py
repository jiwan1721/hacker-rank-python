class Employee:
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@gmail.com'
        self.pay = pay

    def fullname(self):
        return f"{self.first} {self.last}"

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


class Developer(Employee):
    raise_amount = 5

    def __init__(self, first, last, pay, progmammig_lang):
        super().__init__(first, last, pay)
        # Employee.__init__(self, first, last, pay) this is optional
        self.progmammig_lang = progmammig_lang


class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        Employee.__init__(self, first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
    
    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
    
    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
    
    def print_emps(self):
        for emp in self.employees:
            print(emp.fullname())



dev = Developer('jiwan', 'chand', 3444, 'python')
dev1 = Developer('eam', 'haei', 233, 'java')
# print(dev.pay)
dev.apply_raise()
# print(dev.pay)

# print(f"email of {dev.fullname()} is {dev.email} with raise amount {dev.pay}.He is {dev.progmammig_lang} developer.")
# print(help(dev))

mang1 = (Manager('ram', 'nath', 3444, [dev]))
mang1.add_emp(dev1)
print(mang1.email)

mang1.print_emps()
print(issubclass(Manager, Employee))
