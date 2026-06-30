"""test employee class with fixtures """
import pytest
from employee import Employee

@pytest.fixture
def my_employee():
    return Employee("Marc","Sanchez","100000")

def test_give_default_raise(my_employee):
    my_employee.give_raise()
    test_employee_data = ["Marc","Sanchez","105000"]
    for data in test_employee_data:
        assert data in my_employee.data
    

def test_give_custome_raise(my_employee):
    my_employee.give_raise(100000)
    test_employee_data = ["Marc","Sanchez","200000"]
    for data in test_employee_data:
        assert data in my_employee.data