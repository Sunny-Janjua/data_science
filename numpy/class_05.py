import numpy as np

array=np.arange(1,10)
print(array)
new_array=array.reshape(3,3)
print(new_array)

print(array[3])
print(array[0:7:2])
print(array[0:7:4])
print(array[:4])

print("Indexing in multi demensional array!")

print(new_array[:2])
print(new_array[2:])



