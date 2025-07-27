import unittest
from grades import calculate_grade

class TestGrades(unittest.TestCase):

    def test_valid_grades(self):
        self.assertEqual(calculate_grade(95), "A")
        self.assertEqual(calculate_grade(80), "B")
        self.assertEqual(calculate_grade(60), "C")

    def test_edge_cases(self):
        self.assertEqual(calculate_grade(90), "A")
        self.assertEqual(calculate_grade(75), "B")
        self.assertEqual(calculate_grade(0), "C")

    def test_invalid_grades(self):
        self.assertEqual(calculate_grade(-5), "Invalid")
        self.assertEqual(calculate_grade(105), "Invalid")

if __name__ == '__main__':
    unittest.main()
