## Code to demonstrate greedy matching. Takes everything from specified parameters to the extra unspecified parameters
## with the same properties

#import regular expression module
import re

x = "Example: A sentence with a collon: period!"

y = re.findall('^E.+:', x)

print(y)