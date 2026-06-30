from employee import Employee
#CrashCourse p223 ex 11-3 without fixture
def test_give_default_raise():
    my_test = my_employee = Employee("Marc","Sanchez","100000")
    my_test.give_raise()
    test_employee_data = ["Marc","Sanchez","105000"]
    for data in test_employee_data:
        assert data in my_test.data
    

def test_give_custome_raise():
    my_test = my_employee = Employee("Marc","Sanchez","100000")
    my_test.give_raise(100000)
    test_employee_data = ["Marc","Sanchez","200000"]
    for data in test_employee_data:
        assert data in my_test.data