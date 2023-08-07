import pandas as pd
import numpy as np
# # Creating empty series 
# ser=pd.Series()
# print("normal series",ser)
# # simple array 
# data=np.array(['g','r','e','e','k','s'])
# ser = pd.Series(data)
# print(ser)
 
# Calling DataFrame constructor
# df=pd.DataFrame()
# print(df)
# # list of strings
# data=['greeks','for','greeks']
# # Calling DataFrame constructor on list 
# df=pd.DataFrame(data)
# print(df)

#single decorator
#=========================
# def extra_func(func):
#     def inner(x,y):
#         if x%2==0 and y%2==0:
#             func(x,y)
#     return inner
# @extra_func
# def sum(a,b):
#     print(a+b)
# sum(10,20)

#chaining Decorators
#==========================
# def extra_func1(func):
#     def inner(x):
#         x1 = func(x)
#         n = 1
#         if x1 >= 1:
#             n = n * x1
#             x1 = x1 - 1
#         print("Factorial:", n)
#         return x1  # Corrected to return x1 instead of r
#     return inner

# @extra_func1
# def display(a):
#     print("this is a", a)
#     return a  # Added a return statement in the original function

# display(5)

#chaining decorator with parameters
# First decorator to calculate the square of a number
def square_decorator(func):
    def inner(x):
        result = func(x)
        return result ** 2
    return inner
# Second decorator to calculate the cube of a number
def cube_decorator(func):
    def inner(x):
        result = func(x)
        return result ** 3
    return inner
# Applying both decorators to the display function
@square_decorator
@cube_decorator
def display(a):
    return a

# Calling the decorated function
result = display(3)
print("Result:", result)


