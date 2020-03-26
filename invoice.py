"""
Program: Invoice.py
Author: Emmanuel Atanga
Last date modified: 03/25/2020



The purpose of this program is to demonstrates the use Class and their constructors
and dictionaries in a class
"""


class Invoice:
    """
        class Invoice
    """

    # constructor
    def __init__(self, iid, cid, address, lname, fname, phone, **kwargs):
        self._invoice_id = int(iid)
        self._customer_id = int(cid)
        self._last_name = str(lname)
        self._first_name = str(fname)
        self._phone_number = str(phone)
        self._address = str(address)
        self._items_with_price = kwargs

    def set_invoice_id(self, iid):
        self._invoice_id = int(iid)

    def set_customer_id(self, cid):
        self._customer_id = int(id)

    def set_last_name(self, lname):
        self._last_name = str(lname)

    def set_first_name(self, fname):
        self._first_name = str(fname)

    def set_phone_number(self, phone):
        self._phone_number = str(phone)

    def set_address(self, address):
        self._address = str(address)

    def set_items_with_price(self, **kwargs):
        self._items_with_price = kwargs

    def __str__(self):
        return f'Invoice Id: {self._invoice_id} \nCustomer Id: {self._customer_id} \nLast Name: {self._last_name} \nFirst Name: {self._first_name} \nPhone Number: {self._phone_number} \nAddress: {self._address} \nItem plus Price: {self._items_with_price}'

    def __repr__(self):
        return f' {type(self._invoice_id)} - {type(self._customer_id)} - {type(self._last_name)} - {type(self._first_name)} - {type(self._phone_number)} - {type(self._address)} - {type(self._items_with_price)}'

    def add_item(self, items):
        self._items_with_price.update(items)

    def create_invoice(self):
        for key, value in self._items_with_price.items():
            print('{}....${}'.format(key, float(value)))
        tax = (float(sum(self._items_with_price.values())) * 0.06)
        total = float(sum(self._items_with_price.values()) + tax)
        print(f'Tax....${"%.2f" % tax} \nTotal....${"%.2f" % total}')


if __name__ == '__main__':
    invoice = Invoice(1, 123, '1313 Disneyland Dr, Anaheim, CA 92802', 'Mouse', 'Minnie', '555-867-5309')
    invoice.add_item({'iPad': 799.99})
    invoice.add_item({'Surface': 999.99})
    invoice.create_invoice()
