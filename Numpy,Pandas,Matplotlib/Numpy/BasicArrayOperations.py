import numpy as np
a=np.array([5,6,9])
print(a[0])

#2D array
b=np.array([[1,2],[3,4],[5,6]])
#ndim used to print dimensions
print(b.ndim)
#itemsize prints byte size  integers occupy 4 bites
print(b.itemsize)
print(b.dtype)
#initializing the same array with a different data type
b=np.array([[1,2],[3,4],[5,6]], dtype=np.float64)
print(b.itemsize)
#64 meanss it occupies 8 bites
print(b)
#size shoes the total number of elements
print(b.size)
#shape represents the information on dimensions
print(b.shape)
#using dtype to initialize array with a specific data type
c=np.array([[1,2],[3,4],[5,6]], dtype=complex)
print(c)
#initializing array with all zeros
d=np.zeros((3,4))
e=np.ones((3,4))
print(d)
print(e)
#using a function used similar to range
print(np.arange(1,5))
#printng array of range with steps of 2 numbers
print(np.arange(1,5,2))
#using lean space funtion(startnumber,stopnumber,numbers to generate)
#it will generate ten numebers beteen 1 and 5 which are linearrly spaced
print(np.linspace(1,5,10))
print(np.linspace(1,5,5))
#reshaping dimensions of an array
f=np.array([[1,2],[3,4],[5,6]])
print(f)
print(f.reshape(2,3))
#revel function to make array one dimensonal
print(f.ravel())
#mathematcal funtion of numpy ray
print(f.min())
print(f.max())
print(f.sum())
#concept of axis in numpy array
#axis mean dimens
#axis 0=coloums
#axis 1=rows
print(f.sum(axis=0))
print(f.sum(axis=1))
#squareroot
print(np.sqrt(f))
#standar diviation
print(np.std(f))