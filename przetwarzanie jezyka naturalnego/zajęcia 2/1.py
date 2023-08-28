import re


def checker(data, input_string):
    check = re.search('^[A-Z][a-z]+$', input_string)
    if check:
        print(f'{data.capitalize()} is correct')
    else:
        print(f'Incorrect {data}')


name = input('Name: ')
checker('name', name)
# check_name = re.search('^[A-Z][a-z]+$', name)
# if check_name:
#     print('Name is correct')
# else:
#     print('Incorrect name')


surname = input('Surname: ')
checker('surname', surname)
# check_surname = re.search('^[A-Z][a-z]+$', surname)
# if check_surname:
#     print('Surname is correct')
# else:
#     print('Incorrect surname')


city = input('City: ')
checker('city', city)
# check_city = re.search('^[A-Z][a-z]+$', city)
# if check_city:
#     print('City is correct')
# else:
#     print('Incorrect city')


phone_number = input('Phone number: ')
check_phone_number = re.search('^\(61\)[0-9]{3}-[0-9]{2}-[0-9]{2}$', phone_number)
if check_phone_number:
    print('Phone number is correct')
else:
    print('Incorrect phone number')


post_code = input('Post code: ')
check_post_code = re.search('^[1-9][0-9]-[1-9][0-9]{2}$', post_code)
if check_post_code:
    print('Post code is correct')
else:
    print('Incorrect post code')
