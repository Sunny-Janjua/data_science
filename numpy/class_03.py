import numpy as np

# Some most important function of numpy as Random

rand_value=np.random.rand(1,10)
print(rand_value)

rand_value_int=np.random.randint(1,20)
print(rand_value_int)

rand_value_n=np.random.randn(1,10)
print(rand_value_n)

arr = np.array([1, 2, 3, 4, 5])

# Generate a random sample of size 3 from arr
random_sample = np.random.choice(arr, size=3)

print(random_sample)
# Original array
arr = np.array([1, 2, 3, 4, 5])

# Shuffle the array in place
np.random.shuffle(arr)

print(arr)

np.random.seed(42)

# Now any random operation will be reproducible
random_numbers = np.random.randint(0, 10, size=5)
print(random_numbers)