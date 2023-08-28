import re

with open('bad_english_words.txt') as file:
    answer = []
    list_of_rows = [row.rstrip() for row in file.readlines()]
    for row in list_of_rows:
        # print(row)
        tmp = re.findall('[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}', row, flags=re.I)
        answer.extend(tmp)
    print(answer)