#%%
import numpy as np
from matplotlib import pyplot

def sub_error(n):
    return abs(n / 7 / 10 * 7 - n / 10)

def next_error(start):
    while True:
        if sub_error(start)>0:
            print(start)
            return sub_error(start)
        start+=1

R = np.arange(15)
X = 10.0 ** R
Y = np.array([ next_error(x) for x in X ])

#%%
pyplot.plot(X, Y)
pyplot.yscale('log')
pyplot.xscale('log')
pyplot.show()

#%%
