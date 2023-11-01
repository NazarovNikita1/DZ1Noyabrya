def solution(text):
    words = text.lower().split()

    unique_tokens = set(words)

    return unique_tokens

test_data = ['NLP is the future of AI and the future is now',
             'Count the word frequency to build a frequency dictionary',
             'This task is not hard this task is fun']
test_result = [{'the', 'is', 'and', 'now', 'of', 'ai', 'nlp', 'future'},
               {'the', 'count', 'dictionary', 'frequency', 'a', 'build', 'to', 'word'},
               {'hard', 'is', 'task', 'not', 'this', 'fun'}]

result = [solution(text) for text in test_data]

print(result)

if result == test_result:
    print('Correct!')
else:
    print('Improve')
