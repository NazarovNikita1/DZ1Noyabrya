def solution(a, b):
    """
    Программа принимает на вход две переменные (a, b) и меняет местами их значения
    """
    a, b = b, a
    return a, b

test_data = [(5, 10),
             ('cat', 'dog'),
             ({'name': 'John', 'surname': 'Doe'}, {'name': 'John', 'surname': 'Smith'})]
test_result = [(10, 5),
               ('dog', 'cat'),
               ({'name': 'John', 'surname': 'Smith'}, {'name': 'John', 'surname': 'Doe'})]

result = [solution(x, y) for x, y in test_data]

print(result)

if result == test_result:
    print('Correct!')
else:
    print('Improve')

