# ------------------------------------------------------------------------------- #
# Title: Test Processing Classes Module
# # Description: A collection of tests for the processing classes module
# ChangeLog: (Who, When, What)
# RRoot,1.5.2030,Created Script
# ------------------------------------------------------------------------------- #

import unittest
import tempfile
import json
import data_classes as data
from processing_classes import FileProcessor


class TestFileProcessor(unittest.TestCase):
    def setup(self):
        # Create a temporary file for testing
        self.temp_file = tempfile.NamedTemporaryFile()
        self.temp_file_name = self.temp_file.name
        self.employee_data = []

    def teardown(self):
        # Clean up and delete the temporary file
        self.temp_file.close()

    def test_read_employee_data_from_file(self):
        # Create some sample data and write it to the temporary file
        sample_data = [
            {"FirstName": "John", "LastName": "Doe", "ReviewDate": "2021-02-16", "ReviewRating": 2},
            {"FirstName": "Vic", "LastName": "Vu", "ReviewDate": "2020-08-25", "ReviewRating": 4}
        ]
        with open(self.temp_file_name, "w") as file:
            json.dump(sample_data, file)

        # Call the read_data_from_file method and check if it returns the expected data
        FileProcessor.read_employee_data_from_file(self.temp_file_name, self.employee_data_data)

        # Assert that the employee_data list contains the expected student objects
        self.assertEqual(len(self.employee_data), len(sample_data))
        self.assertEqual(self.employee_data[0].first_name, "John")
        self.assertEqual(self.employee_data[1].review_rating, 4)


if __name__ == "__main__":
    unittest.main()
