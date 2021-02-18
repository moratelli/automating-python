import pprint

message = 'It was a bright cold day in April, and the clocks were striking thirtheen'
count = {}

for character in message.upper():
    count.setdefault(character, 0)
    count[character] = count[character] + 1

pprint.pprint(count)
result = pprint.pformat(count)
print(result)
