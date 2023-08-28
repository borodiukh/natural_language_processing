import nltk

sentence = "Replace it with a new one."
tokens = nltk.word_tokenize(sentence)
print(f'Tokens: {tokens}')
print()

tagged = nltk.pos_tag(tokens)
print(f'Pos-tagging: {tagged}')
print()

if (tagged[-1][0] == '.' or tagged[-1][0] == '!') and tagged[0][1] in ('VB', 'VBD', 'VBN', 'VBP', 'VBZ'):
    # the sentence ends with a full stop or exclamation mark
    # the POS for the first token corresponds to a verb
    print(f'akcja: {tagged[0][0]}')
    obiekt = ' '.join([tuples[0] for tuples in tagged[1:-1]])
    print(f'obiekt: {obiekt}')