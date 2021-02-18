import re

agent_names_regex = re.compile(r'Agent \w+')
print(agent_names_regex.findall('Agent Alice gave the secret documents to Agent Bob.'))
# sub() == find and replace
print(agent_names_regex.sub('REDACTED', 'Agent Alice gave the secret documents to Agent Bob.'))

agent_names_regex = re.compile(r'Agent (\w)\w*')  # using groups to get part of the original string
print(agent_names_regex.findall('Agent Alice gave the secret documents to Agent Bob.'))
print(agent_names_regex.sub(r'Agent \1****', 'Agent Alice gave the secret documents to Agent Bob.'))

re.compile(r'''
\d\d\d   # area code
-
\d\d\d   # first 3 digits
-
\d\d\d\d''', re.VERBOSE)  # verbose lets us use huge regex strings and add comments
