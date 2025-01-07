"""
Slicing/Stacking and indexing with boolean
arrays
Topics:
1.Indexing and Slicing
2.Iterating through arrays
3.Stacking together two arrays
4.indexing with boolean arrays
"""

"""
Indexing And Slicing
"""
#indexing
import numpy as np
a=np.array([6,7,8])
print(a[0:2])
print(a[-1])

"""
working with multidimensional array
"""
b=np.array([[6,7,8],[1,2,3],[9,3,2]])
print(b)
print(b[1,2]) #1 is a row 2 is a  second element/column in that row
print(b[0:2,2])#0:2 it will go to the first row as the last element is not included
#  , 2 will print the second elements of 0 and 1 row
print(b[-1]) #the last elemnt/row
print(b[-1,0:2])
# let say you want to fo through all the rows and print coloumn 1 and 2
print(b[:,1:3])#: goes through all the rows

'''
ITERATING THROUGH AN ARRAT
'''
c=np.array([[6,7,8],[1,2,3],[9,3,2]])
for row in c:
    print(row)

#flattening the list and print every cell using flat function
for cell in c.flat:
    print(cell)

#Stacking two arrays together
d=np.arange(6).reshape(3,2)
e=np.arange(6,12).reshape(3,2)
print(d)
print(e)
#vertical stacking
print(np.vstack((d,e)))
#Horizontal stacking
print(np.hstack((d,e)))

#Horizontal Split
f=np.arange(30).reshape(2,15)
print(f)
#vertivally splitting/slicing this array into 3 equal parts
print(np.hsplit(f,3))
#its kind of hard to visualiza these array so we are going to store them
#into variables
result = (np.hsplit(f,3))
print(result[0])
print(result[1])
print(result[2])
#you can also do the same thing with a vertical split
result2=(np.vsplit(f,2))
print(result2[0])
print(result2[1])

#4 indexing with boolean arrays
g = np.arange(12).reshape(3,4)
print(g)

#boolean array
i = g>4
print(i)
#or this looks at i array and returns the values for True
print(g[i])
#useful for extracting elemets >4
#useful for replacing those elements with a certain number
#eg
g[i]=-1
print(g)