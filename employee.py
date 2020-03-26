"""
Program: employee.py
Author: Emmanuel Atanga
Last date modified: 03/25/2020



The purpose of this program is to demonstrate classes in python
"""
from datetime import date


class Employee:
    """Employee Class"""

    # Constructor
    def __init__(self, lname, fname, address, phone, salary, new_date, salaried=True):
        self._last_name = str(lname)
        self._first_name = str(fname)
        self._address = str(address)
        self._phone_number = str(phone)
        self._salaried = bool(salaried)
        self._start_date = new_date
        self._salary = '%.2f' % float(salary)

    def set_last_name(self, lname):
        self._last_name = lname

    def set_first_name(self, fname):
        self._first_name = fname

    def set_address(self, address):
        self._address = address

    def set_phone_number(self, phone):
        self._phone_number = phone

    def set_salaried(self, salaried):
        self._salaried = salaried

    def set_start_date(self, new_date):
        self._start_date = date(new_date)

    def set_salary(self, salary):
        self._salary = salary

    def display(self):
        print(self._last_name + " " + self._first_name)
        print(self._address)
        if self._salaried:
            print(f'salaried employee: ${self._salary}')
        else:
            print(f'Hourly employee: ${self._salary}')
        print(f'Start date:{self._start_date}')


# Driver
if __name__ == '__main__':
    employee1 = Employee('Ruiz', 'Matthew', '801 SE mandarin Dr.\nGrimes, Iowa', '555-555-555', 40000,
                         date(2019, 3, 12))
    employee2 = Employee('John', 'Stockman', '2654 old pig rd.\nJohnson, Iowa', '555-666-888', 32000, date(2019, 6, 24),
                         salaried=False)

    employee1.display()
    employee2.display()
