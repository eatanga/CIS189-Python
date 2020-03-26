"""
Program: customer.py
Author: Emmanuel Atanga
Last date modified: 03/25/2020



The purpose of this program is to demonstrates the use Class and their constructors
"""


class Customer:
    """
        class customer
    """

    # constructor
    def __init__(self, cid, lname, fname, phone, address):
        self._customer_id = int(cid)
        self._last_name = str(lname)
        self._first_name = str(fname)
        self._phone_number = str(phone)
        self._address = str(address)

    def set_customer_id(self, cid):
        self._customer_id = id

    def set_last_name(self, lname):
        self._last_name = lname

    def set_first_name(self, fname):
        self._first_name = fname

    def set_phone_number(self, phone):
        self._phone_number = phone

    def set_address(self, address):
        self._address = address

    def __str__(self):
        return f'Customer Id: {self._customer_id} \nLast Name: {self._last_name} \nFirst Name: {self._first_name} \nPhone Number: {self._phone_number} \nAddress: {self._address}'

    def __repr__(self):
        return f'{type(self._customer_id)} - {type(self._last_name)} - {type(self._first_name)} - {type(self._phone_number)} - {type(self._address)}'

    def display(self):
        return f' Id: {self._customer_id}  Name:{self._last_name} {self._first_name}  Phone:{self._phone_number}  Address:{self._address}'


if __name__ == '__main__':
    customer1 = Customer(1, "Hopkins", "John", "555-555-5555", "6500 Hopkins Rd")
    print(customer1.display())
    try:
        customer2 = Customer("b", "Hops", "James", "555-655-4444", "200 Lineman Dr.")
        print(customer2.display())
    except ValueError:
        print("constructor error. Customer not created")
    """ When display() is called on on customer2, a Value Error is displayed.
    This is because an invalid literal(string) has been used in the place of
    an integer"""
