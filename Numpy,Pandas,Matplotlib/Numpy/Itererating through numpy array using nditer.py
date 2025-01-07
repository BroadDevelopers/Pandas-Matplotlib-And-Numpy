import numpy as np
a= np.arange(12).reshape(3,4)
print(a)

"""
iterating through the array using for loop
"""
for row in a:
    print(row)
"""
iterating through each element one by one
using another for loop
"""
for row in a:
    for cell in row:
        print(cell)

"""
flattening this array into a list using
flatten function without 2 for loops
"""
for cell in  a.flatten():
    print(cell)

"""
numpy offers nditer whichc allows more
sophisticated way of iteration
"""
#achiving same goal as flatten using nditer
#nditer take two arguements(array,order) c odred is row by tow
for x in np.nditer(a,order='C'):
    print(x)
#Fortran order uses column iteration
for x in np.nditer(a,order='F'):
    print(x)
#lets say you want to print each individual column
#you can use flags
for x in np.nditer(a,order='F',flags=['external_loop']):
    print(x)

#readwrite op-flags
#lets say you are iterating through the arrau and
#you want to modify the elements
#lets say we want to find the square of each element of the array
#and update the array
for x in np.nditer(a, op_flags=['readwrite']):
    x[...]=x*x
print(a)

#iterating through two a and b arrays simultanuously
b = np.arange(3,15,4).reshape(3,1)
print(b)

for x,y in np.nditer([a,b]):
    print(x,y)