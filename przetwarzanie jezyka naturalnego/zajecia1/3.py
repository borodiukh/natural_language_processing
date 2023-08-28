dictionary_colors = {
    'biały': 'white',
    'czarny': 'black',
    'żółty': 'yellow',
    'pomarańczowy': 'orange',
    'czerwony': 'red',
    'zielony': 'green',
    'niebieski': 'blue',
    'fioletowy': 'purple',
    'szary': 'grey',
    'różowy': 'purple'
}

print('Available colors: [biały, czarny, żółty, pomarańczowy, czerwony, zielony, niebieski, fioletowy, szary, różowy]')
print()

while True:
    input_from_user = input('Enter the Polish word or "q" for exit: ')
    if input_from_user == 'q':
        break
    answer = dictionary_colors.get(input_from_user.lower())
    if answer is None:
        print('Word does not exist')
    else:
        print(answer)