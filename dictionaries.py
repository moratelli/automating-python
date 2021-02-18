my_cat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud'}
print(my_cat['size'])

spam = {12345: 'Luggage combination', 42: 'The Answer'}
spam2 = {42: 'The Answer', 12345: 'Luggage combination'}
print(spam == spam2)

print('size' in my_cat)
print('size' not in my_cat)

eggs = {'name': 'Panda', 'species': 'cat', 'age': 3}

print(list(eggs.keys()))
print(list(eggs.values()))
print(list(eggs.items()))

for k in eggs:
    print(k)

for v in eggs.values():
    print(v)

for k, v in eggs.items():
    print(k, v)

for i in eggs.items():
    print(i)

print(eggs.get('age', 0))

eggs.setdefault('color', 'black')
