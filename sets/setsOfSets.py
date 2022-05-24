# Sets can have multiple sets eg

set1 = {{1,2}, {3,4}}
# Above results in TypeError: unhashable type:'set'

# Use frozenset instead
set2 = {frozenset({1,2}), frozenset({3,4})}
