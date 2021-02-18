import re

# Create a regex for phone numbers
phone_regex = re.compile(r'''
(
((\d{3})|(\(\d{3}\)))?    # area code (optional)
(\s|-)                    # first separator
\d{3}                     # first 3 digits
-                         # separator
\d{4}                     # last 4 digits
(((ext(\.)?\s)|x)         # extension word-part (optional)
(\d{2,5}))?               # extension number-part (optional)
)
''', re.VERBOSE)
extracted_phone = phone_regex.findall("415-555-0000, 555-0000,(415) 555-0000, 555-0000 ext 12345")
print(extracted_phone)

# Create a regex for email addresses
email_regex = re.compile(r'\S+@\S+')
extracted_email = email_regex.findall('''pedro@moratelli.dev
shyann.bashirian@yahoo.com
arturo.thompson@cassin.net
molson@haag.com
''')
print(extracted_email)

all_phone_numbers = []
for phone_number in extracted_phone:
    all_phone_numbers.append(phone_number[0])

results = '\n'.join(all_phone_numbers) + '\n' + '\n'.join(extracted_email)
print(results)
