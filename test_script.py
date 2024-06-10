"""
Unit tests
"""

import csv
import io
import unittest
from unittest.mock import patch
from script import parse_input_data, write_to_csv


class TestConvertToCSV(unittest.TestCase):

    def setUp(self):
        self.input_data = """Script Name: An Introduction to Python
Question: What is Python?
Correct Answer: A programming language
Incorrect 1: A snake
Incorrect 2: A type of coffee
Incorrect 3: A brand of car
Correct Explanation: Python is a high-level programming language.
Incorrect 1 Explanation: While Python is also a type of snake, it is not the correct answer in this context.
Incorrect 2 Explanation: Python is not related to coffee.
Incorrect 3 Explanation: Python is not a car brand.
"""

        self.expected_data = [
            {
                "Video Title (from TOC)": "An Introduction to Python",
                "Question": "What is Python?",
                "Correct": "A programming language",
                "Incorrect 1": "A snake",
                "Incorrect 2": "A type of coffee",
                "Incorrect 3": "A brand of car",
                "Correct Explanation": "Python is a high-level programming language.",
                "Incorrect 1 Explanation": "While Python is also a type of snake, it is not the correct answer in this context.",
                "Incorrect 2 Explanation": "Python is not related to coffee.",
                "Incorrect 3 Explanation": "Python is not a car brand.",
            }
        ]

    def test_parse_input_data(self):
        parsed_data = parse_input_data(self.input_data)
        self.assertEqual(parsed_data, self.expected_data)

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_write_to_stdout(self, mock_stdout):
        parsed_data = parse_input_data(self.input_data)
        write_to_csv(parsed_data, None)

        output = mock_stdout.getvalue()
        reader = csv.DictReader(io.StringIO(output))
        rows = list(reader)

        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0]["Video Title (from TOC)"], "An Introduction to Python")
        self.assertEqual(rows[0]["Question"], "What is Python?")
        self.assertEqual(rows[0]["Correct"], "A programming language")
        self.assertEqual(rows[0]["Incorrect 1"], "A snake")
        self.assertEqual(rows[0]["Incorrect 2"], "A type of coffee")
        self.assertEqual(rows[0]["Incorrect 3"], "A brand of car")
        self.assertEqual(
            rows[0]["Correct Explanation"],
            "Python is a high-level programming language.",
        )
        self.assertEqual(
            rows[0]["Incorrect 1 Explanation"],
            "While Python is also a type of snake, it is not the correct answer in this context.",
        )
        self.assertEqual(
            rows[0]["Incorrect 2 Explanation"], "Python is not related to coffee."
        )
        self.assertEqual(
            rows[0]["Incorrect 3 Explanation"], "Python is not a car brand."
        )


if __name__ == "__main__":
    unittest.main()
