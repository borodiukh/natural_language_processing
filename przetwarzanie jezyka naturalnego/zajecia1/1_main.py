import csv
from datetime import datetime
from classes import Employee, IssuedInvoice, ReceivedInvoice

employee_file = csv.reader(open('employee.csv'))
next(employee_file)
employee_list = [Employee(x[0], x[1], x[2]) for x in employee_file]

issued_file = csv.reader(open('issued_invoice.csv'))
next(issued_file)
issued_list = [IssuedInvoice(x[0], x[1]) for x in issued_file]

received_file = csv.reader(open('received_invoice.csv'))
next(received_file)
received_list = [ReceivedInvoice(x[0], x[1]) for x in received_file]

sum_of_salary_per_month = 0
for employee in employee_list:
    sum_of_salary_per_month += employee.get_salary()
# print(sum_of_salary_per_month)

for number_of_month in range(1, 13):
    issued_amount = 0
    received_amount = 0

    for issued in issued_list:
        if number_of_month == issued.get_month():
            issued_amount = issued.get_issued_amount()
            break

    for received in received_list:
        if number_of_month == received.get_month():
            received_amount = received.get_received_amount()
            break

    print(f'MONTH {number_of_month}')
    print(f'SUMA PRZYCHODÓW {issued_amount}')
    print(f'SUMA WYDATKÓW {received_amount + sum_of_salary_per_month}')
    print(f'BILANS {issued_amount - (received_amount + sum_of_salary_per_month)}')
    print()

