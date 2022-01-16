# %%
# 07-02 Intro to numpy array
import numbers
from timeit import timeit
import numpy as np
even_array = np.array([x for x in range(2,21,2)])
odd_array = np.array(([x for x in range(2,11,2)], [x for x in range(1,11,2)]))

# %%
# 07-05 numpy array arange and reshape
numbers = np.arange(2,41,2).reshape(4,5)

# %%
# 07-03 Numpy random and Timing processing 
import numpy as np
# import random
# print('random.randrange(1,7) for i in range(1, 6_000_000)')
# %timeit rolls_array = [random.randrange(1,7) for i in range(1, 6_000_000)]

# print('np.random.randint(1, 7, 6_000_000)')
# %timeit -r7 -n1 rolls_array = np.random.randint(1, 7, 6_000_000)

# print('np.random.randint(1, 7, 6_000_000_000)')
# %timeit -r7 -n1 rolls_array = np.random.randint(1, 7, 6_000_000_000)

# print('np.random.randint(1, 7, 6_000_000_000_000)')
# %timeit -r7 -n1 rolls_array = np.random.randint(1, 7, 6_000_000_000_000)

%timeit sum([x for x in range(10_000_000)])

%timeit np.arange(10_000_000).sum()

# %%
# 07-07 ndarray operations 
# =========================
# import numpy as np
numbers = np.arange(1,6)
print(numbers ** 2)

# %%
# 07-08 numpy array statistics
# =============================
# import numpy as np
grades = np.array([np.random.randint(60,101) for x in range(12)]).reshape(3, 4)
grades_class = grades.mean()
grades_subject = grades.mean(axis= 1)
grades_student = grades.mean(axis= 0)

# %%
# 07-10 numpy array slice and dice
# =============================
import numpy as np
numbers = np.arange(1,16).reshape(3,5)
print(f'whole matrix \n {numbers}')
print(f'2nd row {numbers[1]}')
print(f'1st & 3rd rows {numbers[[0,2]]}')
print(f'middle 3 columns \n{numbers[:,1:4]}')


# %%
# 07-13 numpy array stacking (horizontal and vertical)
# =============================
numbers = np.arange(1,7).reshape(2,3)
v_stacked = np.vstack((numbers,numbers))
hv_stacked = np.hstack((v_stacked,v_stacked))

# %%
# 07-14 Pandas series conversion from arrays
# =============================
import numpy as np
import pandas as pd
temperatures = np.random.randint(60,101,5)
pd_temperature = pd.Series(temperatures)

# %%
# 07-14.2 Pandas series manipulation and conversion from dictionary 
# =============================
import pandas as pd

temps = {'Mon': [68, 89], 'Tue': [71, 93], 'Wed': [66, 82],
         'Thu': [75, 97], 'Fri': [62, 79]}
temperatures = pd.DataFrame(temps, index=['Low', 'High'])
print(temperatures.loc[:, ['Mon','Tue','Wed']])
print(temperatures.loc['Low'])
pd.set_option('display.precision',2)
print('each day avg ',temperatures.mean()) 
print('Low / High avg', temperatures.T.mean()) 

