
# coding: utf-8

# In[ ]:

from statistics import mean


# In[ ]:

import numpy as np


# In[ ]:

import matplotlib.pyplot as plt


# In[ ]:

from matplotlib import style


# In[ ]:

style.use('fivethirtyeight')


# In[ ]:

xs = np.array([1,2,3,4,5,6], dtype=np.float64)


# In[ ]:

ys = np.array([5,4,6,5,6,7], dtype=np.float64)


# In[ ]:

def best_fit_slop_and_intercept(xs,ys):
    
    m= ( ((mean(xs)*mean(ys)) - (mean(xs*ys)) ) / ((mean(xs)**2) - (mean(xs**2))) )
    b= ( mean(ys) - m*mean(xs) )
    return m, b


# In[ ]:

def squared_error(ys_orig, ys_line):
    return sum((ys_line - ys_orig)**2)


# In[ ]:

def coefficient_of_determination(ys_orig,ys_line):
    y_mean_line= [mean(ys_orig) for y in ys_orig]
    squared_error_regr= squared_error(ys_orig, ys_line)
    squared_error_y_mean= squared_error(ys_orig, y_mean_line)
    return 1 - (squared_error_regr / squared_error_y_mean)


# In[ ]:

#y_mean_line= [mean(ys) for y in ys]


# In[ ]:

m,b = best_fit_slop_and_intercept(xs,ys)


# In[ ]:

print(m,b)


# In[ ]:

regression_line = [(m*x)+b for x in xs]
#regression_line


# In[ ]:

r_squared= coefficient_of_determination(ys,regression_line)
r_squared


# In[ ]:

predict_x=8
predict_y= (m*predict_x)+b


# In[ ]:

plt.scatter(xs,ys)


# In[ ]:

plt.plot(xs,regression_line)


# In[ ]:

plt.scatter(predict_x,predict_y,color='g')


# In[ ]:

plt.show()

