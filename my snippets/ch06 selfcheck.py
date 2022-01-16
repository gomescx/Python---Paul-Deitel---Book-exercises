#%%
# 06-02-02 Creating a dictionary of states
# ======================================================
from random import random
from typing import Counter


states = {'ACT': 'Australian Capital Territory', 'NSW': 'New South Wales', 'VIC': 'Victoria'}
print(states)

#%%
# 06-02-04 Transforming dictionary into lists
# ========================================================
roman_numerals = {'I': 1, 'II':2, 'III':3, "V": 5,}
roman_keys = list(roman_numerals.keys())
roman_values = list(roman_numerals.values())
roman_items = list(roman_numerals.items())
print(f'keys {roman_keys}')
print(f'values {roman_values}')
print(f'items {roman_items}')
# %%
# 06-02-07 Counter function for summarizing
# ========================================================
import random
from collections import Counter
numbers = [random.randrange(1, 6) for i in range(1,51)]
summarization = Counter(numbers)
for x, y in sorted(summarization.items()):
    print(f'Number {x} = {y} occurrences ')
# %%
# 06-02-09 Dictionary comprehensions
# ========================================================
cubes_dict = {x: x ** 3 for x in range(1,6)}

# %%
# 06-03 Sets
# ========================================================
text = 'to be or not to be that is the question'
words = text.split()
words_set = set(words)
for word in sorted(words_set):
    print(word, end = ' ')

# %%
# 06-03-02 Sets comparisons and operators
# good source at https://betterprogramming.pub/mathematical-set-operations-in-python-e065aac07413
# ========================================================
my_set1 = {10,20,30}
my_set2 = {5,10,15,20}
print(f'30 -> {my_set1 - my_set2}')
print(f'5, 15, 30 -> {my_set1.symmetric_difference(my_set2)}')
print(f'5, 10, 15, 20, 30 -> {my_set1.union(my_set2)}')
print(f'10, 20 -> {my_set1.intersection(my_set2)}')

# %%
