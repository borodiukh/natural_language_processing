import csv
import re


def checker(line):
    answer = re.search('^.+;(0|-?[1-9]+[0-9]*);(0|-?[1-9]+[0-9]*)$', string)
    return answer


file = csv.reader(open('tmp.csv'))
for row in file:
    if len(row) != 3:
        print('Bad csv file.Too many columns.')
        break
    string = ';'.join(row)
    if checker(string):
        pass
    else:
        print('Bad csv file')
        break
else:
    print('Good csv file')



