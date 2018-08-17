import unittest
from student import Student

class TestStudentClass(unittest.TestCase):

    def test_full_name(self):
        student = Student(first_name="Vasily", last_name="Pupkin")
        self.assertEqual(student.full_name(), "Vasily Pupkin")

    def test_no_name(self):
        student = Student()
        self.assertEqual(student.full_name(), "N/A N/A")
    
    def test_passport_missing(self):
        student = Student()
        self.assertIsNone(student.passport)

if __name__ == '__main__':
    unittest.main()