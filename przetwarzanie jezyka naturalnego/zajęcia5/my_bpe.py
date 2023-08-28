import string
import collections
from sys import exit


def preparation(text):
    text_without_punctuation = text.translate(str.maketrans('', '', string.punctuation)).split()
    array = [" ".join(word) + ' </w>' for word in text_without_punctuation]
    array = ' '.join(array)
    return array


def get_pair_stats(vocab):
    pairs = collections.defaultdict(int)

    for word, freq in vocab.items():
        chars = word.split()
        for i in range(len(chars) - 1):
            pairs[chars[i], chars[i + 1]] += freq

    return pairs


def merge(best_pair, word_count):
    best_pair_space = " ".join(best_pair)
    best_pair_merged = "".join(best_pair)
    merged_dict = {}
    for word in word_count:
        word_merged = word.replace(best_pair_space, best_pair_merged)
        merged_dict[word_merged] = word_count[word]
    return merged_dict


# text = "Hurry on, Harry, hurry on!".lower()
# how_many_words_should_be = 10
text = input('Input text: ').lower()
how_many_words_should_be = int(input('How many elements should be in dictionary: '))
TEXT_SPLITED = preparation(text)
# print(TEXT_SPLITED)
# print(type(text))

TOKENS = text.translate(str.maketrans('', '', string.punctuation)).split()
TOKENS = [" ".join(tok) + ' </w>' for tok in TOKENS]
# print(TOKENS)

VOCABYLARY = set(TEXT_SPLITED.split())
# print(f'VOCABYLARY = {VOCABYLARY}')

while True:
    if len(VOCABYLARY) > how_many_words_should_be:
        print(VOCABYLARY)
        exit()
    else:
        COUNT_BIGRAMS = collections.Counter(TEXT_SPLITED.split())
        # print(f'COUNT_BIGRAMS = {COUNT_BIGRAMS}')

        pairs = get_pair_stats(collections.Counter(TOKENS))
        # print(pairs)
        try:
            best_pair = max(pairs, key=pairs.get)
            # print(best_pair)
        except:
            print(VOCABYLARY)
            exit()
        else:
            VOCABYLARY.add(''.join(best_pair))
            # print(len(VOCABYLARY))
            # print(VOCABYLARY)

            TOKENS = merge(best_pair, collections.Counter(TOKENS))
            # print(TOKENS)


