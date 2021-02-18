import re

message = 'Call me at 415-555-1011 tomorrow, or at 415-555-9999 for the office line'

phone_num_regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
match_object = phone_num_regex.search(message)  # finds first, returns an object
print(match_object.group())
print(phone_num_regex.findall(message))  # returns a list with all matches

phone_num_regex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')  # () == groups
match_object = phone_num_regex.search(message)  # finds first, returns object
print(match_object.group())  # returns all groups in a string
print(match_object.group(1))  # returns the first group
print(match_object.group(2))  # returns the second group


phone_num_regex = re.compile(r'\(\d\d\d\) \d\d\d-\d\d\d\d')
match_object = phone_num_regex.search('My number is (415) 555-4242')
print(match_object.group())


bat_regex = re.compile(r'Bat(man|mobile|copter|bat)')  # | == or
match_object = bat_regex.search('Batmobile lost a wheel')
print(match_object.group())
print(match_object.group(1))


bat_regex = re.compile(r'Bat(wo)?man')  # ? == appears 0 or 1 time
match_object = bat_regex.search('The Adventures of Batman')
print(match_object.group())
match_object = bat_regex.search('The Adventures of Batwoman')
print(match_object.group())
match_object = bat_regex.search('The Adventures of Batwowowowoman')
print(match_object is None)


phone_regex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')  # using ()? as optional input
match_object = phone_regex.search('My number is 415-555-4242')
print(match_object.group())
match_object = phone_regex.search('My number is 555-4242')
print(match_object.group())


bat_regex = re.compile(r'Bat(wo)*man')  # * == appears 0 or more times
match_object = bat_regex.search('The Adventures of Batman')
print(match_object.group())
match_object = bat_regex.search('The Adventures of Batwoman')
print(match_object.group())
match_object = bat_regex.search('The Adventures of Batwowowowoman')
print(match_object.group())


bat_regex = re.compile(r'Bat(wo)+man')  # + == appears 1 or more times (must appear once)
match_object = bat_regex.search('The Adventures of Batman')
print(match_object is None)
match_object = bat_regex.search('The Adventures of Batwoman')
print(match_object.group())
match_object = bat_regex.search('The Adventures of Batwowowowoman')
print(match_object.group())


ha_regex = re.compile(r'(Ha){3}')  # {x} == repeats itself x number of times
match_object = ha_regex.search('He said "HaHaHa"!')
print(match_object.group())


# area code optional, comma/comma+space optional, repeats itself in the text 3 times
phone_regex = re.compile(r'((\d\d\d-)?\d\d\d-\d\d\d\d(,)?(, )?){3}')
match_object = phone_regex.search('My numbers are 415-555-1234,415-555-4242,212-555-0000')
print(match_object.group())
match_object = phone_regex.search('My numbers are 415-555-1234, 415-555-4242, 212-555-0000')
print(match_object.group())


ha_regex = re.compile(r'(Ha){3,5}')  # {x,y} == repeats itself a min of x times and a max of y times
match_object = ha_regex.search('He said "HaHaHa"!')
print(match_object.group())


digit_regex = re.compile(r'(\d){3,5}')  # has 3 to 5 digits (max range)
match_object = digit_regex.search('1234567890')
print(match_object.group())  # matches the first 5 (greedy match [default])
digit_regex = re.compile(r'(\d){3,5}?')  # has 3 to 5 digits (low range)
match_object = digit_regex.search('1234567890')
print(match_object.group())  # matches the first 3 (non-greedy match)
