from datetime import datetime


class Employee:
    """Employee Class"""

    # Constructor
    def __init__(self, lname, fname, address, phone, salary, date, salaried="No"):
        self._last_name = str(lname)
        self._first_name = str(fname)
        self._address = str(address)
        self._phone_number = str(phone)
        self._salaried = bool(salaried)
        self._start_date = datetime(date)
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

    def set_start_date(self, date):
        self._start_date = date

    def set_salary(self, salary):
        self._salary = salary

    def display(self):
        return self._last_name + " " + self._first_name + "\n " + self._address + "\n " + self._phone_number + "\n$" + self._salary + "\n" + self._start_date


# Driver

emp = Employee('Ruiz', 'Matthew', '801 SE mandarin Dr', '555-555-555', 40000, datetime(2019, 6, 28))

print(emp.display())  # display returns a str, so print the information
del emp  # clean up!
