import numpy as np
def out(v,a,b):
    x = np.arange(int(v))
    y = x [a:b+1:1]
    return y

v = input()
a = int(input())
b = int(input())
print(out(v,a,b))
