from datetime import datetime


class Employee:
    def __init__(self, name, surname, salary):
        self.name = name
        self.surname = surname
        self.salary = salary

    def get_salary(self):
        return int(self.salary)


class ReceivedInvoice:
    def __init__(self, date, amount):
        self.date = date
        self.amount = amount

    def get_month(self):
        return int(datetime.strptime(self.date, '%Y-%m-%d').month)

    def get_received_amount(self):
        return int(self.amount)


class IssuedInvoice:
    def __init__(self, date, amount):
        self.date = date
        self.amount = amount

    def get_month(self):
        return int(datetime.strptime(self.date, '%Y-%m-%d').month)

    def get_issued_amount(self):
        return int(self.amount)