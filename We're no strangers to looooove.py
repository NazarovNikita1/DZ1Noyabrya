def solution(text):

    vowels = [char for char in text if char in 'aeiouAEIOU']

    #Создаем пустой словарь для подсчета гласных
    vowels_dict = {}

    for vowel in vowels:
        if vowel in vowels_dict:
            vowels_dict[vowel] += 1
        else:
            vowels_dict[vowel] = 1

    return vowels_dict

test_data = ['Never gonna give you up',
             'Never gonna let you down',
             'Never gonna run around and desert you']
test_result = [{'e': 3, 'o': 2, 'a': 1, 'i': 1, 'u': 2},
               {'e': 3, 'o': 3, 'a': 1, 'u': 1},
               {'e': 4, 'o': 3, 'a': 3, 'u': 3}]

result = [solution(text) for text in test_data]

print(result)

if result == test_result:
    print('Correct!')
else:
    print('Improve')
