"""
Program: student.py
Author: Emmanuel Atanga
Last date modified: 03/25/2020



The purpose of this program is to demonstrates testing of a class
with unittest
"""


class Student:
    """Student class"""

    def __init__(self, lname, fname, major, gpa=0.0):
        name_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz.'-")
        gpa_characters = set("1234567890-.")
        if not (name_characters.issuperset(lname) and name_characters.issuperset(fname)):
            raise ValueError
        if major and not name_characters.issuperset(major):
            raise ValueError
        if gpa and not gpa_characters.issuperset(gpa):
            raise ValueError
        self.last_name = lname
        self.first_name = fname
        self.major = major
        self.gpa = gpa

    def __str__(self):
        return self.last_name + ", " + self.first_name + " has major " + self.major + " with gpa: " + str(self.gpa)
