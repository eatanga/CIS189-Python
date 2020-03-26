"""
Program: test_student_class.py
Author: Emmanuel Atanga
Last date modified: 03/25/2020



The purpose of this program is to demonstrates the unittest with python class
"""
import unittest
from class_definitions import student as s


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.student = s.Student('Atanga', 'Manny', 'B.I.S')

    def tearDown(self):
        del self.student

    def test_object_created_required_attributes(self):
        self.assertEqual(self.student.last_name, 'Atanga')
        self.assertEqual(self.student.first_name, 'Manny')
        self.assertEqual(self.student.major, 'B.I.S')

    def test_object_created_all_attributes(self):
        student = s.Student('Atanga', 'Manny', 'B.I.S', '3.7')
        assert self.student.last_name == 'Atanga'
        assert student.first_name == 'Manny'
        assert student.major == 'B.I.S'
        assert student.gpa == '3.7'

    def test_student_str(self):
        self.assertEqual(str(self.student), 'Atanga, Manny has major B.I.S with gpa: 0.0')

    def test_object_not_created_error_last_name(self):
        with self.assertRaises(ValueError):
            a = s.Student('123', 'Manny', 'B.I.S')

    def test_object_not_created_error_first_name(self):
        with self.assertRaises(ValueError):
            a = s.Student('Atanga', '123', 'B.I.S')

    def test_object_not_created_error_major(self):
        with self.assertRaises(ValueError):
            a = s.Student('Atanga', 'Manny', '578')

    def test_object_not_created_error_gpa(self):
        with self.assertRaises(ValueError):
            a = s.Student('Atanga', 'Manny', 'B.I.S', 'abc')


if __name__ == '__main__':
    unittest.main()
