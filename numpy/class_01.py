import numpy as np

# 1.1.1 Creating a 1D array
a = np.array([1, 2, 3, 4, 5])
print("1D array:", a)

# 1.1.2 Creating a 2D array
b = np.array([[1, 2, 3], [4, 5, 6]])
print("2D array:", b)
# 1.1.3 Creating a 3D array
c = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print("3D array:", c)
# 1.1.4 Creating a 4D array
d = np.array([[[[1, 2], [3, 4]], [[5, 6], [7, 8]]]])
print("4D array:", d)
# 1.1.5 Creating a 5D array
e = np.array([[[[[1, 2], [3, 4]], [[5, 6], [7, 8]]]]])
print("5D array:", e)


# 1.2.1 Creating an array of zeros
f = np.zeros((2, 3))
print("Array of zeros:", f)
