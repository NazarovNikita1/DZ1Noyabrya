def solution(sentence):
    # Приводим текст к нижнему регистру
    sentence = sentence.lower()

    # Разбиваем текст на слова
    words = sentence.split()

    words = sentence.lower().split()
    return words

test_data = ['This a sample sentence',
             'THIS IS A CAPITALIZED SENTENCE',
             'and one MORE SENTENCE']
test_result = [['this', 'a', 'sample', 'sentence'],
               ['this', 'is', 'a', 'capitalized', 'sentence'],
               ['and', 'one', 'more', 'sentence']]

result = [solution(sentence) for sentence in test_data]

print(result)

if result == test_result:
    print('Correct!')
else:
    print('Improve')

