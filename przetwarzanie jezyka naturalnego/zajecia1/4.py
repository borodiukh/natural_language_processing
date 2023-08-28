# input file should be in the same directory with name 'text.txt'

with open('text.txt') as input_file:
    input_file = input_file.readlines()
    with open('answer.txt', 'w', encoding='utf-8') as output_file:
        counter = 1
        for line in input_file:
            if counter % 3 == 0 or 'kocham' in line.lower():
                output_file.write('*****\n')
                counter += 1
                continue
            else:
                output_file.write(line)
                counter += 1
