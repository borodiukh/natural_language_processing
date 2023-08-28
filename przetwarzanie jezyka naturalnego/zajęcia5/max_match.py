def max_match(string, words_dict):
    tokens = []
    if sentence == '':
        print([])
    i = 0
    while i < len(string):
        maxWord = ""
        for j in range(i, len(string)):
            tempWord = string[i:j + 1]
            if tempWord in words_dict and len(tempWord) > len(maxWord):
                maxWord = tempWord
        i = i + len(maxWord)
        tokens.append(maxWord)
        # print(tokens)
    print(tokens)


with open('polish_words.txt', encoding='utf-8') as words_file:
    words = [word.rstrip() for word in words_file.readlines()]
    print(words)


sentence = input('Input sentence: ')
sentence = sentence.replace(' ', '').replace(',', '')
print(sentence)

max_match(sentence, words)