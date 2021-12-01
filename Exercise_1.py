'''
Write a function that takes as arguments a numpy array, v and a tuple of two numbers a and b (with b >= a).
the function will return a Numpy array that contains all the values in v that are in the interval [a,b] (notice the inclusion).

example: input1 = np.array([1,2,3,4,5,6]), input2 = (1,5), output = np.array([1,2,3,4,5])
Provide examples to showcase that the functions works.

Weight: 1
'''

import numpy as np
def out(v,a,b):
    x = np.arange(int(v))
    y = x [a:b+1:1]
    return y

v = input()
a = int(input())
b = int(input())
print(out(v,a,b))
