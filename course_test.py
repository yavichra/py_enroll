import unittest
from course import Course

class TestCourseClass(unittest.TestCase):

    def test_name_missing(self):
        with self.assertRaises(KeyError) as e:
            Course()
            self.assertEqual(e.exception, 'name')


if __name__ == '__main__':
    unittest.main()