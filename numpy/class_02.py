import numpy as np

first_array=np.array([1,2,3,4,5,6,7,8,9])
print(f"This is my first array one dem : {first_array}")

second_array=np.array([[1,2,3],[1,2,3]])
print(f"This is my second array of two dem : {second_array}")
print(second_array)

third_array=np.array([[[1,2,3],[1,2,3],[1,2,3]]])
print(f"This is my third array : {third_array}")
print(third_array)



# Now we define multiple methods of numpy 

zeros=np.zeros((4,4))
print(zeros)

ones=np.ones((4,4))
print(ones)

our_values=np.full((4,4),44)
print(our_values)

our_values=np.full((4,4),44)
print(our_values)

our_new_value=np.arange(1,10)
print(our_new_value)

line_space=np.linspace(1,10,3)
print(line_space)

empty=np.empty((4,4))
print(empty)

eye_value=np.eye(4,4)
print(eye_value)