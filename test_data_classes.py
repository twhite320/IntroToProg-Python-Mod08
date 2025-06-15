# ------------------------------------------------------------------------------- #
# Title: Test Data Classes Module
# # Description: A collection of tests for the data classes module
# ChangeLog: (Who, When, What)
# RRoot,1.5.2030,Created Script
# ------------------------------------------------------------------------------- #

import unittest
from data_classes import Person, Employee


class TestPerson(unittest.TestCase):

    def test_person_init(self):  # Tests the constructor
        person = Person("John", "Doe")
        self.assertEqual(person.first_name, "John")
        self.assertEqual(person.last_name, "Doe")

    def test_person_invalid_name(self):  # Test the first and last name validations
        with self.assertRaises(ValueError):
            person = Person("123", "Doe")
        with self.assertRaises(ValueError):
            person = Person("John", "123")

    def test_person_str(self):  # Tests the __str__() magic method
        person = Person("John", "Doe")
        self.assertEqual(str(person), "John,Doe")


class TestEmployee(unittest.TestCase):

    def test_employee_init(self):  # Tests the constructor
        employee = Employee("Alice", "Smith", "2023-03-16", 4)
        self.assertEqual(employee.first_name, "Alice")
        self.assertEqual(employee.last_name, "Smith")
        self.assertEqual(employee.review_date, "2023-03-16")
        self.assertEqual(employee.review_rating, 4)

    def test_employee_rating_type(self):  # Tests validation for review rating attribute
        with self.assertRaises(ValueError):
            employee = Employee("Bob", "Johnson", "2025-03-16", 6)

    def test_employee_str(self):
        employee = Employee("Eve", "Brown", "2021-02-15", 4)  # Tests the __str__() magic method
        self.assertEqual(str(employee), "Eve,Brown,2021-02-15,4")

if __name__ == '__main__':
    unittest.main()


