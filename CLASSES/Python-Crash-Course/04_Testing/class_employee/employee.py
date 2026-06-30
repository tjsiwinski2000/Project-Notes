class Employee:
    """ store info about an employee, with ability to give raise"""

    def __init__(self,first,last,salary):
        self.fname = first
        self.lname = last
        self.salary = int(salary)
        self.data = []
        self.data.append(first)
        self.data.append(last)
        self.data.append(salary)
        
    def give_raise(self,raise_amount = 5000):
        self.salary += int(raise_amount)
        self.data.clear()
        self.data.append(self.fname)
        self.data.append(self.lname)
        self.data.append(str(self.salary))

    def output_employee_data(self):
        print(self.fname, self.lname, self.salary)