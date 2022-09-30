import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    def setUp(self):
        # self.first_name = 'lily'
        # self.last_name = 'brown'
        # self.salary =  2000
        # self.give_raise = Employee.give_raise(self)
        self.one_employee = Employee('lily', 'brown', 2000)
        self.give_raise = self.one_employee.give_raise

    # def test_give_default_raise(self):
    #     expected_result = self.give_raise()
    #     self.assertEqual(7000, self.salary)

    def test_give_custom_raise(self):
        self.give_raise(10000)
        self.assertEqual(12000, self.one_employee.salary)

unittest.main()