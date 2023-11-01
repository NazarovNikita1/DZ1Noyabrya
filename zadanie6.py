def solution(price_list):
    items_list = []

    for item, price in price_list.items():
        item_string = f'{item}: ${price:.2f}'
        items_list.append(item_string)

    return items_list

test_data = [{'Apples': 2.48, 'Bananas': 1.99, 'Bread': 3.49},
             {'Dress': 9.78, 'Pants': 19.96},
             {'Ball': 1.33, 'Doll': 1.99, 'Car': 3.50}]
test_result = [['Apples: $2.48', 'Bananas: $1.99', 'Bread: $3.49'],
               ['Dress: $9.78', 'Pants: $19.96'],
               ['Ball: $1.33', 'Doll: $1.99', 'Car: $3.50']]

result = [solution(price_list) for price_list in test_data]

print(result)

if result == test_result:
    print('Correct!')
else:
    print('Improve')
