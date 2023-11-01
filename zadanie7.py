def solution(sentence):
    words = sentence.split()
    words = [word.lower() for word in words]

    filtered_words = [word for word in words if 3 <= len(word) <= 10]

    return filtered_words


test_data = ['This is a sentence',
             'Thissentence contains a mistake',
             'One more sentence to test_this_code']
test_result = [['this', 'sentence'],
               ['contains', 'mistake'],
               ['one', 'more', 'sentence']]

result = [solution(sentence) for sentence in test_data]

print(result)

if result == test_result:
    print('Correct!')
else:
    print('Improve')
