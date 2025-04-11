import numpy as np

# Creating a 1D NumPy array
array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(array)               # ➤ [1 2 3 4 5 6 7 8 9]
print(array.shape)         # ➤ (9,) — it's a 1D array with 9 elements

# Reshaping it into a 3x3 matrix
new_array = array.reshape((3, 3))
print(new_array)
# ➤ [[1 2 3]
#     [4 5 6]
#     [7 8 9]]

print(new_array.shape)     # ➤ (3, 3)

# Transpose of the array
print(new_array.T)
# ➤ [[1 4 7]
#     [2 5 8]
#     [3 6 9]]

# Flattening back to 1D
new_array_flat = new_array.flatten()
print(new_array_flat)      # ➤ [1 2 3 4 5 6 7 8 9]

# Squeeze (not needed here, but works)
squeeze = np.squeeze(new_array)
print(squeeze)
# ➤ Same as new_array since no singleton dimension to squeeze