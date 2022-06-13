## Code to demonstrate the way python matches data ungreedily

import re


x = "Example: A sentence with a collon: period!"

# use a question mark in the regex
y = re.findall('^E.+?:', x)

print(y)