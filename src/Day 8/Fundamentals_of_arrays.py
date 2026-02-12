import numpy as np
a=np.array([[1,2,3],[4,5,6]])
b=np.array([10,20,30])
result=a+b
print(result)

#broadcasting and vectorization
import numpy as np
a = np.array([[1, 2, 3],
              [4, 5, 6]])
b = np.array([10, 20, 30])
result = a + b
print(result)
# Vectorized vs Loop example
arr = np.random.rand(1000000)
# Vectorized
squared = arr ** 2

#array manipulation
arr = np.arange(12)
reshaped = arr.reshape(3, 4)
print(reshaped)

a = np.array([[1, 2]])
b = np.array([[3, 4]])

vstacked = np.vstack((a, b))
print(vstacked)


#hstack
a=np.array([[1,2],
            [3,4]])
b=np.array([[5,6],
            [7,8]])
print(np.stack((a,b)))


#statistcal function in numpy
data=np.array([[10,20,30],
               [40,50,60]])
print(np.mean(data))
print(np.mean(data,axis=0))

#matrix multiplication
A=np.array([[1,2],
           [3,4]])
B=np.array([[5,6],
            [7,8]])
print(np.dot(A,B))


