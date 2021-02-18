import re

lyrics = '12 drummers drumming, 11 pipers piping, 10 lords a leaping, 9 ladies dancing, 8 maids a milking, 7 swans a swimming, 6 geese a laying, 5 gold rings, 4 calling birds, 3 french hens, 2 turtle doves and a partridge in a pear tree'

xmas_regex = re.compile(r'\d+\s\w+')  # 1 or more digit, 1 space, 1 or more letters
print(xmas_regex.findall(lyrics))

vowel_regex = re.compile(r'[aeiouAEIOU]')  # find these characters (also supports ranges -- [a-z])
print(vowel_regex.findall('Robocop eats baby food.'))

double_vowel_regex = re.compile(r'[aeiouAEIOU]{2}')
print(double_vowel_regex.findall('Robocop eats baby food.'))

consonants_regex = re.compile(r'[^aeiouAEIOU]')  # ^ == not. find everything EXCEPT these characters
print(consonants_regex.findall('Robocop eats baby food.'))

begins_with_hello_regex = re.compile(r'^Hello')  # string needs to BEGIN with Hello
match_object = begins_with_hello_regex.search('Hello there!')
print(match_object.group())
match_object = begins_with_hello_regex.search('He said "Hello!".')
print(match_object is None)


ends_with_world_regex = re.compile(r'world!$')  # string needs to END with world!
match_object = ends_with_world_regex.search('Hello world!')
print(match_object.group())
match_object = ends_with_world_regex.search('Hello worldasdasdasdd!')
print(match_object is None)

# ˆ...$ == begins and ends with this pattern (exact text). finds one digit or more.
all_digits_regex = re.compile(r'^\d+$')
match_object = all_digits_regex.search('1298731280')
print(match_object.group())
match_object = all_digits_regex.search('129873x1280')
print(match_object is None)

at_regex = re.compile(r'.at')  # . == wildcard. find any character except a new line
print(at_regex.findall('The cat in the hat sat on the flat mat.'))

name_regex = re.compile(r'First Name: (.*) Last Name: (.*)')  # .* finds anything
print(name_regex.findall('First Name: Pedro Last Name: Moratelli'))

prime_directives = 'Serve the public trust.\nProtect the innocent.\nUphold the law.'
dot_star_regex = re.compile(r'.*', re.DOTALL)  # finds everything, including new lines
match_object = dot_star_regex.search(prime_directives)
print(match_object.group())

vowel_regex = re.compile(r'[aeiou]', re.IGNORECASE)  # matches upper and lower case (also found as re.I)
print(vowel_regex.findall('Alberto Ulisses'))
