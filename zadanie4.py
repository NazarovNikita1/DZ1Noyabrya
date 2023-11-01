def solution(text):

    text = text.lower()

    words = text.split()

    #Сделаем частотный словарь
    freq_dict = {}

    for word in words:
        # Если слово еще не записано в частотный словарь, внесем его в словарь со значением 1
        if word not in freq_dict:
            freq_dict[word] = 1
        else:
            # Если слово уже записано в частотный словарь, прибавим к его значению единицу
            freq_dict[word] += 1

    return freq_dict


test_data = ['NLP is a subfield of AI and NLP is widely used',
             'Count the word frequency and build a frequency dictionary',
             'This task is not hard this task is ovewhelming this task is fun']
test_result = [{'nlp': 2, 'is': 2, 'a': 1, 'subfield': 1, 'of': 1, 'ai': 1, 'and': 1, 'widely': 1, 'used': 1},
               {'count': 1, 'the': 1, 'word': 1, 'frequency': 2, 'and': 1, 'build': 1, 'a': 1, 'dictionary': 1},
               {'this': 3, 'task': 3, 'is': 3, 'not': 1, 'hard': 1, 'ovewhelming': 1, 'fun': 1}]

result = [solution(text) for text in test_data]

print(result)

if result == test_result:
    print('Correct!')
else:
    print('Improve')
