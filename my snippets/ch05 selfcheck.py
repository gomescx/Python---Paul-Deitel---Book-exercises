#%%
# 05-02 3. cube_list function to cube each element of a list
# ====================================================

def cube_list(mylist):
    for i in range(0,len(mylist)):  
        mylist[i] = mylist[i] ** 3  
    return mylist 

numbers = []
for i in range(1,11):
    numbers += [i]

numbers = cube_list(numbers)

## Comments:
#  - parameters in functions are passed as the variable itself. Changes to the parameters reflect in the underlying variable
#  - Assignment operators go beyond arythmetic + - * / **= is also valid.

# Alternative the code above could be replaced by the one below
# def cube_list(mylist):
#     for i in range(0,len(mylist)):  
#          mylist[i] **= 3  
# numbers = []
# for i in range(1,11):
#     numbers += [i]

# cube_list(numbers)

#%%
# 05-02 4. Turning a string into a list of individual characters
# ========================================================
my_string = "Birthday"
my_list = []
for character in my_string:
    my_list += [character]

## Comments:
# - a string is actually a list of individual characters therefore I don't need to use a for loop
#   either lines of codes below will suffice
#   my_list += "Birthday" 
#   my_list += my_string


#%%
# 05-03 3. Single element tuple
my_tuple = (123.45,)

# 05-03 4. Concatenating different types of sequences tuple & list
my_list = [1, 2, 3]
my_tuple = (4, 5, 6)
my_concat = my_list + my_tuple



# %%
# 05-04 3. Unpacking a tuple

high_low = 'Monday', 32, 21
print(f' {high_low[0]} {high_low[1]} {high_low[2]}')

day, high, low = high_low

# 05-04 4. enumerate function
my_list = ['Amy', 'Claudio', 'Kate']

for i, name in enumerate(my_list):
    print(f'{i} {name}')

# %%
# 05-05 3 Working with Slices
# a.
#   more elegant than the below is numbers = list(range(1,16)) 
numbers = []
for i in range(1,16):
    numbers += [i]
numbers[1::2]

print(f'a. {numbers}')

# b.
numbers[5:10] = [0] * 5
print(f'b. {numbers}')
# c.
numbers = numbers[:5] # or alternatively numbers[5:] = []
print(f'c. {numbers}')
# d.
numbers = []
print(f'd. {numbers}')
# %%
# 05-06 DEL statement for lists
# ================================
numbers = list(range(1,16))
del numbers[:4]
print(f'a. {numbers}')

del numbers[::2]
print(f'b. {numbers}')

# %%
# 05-09 Finding elements in a list
# ================================
def index_safe(numbers, value):
    if value in numbers:
        print(f'The value {value} is in position {numbers.index(value)}')
    else:
        print(f'The value {value} is not present in {numbers}')


numbers = [67, 12, 46,43,13]
index_safe(numbers, 43)
index_safe(numbers, 44)

# %%
# 05-10 List methods
# ================================
rainbow = ['green', 'orange', 'violet']

rainbow.insert(rainbow.index('violet'),'red')
print(rainbow)
rainbow.append('yellow')
print(rainbow)
rainbow.reverse()
print(rainbow)
rainbow.remove('orange')
print(rainbow)

# %%
# 05-12 List Compreheensions
# ================================
cubes_tuples_list = [(i, i **3) for i in range(1,6)]
multiples3 = [ i for i in range(1,31) if i % 3 == 0]
# %%
# 05-13 Generator expressions
# ================================
numbers = [10,3,7,1,9,4,2]
cube_list = list( item ** 3 for item in numbers if item % 2 == 0 )
# %%
# 05-14 Lambda expressions
# ================================
numbers = list(range(1,16))
numbers_even = list( filter(lambda x: x % 2 == 0, numbers) )
numbers_square = list(map(lambda x: x ** 2, numbers))
numbers_even_squared = list( map(lambda x: x ** 2, filter( lambda y: y % 2 == 0, numbers)))

temperatures_fh = [41,32,212]
temperatures_fh_cel = list(map(lambda fh: (fh, (fh - 32)*5/9 ), temperatures_fh))
# %%
# 05-15 String sequence processing functions and Zip
# ==================================================
foods = ['Cookies', 'pizza', 'grapes', 'Steak', 'apples', 'Bacon']
print(f'Without Lambda {min(foods)}')
print(f'With Lambda {min(map(lambda x: x.lower(), foods)) }') 
# using the key function simplifies it as per below 
print(min(foods, key = lambda x: x.lower()))

# zip to add 2 lists
numbers_even = list(range(2,16,2))
numbers_odd = list(range(1,16,2))

[(x, y, z, y + z)  for x, y, z in zip(range(16), numbers_even, numbers_odd) ]

# %%
