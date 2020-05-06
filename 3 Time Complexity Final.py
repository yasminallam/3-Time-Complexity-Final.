#!/usr/bin/env python
# coding: utf-8

# In[1]:


# import symbolic capability to Python
from sympy import *
from sympy.abc import *
from sympy.plotting import plot
from IPython.display import display
# print things all pretty
init_printing()


# # Size of the problem: n 

# In[2]:


n = symbols("n", positive=True, real=True)


# # Different Functions f with different Time complexity

# In[3]:


f_constant = 20
f_linear = 4 * n + 10
f_linear2 = 10 * n +1
f_quadratic = 1/4 * n**2 + 1/2*n +1 
f_quadratic2 = 1/8 * n**2 


# # Definition of Order of Growth (O) ("Big O")
# 
# Order of growth (O) is a set of functions whose asymptotic growth behavior is considered equivalent:
# 
# Two functions f(n) and g(n) have the equivalent order of growth if $\displaystyle \lim_{n \rightarrow \infty} \frac{f(n)}{g(n)} = c$ with $c > 0$ and $c < \infty $.
# 
# 
# f(n) has a higher order of growth than g(n) if
# $\displaystyle \lim_{n \rightarrow \infty} \frac{f(n)}{g(n)} = \infty $.
# 
# f(n) has a smaller order of growth than g(n) if $\displaystyle \lim_{n \rightarrow \infty} \frac{f(n)}{g(n)} = 0 $.
# 
# $f(n) \in O(g(n))$ if $\displaystyle \lim_{n \rightarrow \infty} \frac{f(n)}{g(n)} = c$ with $c < \infty $.

# # Test Order of Growth with the Sympy limit function

# In[4]:


limit(f_quadratic / f_quadratic2, n, oo)


# In[5]:


limit(f_quadratic / f_linear, n, oo)


# In[6]:


limit( f_linear2 / f_quadratic2, n, oo)


# # Plotting Time Complexity

# In[7]:


expr_range = (n,0,30)
p = plot(
    f_constant,
    f_linear,
    f_quadratic,
    expr_range,
    show = False,
    legend = True
);

p[0].line_color = 'g'
p[1].line_color = 'b'
p[2].line_color = 'r'



p[0].label = 'constant'
p[1].label = 'linear'
p[2].label = 'quadratic'

p.show()


# # Crossover point

# In[8]:


e1 = Eq(f_quadratic, f_linear)
e1


# In[9]:


solve(e1, n)


# In[10]:


solve(e1, n)[0].evalf()


# # Todo

# In[11]:


# TODO: Define 
# - a logarithmic function
# - a log-linear (n log n) function
# - a cubic function
# - an exponential function
# - a factorial function


# In[12]:


# - a logarithmic function
data = [1, 2, 9, 8, 3, 4, 7, 6, 5]
def logarithmic (x):
    for index in range(0, len(data), 3):
        print(data[index])
        
logarithmic (data)


# In[13]:


# - a log-linear (n log n) function .. mergesort algorithm

def log_linear(data):
    if len(data) <= 1:
        return
    
    mid = len(data) // 2
    left_data = data[:mid]
    right_data = data[mid:]
    
    log_linear(left_data)
    log_linear(right_data)
    
    left_index = 0
    right_index = 0
    data_index = 0
    
    while left_index < len(left_data) and right_index < len(right_data):
        if left_data[left_index] < right_data[right_index]:
            data[data_index] = left_data[left_index]
            left_index += 1
        else:
            data[data_index] = right_data[right_index]
            right_index += 1
        data_index += 1
    
    if left_index < len(left_data):
        del data[data_index:]
        data += left_data[left_index:]
    elif right_index < len(right_data):
        del data[data_index:]
        data += right_data[right_index:]
    
data_merge = [9, 1, 7, 6, 2, 8, 5, 3, 4, 0]
log_linear(data_merge)
print(data_merge)
    


# In[14]:


# - a cubic function

from sympy import symbols

def cubic(x):
    return 3*x**3 + 2*x**2 + 7*x + 1

x = symbols('x')

print(cubic(x))           
print(cubic(x).subs(x, 5))


# In[15]:


# - an exponential function
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)


# In[16]:


# - a factorial function
data_heap = [1, 2, 3]

def heap_permutation(data, n):
    if n == 1:
        print(data)
        return
    
    for i in range(n):
        heap_permutation(data, n - 1)
        if n % 2 == 0:
            data[i], data[n-1] = data[n-1], data[i]
        else:
            data[0], data[n-1] = data[n-1], data[0]
    
heap_permutation(data_heap, len(data_heap))


# In[17]:


# - a quadratic function 

data = [1, 2, 9, 8, 3, 4, 7, 6, 5]
def quadratic_2 (x):
    for x in data:
        for y in data:
            print(x, y)
quadratic_2(data)


# In[18]:


# TODO create multiple plots with different combinations of functions
# TODO create a log-log plot with your factorial, exponential, quadratic, log-linear, and linear function

# calling all functions in one function 
def all_functions():
    items = [10, 50, 100, 200, 300, 400, 600, 800]
    logarithmic(items)
    log_linear(items)
    quadratic_2(items)
    


# In[ ]:


import random 
import matplotlib.pyplot as plt
list_of_n = [50, 100, 200, 300, 400, 500, 600, 700, 800, 900]
value = -1
measures = []
for n in list_of_n:
    value = n+1
    items = [int(random.random()*n) for _ in range(n)]
    items = sorted(items)
    time = get_ipython().run_line_magic('timeit', '-o all_functions')
    measures.append((n, time.average))
plt.plot(*zip(*measures))
plt.ylim(ymin=0)
plt.show()


# In[ ]:


# TODO Calculate one crossover point for two functions

