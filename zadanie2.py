def solution(name):
    """
    Программа принимает на вход имена, записанные в нижнем регистре,
    и возвращает те же имена, написанные с большой буквы
    """
    capitalized_name = name.capitalize()
    return capitalized_name

test_data = ['john', 'mary', 'samantha']
test_result = ['John', 'Mary', 'Samantha']

result = [solution(name) for name in test_data]

print(result)

if result == test_result:
    print('Correct!')
else:
    print('Improve!')

